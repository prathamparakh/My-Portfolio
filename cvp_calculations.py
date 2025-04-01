"""
CVP Analysis Calculation Module
Contains all calculation functions for CVP and Sales Mix Analysis
"""
import numpy as np
import pandas as pd

def calculate_cvp(fixed_costs, variable_cost_per_unit, selling_price_per_unit, sales_volume):
    """
    Calculate Cost-Volume-Profit metrics
    
    Parameters:
    -----------
    fixed_costs : float
        Total fixed costs
    variable_cost_per_unit : float
        Variable cost per unit
    selling_price_per_unit : float
        Selling price per unit
    sales_volume : int
        Current or expected sales volume in units
        
    Returns:
    --------
    dict
        Dictionary containing all calculated CVP metrics
    """
    # Input validation
    if selling_price_per_unit <= 0:
        return {"error": "Selling price must be greater than zero."}
    if variable_cost_per_unit < 0:
        return {"error": "Variable cost cannot be negative."}
    if fixed_costs < 0:
        return {"error": "Fixed costs cannot be negative."}
    if selling_price_per_unit <= variable_cost_per_unit:
        return {"error": "Selling price must be greater than variable cost per unit."}
    
    # Basic calculations
    contribution_margin = selling_price_per_unit - variable_cost_per_unit
    contribution_margin_ratio = contribution_margin / selling_price_per_unit
    break_even_units = fixed_costs / contribution_margin
    break_even_sales = break_even_units * selling_price_per_unit
    
    # Advanced calculations
    total_contribution_margin = contribution_margin * sales_volume
    variable_costs_total = variable_cost_per_unit * sales_volume
    total_costs = fixed_costs + variable_costs_total
    total_revenue = selling_price_per_unit * sales_volume
    operating_income = total_revenue - total_costs
    
    # Operating leverage calculation with safeguards
    if operating_income > 0:
        operating_leverage = total_contribution_margin / operating_income
    else:
        operating_leverage = float('inf')
    
    # Margin of safety calculation
    actual_sales = sales_volume * selling_price_per_unit
    if actual_sales > 0:
        margin_of_safety_units = sales_volume - break_even_units
        margin_of_safety_revenue = actual_sales - break_even_sales
        margin_of_safety_percentage = (margin_of_safety_revenue / actual_sales) * 100
    else:
        margin_of_safety_units = 0
        margin_of_safety_revenue = 0
        margin_of_safety_percentage = 0
    
    # Calculate profit or loss
    profit_loss = operating_income
    profit_per_unit = profit_loss / sales_volume if sales_volume > 0 else 0
    
    # Return comprehensive results dictionary
    return {
        'contribution_margin': contribution_margin,
        'contribution_margin_ratio': contribution_margin_ratio,
        'break_even_units': break_even_units,
        'break_even_sales': break_even_sales,
        'total_contribution_margin': total_contribution_margin,
        'variable_costs_total': variable_costs_total,
        'total_costs': total_costs,
        'total_revenue': total_revenue,
        'operating_income': operating_income,
        'operating_leverage': operating_leverage,
        'margin_of_safety_units': margin_of_safety_units,
        'margin_of_safety_revenue': margin_of_safety_revenue,
        'margin_of_safety': margin_of_safety_percentage,
        'profit_loss': profit_loss,
        'profit_per_unit': profit_per_unit
    }

def calculate_target_profit(fixed_costs, variable_cost, selling_price, target_profit):
    """
    Calculate units required to achieve target profit
    
    Parameters:
    -----------
    fixed_costs : float
        Total fixed costs
    variable_cost : float
        Variable cost per unit
    selling_price : float
        Selling price per unit
    target_profit : float
        Desired profit amount
        
    Returns:
    --------
    dict
        Dictionary containing target profit analysis results
    """
    # Input validation
    if selling_price <= variable_cost:
        return {"error": "Selling price must be greater than variable cost per unit."}
    
    # Calculate contribution margin
    contribution_margin = selling_price - variable_cost
    
    # Calculate target units and sales
    target_units = (fixed_costs + target_profit) / contribution_margin
    target_sales = target_units * selling_price
    
    # Calculate margin over target
    margin_over_target = contribution_margin / selling_price
    
    return {
        "contribution_margin": contribution_margin,
        "target_units": target_units,
        "target_sales": target_sales,
        "margin_over_target": margin_over_target
    }

