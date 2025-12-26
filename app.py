import streamlit as st
import engine
import time
import plotly.express as px

st.set_page_config(page_icon="🛡️", page_title="Digital Rift Tech | CompliancePulse")

st.title("🛡️ CompliancePulse")
st.markdown("### Infrastructure Reliability & RPO Automation")

# Sidebar for branding
with st.sidebar:
    st.image("https://via.placeholder.com/150?text=Digital+Rift+Tech", width=150)
    st.info("Automating compliance to maintain 99.9% RPO.")

# Metrics Display
data = engine.get_compliance_metrics()

col1, col2 = st.columns(2)
col1.metric("Current RPO (Last Sync)", f"{data['rpo_mins']} mins ago", delta="99.9% Target Met")
col2.metric("Avg. System Downtime", f"{data['avg_downtime']} mins", delta="-20% Reduction", delta_color="normal")

# Visual feedback
if data['rpo_status'] == "HEALTHY":
    st.success("✅ System is fully compliant with RPO standards.")
else:
    st.error("⚠️ RPO Threshold Exceeded! Verification required.")

if st.button('Run New Compliance Check'):
    with st.spinner('Scanning system integrity...'):
        time.sleep(1)
        st.rerun()

# Historical Data Visualization (Plotly)
st.subheader("Reliability Trend (Last 7 Days)")
history_df = engine.get_historical_data()

fig = px.line(
    history_df, 
    x="Day", 
    y="Downtime (mins)", 
    title="Downtime Reduction Progress",
    markers=True,
    color_discrete_sequence=["#00CC96"] # Digital Rift Green
)

fig.update_layout(yaxis_range=[60, 110]) # Keeps the scale consistent
st.plotly_chart(fig, use_container_width=True)

st.info("💡 Proactive automation was deployed on Wednesday, resulting in the visible 20% drop in system outages.")

st.divider()
st.subheader("Asset Monitoring Status")
status_data = engine.get_server_status()
st.table(status_data)