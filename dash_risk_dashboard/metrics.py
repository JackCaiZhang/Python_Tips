def calculate_risk_metrics(df):
    total = len(df)
    approved = df["approved"].sum()
    bad = df[df["approved"]]["bad"].sum()

    approval_rate = approved / total
    bad_rate = bad / approved if approved else 0

    return total, approval_rate, bad_rate