def generate_sensitivity_analysis(base_params, param_to_vary, range_values):
    """
    Generate sensitivity analysis by varying one parameter
    
    Parameters:
    -----------
    base_params : dict
        Base parameters including fixed_costs, variable_cost_per_unit, 
        selling_price_per_unit, and sales_volume
    param_to_vary : str
        Parameter to vary ('fixed_costs', 'variable_cost_per_unit', 
        'selling_price_per_unit', or 'sales_volume')
    range_values : list
        List of values to use for the sensitivity analysis
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame containing sensitivity analysis results
    """
    results = []
    
    for value in range_values:
        # Create a copy of base parameters and update the varied parameter
        params = base_params.copy()
        params[param_to_vary] = value
        
        # Calculate CVP metrics with updated parameters
        cvp_results = calculate_cvp(
            params['fixed_costs'],
            params['variable_cost_per_unit'],
            params['selling_price_per_unit'],
            params['sales_volume']
        )
        
        # Skip if error
        if 'error' in cvp_results:
            continue
            
        # Add the varied parameter value and results to the list
        result_row = {
            param_to_vary: value,
            'break_even_units': cvp_results['break_even_units'],
            'operating_income': cvp_results['operating_income'],
            'margin_of_safety': cvp_results['margin_of_safety'],
            'operating_leverage': min(cvp_results['operating_leverage'], 100)  # Cap for visualization
        }
        results.append(result_row)
    
    # Convert list of dictionaries to DataFrame
    return pd.DataFrame(results)

def calculate_sales_mix(products, fixed_costs, target_profit=None):
    """
    Calculate sales mix analysis results
    
    Parameters:
    -----------
    products : list
        List of product dictionaries, each containing:
        - product_name: str
        - sell_price: float
        - var_cost: float
        - sales_volume: int
        - mix_percentage: float
    fixed_costs : float
        Total fixed costs
    target_profit : float, optional
        Desired target profit
        
    Returns:
    --------
    dict
        Dictionary containing sales mix analysis results
    """
    # Input validation
    if not products:
        return {"error": "No products provided for analysis."}
    
    for p in products:
        if p['sell_price'] <= p['var_cost']:
            return {"error": f"Selling price must be greater than variable cost for {p['product_name']}."}
    
    # Calculate weighted average contribution margin and selling price
    weighted_contribution_margin = sum(
        (p['sell_price'] - p['var_cost']) * (p['mix_percentage'] / 100) for p in products
    )
    
    weighted_selling_price = sum(
        p['sell_price'] * (p['mix_percentage'] / 100) for p in products
    )
    
    # Error handling for zero contribution margin
    if weighted_contribution_margin <= 0:
        return {"error": "Weighted contribution margin is zero or negative. Check product pricing and costs."}
    
    # Calculate break-even units and sales
    break_even_units = fixed_costs / weighted_contribution_margin
    break_even_sales = break_even_units * weighted_selling_price
    
    # Calculate break-even volume for each product
    break_even_product_volumes = {
        p['product_name']: break_even_units * (p['mix_percentage'] / 100) for p in products
    }
    
    # Target profit calculations
    target_units = None
    target_sales = None
    target_product_volumes = None
    
    if target_profit is not None:
        target_units = (fixed_costs + target_profit) / weighted_contribution_margin
        target_sales = target_units * weighted_selling_price
        target_product_volumes = {
            p['product_name']: target_units * (p['mix_percentage'] / 100) for p in products
        }
    
    # Calculate individual product metrics
    product_metrics = []
    for p in products:
        cm = p['sell_price'] - p['var_cost']
        cm_ratio = cm / p['sell_price'] if p['sell_price'] > 0 else 0
        
        product_metrics.append({
            'product_name': p['product_name'],
            'contribution_margin': cm,
            'contribution_margin_ratio': cm_ratio,
            'weighted_contribution': cm * (p['mix_percentage'] / 100),
            'percentage': p['mix_percentage']
        })
    
    # Return comprehensive results
    return {
        "weighted_contribution_margin": weighted_contribution_margin,
        "weighted_selling_price": weighted_selling_price,
        "break_even_units": break_even_units,
        "break_even_sales": break_even_sales,
        "break_even_product_volumes": break_even_product_volumes,
        "target_units": target_units,
        "target_sales": target_sales,
        "target_product_volumes": target_product_volumes,
        "product_metrics": product_metrics
    }

