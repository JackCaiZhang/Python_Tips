from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from data import load_data
from metrics import calculate_risk_metrics
from psi import calculate_psi

df = load_data()

app = Dash(__name__)
app.title = "风控策略监控仪表板"

# ======================
# 布局
# ======================
app.layout = html.Div(
    style={"padding": "20px", "fontFamily": "Arial"},
    children=[
        html.H2("💳 信贷风控策略 & 模型稳定性监控"),

        html.Div(id="kpi", style={"display": "flex", "gap": "50px"}),

        html.Hr(),

        html.H4("📈 风险指标趋势"),
        dcc.Graph(id="risk-trend"),

        html.Hr(),

        html.H4("📉 模型分数分布"),
        dcc.Graph(id="score-dist"),

        html.Hr(),

        html.H4("🚨 模型稳定性 PSI"),
        html.Div(id="psi-value"),
    ],
)

# ======================
# KPI
# ======================
@app.callback(
    Output("kpi", "children"),
    Input("risk-trend", "id"),
)
def update_kpi(_):
    total, approval_rate, bad_rate = calculate_risk_metrics(df)

    return [
        html.Div([html.H4("进件量"), html.H3(f"{total:,}")]),
        html.Div([html.H4("通过率"), html.H3(f"{approval_rate:.2%}")]),
        html.Div([html.H4("坏账率"), html.H3(f"{bad_rate:.2%}")]),
    ]

# ======================
# 风险趋势
# ======================
@app.callback(
    Output("risk-trend", "figure"),
    Input("score-dist", "id"),
)
def update_trend(_):
    daily = (
        df.groupby("date")
        .apply(lambda x: x[x["approved"]]["bad"].mean())
        .reset_index(name="bad_rate")
    )

    return px.line(
        daily,
        x="date",
        y="bad_rate",
        title="通过样本坏账率趋势",
    )

# ======================
# 分数分布
# ======================
@app.callback(
    Output("score-dist", "figure"),
    Input("risk-trend", "id"),
)
def update_distribution(_):
    return px.histogram(
        df,
        x="score",
        nbins=40,
        title="模型评分分布",
    )

# ======================
# PSI
# ======================
@app.callback(
    Output("psi-value", "children"),
    Input("score-dist", "id"),
)
def update_psi(_):
    baseline = df[df["date"] < df["date"].quantile(0.8)]["score"]
    recent = df[df["date"] >= df["date"].quantile(0.8)]["score"]

    psi = calculate_psi(baseline, recent)

    level = "🟢 稳定"
    if psi > 0.25:
        level = "🔴 严重漂移"
    elif psi > 0.1:
        level = "🟠 轻微漂移"

    return html.H3(f"PSI = {psi:.3f}  {level}")


if __name__ == "__main__":
    app.run(debug=True)
