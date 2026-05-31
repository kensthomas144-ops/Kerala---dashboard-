import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# Page Configuration
st.set_page_config(
    page_title="Kerala Central Command",
    page_icon="🚨",
    layout="wide"
)

# സുഗമമായ റീഫ്രെഷിങ്ങിനായി ചെറിയൊരു ഡിലേ
time.sleep(0.5)

st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
st.markdown("---")

st.sidebar.title("🔒 ACCESS CONTROL")
st.sidebar.success("SECURE CONNECTION: ACTIVE")
st.sidebar.info("System auto-refreshing every 3 seconds...")

# റാൻഡം ഡാറ്റ (ഓരോ 3 സെക്കൻഡിലും ഇത് തനിയെ മാറും)
drone_count = random.randint(7100, 7500)
elevator_speed = round(random.uniform(4.1, 4.9), 2)
shield_status = random.randint(95, 100)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🚀 KALINGA ELEVATOR SPEED", value=f"MACH {elevator_speed}", delta="VERTICAL ASCENT")
with col2:
    st.metric(label="🐝 CARGO DRONES IN AIR", value=f"{drone_count} Units", delta=f"{random.randint(-50, 50)} vs last min")
with col3:
    st.metric(label="🛡️ DEFENSE SHIELD INTEGRITY", value=f"{shield_status}%", delta="STABLE")

st.markdown("---")

# LIVE MAP
st.subheader("🌐 LIVE GEOSPATIAL SECURITY GRID (KERALA)")
map_data = pd.DataFrame({
    'lat': [8.5241, 9.9312, 11.2588],  # TVM, Kochi, Kozhikode
    'lon': [76.9366, 76.2673, 75.7804]
})
st.map(map_data, zoom=6)

# ഓട്ടോമാറ്റിക് റീഫ്രെഷ് ട്രിഗർ ചെയ്യാനുള്ള കമാൻഡ്
st.rerun()
