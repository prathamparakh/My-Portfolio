"""
CVP Analysis Tool - Main Application
A web application for Cost-Volume-Profit analysis and Sales Mix Analysis.
"""
import streamlit as st
from backend.utils import set_custom_theme

# Set up Streamlit page with enhanced design
st.set_page_config(
    page_title="CVP Analysis Tool",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Apply custom theme and styling
set_custom_theme()

# App header and description
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #4CAF50;">📊 CVP Analysis Tool</h1>
        <p style="font-size: 1.2em;">Comprehensive tool for Cost-Volume-Profit Analysis and Sales Mix Optimization</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Sidebar for page navigation with improved styling
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h3>Navigation Menu</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # More descriptive page options with icons
    page = st.selectbox(
        "Choose Analysis Type",
        [
            "🏠 Home",
            "📈 CVP Analysis",
            "🧩 Sales Mix Analysis",
            "📚 Education Hub",
            "⚙️ Settings"
        ]
    )

# Importing and running relevant module based on selected analysis type
if page == "🏠 Home":
    from backend import home
    home.run()
elif page == "📈 CVP Analysis":
    from backend import cvp_analysis
    cvp_analysis.run()
elif page == "🧩 Sales Mix Analysis":
    from backend import sales_mix_analysis 
    sales_mix_analysis.run()
elif page == "📚 Education Hub":
    from backend import education_hub
    education_hub.run()
elif page == "⚙️ Settings":
    from backend import settings
    settings.run()

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 10px; border-top: 1px solid #ddd;">
    <p>CVP Analysis Tool - Developed with ❤️</p>
</div>
""", unsafe_allow_html=True)