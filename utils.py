"""
Utility functions for the CVP Analysis Tool
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import io
import base64

# Color scheme for the application
COLOR_SCHEME = {
    'primary': '#4CAF50',
    'secondary': '#2196F3',
    'accent': '#FFC107',
    'fixed_costs': '#2196F3',
    'total_cost': '#FF5722',
    'revenue': '#4CAF50',
    'break_even': '#FFFFFF',
    'target_profit': '#FFEB3B',
    'background': '#0E1117',
    'text': '#FFFFFF',
    'highlight': '#FFD700'
}

def set_custom_theme():
    """Set custom CSS styles for the Streamlit application"""
    st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .st-bx {
        background-color: #1E1E1E;
    }
    .st-cb {
        border-radius: 10px;
    }
    .stNumberInput, .stSelectbox {
        border-radius: 8px;
    }
    .stButton>button {
        border-radius: 8px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 15px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #3d8c40;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0px 0px;
        padding: 10px 20px;
        background-color: #2c2c2c;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50;
        color: white;
    }
    .metric-container {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 10px 0;
    }
    .metric-label {
        font-size: 0.9em;
        color: #CCC;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 1.8em;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)
    
def validate_input_greater_than(value, min_value, message):
    """Validate that an input is greater than a minimum value"""
    if value <= min_value:
        st.sidebar.error(message)
        return False
    return True

def display_custom_metric(label, value, description=None, color=COLOR_SCHEME['primary']):
    """Display a metric with custom styling"""
    st.markdown(f"""
    <div class="metric-container">
        <div class="metric-label">{label}</div>
        <div class="metric-value" style="color: {color};">{value}</div>
        {f'<div style="font-size: 0.8em; margin-top: 5px; color: #AAA;">{description}</div>' if description else ''}
    </div>
    """, unsafe_allow_html=True)

def create_excel_download_link(df, filename="data.xlsx", sheet_name="Sheet1"):
    """Create a download link for a DataFrame as an Excel file"""
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Add some styling to the Excel file
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    
    # Add a header format
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Write the column headers with the defined format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        
    # Set column widths
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(i, i, max_len)
        
    writer.close()
    
    # Create a download link
    b64 = base64.b64encode(output.getvalue()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}" class="download-link">Download Excel File</a>'
    return href

def create_plotly_break_even_chart(fixed_costs, volume_range, total_costs, total_revenues, 
                                  break_even_point, break_even_revenue,
                                  target_profit_point=None, target_profit_revenue=None):
    """
    Create a plotly break-even chart for CVP analysis
    """
    fig = go.Figure()
    
    # Add fixed costs line
    fig.add_trace(go.Scatter(
        x=volume_range,
        y=[fixed_costs] * len(volume_range),
        mode='lines',
        name='Fixed Costs',
        line=dict(color=COLOR_SCHEME['fixed_costs'], width=2, dash='dash')
    ))
    
    # Add total costs line
    fig.add_trace(go.Scatter(
        x=volume_range,
        y=total_costs,
        mode='lines',
        name='Total Cost',
        line=dict(color=COLOR_SCHEME['total_cost'], width=2)
    ))
    
    # Add total revenue line
    fig.add_trace(go.Scatter(
        x=volume_range,
        y=total_revenues,
        mode='lines',
        name='Total Revenue',
        line=dict(color=COLOR_SCHEME['revenue'], width=2)
    ))
    
    # Add profit area (shaded region between revenue and cost)
    fig.add_trace(go.Scatter(
        x=volume_range,
        y=total_revenues,
        mode='none',
        name='Profit Area',
        fill='tonexty',
        fillcolor='rgba(76, 175, 80, 0.2)',
        showlegend=False
    ))
    
    # Add break-even line
    fig.add_trace(go.Scatter(
        x=[break_even_point, break_even_point],
        y=[0, break_even_revenue],
        mode='lines',
        name='Break-Even Point',
        line=dict(color=COLOR_SCHEME['break_even'], width=2, dash='dot')
    ))
    
    # Add break-even annotation
    fig.add_annotation(
        x=break_even_point,
        y=break_even_revenue,
        text="Break-Even",
        showarrow=True,
        arrowhead=7,
        ax=0,
        ay=-40,
        arrowcolor=COLOR_SCHEME['break_even'],
        font=dict(color=COLOR_SCHEME['break_even'])
    )
    
    # Add target profit line if provided
    if target_profit_point is not None and target_profit_revenue is not None:
        fig.add_trace(go.Scatter(
            x=[target_profit_point, target_profit_point],
            y=[0, target_profit_revenue],
            mode='lines',
            name='Target Profit Point',
            line=dict(color=COLOR_SCHEME['target_profit'], width=2, dash='dot')
        ))
        
        # Add target profit annotation
        fig.add_annotation(
            x=target_profit_point,
            y=target_profit_revenue,
            text="Target Profit",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40,
            arrowcolor=COLOR_SCHEME['target_profit'],
            font=dict(color=COLOR_SCHEME['target_profit'])
        )
    
    # Format and display the plot
    fig.update_layout(
        title="Break-Even Analysis Chart",
        xaxis_title='Sales Volume (Units)',
        yaxis_title='Amount ($)',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template="plotly_dark",
        margin=dict(l=40, r=40, t=60, b=40),
        hovermode="x unified"
    )
    
    return fig

def create_sensitivity_analysis_chart(sensitivity_data, x_column, y_column, title, template="plotly_dark"):
    """Create a line chart for sensitivity analysis"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=sensitivity_data[x_column],
        y=sensitivity_data[y_column],
        mode='lines+markers',
        line=dict(color=COLOR_SCHEME['primary'], width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_column,
        yaxis_title=y_column,
        template=template,
        hovermode="x unified"
    )
    
    return fig