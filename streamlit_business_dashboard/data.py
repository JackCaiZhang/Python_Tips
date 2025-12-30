import pandas as pd
import numpy as np

def load_data(days=60):
    """
    Generate a sample dataset for streamlit business dashboard.

    Parameters
    ----------
    days : int, optional
        The number of days to generate data for, by default 60.

    Returns
    -------
    pd.DataFrame
        The generated dataset, with columns 'date', 'city', 
        'channel', 'user_type', 'exposure', 'clicks', 'orders'.
    """
    np.random.seed(42)

    dates = pd.date_range(end=pd.Timestamp.today(), periods=days)

    cities = ['北京', '上海', '广州', '深圳']
    channels = ['自然流量', '信息流', '搜索', '渠道合作']
    user_types = ['新用户', '老用户']

    data = []

    for date in dates:
        for city in cities:
            for channel in channels:
                for user in user_types:
                    exposure = np.random.randint(500, 3000)
                    ctr = np.random.uniform(0.05, 0.15)
                    cvr = np.random.uniform(0.01, 0.05)

                    # 人为制造异常
                    if city == '上海' and channel == '信息流' and date > dates[-7]:
                        cvr *= 0.6

                    clicks = int(exposure * ctr)
                    orders = int(clicks * cvr)

                    data.append([
                        date, city, channel, user,
                        exposure, clicks, orders
                    ])

    df = pd.DataFrame(
        data,
        columns=[
            'date', 'city', 'channel', 'user_type',
            'exposure', 'clicks', 'orders'
        ]
    )

    return df