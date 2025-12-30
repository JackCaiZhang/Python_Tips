import panel as pn
import pandas as pd
import plotly.express as px

from data import load_data
from model import train_model
from metrics import evaluate

pn.extension("plotly")

df = load_data()

# ======================
# 控件
# ======================
alpha_slider = pn.widgets.FloatSlider(
    name="Ridge Alpha",
    start=0.01,
    end=10,
    step=0.1,
    value=1.0,
)

feature_selector = pn.widgets.Select(
    name="误差切片特征",
    options=["feature_1", "feature_2", "feature_3"],
)

# ======================
# 核心逻辑
# ======================
@pn.depends(alpha_slider)
def run_model(alpha):
    y_true, y_pred, X_test = train_model(df, alpha)
    metrics = evaluate(y_true, y_pred)

    result_df = X_test.copy()
    result_df["y_true"] = y_true.values
    result_df["y_pred"] = y_pred
    result_df["residual"] = y_pred - y_true.values

    return metrics, result_df

@pn.depends(alpha_slider)
def metric_cards(alpha):
    metrics, _ = run_model(alpha)
    return pn.Row(
        *[
            pn.indicators.Number(
                name=k,
                value=v,
                format="{value:.3f}",
                font_size="24pt",
            )
            for k, v in metrics.items()
        ]
    )

@pn.depends(alpha_slider)
def prediction_plot(alpha):
    _, result_df = run_model(alpha)
    fig = px.scatter(
        result_df,
        x="y_true",
        y="y_pred",
        title="真实值 vs 预测值",
        opacity=0.5,
    )
    fig.add_shape(
        type="line",
        x0=result_df["y_true"].min(),
        y0=result_df["y_true"].min(),
        x1=result_df["y_true"].max(),
        y1=result_df["y_true"].max(),
        line=dict(dash="dash"),
    )
    return fig

@pn.depends(alpha_slider, feature_selector)
def residual_slice(alpha, feature):
    _, result_df = run_model(alpha)

    bins = pd.qcut(
        result_df[feature],
        10,
        duplicates="drop"
    )

    result_df["feature_bin"] = bins.astype(str)

    fig = px.box(
        result_df,
        x="feature_bin",
        y="residual",
        title=f"残差在 {feature} 分位区间的分布",
    )
    return fig

# ======================
# 页面布局
# ======================
dashboard = pn.Column(
    "## 🧪 模型评估 & 误差诊断实验室",
    pn.Row(alpha_slider),
    metric_cards,
    prediction_plot,
    pn.Row(feature_selector),
    residual_slice,
)

dashboard.servable()
