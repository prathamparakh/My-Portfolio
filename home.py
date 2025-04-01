"""
Home page for the CVP Analysis Tool
"""
import streamlit as st

def run():
    """Display the home page content"""
    # Welcome section
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 30px;">
            <h2>Welcome to the CVP Analysis Tool</h2>
            <p style="font-size: 1.2em;">A powerful platform for business financial analysis and decision-making</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Main features in cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="color: #4CAF50;">📈 CVP Analysis</h3>
                <p>Perform comprehensive Cost-Volume-Profit analysis to understand your business's break-even point, profit potential, and financial structure.</p>
                <ul>
                    <li>Calculate break-even points in units and dollars</li>
                    <li>Determine contribution margin and ratio</li>
                    <li>Analyze operating leverage and margin of safety</li>
                    <li>Visualize cost-volume-profit relationships</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="color: #4CAF50;">🧩 Sales Mix Analysis</h3>
                <p>Optimize your product mix to maximize profitability and understand how different product combinations affect your bottom line.</p>
                <ul>
                    <li>Analyze multiple products simultaneously</li>
                    <li>Calculate weighted contribution margins</li>
                    <li>Determine optimal product mix</li>
                    <li>Visualize sales mix distributions and break-even points</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # New features section
    st.markdown(
        """
        <div style="text-align: center; margin: 40px 0 20px 0;">
            <h2>New Features</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; height: 150px;">
                <h4 style="color: #4CAF50;">📊 Sensitivity Analysis</h4>
                <p>Understand how changes in price, costs, and volume affect your profitability with interactive sensitivity charts.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; height: 150px;">
                <h4 style="color: #4CAF50;">💾 Data Export</h4>
                <p>Export your analysis results to Excel or CSV format for sharing or further analysis in other tools.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; height: 150px;">
                <h4 style="color: #4CAF50;">📚 Education Hub</h4>
                <p>Access educational resources to help you understand CVP concepts and make better business decisions.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Getting started section
    st.markdown(
        """
        <div style="text-align: center; margin: 40px 0 20px 0;">
            <h2>Getting Started</h2>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px;">
            <p>Follow these steps to get started with the CVP Analysis Tool:</p>
            <ol>
                <li>Select your desired analysis type from the sidebar menu</li>
                <li>Enter your business parameters in the input fields</li>
                <li>Review the calculated metrics and visualizations</li>
                <li>Adjust parameters to perform what-if analysis</li>
                <li>Export your results or save your scenarios for future reference</li>
            </ol>
            <p>Need help? Visit the Education Hub for tutorials and resources.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Call to action
    st.markdown(
        """
        <div style="text-align: center; margin: 40px 0;">
            <h3>Ready to analyze your business?</h3>
            <p>Select an analysis type from the sidebar to begin.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )