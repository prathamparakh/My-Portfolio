"""
CVP Analysis Module
UI and interaction logic for Cost-Volume-Profit Analysis
"""
import streamlit as st
import numpy as np
import pandas as pd
from backend.cvp_calculations import (
    calculate_cvp, 
    calculate_target_profit, 
    generate_sensitivity_analysis
)
from backend.utils import (
    validate_input_greater_than, 
    display_custom_metric, 
    create_excel_download_link,
    create_plotly_break_even_chart,
    create_sensitivity_analysis_chart
)

def run():
    """Main function to run the CVP analysis page"""
    # Page title and description
    st.markdown("<h1 style='text-align: left; color: #4CAF50;'>📈 Cost-Volume-Profit (CVP) Analysis</h1>", 
                unsafe_allow_html=True)
    st.write(
        """
        <div style='text-align: left;'>
        This tool helps you analyze your business's cost structure and profit potential. 
        Enter your cost and pricing parameters to calculate break-even points, contribution margins, 
        and perform sensitivity analysis.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Create tabs for different analysis types
    tab1, tab2, tab3 = st.tabs(["Basic Analysis", "Sensitivity Analysis", "What-If Scenarios"])
    
    with tab1:
        run_basic_analysis()
    
    with tab2:
        run_sensitivity_analysis()
    
    with tab3:
        run_what_if_analysis()

def run_basic_analysis():
    """Run basic CVP analysis with visualizations"""
    # Sidebar for input fields with improved organization
    st.sidebar.markdown("### Basic Parameters 📊")
    
    # Input fields with defaults and validation
    fxd_costs = st.sidebar.number_input(
        "Fixed Costs ($)", 
        min_value=0.0, 
        value=2000.0, 
        step=100.0,
        help="Total fixed costs regardless of production volume"
    )
    
    var_costs = st.sidebar.number_input(
        "Variable Cost per Unit ($)", 
        min_value=0.0, 
        value=25.0, 
        step=5.0,
        help="Cost that varies directly with each unit produced"
    )
    
    sell_price = st.sidebar.number_input(
        "Selling Price per Unit ($)", 
        min_value=0.0, 
        value=50.0, 
        step=5.0,
        help="Revenue received for each unit sold"
    )
    
    sales_volume = st.sidebar.number_input(
        "Sales Volume (units)", 
        min_value=0, 
        value=300, 
        step=50,
        help="Expected or current number of units sold"
    )
    
    # Target profit input
    st.sidebar.markdown("### Target Profit Analysis 🎯")
    tgt_profit = st.sidebar.number_input(
        "Desired Profit ($)", 
        min_value=0.0, 
        value=3000.0, 
        step=500.0,
        help="Target profit goal to calculate required sales"
    )
    
    # Input validation
    valid_inputs = True
    if not validate_input_greater_than(sell_price, var_costs, "Selling price must be greater than variable cost per unit."):
        valid_inputs = False
    
    # Calculate if inputs are valid
    if valid_inputs:
        # Perform calculations
        results = calculate_cvp(fxd_costs, var_costs, sell_price, sales_volume)
        
        if "error" in results:
            st.error(results["error"])
        else:
            # Display Basic CVP Analysis with improved metrics presentation
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Basic CVP Analysis</h2>", unsafe_allow_html=True)
            
            # First row of metrics - Contribution and Break-even
            col1, col2, col3 = st.columns(3)
            with col1:
                display_custom_metric(
                    "Contribution Margin per Unit",
                    f"${results['contribution_margin']:.2f}",
                    "Revenue remaining after variable costs"
                )
            
            with col2:
                display_custom_metric(
                    "Contribution Margin Ratio",
                    f"{results['contribution_margin_ratio']:.2%}",
                    "Percentage of each sale available for fixed costs and profit"
                )
            
            with col3:
                display_custom_metric(
                    "Break-Even Point",
                    f"{results['break_even_units']:.0f} units",
                    f"${results['break_even_sales']:.2f} in sales"
                )
            
            # Second row of metrics - Profitability and Safety
            col4, col5, col6 = st.columns(3)
            with col4:
                display_custom_metric(
                    "Operating Income",
                    f"${results['operating_income']:.2f}",
                    "Profit before interest and taxes"
                )
            
            with col5:
                display_custom_metric(
                    "Margin of Safety",
                    f"{results['margin_of_safety']:.2f}%",
                    "How far sales can drop before reaching break-even"
                )
            
            with col6:
                display_custom_metric(
                    "Operating Leverage",
                    f"{min(results['operating_leverage'], 999):.2f}",
                    "Impact of sales changes on profit"
                )
            
            # Target Profit Analysis
            target_results = calculate_target_profit(fxd_costs, var_costs, sell_price, tgt_profit)
            
            if "error" in target_results:
                st.warning(target_results["error"])
            else:
                st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Target Profit Analysis</h2>", 
                            unsafe_allow_html=True)
                
                col7, col8 = st.columns(2)
                with col7:
                    display_custom_metric(
                        "Units Required for Target Profit",
                        f"{target_results['target_units']:.0f} units",
                        f"To achieve ${tgt_profit:.2f} profit"
                    )
                
                with col8:
                    display_custom_metric(
                        "Sales Required for Target Profit",
                        f"${target_results['target_sales']:.2f}",
                        f"Total revenue needed for ${tgt_profit:.2f} profit"
                    )
            
            # Enhanced Break-Even Chart
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Break-Even Analysis Chart</h2>", 
                        unsafe_allow_html=True)
            
            # Create volume range for the chart
            max_volume = max(sales_volume, target_results['target_units'] * 1.2) if "target_units" in target_results else sales_volume * 1.2
            volume_range = np.linspace(0, max_volume, 100)
            
            # Calculate values for each point in the range
            total_costs = [fxd_costs + (var_costs * vol) for vol in volume_range]
            total_revenues = [sell_price * vol for vol in volume_range]
            
            # Create and display the chart
            fig = create_plotly_break_even_chart(
                fixed_costs=fxd_costs,
                volume_range=volume_range,
                total_costs=total_costs,
                total_revenues=total_revenues,
                break_even_point=results['break_even_units'],
                break_even_revenue=results['break_even_sales'],
                target_profit_point=target_results.get('target_units'),
                target_profit_revenue=target_results.get('target_sales')
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Create a dataframe with results for export
            export_data = pd.DataFrame({
                'Metric': [
                    'Fixed Costs',
                    'Variable Cost per Unit',
                    'Selling Price per Unit',
                    'Sales Volume',
                    'Contribution Margin per Unit',
                    'Contribution Margin Ratio',
                    'Break-Even Point (Units)',
                    'Break-Even Sales',
                    'Operating Income',
                    'Margin of Safety',
                    'Operating Leverage',
                    'Target Profit',
                    'Target Units',
                    'Target Sales'
                ],
                'Value': [
                    f"${fxd_costs:.2f}",
                    f"${var_costs:.2f}",
                    f"${sell_price:.2f}",
                    f"{sales_volume}",
                    f"${results['contribution_margin']:.2f}",
                    f"{results['contribution_margin_ratio']:.2%}",
                    f"{results['break_even_units']:.2f}",
                    f"${results['break_even_sales']:.2f}",
                    f"${results['operating_income']:.2f}",
                    f"{results['margin_of_safety']:.2f}%",
                    f"{results['operating_leverage']:.2f}",
                    f"${tgt_profit:.2f}",
                    f"{target_results.get('target_units', 'N/A')}",
                    f"${target_results.get('target_sales', 0):.2f}" if 'target_sales' in target_results else 'N/A'
                ]
            })
            
            # Export options
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Export Results</h2>", 
                        unsafe_allow_html=True)
            
            st.markdown(create_excel_download_link(export_data, "cvp_analysis_results.xlsx"), unsafe_allow_html=True)

def run_sensitivity_analysis():
    """Run sensitivity analysis on CVP parameters"""
    st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Sensitivity Analysis</h2>", 
                unsafe_allow_html=True)
    
    st.write("""
    Sensitivity analysis helps you understand how changes in different parameters affect your break-even point, 
    operating income, and overall profitability.
    """)
    
    # Base parameters input
    st.sidebar.markdown("### Sensitivity Analysis Parameters 📊")
    
    fxd_costs = st.sidebar.number_input(
        "Base Fixed Costs ($)", 
        min_value=0.0, 
        value=2000.0, 
        step=100.0,
        key="sens_fixed_costs"
    )
    
    var_costs = st.sidebar.number_input(
        "Base Variable Cost per Unit ($)", 
        min_value=0.0, 
        value=25.0, 
        step=5.0,
        key="sens_var_costs"
    )
    
    sell_price = st.sidebar.number_input(
        "Base Selling Price per Unit ($)", 
        min_value=0.0, 
        value=50.0, 
        step=5.0,
        key="sens_sell_price"
    )
    
    sales_volume = st.sidebar.number_input(
        "Base Sales Volume (units)", 
        min_value=0, 
        value=300, 
        step=50,
        key="sens_sales_volume"
    )
    
    # Parameter to vary and range
    param_to_vary = st.selectbox(
        "Parameter to Vary",
        ["Selling Price", "Variable Cost", "Fixed Costs", "Sales Volume"],
        index=0
    )
    
    # Map parameter selection to actual parameter name
    param_map = {
        "Selling Price": "selling_price_per_unit",
        "Variable Cost": "variable_cost_per_unit",
        "Fixed Costs": "fixed_costs",
        "Sales Volume": "sales_volume"
    }
    
    # Set up range values based on parameter selected
    if param_to_vary == "Selling Price":
        min_val = max(var_costs + 1, sell_price * 0.5)
        max_val = sell_price * 1.5
        step_val = (max_val - min_val) / 10
    elif param_to_vary == "Variable Cost":
        min_val = max(1, var_costs * 0.5)
        max_val = min(sell_price - 1, var_costs * 1.5)
        step_val = (max_val - min_val) / 10
    elif param_to_vary == "Fixed Costs":
        min_val = max(100, fxd_costs * 0.5)
        max_val = fxd_costs * 1.5
        step_val = (max_val - min_val) / 10
    else:  # Sales Volume
        min_val = max(1, sales_volume * 0.5)
        max_val = sales_volume * 1.5
        step_val = (max_val - min_val) / 10
    
    # Range input
    col1, col2 = st.columns(2)
    with col1:
        min_range = st.number_input(f"Minimum {param_to_vary}", value=float(min_val), step=float(step_val))
    with col2:
        max_range = st.number_input(f"Maximum {param_to_vary}", value=float(max_val), step=float(step_val))
    
    num_points = st.slider("Number of Points in Range", min_value=5, max_value=20, value=10)
    
    # Create range values
    range_values = np.linspace(min_range, max_range, num_points)
    
    # Create base parameters dictionary
    base_params = {
        "fixed_costs": fxd_costs,
        "variable_cost_per_unit": var_costs,
        "selling_price_per_unit": sell_price,
        "sales_volume": sales_volume
    }
    
    # Input validation
    valid_inputs = True
    if not validate_input_greater_than(sell_price, var_costs, "Base selling price must be greater than variable cost per unit."):
        valid_inputs = False
    
    if min_range >= max_range:
        st.error("Minimum range must be less than maximum range.")
        valid_inputs = False
    
    # Run sensitivity analysis if inputs are valid
    if valid_inputs:
        # Get the actual parameter name
        param_name = param_map[param_to_vary]
        
        # Run sensitivity analysis
        sensitivity_data = generate_sensitivity_analysis(base_params, param_name, range_values)
        
        # Check if we have results
        if not sensitivity_data.empty:
            # Display multiple charts for different metrics
            col1, col2 = st.columns(2)
            
            with col1:
                # Break-even units chart
                be_chart = create_sensitivity_analysis_chart(
                    sensitivity_data,
                    param_name,
                    'break_even_units',
                    f"Impact of {param_to_vary} on Break-Even Point"
                )
                st.plotly_chart(be_chart, use_container_width=True)
                
                # Operating leverage chart
                ol_chart = create_sensitivity_analysis_chart(
                    sensitivity_data,
                    param_name,
                    'operating_leverage',
                    f"Impact of {param_to_vary} on Operating Leverage"
                )
                st.plotly_chart(ol_chart, use_container_width=True)
            
            with col2:
                # Operating income chart
                oi_chart = create_sensitivity_analysis_chart(
                    sensitivity_data,
                    param_name,
                    'operating_income',
                    f"Impact of {param_to_vary} on Operating Income"
                )
                st.plotly_chart(oi_chart, use_container_width=True)
                
                # Margin of safety chart
                mos_chart = create_sensitivity_analysis_chart(
                    sensitivity_data,
                    param_name,
                    'margin_of_safety',
                    f"Impact of {param_to_vary} on Margin of Safety"
                )
                st.plotly_chart(mos_chart, use_container_width=True)
            
            # Display sensitivity data in a table
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Sensitivity Analysis Data</h3>", 
                        unsafe_allow_html=True)
            
            # Format the dataframe for display
            display_df = sensitivity_data.copy()
            display_df.columns = [col.replace('_', ' ').title() for col in display_df.columns]
            
            st.dataframe(display_df, use_container_width=True)
            
            # Export options
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Export Sensitivity Analysis</h3>", 
                        unsafe_allow_html=True)
            
            st.markdown(create_excel_download_link(display_df, "sensitivity_analysis_results.xlsx"), 
                        unsafe_allow_html=True)
        else:
            st.warning("No valid data generated for sensitivity analysis. Check your input parameters.")

def run_what_if_analysis():
    """Run what-if scenario analysis for CVP"""
    st.markdown("<h2 style='text-align: left; color: #4CAF50;'>What-If Scenario Analysis</h2>", 
                unsafe_allow_html=True)
    
    st.write("""
    Compare different business scenarios side by side to make informed decisions. 
    Enter parameters for each scenario and see how they impact your profitability metrics.
    """)
    
    # Allow user to specify number of scenarios
    num_scenarios = st.slider("Number of Scenarios to Compare", min_value=2, max_value=4, value=2)
    
    # Create columns for scenarios
    scenario_cols = st.columns(num_scenarios)
    
    # Store scenario parameters and results
    scenarios = []
    
    # Get input for each scenario
    for i, col in enumerate(scenario_cols):
        with col:
            st.markdown(f"### Scenario {i+1}")
            
            # Input fields for this scenario
            name = st.text_input(f"Scenario Name", value=f"Scenario {i+1}", key=f"name_{i}")
            fxd_costs = st.number_input(
                "Fixed Costs ($)", 
                min_value=0.0, 
                value=2000.0 * (1 + i*0.1),  # Slightly different defaults for each scenario
                step=100.0,
                key=f"fxd_{i}"
            )
            var_costs = st.number_input(
                "Variable Cost per Unit ($)", 
                min_value=0.0, 
                value=25.0 * (1 + i*0.05),
                step=5.0,
                key=f"var_{i}"
            )
            sell_price = st.number_input(
                "Selling Price per Unit ($)", 
                min_value=0.0, 
                value=50.0 * (1 + i*0.05),
                step=5.0,
                key=f"price_{i}"
            )
            sales_volume = st.number_input(
                "Sales Volume (units)", 
                min_value=0, 
                value=300 * (1 + i*0.1),
                step=50,
                key=f"volume_{i}"
            )
            
            # Validate input
            valid = sell_price > var_costs
            
            if not valid:
                st.error("Selling price must be greater than variable cost per unit.")
            else:
                # Calculate results for this scenario
                results = calculate_cvp(fxd_costs, var_costs, sell_price, sales_volume)
                
                # Store scenario info
                scenarios.append({
                    "name": name,
                    "fixed_costs": fxd_costs,
                    "variable_costs": var_costs,
                    "selling_price": sell_price,
                    "sales_volume": sales_volume,
                    "results": results
                })
    
    # Display comparison if we have valid scenarios
    valid_scenarios = [s for s in scenarios if "error" not in s["results"]]
    
    if len(valid_scenarios) >= 2:
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Scenario Comparison</h3>", 
                    unsafe_allow_html=True)
        
        # Create comparison table
        comparison_data = {
            "Metric": [
                "Fixed Costs ($)",
                "Variable Cost per Unit ($)",
                "Selling Price per Unit ($)",
                "Sales Volume (units)",
                "Contribution Margin ($)",
                "Contribution Margin Ratio (%)",
                "Break-Even Point (units)",
                "Operating Income ($)",
                "Margin of Safety (%)",
                "Operating Leverage"
            ]
        }
        
        # Add data for each scenario
        for scenario in valid_scenarios:
            comparison_data[scenario["name"]] = [
                f"{scenario['fixed_costs']:.2f}",
                f"{scenario['variable_costs']:.2f}",
                f"{scenario['selling_price']:.2f}",
                f"{scenario['sales_volume']}",
                f"{scenario['results']['contribution_margin']:.2f}",
                f"{scenario['results']['contribution_margin_ratio']:.2%}",
                f"{scenario['results']['break_even_units']:.0f}",
                f"{scenario['results']['operating_income']:.2f}",
                f"{scenario['results']['margin_of_safety']:.2f}",
                f"{min(scenario['results']['operating_leverage'], 999):.2f}"
            ]
        
        # Convert to DataFrame and display
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True)
        
        # Show which scenario is best for each metric
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Scenario Recommendations</h3>", 
                    unsafe_allow_html=True)
        
        # Determine best scenario for each relevant metric
        best_cm = max(valid_scenarios, key=lambda x: x["results"]["contribution_margin"])
        best_cm_ratio = max(valid_scenarios, key=lambda x: x["results"]["contribution_margin_ratio"])
        lowest_be = min(valid_scenarios, key=lambda x: x["results"]["break_even_units"])
        best_income = max(valid_scenarios, key=lambda x: x["results"]["operating_income"])
        best_safety = max(valid_scenarios, key=lambda x: x["results"]["margin_of_safety"])
        
        # Display recommendations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            - **Highest Contribution Margin**: {best_cm["name"]} (${best_cm["results"]["contribution_margin"]:.2f})
            - **Best Contribution Margin Ratio**: {best_cm_ratio["name"]} ({best_cm_ratio["results"]["contribution_margin_ratio"]:.2%})
            - **Lowest Break-Even Point**: {lowest_be["name"]} ({lowest_be["results"]["break_even_units"]:.0f} units)
            """)
        
        with col2:
            st.markdown(f"""
            - **Highest Operating Income**: {best_income["name"]} (${best_income["results"]["operating_income"]:.2f})
            - **Best Margin of Safety**: {best_safety["name"]} ({best_safety["results"]["margin_of_safety"]:.2f}%)
            """)
        
        # Overall recommendation
        # Simple scoring - could be made more sophisticated
        scores = {}
        for scenario in valid_scenarios:
            score = 0
            if scenario == best_cm: score += 1
            if scenario == best_cm_ratio: score += 1
            if scenario == lowest_be: score += 1
            if scenario == best_income: score += 2  # Weight income more
            if scenario == best_safety: score += 1
            scores[scenario["name"]] = score
        
        best_overall = max(scores.items(), key=lambda x: x[1])[0]
        
        st.success(f"""
        **Overall Recommendation**: {best_overall} appears to be the most favorable scenario based on the key 
        profitability metrics analyzed.
        """)
        
        # Export options
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Export Comparison</h3>", 
                    unsafe_allow_html=True)
        
        st.markdown(create_excel_download_link(comparison_df, "scenario_comparison_results.xlsx"), 
                    unsafe_allow_html=True)
    elif len(valid_scenarios) == 1:
        st.warning("Need at least two valid scenarios to perform comparison.")
    else:
        st.error("No valid scenarios to compare. Please check your inputs.")