def calculate_optimal_sales_mix(products, fixed_costs, constraints=None):
    """
    Calculate the optimal sales mix to maximize profits
    
    Note: This is a simplified approach. For complex optimizations,
    you would use linear programming libraries like scipy.optimize.
    
    Parameters:
    -----------
    products : list
        List of product dictionaries with pricing and cost info
    fixed_costs : float
        Total fixed costs
    constraints : dict, optional
        Dictionary of constraints (e.g., max production capacity)
        
    Returns:
    --------
    dict
        Dictionary containing optimal sales mix results
    """
    # Calculate contribution margin for each product
    for product in products:
        product['contribution_margin'] = product['sell_price'] - product['var_cost']
    
    # Sort products by contribution margin (descending)
    sorted_products = sorted(products, key=lambda x: x['contribution_margin'], reverse=True)
    
    # Simple approach: Allocate more percentage to higher CM products
    # This is a very simplified approach - in practice, you would use
    # linear programming for true optimization
    
    total_cm = sum(p['contribution_margin'] for p in products)
    
    # Calculate suggested mix percentages based on CM ratio
    for product in sorted_products:
        product['suggested_percentage'] = (product['contribution_margin'] / total_cm) * 100 if total_cm > 0 else 0
    
    # Calculate metrics with suggested mix
    suggested_mix_products = sorted_products.copy()
    for p in suggested_mix_products:
        p['mix_percentage'] = p['suggested_percentage']
    
    suggested_mix_results = calculate_sales_mix(suggested_mix_products, fixed_costs)
    
    # Check for errors
    if 'error' in suggested_mix_results:
        return {"error": suggested_mix_results['error']}
    
    # Calculate improvement metrics
    current_weighted_cm = sum(
        (p['sell_price'] - p['var_cost']) * (p.get('original_percentage', p['mix_percentage']) / 100) 
        for p in products
    )
    
    improvement_percentage = ((suggested_mix_results['weighted_contribution_margin'] - current_weighted_cm) 
                             / current_weighted_cm) * 100 if current_weighted_cm > 0 else 0
    
    return {
        "sorted_products": sorted_products,
        "suggested_mix_results": suggested_mix_results,
        "improvement_percentage": improvement_percentage
    }

def calculate_target_profit_sales_mix(products, fixed_costs, target_profit):
    """
    Calculate the volume required for each product to achieve target profit
    
    Parameters:
    -----------
    products : list
        List of product dictionaries with pricing, cost and mix info
    fixed_costs : float
        Total fixed costs
    target_profit : float
        Desired profit amount
        
    Returns:
    --------
    dict
        Dictionary containing sales volume required for each product
    """
    # Calculate weighted contribution margin
    total_weighted_cm = sum(
        (p['sell_price'] - p['var_cost']) * (p['mix_percentage'] / 100) 
        for p in products
    )
    
    # Error handling
    if total_weighted_cm <= 0:
        return {"error": "Weighted contribution margin is zero or negative."}
    
    # Calculate total units needed
    target_units = (fixed_costs + target_profit) / total_weighted_cm
    
    # Calculate units for each product
    target_profit_sales_volume = {
        p['product_name']: target_units * (p['mix_percentage'] / 100) for p in products
    }
    
    # Calculate total sales
    target_total_sales = sum(
        p['sell_price'] * target_profit_sales_volume[p['product_name']] 
        for p in products
    )
    
    return {
        "total_weighted_contribution_margin": total_weighted_cm,
        "target_total_units": target_units,
        "target_profit_sales_volume": target_profit_sales_volume,
        "target_total_sales": target_total_sales
    }