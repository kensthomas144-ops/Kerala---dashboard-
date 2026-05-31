import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Page Configuration
st.set_page_config(
    page_title="Kerala Central Command",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
st.markdown("---")

# സൈഡ്ബാർ സെറ്റിംഗ്സ്
st.sidebar.title("🔒 ACCESS CONTROL")
theme_choice = st.sidebar.radio("SYSTEM THEME", ["🌌 MILITARY DARK", "☀️ OPERATIONAL LIGHT"])
st.sidebar.success("SECURE CONNECTION: ACTIVE")
st.sidebar.info("System auto-refreshing every 3 seconds...")

# --- 🤖 1. NEW FEATURE: AI COMMAND CONTROL SYSTEM ---
st.header("🧠 AI OMNI-CONTROL INTERFACE (JARVIS CORE)")
ai_command = st.text_input("ENTER VOCAL/TEXT COMMAND FOR AI ASSTISTANT:", placeholder="e.g., activate shield, lockdown, standby")

# AI കമാൻഡ് അനുസരിച്ച് മാറുന്ന ഡിഫോൾട്ട് വാല്യൂസ്
default_shield = 98
default_siren = False
default_laser = True
ai_status_message = "AI Core is listening... Status: STABLE"

if ai_command:
    cmd = ai_command.lower().strip()
    if "shield" in cmd or "activate" in cmd:
        default_shield = 100
        default_laser = True
        ai_status_message = "🤖 AI: Executing Protocol 'Aegis'. Shield Maximized. Laser Grid Active."
    elif "lockdown" in cmd or "danger" in cmd:
        default_shield = 100
        default_siren = True
        default_laser = True
        ai_status_message = "🚨 AI: EMERGENCY LOCKDOWN ACTIVATED! Warning sirens blaring across all state grids!"
    elif "standby" in cmd or "safe" in cmd:
        default_shield = 50
        default_siren = False
        default_laser = False
        ai_status_message = "💤 AI: System entering power-saving standby mode. Grid on low-alert."
    else:
        ai_status_message = f"🤖 AI: Command '{ai_command}' analyzed. No immediate threat detected."

st.info(ai_status_message)
st.markdown("---")

# 🎛️ CENTRAL CONTROL SYSTEM PANEL (AI വാല്യൂസ് ഇവിടെ കണക്ട് ചെയ്തിരിക്കുന്നു)
st.header("🎛️ CENTRAL CONTROL SYSTEM PANEL")
col_ctrl1, col_ctrl2 = st.columns(2)

with col_ctrl1:
    st.subheader("⚡ Weapon & Shield Output")
    shield_power = st.slider("MANUAL SHIELD INTEGRITY OVERRIDE (%)", 0, 100, default_shield, key="shield_slider")
    active_sector = st.selectbox("TACTICAL DRONE SECTOR", ["Sector Alpha (North)", "Sector Bravo (Central)", "Sector Gamma (South)"], key="sector_select")

with col_ctrl2:
    st.subheader("🚨 System Status Toggle")
    siren_on = st.toggle("📢 ACTIVATE EMERGENCY SIREN", value=default_siren, key="siren_toggle")
    if siren_on:
        st.warning("🚨 EMERGENCY SIREN ACTIVATED IN ALL BASES! 🚨")
    
    laser_grid = st.toggle("🛡️ LASER GRID DEFENSE SYSTEM", value=default_laser, key="laser_toggle")
    if laser_grid:
        st.success("🔒 LASER GRID IS ACTIVE AND LETHAL.")
    else:
        st.error("⚠️ WARNING: LASER GRID IS DISABLED!")

st.markdown("---")

# 📊 മെട്രിക്കുകൾ
drone_count = random.randint(7100, 7500)
elevator_speed = round(random.uniform(4.1, 4.9), 2)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="🚀 KALINGA ELEVATOR SPEED", value=f"MACH {elevator_speed}", delta="VERTICAL ASCENT")
with col2:
    st.metric(label="🐝 CARGO DRONES IN AIR", value=f"{drone_count} Units", delta=f"{active_sector}")
with col3:
    st.metric(label="🛡️ DEFENSE SHIELD INTEGRITY", value=f"{shield_power}%", delta="AI BALANCED")

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

# 🔄 3 സെക്കൻഡ് നിർത്തിയ ശേഷം പേജ് തനിയെ റീഫ്രെഷ് ചെയ്യാനുള്ള വിദ്യ
time.sleep(3)
st.rerun()
