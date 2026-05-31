import streamlit as st
import pandas as pd
import numpy as np
import random

# Page Configuration
st.set_page_config(
    page_title="Kerala Central Command",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
st.markdown("---")

st.sidebar.title("🔒 ACCESS CONTROL")
st.sidebar.success("SECURE CONNECTION: ACTIVE")
st.sidebar.info("System auto-refreshing every 3 seconds...")

# 🔄 ഈ ഫങ്ക്ഷൻ ഉള്ളിലുള്ള കാര്യങ്ങൾ ഓരോ 3 സെക്കൻഡിലും തനിയെ മാറും
@st.fragment(run_every=3)
def render_dashboard():
    # റാൻഡം ഡാറ്റ ജനറേഷൻ
    drone_count = random.randint(7100, 7500)
    elevator_speed = round(random.uniform(4.1, 4.9), 2)
    shield_status = random.randint(95, 100)

    # 📊 മെട്രിക്കുകൾ
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🚀 KALINGA ELEVATOR SPEED", value=f"MACH {elevator_speed}", delta="VERTICAL ASCENT")
    with col2:
        st.metric(label="🐝 CARGO DRONES IN AIR", value=f"{drone_count} Units", delta=f"{random.randint(-50, 50)} vs last min")
    with col3:
        st.metric(label="🛡️ DEFENSE SHIELD INTEGRITY", value=f"{shield_status}%", delta="STABLE")

    st.markdown("---")

    # 🗺️ ലൈവ് മാപ്പ്
    st.subheader("🌐 LIVE GEOSPATIAL SECURITY GRID (KERALA)")
    
    # മാപ്പിൽ കാണിക്കേണ്ട ലൊക്കേഷനുകൾ (Thiruvananthapuram, Kochi, Kozhikode)
    map_data = pd.DataFrame({
        'lat': [8.5241, 9.9312, 11.2588],
        'lon': [76.9366, 76.2673, 75.7804]
    })
    st.map(map_data, zoom=6)

    st.markdown("---")

    # 📋 മാപ്പിന് താഴെ കാണിക്കേണ്ട പുതിയ ഡാറ്റാ ടേബിൾ (New Feature!)
    st.subheader("📊 COMMAND BASE OPERATIONAL STATUS")
    
    status_data = pd.DataFrame({
        'COMMAND BASE': ['HQ: Thiruvananthapuram Bunker', 'Sub-Station: Kochi Naval Grid', 'Sub-Station: Kozhikode Air Base'],
        'LATITUDE': [8.5241, 9.9312, 11.2588],
        'LONGITUDE': [76.9366, 76.2673, 75.7804],
        'SECURITY LEVEL': ['ALPHA (MAX)', 'BRAVO', 'ALPHA'],
        'WEAPONS SYSTEM': ['ONLINE', 'ONLINE', 'STANDBY']
    })
    
    # ടേബിൾ വെബ്‌സൈറ്റിൽ കാണിക്കാൻ st.dataframe ഉപയോഗിക്കുന്നു
    st.dataframe(status_data, use_container_width=True)

# ഫങ്ക്ഷൻ റൺ ചെയ്യിക്കുന്നു
render_dashboard()
