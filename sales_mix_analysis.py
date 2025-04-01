"""
Sales Mix Analysis Module
UI and interaction logic for Sales Mix Analysis
"""
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from backend.cvp_calculations import (
    calculate_sales_mix,
    calculate_target_profit_sales_mix,
    calculate_optimal_sales_mix
)
from backend.utils import (
    validate_input_greater_than,
    display_custom_metric,
    create_excel_download_link,
    COLOR_SCHEME
)

def run():
    """Main function to run the Sales Mix Analysis page"""
    # Page title and description
    st.markdown("<h1 style='text-align: left; color: #4CAF50;'>🧩 Sales Mix Analysis</h1>", 
                unsafe_allow_html=True)
    st.write(
        """
        <div style='text-align: left;'>
        Analyze your product mix to determine the optimal sales combination for profitability.
        Enter the cost and pricing parameters for each product to calculate break-even points and 
        perform sensitivity analysis across your product portfolio.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Create tabs for different analysis types
    tab1, tab2, tab3 = st.tabs(["Sales Mix Analysis", "Optimal Mix", "Product Comparison"])
    
    with tab1:
        run_basic_sales_mix_analysis()
    
    with tab2:
        run_optimal_mix_analysis()
    
    with tab3:
        run_product_comparison()

def run_basic_sales_mix_analysis():
    """Run basic sales mix analysis"""
    # Sidebar for input fields
    st.sidebar.markdown("### Basic Parameters 📊")
    
    # Fixed costs input
    fxd_costs = st.sidebar.number_input(
        "Fixed Costs ($)", 
        min_value=0.0, 
        value=2000.0, 
        step=100.0,
        help="Total fixed costs across all products"
    )
    
    # Target profit input
    tgt_profit = st.sidebar.number_input(
        "Desired Profit ($) for Sales Mix", 
        min_value=0.0, 
        value=3000.0, 
        step=500.0,
        help="Target profit goal to calculate required sales"
    )
    
    # Product inputs
    st.sidebar.markdown("### Product Information 🏷️")
    num_products = st.sidebar.number_input(
        "Number of Products", 
        min_value=1, 
        max_value=10, 
        value=2, 
        step=1,
        help="Number of different products in your sales mix"
    )
    
    # Initialize products list and validation flag
    products = []
    valid_inputs = True
    total_sales_volume = 0
    
    # Loop through each product to collect inputs
    for i in range(num_products):
        st.sidebar.markdown(f"#### Product {i + 1}")
        
        product_name = st.sidebar.text_input(
            f"Product {i + 1} Name", 
            value=f"Product {i + 1}",
            key=f"name_{i}"
        )
        
        sell_price = st.sidebar.number_input(
            f"Selling Price ($)", 
            min_value=0.0, 
            value=50.0 + i * 10.0,  # Different defaults for each product
            step=5.0,
            key=f"price_{i}"
        )
        
        var_cost = st.sidebar.number_input(
            f"Variable Cost per Unit ($)", 
            min_value=0.0, 
            value=25.0 + i * 5.0,
            step=5.0,
            key=f"cost_{i}"
        )
        
        sales_volume = st.sidebar.number_input(
            f"Expected Sales Volume", 
            min_value=0, 
            value=300 - i * 50,  # Different defaults
            step=50,
            key=f"volume_{i}"
        )
        
        # Validate input for this product
        if not validate_input_greater_than(sell_price, var_cost, 
                                          f"Selling price must be greater than variable cost for {product_name}."):
            valid_inputs = False
        
        # Add product to list
        products.append({
            "product_name": product_name,
            "sell_price": sell_price,
            "var_cost": var_cost,
            "sales_volume": sales_volume
        })
        
        total_sales_volume += sales_volume
    
    # Calculate Sales Mix Percentages Automatically
    for product in products:
        product['mix_percentage'] = (product['sales_volume'] / total_sales_volume) * 100 if total_sales_volume > 0 else 0
    
    # Continue if inputs are valid
    if valid_inputs and total_sales_volume > 0:
        # Calculate Sales Mix Results
        sales_mix_results = calculate_sales_mix(products, fxd_costs, target_profit=tgt_profit)
        
        # Check for errors
        if "error" in sales_mix_results:
            st.error(sales_mix_results["error"])
        else:
            # Display Sales Mix Analysis Results
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Sales Mix Analysis</h2>", 
                        unsafe_allow_html=True)
            
            # Display key metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                display_custom_metric(
                    "Weighted Contribution Margin",
                    f"${sales_mix_results['weighted_contribution_margin']:.2f}",
                    "Average CM weighted by sales mix"
                )
            
            with col2:
                display_custom_metric(
                    "Break-Even Point",
                    f"{sales_mix_results['break_even_units']:.0f} units",
                    f"${sales_mix_results['break_even_sales']:.2f} in sales"
                )
            
            with col3:
                display_custom_metric(
                    "Weighted Selling Price",
                    f"${sales_mix_results['weighted_selling_price']:.2f}",
                    "Average price weighted by sales mix"
                )
            
            # Display Target Profit Analysis
            if sales_mix_results['target_units'] is not None:
                st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Target Profit Analysis</h2>", 
                            unsafe_allow_html=True)
                
                col4, col5 = st.columns(2)
                
                with col4:
                    display_custom_metric(
                        "Total Units for Target Profit",
                        f"{sales_mix_results['target_units']:.0f} units",
                        f"To achieve ${tgt_profit:.2f} profit"
                    )
                
                with col5:
                    display_custom_metric(
                        "Total Sales for Target Profit",
                        f"${sales_mix_results['target_sales']:.2f}",
                        f"Revenue needed for ${tgt_profit:.2f} profit"
                    )
            
            # Product-specific metrics
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Product-Specific Metrics</h2>", 
                        unsafe_allow_html=True)
            
            # Create a DataFrame for product metrics
            product_metrics_df = pd.DataFrame(sales_mix_results["product_metrics"])
            product_metrics_df["contribution_margin"] = product_metrics_df["contribution_margin"].map("${:.2f}".format)
            product_metrics_df["contribution_margin_ratio"] = product_metrics_df["contribution_margin_ratio"].map("{:.2%}".format)
            product_metrics_df["weighted_contribution"] = product_metrics_df["weighted_contribution"].map("${:.2f}".format)
            product_metrics_df["percentage"] = product_metrics_df["percentage"].map("{:.2f}%".format)
            
            # Rename columns for display
            product_metrics_df.columns = [
                "Product Name", 
                "Contribution Margin", 
                "CM Ratio", 
                "Weighted Contribution", 
                "Mix Percentage"
            ]
            
            st.dataframe(product_metrics_df, use_container_width=True)
            
            # Break-Even and Target Volumes for Each Product
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Required Volume by Product</h3>", 
                        unsafe_allow_html=True)
            
            # Prepare data for break-even and target volumes
            be_volumes = sales_mix_results["break_even_product_volumes"]
            target_volumes = sales_mix_results["target_product_volumes"] if sales_mix_results["target_product_volumes"] is not None else {}
            
            volume_data = []
            for product in products:
                product_name = product["product_name"]
                volume_data.append({
                    "Product Name": product_name,
                    "Current Volume": product["sales_volume"],
                    "Break-Even Volume": f"{be_volumes[product_name]:.0f}",
                    "Target Profit Volume": f"{target_volumes[product_name]:.0f}" if product_name in target_volumes else "N/A"
                })
            
            # Display volume data
            volume_df = pd.DataFrame(volume_data)
            st.dataframe(volume_df, use_container_width=True)
            
            # Sales Mix Distribution - Pie Chart
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Sales Mix Distribution</h2>", 
                        unsafe_allow_html=True)
            
            # Prepare data for pie chart
            product_labels = [product['product_name'] for product in products]
            product_mix_percentages = [product['mix_percentage'] for product in products]
            
            # Create pie chart
            fig_pie = go.Figure(data=[go.Pie(
                labels=product_labels, 
                values=product_mix_percentages, 
                hole=.3,
                marker=dict(colors=px.colors.qualitative.G10)
            )])
            
            fig_pie.update_layout(
                title="Current Sales Mix Distribution",
                template="plotly_dark",
                margin=dict(l=40, r=40, t=40, b=40)
            )
            
            st.plotly_chart(fig_pie, use_container_width=True)
            
            # Break-Even Graph for Sales Mix
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Sales Mix Break-Even Analysis</h2>", 
                        unsafe_allow_html=True)
            
            # Calculate values for break-even chart
            max_units = max(total_sales_volume, sales_mix_results["target_units"] * 1.2 if sales_mix_results["target_units"] is not None else 0)
            units_range = np.linspace(0, max(1000, max_units), 100)
            
            # Calculate costs and revenues
            weighted_var_cost = sum(p["var_cost"] * (p["mix_percentage"] / 100) for p in products)
            weighted_sell_price = sales_mix_results["weighted_selling_price"]
            
            total_costs = [fxd_costs + (weighted_var_cost * units) for units in units_range]
            total_revenues = [weighted_sell_price * units for units in units_range]
            
            # Create break-even chart
            fig_be = go.Figure()
            
            # Add fixed costs line
            fig_be.add_trace(go.Scatter(
                x=units_range,
                y=[fxd_costs] * len(units_range),
                mode='lines',
                name='Fixed Costs',
                line=dict(color=COLOR_SCHEME["fixed_costs"], width=2, dash='dash')
            ))
            
            # Add total costs line
            fig_be.add_trace(go.Scatter(
                x=units_range,
                y=total_costs,
                mode='lines',
                name='Total Costs',
                line=dict(color=COLOR_SCHEME["total_cost"], width=2)
            ))
            
            # Add total revenue line
            fig_be.add_trace(go.Scatter(
                x=units_range,
                y=total_revenues,
                mode='lines',
                name='Total Revenue',
                line=dict(color=COLOR_SCHEME["revenue"], width=2)
            ))
            
            # Add profit area (shaded region between revenue and cost)
            fig_be.add_trace(go.Scatter(
                x=units_range,
                y=total_revenues,
                mode='none',
                name='Profit Area',
                fill='tonexty',
                fillcolor='rgba(76, 175, 80, 0.2)',
                showlegend=False
            ))
            
            # Add break-even line
            fig_be.add_trace(go.Scatter(
                x=[sales_mix_results["break_even_units"], sales_mix_results["break_even_units"]],
                y=[0, sales_mix_results["break_even_sales"]],
                mode='lines',
                name='Break-Even Point',
                line=dict(color=COLOR_SCHEME["break_even"], width=2, dash='dot')
            ))
            
            # Add break-even annotation
            fig_be.add_annotation(
                x=sales_mix_results["break_even_units"],
                y=sales_mix_results["break_even_sales"],
                text="Break-Even",
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40,
                arrowcolor=COLOR_SCHEME["break_even"],
                font=dict(color=COLOR_SCHEME["break_even"])
            )
            
            # Add target profit line if available
            if sales_mix_results["target_units"] is not None:
                fig_be.add_trace(go.Scatter(
                    x=[sales_mix_results["target_units"], sales_mix_results["target_units"]],
                    y=[0, sales_mix_results["target_sales"]],
                    mode='lines',
                    name='Target Profit Point',
                    line=dict(color=COLOR_SCHEME["target_profit"], width=2, dash='dot')
                ))
                
                # Add target profit annotation
                fig_be.add_annotation(
                    x=sales_mix_results["target_units"],
                    y=sales_mix_results["target_sales"],
                    text="Target Profit",
                    showarrow=True,
                    arrowhead=7,
                    ax=0,
                    ay=-40,
                    arrowcolor=COLOR_SCHEME["target_profit"],
                    font=dict(color=COLOR_SCHEME["target_profit"])
                )
            
            # Format chart
            fig_be.update_layout(
                title="Sales Mix Break-Even Analysis",
                xaxis_title="Total Units",
                yaxis_title="Amount ($)",
                template="plotly_dark",
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                margin=dict(l=40, r=40, t=60, b=40),
                hovermode="x unified"
            )
            
            st.plotly_chart(fig_be, use_container_width=True)
            
            # Export options
            st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Export Results</h2>", 
                        unsafe_allow_html=True)
            
            # Prepare data for export
            export_data = {
                "Basic Parameters": [
                    "Fixed Costs ($)",
                    "Target Profit ($)",
                    "Total Sales Volume (units)",
                    "Weighted Contribution Margin ($)",
                    "Weighted Selling Price ($)",
                    "Break-Even Units",
                    "Break-Even Sales ($)",
                    "Target Units",
                    "Target Sales ($)"
                ],
                "Value": [
                    f"{fxd_costs:.2f}",
                    f"{tgt_profit:.2f}",
                    f"{total_sales_volume}",
                    f"{sales_mix_results['weighted_contribution_margin']:.2f}",
                    f"{sales_mix_results['weighted_selling_price']:.2f}",
                    f"{sales_mix_results['break_even_units']:.2f}",
                    f"{sales_mix_results['break_even_sales']:.2f}",
                    f"{sales_mix_results['target_units']:.2f}" if sales_mix_results['target_units'] is not None else "N/A",
                    f"{sales_mix_results['target_sales']:.2f}" if sales_mix_results['target_sales'] is not None else "N/A"
                ]
            }
            
            # Create DataFrames for export
            export_df = pd.DataFrame(export_data)
            product_df = pd.DataFrame([{
                "Product Name": p["product_name"],
                "Selling Price ($)": p["sell_price"],
                "Variable Cost ($)": p["var_cost"],
                "Current Volume": p["sales_volume"],
                "Mix Percentage (%)": p["mix_percentage"],
                "Break-Even Volume": be_volumes[p["product_name"]],
                "Target Volume": target_volumes.get(p["product_name"], "N/A")
            } for p in products])
            
            # Create download links
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(create_excel_download_link(export_df, "sales_mix_summary.xlsx", "Summary"), 
                            unsafe_allow_html=True)
            with col_b:
                st.markdown(create_excel_download_link(product_df, "product_details.xlsx", "Products"), 
                            unsafe_allow_html=True)
    
    elif total_sales_volume <= 0:
        st.error("Total sales volume must be greater than zero.")

def run_optimal_mix_analysis():
    """Run optimal sales mix analysis"""
    st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Optimal Sales Mix Analysis</h2>", 
                unsafe_allow_html=True)
    
    st.write("""
    This analysis helps you identify the optimal allocation of your sales mix to maximize profitability, 
    based on the contribution margin of each product.
    """)
    
    # Fixed costs input
    fxd_costs = st.sidebar.number_input(
        "Fixed Costs for Optimal Mix ($)", 
        min_value=0.0, 
        value=2000.0, 
        step=100.0,
        key="opt_fixed_costs",
        help="Total fixed costs across all products"
    )
    
    # Number of products
    num_products = st.sidebar.number_input(
        "Number of Products for Optimal Mix", 
        min_value=1, 
        max_value=10, 
        value=3, 
        step=1,
        key="opt_num_products",
        help="Number of products to consider in optimization"
    )
    
    # Initialize products list and validation flag
    products = []
    valid_inputs = True
    total_sales_volume = 0
    
    # Product inputs
    for i in range(num_products):
        st.sidebar.markdown(f"#### Optimization Product {i + 1}")
        
        product_name = st.sidebar.text_input(
            f"Product Name", 
            value=f"Product {i + 1}",
            key=f"opt_name_{i}"
        )
        
        sell_price = st.sidebar.number_input(
            f"Selling Price ($)", 
            min_value=0.0, 
            value=50.0 + i * 15.0,  # Different defaults
            step=5.0,
            key=f"opt_price_{i}"
        )
        
        var_cost = st.sidebar.number_input(
            f"Variable Cost per Unit ($)", 
            min_value=0.0, 
            value=20.0 + i * 7.0,
            step=5.0,
            key=f"opt_cost_{i}"
        )
        
        sales_volume = st.sidebar.number_input(
            f"Current Sales Volume", 
            min_value=0, 
            value=300 - i * 75,
            step=50,
            key=f"opt_volume_{i}"
        )
        
        # Add any constraints specific to this product
        min_percentage = st.sidebar.slider(
            f"Minimum Mix % for {product_name}", 
            min_value=0, 
            max_value=100, 
            value=10,
            key=f"min_pct_{i}"
        )
        
        # Validate input
        if not validate_input_greater_than(sell_price, var_cost, 
                                          f"Selling price must be greater than variable cost for {product_name}."):
            valid_inputs = False
        
        # Add product to list
        products.append({
            "product_name": product_name,
            "sell_price": sell_price,
            "var_cost": var_cost,
            "sales_volume": sales_volume,
            "min_percentage": min_percentage,
            "contribution_margin": sell_price - var_cost
        })
        
        total_sales_volume += sales_volume
    
    # Calculate current mix percentages
    for product in products:
        product['original_percentage'] = (product['sales_volume'] / total_sales_volume) * 100 if total_sales_volume > 0 else 0
        product['mix_percentage'] = product['original_percentage']  # Initialize with current mix
    
    # Continue with valid inputs
    if valid_inputs and total_sales_volume > 0:
        # Calculate optimal mix
        optimal_mix_results = calculate_optimal_sales_mix(products, fxd_costs)
        
        # Check for errors
        if "error" in optimal_mix_results:
            st.error(optimal_mix_results["error"])
        else:
            # Display optimization results
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Current vs. Optimal Sales Mix</h3>", 
                        unsafe_allow_html=True)
            
            # Prepare data for comparison
            comparison_data = []
            
            for product in optimal_mix_results["sorted_products"]:
                comparison_data.append({
                    "Product": product["product_name"],
                    "Contribution Margin": f"${product['contribution_margin']:.2f}",
                    "Current Mix %": f"{product.get('original_percentage', 0):.2f}%",
                    "Suggested Mix %": f"{product['suggested_percentage']:.2f}%",
                    "Change": f"{product['suggested_percentage'] - product.get('original_percentage', 0):.2f}%"
                })
            
            # Display comparison
            comparison_df = pd.DataFrame(comparison_data)
            st.dataframe(comparison_df, use_container_width=True)
            
            # Improvement metrics
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Optimization Impact</h3>", 
                        unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                suggested_results = optimal_mix_results["suggested_mix_results"]
                display_custom_metric(
                    "Optimized Contribution Margin",
                    f"${suggested_results['weighted_contribution_margin']:.2f}",
                    "Per unit after optimization"
                )
            
            with col2:
                improvement = optimal_mix_results["improvement_percentage"]
                display_custom_metric(
                    "Potential Improvement",
                    f"{improvement:.2f}%",
                    "Increase in weighted contribution margin"
                )
            
            # Compare break-even points
            col3, col4 = st.columns(2)
            
            with col3:
                display_custom_metric(
                    "Current Break-Even Point",
                    f"{calculate_sales_mix(products, fxd_costs)['break_even_units']:.0f} units",
                    "With current sales mix"
                )
            
            with col4:
                display_custom_metric(
                    "Optimized Break-Even Point",
                    f"{suggested_results['break_even_units']:.0f} units",
                    "With optimized sales mix"
                )
            
            # Visualization of current vs. suggested mix
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Current vs. Suggested Mix Visualization</h3>", 
                        unsafe_allow_html=True)
            
            # Prepare data for comparison chart
            viz_data = pd.DataFrame({
                "Product": [p["product_name"] for p in products],
                "Current Mix": [p.get("original_percentage", 0) for p in products],
                "Suggested Mix": [p["suggested_percentage"] for p in optimal_mix_results["sorted_products"]]
            })
            
            # Create comparison bar chart
            fig_comp = go.Figure()
            
            # Add current mix bars
            fig_comp.add_trace(go.Bar(
                x=viz_data["Product"],
                y=viz_data["Current Mix"],
                name="Current Mix %",
                marker_color=COLOR_SCHEME["secondary"]
            ))
            
            # Add suggested mix bars
            fig_comp.add_trace(go.Bar(
                x=viz_data["Product"],
                y=viz_data["Suggested Mix"],
                name="Suggested Mix %",
                marker_color=COLOR_SCHEME["primary"]
            ))
            
            # Format chart
            fig_comp.update_layout(
                title="Sales Mix Comparison",
                xaxis_title="Products",
                yaxis_title="Percentage of Sales Mix",
                barmode='group',
                template="plotly_dark",
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                margin=dict(l=40, r=40, t=60, b=40)
            )
            
            st.plotly_chart(fig_comp, use_container_width=True)
            
            # Implementation guidance
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Implementation Guidance</h3>", 
                        unsafe_allow_html=True)
            
            st.markdown("""
            To move toward the suggested optimal mix, consider these strategies:
            
            1. **Marketing Focus**: Allocate more marketing resources to high-contribution products
            2. **Pricing Strategy**: Review pricing structures to enhance demand for optimal products
            3. **Sales Incentives**: Adjust sales commission structures to promote the optimal mix
            4. **Production Capacity**: Ensure production can meet the suggested mix requirements
            5. **Phased Implementation**: Make gradual adjustments to minimize disruption
            
            Remember that the optimization is based solely on contribution margin analysis and may need to be 
            balanced with other business considerations like market demand, production constraints, and 
            customer preferences.
            """)
            
            # Export options
            st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Export Optimization Results</h3>", 
                        unsafe_allow_html=True)
            
            st.markdown(create_excel_download_link(comparison_df, "optimal_mix_results.xlsx"), 
                        unsafe_allow_html=True)
    
    elif total_sales_volume <= 0:
        st.error("Total sales volume must be greater than zero.")

def run_product_comparison():
    """Run product comparison analysis"""
    st.markdown("<h2 style='text-align: left; color: #4CAF50;'>Product Comparison Analysis</h2>", 
                unsafe_allow_html=True)
    
    st.write("""
    Compare individual product profitability metrics side by side to gain insights into 
    which products contribute most to your overall profitability.
    """)
    
    # Get products from the sidebar
    num_products = st.sidebar.number_input(
        "Number of Products to Compare", 
        min_value=2, 
        max_value=10, 
        value=3, 
        step=1,
        key="comp_num_products"
    )
    
    # Initialize products list
    products = []
    valid_inputs = True
    
    # Product inputs
    for i in range(num_products):
        st.sidebar.markdown(f"#### Comparison Product {i + 1}")
        
        product_name = st.sidebar.text_input(
            f"Product Name", 
            value=f"Product {i + 1}",
            key=f"comp_name_{i}"
        )
        
        sell_price = st.sidebar.number_input(
            f"Selling Price ($)", 
            min_value=0.0, 
            value=50.0 + i * 10.0,
            step=5.0,
            key=f"comp_price_{i}"
        )
        
        var_cost = st.sidebar.number_input(
            f"Variable Cost per Unit ($)", 
            min_value=0.0, 
            value=25.0 + i * 5.0,
            step=5.0,
            key=f"comp_cost_{i}"
        )
        
        sales_volume = st.sidebar.number_input(
            f"Annual Sales Volume", 
            min_value=0, 
            value=1000 - i * 200,
            step=100,
            key=f"comp_volume_{i}"
        )
        
        # Validate input
        if not validate_input_greater_than(sell_price, var_cost, 
                                          f"Selling price must be greater than variable cost for {product_name}."):
            valid_inputs = False
        
        # Add product to list
        products.append({
            "product_name": product_name,
            "sell_price": sell_price,
            "var_cost": var_cost,
            "sales_volume": sales_volume
        })
    
    # Continue with valid inputs
    if valid_inputs:
        # Calculate comparison metrics for each product
        for product in products:
            product["contribution_margin"] = product["sell_price"] - product["var_cost"]
            product["cm_ratio"] = product["contribution_margin"] / product["sell_price"] if product["sell_price"] > 0 else 0
            product["total_contribution"] = product["contribution_margin"] * product["sales_volume"]
            product["total_revenue"] = product["sell_price"] * product["sales_volume"]
        
        # Create comparison table
        comparison_data = []
        
        for product in products:
            comparison_data.append({
                "Product": product["product_name"],
                "Selling Price": f"${product['sell_price']:.2f}",
                "Variable Cost": f"${product['var_cost']:.2f}",
                "Contribution Margin": f"${product['contribution_margin']:.2f}",
                "CM Ratio": f"{product['cm_ratio']:.2%}",
                "Annual Volume": f"{product['sales_volume']}",
                "Total Contribution": f"${product['total_contribution']:.2f}",
                "Total Revenue": f"${product['total_revenue']:.2f}"
            })
            
        # Display comparison table
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True)
        
        # Create summary metrics
        total_revenue = sum(p["total_revenue"] for p in products)
        total_contribution = sum(p["total_contribution"] for p in products)
        avg_cm_ratio = total_contribution / total_revenue if total_revenue > 0 else 0
        
        # Display summary metrics
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Product Portfolio Summary</h3>", 
                    unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            display_custom_metric(
                "Total Annual Revenue",
                f"${total_revenue:.2f}",
                "Combined revenue from all products"
            )
        
        with col2:
            display_custom_metric(
                "Total Contribution Margin",
                f"${total_contribution:.2f}",
                "Combined contribution to fixed costs and profit"
            )
        
        with col3:
            display_custom_metric(
                "Overall CM Ratio",
                f"{avg_cm_ratio:.2%}",
                "Portfolio-wide contribution margin ratio"
            )
        
        # Product contribution visualization
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Product Contribution Analysis</h3>", 
                    unsafe_allow_html=True)
        
        # Prepare data for visualizations
        viz_data = pd.DataFrame({
            "Product": [p["product_name"] for p in products],
            "Contribution Margin": [p["contribution_margin"] for p in products],
            "CM Ratio": [p["cm_ratio"] for p in products],
            "Total Contribution": [p["total_contribution"] for p in products]
        })
        
        # Create CM Ratio bar chart
        fig_cm = px.bar(
            viz_data,
            x="Product",
            y="CM Ratio",
            title="Contribution Margin Ratio by Product",
            color="CM Ratio",
            color_continuous_scale="Viridis",
            template="plotly_dark"
        )
        
        fig_cm.update_layout(
            yaxis_title="Contribution Margin Ratio",
            yaxis_tickformat=".0%",
            coloraxis_showscale=False,
            margin=dict(l=40, r=40, t=60, b=40)
        )
        
        # Create Total Contribution pie chart
        fig_tc = px.pie(
            viz_data,
            values="Total Contribution",
            names="Product",
            title="Share of Total Contribution Margin",
            template="plotly_dark",
            hole=0.4
        )
        
        fig_tc.update_layout(
            margin=dict(l=40, r=40, t=60, b=40)
        )
        
        # Display charts side by side
        col5, col6 = st.columns(2)
        
        with col5:
            st.plotly_chart(fig_cm, use_container_width=True)
        
        with col6:
            st.plotly_chart(fig_tc, use_container_width=True)
        
        # Recommendations
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Product Strategy Recommendations</h3>", 
                    unsafe_allow_html=True)
        
        # Sort products by various metrics
        best_cm = max(products, key=lambda x: x["contribution_margin"])
        best_cm_ratio = max(products, key=lambda x: x["cm_ratio"])
        best_total_contribution = max(products, key=lambda x: x["total_contribution"])
        worst_cm_ratio = min(products, key=lambda x: x["cm_ratio"])
        
        # Display recommendations
        st.markdown(f"""
        Based on the product comparison analysis, here are some strategic recommendations:
        
        1. **Focus on High Contribution Products**: {best_total_contribution["product_name"]} contributes the most to your overall profitability (${best_total_contribution["total_contribution"]:.2f}). Consider allocating more marketing resources to this product.
        
        2. **Improve or Reconsider Low CM Products**: {worst_cm_ratio["product_name"]} has the lowest contribution margin ratio ({worst_cm_ratio["cm_ratio"]:.2%}). Consider either:
           - Increasing its price
           - Finding ways to reduce variable costs
           - Re-evaluating its place in your product mix
        
        3. **Pricing Strategy**: {best_cm_ratio["product_name"]} has the highest CM ratio ({best_cm_ratio["cm_ratio"]:.2%}). Consider using similar pricing strategies for other products.
        
        4. **Product Development**: Future products should aim for contribution margins similar to or better than {best_cm["product_name"]} (${best_cm["contribution_margin"]:.2f} per unit).
        """)
        
        # Export options
        st.markdown("<h3 style='text-align: left; color: #4CAF50;'>Export Comparison</h3>", 
                    unsafe_allow_html=True)
        
        st.markdown(create_excel_download_link(comparison_df, "product_comparison_results.xlsx"), 
                    unsafe_allow_html=True)