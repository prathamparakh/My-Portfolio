"""
Settings page for the CVP Analysis Tool
Allows users to configure application preferences
"""
import streamlit as st
import json
import os

# Default settings
DEFAULT_SETTINGS = {
    "currency_symbol": "$",
    "decimal_places": 2,
    "color_theme": "default",
    "chart_template": "plotly_dark",
    "show_annotations": True,
    "auto_calculate": True
}

def load_settings():
    """Load user settings or create default if not exists"""
    try:
        if os.path.exists("settings.json"):
            with open("settings.json", "r") as f:
                return json.load(f)
        return DEFAULT_SETTINGS
    except Exception:
        return DEFAULT_SETTINGS

def save_settings(settings):
    """Save user settings to file"""
    try:
        with open("settings.json", "w") as f:
            json.dump(settings, f)
        return True
    except Exception:
        return False

def run():
    """Display and manage settings page"""
    st.markdown("<h1 style='text-align: left; color: #4CAF50;'>⚙️ Settings</h1>", unsafe_allow_html=True)
    st.write(
        """
        <div style='text-align: left;'>
        Configure your application preferences to customize your experience with the CVP Analysis Tool.
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Load current settings
    settings = load_settings()
    
    # Create settings form
    with st.form("settings_form"):
        st.markdown("### Display Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            currency_symbol = st.text_input("Currency Symbol", value=settings["currency_symbol"])
            decimal_places = st.number_input("Decimal Places", 
                                           min_value=0, 
                                           max_value=4, 
                                           value=settings["decimal_places"])
        
        with col2:
            color_theme = st.selectbox("Color Theme", 
                                     options=["default", "blue", "green", "purple"],
                                     index=["default", "blue", "green", "purple"].index(settings["color_theme"]))
            
            chart_template = st.selectbox("Chart Template", 
                                        options=["plotly_dark", "plotly", "plotly_white", "ggplot2"],
                                        index=["plotly_dark", "plotly", "plotly_white", "ggplot2"].index(settings["chart_template"]))
        
        st.markdown("### Calculation Settings")
        
        col3, col4 = st.columns(2)
        
        with col3:
            show_annotations = st.checkbox("Show Chart Annotations", value=settings["show_annotations"])
        
        with col4:
            auto_calculate = st.checkbox("Auto-Calculate Results", value=settings["auto_calculate"])
        
        # Save button
        submitted = st.form_submit_button("Save Settings")
        
        if submitted:
            # Update settings
            new_settings = {
                "currency_symbol": currency_symbol,
                "decimal_places": decimal_places,
                "color_theme": color_theme,
                "chart_template": chart_template,
                "show_annotations": show_annotations,
                "auto_calculate": auto_calculate
            }
            
            # Save settings to file
            if save_settings(new_settings):
                st.success("Settings saved successfully!")
                # Update session state
                for key, value in new_settings.items():
                    settings[key] = value
            else:
                st.error("Failed to save settings. Please try again.")
    
    # Reset to defaults button (outside the form)
    if st.button("Reset to Defaults"):
        if save_settings(DEFAULT_SETTINGS):
            st.success("Settings reset to defaults. Please refresh the page.")
        else:
            st.error("Failed to reset settings. Please try again.")
    
    # Display current active settings
    st.markdown("### Current Settings")
    
    st.json(settings)
    
    # Help section
    with st.expander("Settings Help"):
        st.markdown("""
        - **Currency Symbol**: The symbol used to display monetary values (e.g., $, €, £)
        - **Decimal Places**: The number of decimal places to display in numerical results
        - **Color Theme**: The color scheme used throughout the application
        - **Chart Template**: The visual style of charts and graphs
        - **Show Chart Annotations**: Whether to display annotations on charts (labels, arrows, etc.)
        - **Auto-Calculate Results**: Automatically update results when input values change
        """)