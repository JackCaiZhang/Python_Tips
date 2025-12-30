import pandas as pd
import numpy as np

def load_data(days=60, daily_samples=800):
    np.random.seed(42)

    dates = pd.date_range(end=pd.Timestamp.today(), periods=days)
    rows = []

    for date in dates:
        for _ in range(daily_samples):
            score = np.random.normal(600, 50)

            # 最近一周风险上升（分布漂移）
            if date >= dates[-7]:
                score -= np.random.normal(20, 10)

            approved = score > 580
            bad = np.random.rand() < (0.08 if approved else 0.15)

            rows.append([
                date, score, approved, bad
            ])

    return pd.DataFrame(
        rows,
        columns=["date", "score", "approved", "bad"]
    )
