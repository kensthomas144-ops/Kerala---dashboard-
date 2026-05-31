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

# സൈഡ്ബാർ സെറ്റിംഗ്സ്
st.sidebar.title("🔒 ACCESS CONTROL")
theme_choice = st.sidebar.radio("SYSTEM THEME", ["🌌 MILITARY DARK", "☀️ OPERATIONAL LIGHT"])
st.sidebar.success("SECURE CONNECTION: ACTIVE")
st.sidebar.info("System auto-refreshing every 3 seconds...")

# 🔄 ഓട്ടോമാറ്റിക് റീഫ്രെഷ് ഫങ്ക്ഷൻ
@st.fragment(run_every=3)
def render_dashboard():
    
    # 🚨 ലൈവ് അലേർട്ട് ടിക്കർ
    alerts = [
        "⚠️ ALERT: Unknown Drone spotted near Kochi Naval Grid.",
        "⚡ SYSTEM: Kalinga Elevator approaching MACH 4.8.",
        "🛡️ SHIELD: Cyber defense protocol activated for TVM Bunker.",
        "🌐 WEATHER: Heavy rain detected in Kozhikode Base."
    ]
    st.error(f"**LIVE SECURITY FEED:** {random.choice(alerts)}")

    st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
    st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
    st.markdown("---")

    # 🎛️ NEW FEATURE: CONTROL SYSTEM PANEL (രണ്ട് കോളം ആയി തിരിക്കുന്നു)
    st.header("🎛️ CENTRAL CONTROL SYSTEM PANEL")
    col_ctrl1, col_ctrl2 = st.columns(2)

    with col_ctrl1:
        st.subheader("⚡ Weapon & Shield Output")
        # സ്ലൈഡർ വഴി ഷീൽഡ് പവർ മാറ്റാം (യൂസർ കൺട്രോൾ)
        shield_power = st.slider("MANUAL SHIELD INTEGRITY OVERRIDE (%)", 0, 100, 98)
        # സെലക്ട് ബോക്സ് വഴി സെക്ടർ മാറ്റാം
        active_sector = st.selectbox("TACTICAL DRONE SECTOR", ["Sector Alpha (North)", "Sector Bravo (Central)", "Sector Gamma (South)"])

    with col_ctrl2:
        st.subheader("🚨 System Status Toggle")
        # ബട്ടണുകൾ (ക്ലിക്ക് ചെയ്യാൻ സാധിക്കുന്നത്)
        siren_on = st.button("📢 ACTIVATE EMERGENCY SIREN")
        if siren_on:
            st.warning("🚨 EMERGENCY SIREN ACTIVATED IN ALL BASES! 🚨")
        
        laser_grid = st.toggle("🛡️ LASER GRID DEFENSE SYSTEM", value=True)
        if laser_grid:
            st.success("🔒 LASER GRID IS ACTIVE AND LETHAL.")
        else:
            st.error("⚠️ WARNING: LASER GRID IS DISABLED!")

    st.markdown("---")

    # 📊 മെട്രിക്കുകൾ (സ്ലൈഡറിലെ വാല്യൂ കൂടി ഇവിടെ കണക്ട് ചെയ്തിട്ടുണ്ട്)
    drone_count = random.randint(7100, 7500)
    elevator_speed = round(random.uniform(4.1, 4.9), 2)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🚀 KALINGA ELEVATOR SPEED", value=f"MACH {elevator_speed}", delta="VERTICAL ASCENT")
    with col2:
        st.metric(label="🐝 CARGO DRONES IN AIR", value=f"{drone_count} Units", delta=f"{active_sector}")
    with col3:
        st.metric(label="🛡️ DEFENSE SHIELD INTEGRITY", value=f"{shield_power}%", delta="MANUAL OVERRIDE")

    st.markdown("---")

    # 🗺️ ലൈവ് മാപ്പും ഗ്രാഫും
    col_map, col_graph = st.columns([1, 1])

    with col_map:
        st.subheader("🌐 LIVE GEOSPATIAL GRID")
        map_data = pd.DataFrame({
            'lat': [8.5241, 9.9312, 11.2588],
            'lon': [76.9366, 76.2673, 75.7804]
        })
        st.map(map_data, zoom=6)

    with col_graph:
        st.subheader("📈 GRID PROCESSSING LOAD (REAL-TIME)")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['TVM Core', 'Kochi Grid', 'Kozhikode Base']
        )
        st.line_chart(chart_data)

    st.markdown("---")

    # 📋 കമാൻഡ് ബേസ് സ്റ്റാറ്റസ് ടേബിൾ
    st.subheader("📊 COMMAND BASE OPERATIONAL STATUS")
    status_data = pd.DataFrame({
        'COMMAND BASE': ['HQ: Thiruvananthapuram Bunker', 'Sub-Station: Kochi Naval Grid', 'Sub-Station: Kozhikode Air Base'],
        'SECURITY LEVEL': ['ALPHA (MAX)', 'BRAVO', 'ALPHA'],
        'WEAPONS SYSTEM': ['ONLINE', 'ONLINE', 'STANDBY']
    })
    st.dataframe(status_data, use_container_width=True)

# ഫങ്ക്ഷൻ റൺ ചെയ്യുന്നു
render_dashboard()
