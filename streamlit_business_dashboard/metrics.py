def calculate_metrics(df):
    """
    Calculate key metrics from the given dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        A dataframe containing the columns 'exposure', 'clicks', and 'orders'

    Returns
    -------
    dict
        A dictionary containing the calculated metrics: 'exposure', 'ctr', 'cvr', and 'orders'.
    """
    total_exposure = df['exposure'].sum()
    total_clicks = df['clicks'].sum()
    total_orders = df['orders'].sum()

    ctr = total_clicks / total_exposure if total_exposure > 0 else 0
    cvr = total_orders / total_clicks if total_clicks > 0 else 0

    return {
        'exposure': total_exposure,
        'ctr': ctr,
        'cvr': cvr,
        'orders': total_orders
    }