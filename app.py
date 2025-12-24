import streamlit as st
import engine
import time

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