# CVP Analysis Tool

A comprehensive web application for Cost-Volume-Profit (CVP) analysis and Sales Mix optimization to support business financial decision-making.

## Overview

The CVP Analysis Tool is a Streamlit-based web application designed to help businesses analyze their cost structures, break-even points, and profitability metrics. This tool enables decision-makers to understand the relationships between costs, sales volume, and profit, and to make informed decisions about pricing, product mix, and business strategy.

## Features

### Cost-Volume-Profit Analysis
- Calculate break-even points in units and dollars
- Determine contribution margin and contribution margin ratio
- Analyze operating leverage and margin of safety
- Perform target profit analysis
- Visualize cost-volume-profit relationships with interactive charts

### Sales Mix Analysis
- Analyze multiple products simultaneously
- Calculate weighted contribution margins
- Determine optimal product mix for maximum profitability
- Visualize sales mix distributions
- Compare product performance metrics

### Advanced Features
- Sensitivity analysis to see how changes in variables affect outcomes
- What-if scenario analysis for comparing different business scenarios
- Data export to Excel for further analysis
- Interactive visualizations for better insights
- Educational resources for understanding CVP concepts

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/prathamparakh/cvp_analysis.git
cd cvp_analysis
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

5. Access the application in your web browser at `http://localhost:8501`

## Usage Guide

### Basic CVP Analysis

1. Navigate to the "CVP Analysis" page from the sidebar
2. Enter your business parameters:
   - Fixed costs
   - Variable cost per unit
   - Selling price per unit
   - Sales volume
3. Specify a target profit amount if desired
4. Review the calculated metrics and visualizations
5. Use the sensitivity analysis tab to understand how changes in parameters affect profitability
6. Export results to Excel for sharing or further analysis

### Sales Mix Analysis

1. Navigate to the "Sales Mix Analysis" page from the sidebar
2. Enter your fixed costs and target profit
3. Specify the number of products in your mix
4. For each product, enter:
   - Product name
   - Selling price per unit
   - Variable cost per unit
   - Expected sales volume
5. Review the weighted contribution margin and break-even points
6. Analyze the product mix distribution and break-even chart
7. Use the optimal mix tab to identify the most profitable product mix
8. Compare individual product metrics to inform product strategy decisions

## Project Structure

```
cvp_analysis/
│
├── app.py                   # Main application entry point
├── requirements.txt         # Python dependencies
│
├── backend/                 # Backend modules
│   ├── __init__.py
│   ├── cvp_analysis.py      # CVP analysis UI module
│   ├── cvp_calculations.py  # Core calculation functions
│   ├── education_hub.py     # Educational resources
│   ├── home.py              # Home page
│   ├── sales_mix_analysis.py# Sales mix analysis UI module
│   ├── settings.py          # User settings 
│   └── utils.py             # Utility functions
│
└── screenshots/             # Application screenshots
    └── cvp_analysis.png     # Screenshot of application
```

## Educational Resources

The application includes an Education Hub with information about:
- CVP Analysis fundamentals
- Key metrics and formulas
- Sales Mix concepts
- Interpretation guide for analysis results
- Glossary of terms

## Contributing

Contributions to the CVP Analysis Tool are welcome! Please feel free to submit a Pull Request.

### Development Guidelines
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developed with ❤️ by Pratham Parakh
- Thanks to all the contributors who have helped to improve this tool.

## Contact

For any questions or feedback, please contact [pratham.parakh@example.com](mailto:pratham.parakh@example.com).

---

*Note: This tool is designed for
