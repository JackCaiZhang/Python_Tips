def attribution_analysis(df, dimension):
    """
    Calculate attribution metrics for a given dimension.

    Parameters
    ----------
    df : pandas.DataFrame
        A dataframe containing the columns 'exposure', 'clicks', and 'orders'
    dimension : str
        The column name in df to group by for attribution analysis

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the calculated attribution metrics: 'exposure', 'clicks', 'orders', and 'cvr'
    """

    result = (
        df.groupby(dimension)
        .agg(
            exposure=('exposure', 'sum'),
            clicks=('clicks', 'sum'),
            orders=('orders', 'sum')
        )
        .reset_index()
    )

    result['cvr'] = result['orders'] / result['clicks']
    return result.sort_values(by='cvr')