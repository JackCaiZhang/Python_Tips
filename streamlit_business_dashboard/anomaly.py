import pandas as pd

def detect_cvr_anomaly(df):
    """
    Detects anomalies in conversion rate (CVR) by calculating the mean 
    and standard deviation of CVR over a 7-day rolling window, and then 
    calculating the z-score of each day's CVR. Days with a z-score greater 
    than 2 are considered anomalies.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe containing click and order data with a date index.

    Returns
    -------
    daily : pandas.DataFrame
        Dataframe containing the daily CVR, mean and standard deviation 
        of CVR over a 7-day rolling window, and the z-score of each day's CVR.
    anomalies : pandas.DataFrame
        Dataframe containing the anomalies detected.
    """
    daily = (
        df.groupby('date')
        .agg(clicks=('clicks', 'sum'), orders=('orders', 'sum'))
        .reset_index()
    )

    daily['cvr'] = daily['orders'] / daily['clicks']
    daily['mean_7d'] = daily['cvr'].rolling(7).mean()
    daily['std_7d'] = daily['cvr'].rolling(7).std()

    daily['z_score'] = (daily['cvr'] - daily['mean_7d']) / daily['std_7d']

    anomalies = daily[daily['z_score'].abs() > 2]

    return daily, anomalies