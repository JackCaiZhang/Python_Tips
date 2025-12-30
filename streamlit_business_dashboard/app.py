import streamlit as st
from data import load_data
from metrics import calculate_metrics
from anomaly import detect_cvr_anomaly
from analysis import attribution_analysis

st.set_page_config(page_title='业务异常监控平台', layout='wide')

st.title('📊 业务异常监控 & 归因分析平台')

# 加载数据
df = load_data()

# ======================
# 指标总览
# ======================
st.header('📌 核心指标')

metrics = calculate_metrics(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric('曝光量', f"{metrics['exposure']:,}")
col2.metric('点击率 CTR', f"{metrics['ctr']:.2%}")
col3.metric('转化率 CVR', f"{metrics['cvr']:.2%}")
col4.metric('订单量', f"{metrics['orders']:,}")

# ======================
# 异常检测
# ======================
st.header("🚨 转化率异常检测")

daily, anomalies = detect_cvr_anomaly(df)

st.line_chart(daily.set_index('date')['cvr'])

if anomalies.empty:
    st.success('暂无明显异常')
else:
    st.error('检测到转化率异常')
    st.dataframe(anomalies[['date', 'cvr', 'z_score']])

# ======================
# 归因分析
# ======================
st.header("🔍 归因分析")

dimension = st.selectbox(
    '选择分析维度',
    ['city', 'channel', 'user_type']
)

result = attribution_analysis(df, dimension)
st.bar_chart(result.set_index(dimension)['cvr'])

st.dataframe(result)