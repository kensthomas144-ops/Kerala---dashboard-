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

# 🧠 SYSTEM MEMORY (Session State)
if "shield_val" not in st.session_state:
    st.session_state.shield_val = 98
if "siren_val" not in st.session_state:
    st.session_state.siren_val = False
if "laser_val" not in st.session_state:
    st.session_state.laser_val = True
if "ai_msg" not in st.session_state:
    st.session_state.ai_msg = "AI Core is listening... Status: STABLE"

st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
st.markdown("---")

# 🤖 AI COMMAND CONTROL SYSTEM
st.header("🧠 AI OMNI-CONTROL INTERFACE (JARVIS CORE)")

# ഈ ഫങ്ക്ഷൻ വഴി കമാൻഡ് റൺ ചെയ്ത ഉടൻ ഇൻപുട്ട് ബോക്സ് തനിയെ ക്ലിയർ ചെയ്യും
def process_command():
    raw_cmd = st.session_state.cmd_input
    if raw_cmd:
        cmd = raw_cmd.lower().strip()
        if "shield" in cmd or "activate" in cmd:
            st.session_state.shield_val = 100
            st.session_state.laser_val = True
            st.session_state.ai_msg = "🤖 AI: Executing Protocol 'Aegis'. Shield Maximized. Laser Grid Active."
        elif "lockdown" in cmd or "danger" in cmd:
            st.session_state.shield_val = 100
            st.session_state.siren_val = True
            st.session_state.laser_val = True
            st.session_state.ai_msg = "🚨 AI: EMERGENCY LOCKDOWN ACTIVATED! Warning sirens blaring across all state grids!"
        elif "standby" in cmd or "safe" in cmd:
            st.session_state.shield_val = 50
            st.session_state.siren_val = False
            st.session_state.laser_val = False
            st.session_state.ai_msg = "💤 AI: System entering power-saving standby mode. Grid on low-alert."
        else:
            st.session_state.ai_msg = f"🤖 AI: Command '{raw_cmd}' analyzed. No immediate action required."
        
        # കമാൻഡ് മെമ്മറിയിൽ എടുത്ത ശേഷം ബോക്സ് ഒഴിഞ്ഞതാക്കുന്നു
        st.session_state.cmd_input = ""

# ഇൻപുട്ട് ബോക്സ് (on_change ഉപയോഗിച്ച് ഫങ്ക്ഷൻ കണക്ട് ചെയ്തിരിക്കുന്നു)
st.text_input("ENTER VOCAL/TEXT COMMAND FOR AI ASSTISTANT:", placeholder="e.g., activate shield, lockdown, standby", key="cmd_input", on_change=process_command)

# നിലവിലെ AI മെസ്സേജ് കാണിക്കുന്നു
st.info(st.session_state.ai_msg)
st.markdown("---")

# 🔒 സൈഡ്ബാർ സെറ്റിംഗ്സ്
st.sidebar.title("🔒 ACCESS CONTROL")
theme_choice = st.sidebar.radio("SYSTEM THEME", ["🌌 MILITARY DARK", "☀️ OPERATIONAL LIGHT"])
st.sidebar.success("SECURE CONNECTION: ACTIVE")
st.sidebar.info("System auto-refreshing every 3 seconds...")

# 🎛️ CENTRAL CONTROL SYSTEM PANEL
st.header("🎛️ CENTRAL CONTROL SYSTEM PANEL")
col_ctrl1, col_ctrl2 = st.columns(2)

with col_ctrl1:
    st.subheader("⚡ Weapon & Shield Output")
    # സ്ലൈഡർ മെമ്മറിയുമായി സിങ്ക് ചെയ്തിരിക്കുന്നു
    shield_power = st.slider("MANUAL SHIELD INTEGRITY OVERRIDE (%)", 0, 100, value=st.session_state.shield_val, key="shield_slider_manual")
    active_sector = st.selectbox("TACTICAL DRONE SECTOR", ["Sector Alpha (North)", "Sector Bravo (Central)", "Sector Gamma (South)"], key="sector_select")

with col_ctrl2:
    st.subheader("🚨 System Status Toggle")
    siren_on = st.toggle("📢 ACTIVATE EMERGENCY SIREN", value=st.session_state.siren_val, key="siren_toggle_manual")
    if siren_on:
        st.warning("🚨 EMERGENCY SIREN ACTIVATED IN ALL BASES! 🚨")
    
    laser_grid = st.toggle("🛡️ LASER GRID DEFENSE SYSTEM", value=st.session_state.laser_val, key="laser_toggle_manual")
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

# 🔄 3 സെക്കൻഡ് നിർത്തിയ ശേഷം പേജ് തനിയെ റീഫ്രെഷ് ചെയ്യാനുള്ള വിദ്യ
time.sleep(3)
st.rerun()
