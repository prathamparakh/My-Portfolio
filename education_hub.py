"""
Education Hub for the CVP Analysis Tool
Provides educational resources and explanations for CVP concepts
"""
import streamlit as st

def run():
    """Display educational content about CVP Analysis"""
    
    st.markdown("<h1 style='text-align: left; color: #4CAF50;'>📚 Education Hub</h1>", unsafe_allow_html=True)
    st.write(
        """
        <div style='text-align: left;'>
        Welcome to the Education Hub! Here you can find resources to help you understand 
        Cost-Volume-Profit (CVP) analysis concepts and how to interpret the results.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Create tabs for different educational topics
    tab1, tab2, tab3, tab4 = st.tabs([
        "CVP Fundamentals", 
        "Key Metrics", 
        "Sales Mix Concepts", 
        "Interpretation Guide"
    ])
    
    with tab1:
        st.markdown("<h2 style='color: #4CAF50;'>Cost-Volume-Profit Analysis Fundamentals</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            ### What is CVP Analysis?
            
            Cost-Volume-Profit (CVP) analysis is a managerial accounting technique that examines the relationships between:
            
            - **Costs** (both fixed and variable)
            - **Volume** (sales quantity)
            - **Price** (selling price per unit)
            - **Profit** (the financial outcome)
            
            This analysis helps managers understand how changes in these factors affect a company's operating profit.
            
            ### The CVP Equation
            
            The basic CVP equation is:
            
            **Profit = (Price × Quantity) - (Variable Cost per Unit × Quantity) - Fixed Costs**
            
            This can be rewritten as:
            
            **Profit = (Contribution Margin per Unit × Quantity) - Fixed Costs**
            
            Where contribution margin per unit is the selling price minus the variable cost per unit.
            
            ### Assumptions of CVP Analysis
            
            CVP analysis relies on several assumptions:
            
            1. The selling price per unit remains constant
            2. Variable costs per unit remain constant
            3. Fixed costs remain constant within the relevant range
            4. In multi-product scenarios, the sales mix remains constant
            5. Productivity and efficiency remain constant
            6. There's a linear relationship between costs and volume
            """
        )
        
        st.info("CVP analysis is most accurate within a relevant range of activity where these assumptions hold true.")
    
    with tab2:
        st.markdown("<h2 style='color: #4CAF50;'>Key CVP Metrics and Formulas</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            ### Contribution Margin
            
            **Contribution Margin (per unit) = Selling Price per Unit - Variable Cost per Unit**
            
            This represents the portion of each sales dollar available to cover fixed costs and generate profit.
            
            ### Contribution Margin Ratio
            
            **Contribution Margin Ratio = Contribution Margin per Unit / Selling Price per Unit**
            
            This ratio shows the percentage of each sales dollar available to cover fixed costs and generate profit.
            
            ### Break-Even Point
            
            **Break-Even Point (in units) = Fixed Costs / Contribution Margin per Unit**
            
            This represents the volume of sales needed to cover all costs, resulting in zero profit.
            
            **Break-Even Point (in dollars) = Fixed Costs / Contribution Margin Ratio**
            
            ### Target Profit Analysis
            
            **Units Required for Target Profit = (Fixed Costs + Target Profit) / Contribution Margin per Unit**
            
            ### Margin of Safety
            
            **Margin of Safety = (Current Sales - Break-Even Sales) / Current Sales**
            
            This shows the percentage by which sales can drop before reaching the break-even point.
            
            ### Operating Leverage
            
            **Degree of Operating Leverage (DOL) = Contribution Margin / Operating Income**
            
            This measures the sensitivity of operating income to changes in sales volume.
            """
        )
        
        st.success("""
        **Quick Tip:** A higher contribution margin ratio indicates greater profit potential from each additional sale.
        """)
    
    with tab3:
        st.markdown("<h2 style='color: #4CAF50;'>Sales Mix Analysis Concepts</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            ### What is Sales Mix?
            
            Sales mix refers to the relative proportions of different products sold by a business. In a multi-product 
            company, the overall profitability depends not just on the total volume of sales, but also on the 
            mix of products sold.
            
            ### Weighted Average Contribution Margin
            
            When dealing with multiple products, we calculate a weighted average contribution margin:
            
            **Weighted CM = Σ [(CMᵢ) × (Sales Mix Percentageᵢ)]**
            
            Where CMᵢ is the contribution margin of product i.
            
            ### Break-Even in Sales Mix
            
            **Break-Even Units = Fixed Costs / Weighted Average Contribution Margin**
            
            ### Sales Mix Impact on Profitability
            
            Changes in sales mix can significantly impact profitability even when total sales volume remains constant. 
            Shifting the mix toward higher contribution margin products improves overall profitability.
            
            ### Optimal Product Mix
            
            The optimal product mix maximizes total contribution margin subject to various constraints such as:
            
            - Production capacity
            - Market demand
            - Resource availability
            - Minimum production requirements
            """
        )
        
        st.warning("""
        **Important:** In CVP analysis for multiple products, if the sales mix changes, the break-even point and 
        profit projections will also change.
        """)
    
    with tab4:
        st.markdown("<h2 style='color: #4CAF50;'>Interpretation Guide</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            ### How to Interpret CVP Analysis Results
            
            #### Break-Even Analysis Chart
            
            - The **intersection** of the total revenue and total cost lines represents the break-even point
            - The area **above** the break-even point represents profit
            - The area **below** the break-even point represents loss
            - The **steeper** the revenue line (compared to the cost line), the more profitable each additional unit sold
            
            #### Contribution Margin Ratio
            
            - Higher ratios indicate greater profitability potential
            - Use this to quickly estimate the impact of sales changes on profit
            
            #### Operating Leverage
            
            - **High operating leverage** (ratio > 5): Small changes in sales result in large changes in profit
            - **Low operating leverage** (ratio < 3): Changes in sales have a smaller impact on profit
            
            #### Margin of Safety
            
            - Higher values indicate lower risk
            - A margin of safety below 20% typically indicates higher business risk
            
            ### Making Business Decisions
            
            Use CVP analysis to evaluate:
            
            1. **Pricing decisions**: How will price changes affect profit?
            2. **Cost structure changes**: What happens if we shift between fixed and variable costs?
            3. **Product mix decisions**: Which products should we emphasize?
            4. **Target profit planning**: What volume is needed to achieve profit goals?
            5. **Risk assessment**: How vulnerable is the business to sales fluctuations?
            """
        )
        
        st.info("""
        **Pro Tip:** Always perform sensitivity analysis by varying key assumptions to understand the range of 
        possible outcomes.
        """)
    
    # Additional resources
    st.markdown("<h2 style='color: #4CAF50;'>Additional Resources</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Video Tutorials
        
        - [Understanding CVP Basics](https://www.youtube.com/results?search_query=cvp+analysis+tutorial)
        - [Break-Even Analysis Explained](https://www.youtube.com/results?search_query=break+even+analysis)
        - [Sales Mix Analysis for Multiple Products](https://www.youtube.com/results?search_query=sales+mix+analysis)
        """)
    
    with col2:
        st.markdown("""
        ### Recommended Reading
        
        - Managerial Accounting by Garrison, Noreen, and Brewer
        - Cost Accounting: A Managerial Emphasis by Horngren
        - Management Accounting: Concepts, Techniques, and Controversial Issues by Bierman
        """)
    
    # Glossary
    with st.expander("Glossary of Terms"):
        st.markdown("""
        - **Break-Even Point**: The level of sales at which total revenues equal total costs, resulting in zero profit.
        - **Contribution Margin**: The difference between selling price and variable cost per unit.
        - **Fixed Costs**: Costs that remain constant regardless of the volume of activity.
        - **Margin of Safety**: The excess of actual or budgeted sales over break-even sales.
        - **Operating Leverage**: A measure of how changes in sales affect operating income.
        - **Relevant Range**: The range of activity within which assumptions about cost behavior hold true.
        - **Sales Mix**: The relative proportions of products sold by a multi-product company.
        - **Target Profit**: A specified profit goal used to determine the required sales volume.
        - **Variable Costs**: Costs that change in direct proportion to the level of activity.
        """)