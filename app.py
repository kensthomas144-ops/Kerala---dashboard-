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
if "radar_angle" not in st.session_state:
    st.session_state.radar_angle = 0

# റഡാർ സ്കാനിംഗ് ആനിമേഷൻ
st.session_state.radar_angle = (st.session_state.radar_angle + 20) % 360

st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
st.markdown("---")

# 🔒 SIDEBAR ACCESS
st.sidebar.title("🔒 ACCESS CONTROL")
theme_choice = st.sidebar.radio("SYSTEM THEME", ["🌌 MILITARY DARK", "☀️ OPERATIONAL LIGHT"])
st.sidebar.success("SECURE CONNECTION: ACTIVE")
st.sidebar.info("System auto-refreshing every 3 seconds...")

# 🎛️ OMNI OPTIONS (TABS) - അഞ്ചാമത്തെ പുതിയ ടാബ് ആഡ് ചെയ്തിരിക്കുന്നു
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🧠 AI CORE INTELLIGENCE", 
    "🎛️ CENTRAL CONTROL PANEL", 
    "🛰️ GEOSPATIAL & RADAR", 
    "📊 SYSTEM METRICS & STATUS",
    "🛸 TRANSIT & FLIGHT TRACKER"  # New Feature!
])

# ==========================================
# 🧠 OPTION 1: AI CORE INTELLIGENCE
# ==========================================
with tab1:
    st.header("🧠 AI OMNI-CONTROL INTERFACE (JARVIS CORE)")
    
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
            
            st.session_state.cmd_input = ""

    st.text_input("ENTER VOCAL/TEXT COMMAND FOR AI ASSTISTANT:", placeholder="e.g., activate shield, lockdown, standby", key="cmd_input", on_change=process_command)
    st.info(st.session_state.ai_msg)
    
    st.markdown("---")
    
    col_bio1, col_bio2 = st.columns(2)
    with col_bio1:
        st.subheader("🔑 BIOMETRIC ACCESS LOG")
        st.code("""
👤 USER: CHIEF MINISTER
🔑 KEY: OPTICAL_SCAN_OK
🛡️ RANK: SUPREME COMMANDER
🌐 IP: 10.0.0.99 [SECURE]
        """, language="markdown")
    with col_bio2:
        st.subheader("⚡ QUANTUM CORE LOAD")
        st.markdown("**Core 01 (Neural Net):**")
        st.progress(random.randint(70, 95))
        st.markdown("**Core 02 (Encryption):**")
        st.progress(random.randint(40, 60))

# ==========================================
# 🎛️ OPTION 2: CENTRAL CONTROL PANEL
# ==========================================
with tab2:
    st.header("🎛️ CENTRAL CONTROL SYSTEM PANEL")
    col_ctrl1, col_ctrl2 = st.columns(2)

    with col_ctrl1:
        st.subheader("⚡ Weapon & Shield Output")
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

# ==========================================
# 🛰️ OPTION 3: GEOSPATIAL & RADAR
# ==========================================
with tab3:
    st.header("🛰️ GEOSPATIAL & RADAR SCANNER")
    col_map1, col_rad1 = st.columns([2, 1])
    
    with col_map1:
        st.subheader("🌐 LIVE GEOSPATIAL GRID")
        map_data = pd.DataFrame({
            'lat': [8.5241, 9.9312, 11.2588],
            'lon': [76.9366, 76.2673, 75.7804]
        })
        st.map(map_data, zoom=6)
        
    with col_rad1:
        st.subheader("🛰️ SATELLITE RADAR")
        radar_symbols = ["◜", "◝", "◞", "◟"]
        current_symbol = radar_symbols[(st.session_state.radar_angle // 90) % 4]
        st.metric(label="🛰️ RADAR STATUS", value=f"SWEEPING {st.session_state.radar_angle}°", delta=f"AZIMUTH {current_symbol}")
        
        st.code(f"""
[RADAR FEED ACTIVE]
Target 01: TVM Bunker [SAFE]
Target 02: Kochi Naval [TRACKING]
Target 03: Kozhikode  [STANDBY]
🛸 Unknown Signatures: 0
        """, language="markdown")

# ==========================================
# 📊 OPTION 4: SYSTEM METRICS & STATUS
# ==========================================
with tab4:
    st.header("📊 REAL-TIME CORE METRICS")
    
    drone_count = random.randint(7100, 7500)
    elevator_speed = round(random.uniform(4.1, 4.9), 2)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="🚀 KALINGA ELEVATOR SPEED", value=f"MACH {elevator_speed}")
    with col_m2:
        st.metric(label="🐝 CARGO DRONES IN AIR", value=f"{drone_count} Units")
    with col_m3:
        st.metric(label="🛡️ SHIELD POWER STATUS", value=f"{st.session_state.shield_val}%")
        
    st.markdown("---")
    
    st.subheader("📈 GRID PROCESSSING LOAD")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['TVM Core', 'Kochi Grid', 'Kozhikode Base']
    )
    st.line_chart(chart_data)
    
    st.markdown("---")
    
    st.subheader("📊 COMMAND BASE OPERATIONAL STATUS")
    status_data = pd.DataFrame({
        'COMMAND BASE': ['HQ: Thiruvananthapuram Bunker', 'Sub-Station: Kochi Naval Grid', 'Sub-Station: Kozhikode Air Base'],
        'SECURITY LEVEL': ['ALPHA (MAX)', 'BRAVO', 'ALPHA'],
        'WEAPONS SYSTEM': ['ONLINE', 'ONLINE', 'STANDBY']
    })
    st.dataframe(status_data, use_container_width=True)

# ==========================================
# 🛸 NEW OPTION 5: TRANSIT & FLIGHT TRACKER (പുതിയ ഫീച്ചർ!)
# ==========================================
with tab5:
    st.header("🛰️ REAL-TIME TRANSIT & FLIGHT TRACKING NETWORK")
    st.markdown("---")
    
    col_track1, col_track2 = st.columns(2)
    
    with col_track1:
        st.subheader("🚀 KALINGA ELEVATOR STATUS")
        # ലിഫ്റ്റിന്റെ ഡയറക്ഷനും ലൊക്കേഷനും റാൻഡം ആയി മാറുന്നു
        lift_direction = random.choice(["🔼 ASCENDING (മുകളിലോട്ട്)", "🔽 DESCENDING (താഴോട്ട്)"])
        lift_location = random.choice(["Leaving Thiruvananthapuram Bunker", "Passing Stratosphere", "Docking at Space Station Alpha", "Approaching Meso-Core"])
        
        st.info(f"**CURRENT POSITION:** {lift_location}")
        st.metric(label="TRACKING DIRECTION", value=lift_direction, delta="VERTICAL PROPULSION ACTIVE")
        
    with col_track2:
        st.subheader("🛸 ACTIVE AIR POD LOGS")
        # എയർ പോഡുകളുടെ ഡയറക്ഷൻ ടേബിൾ
        air_pod_data = pd.DataFrame({
            'AIR POD ID': ['POD-01 (VIP)', 'POD-02 (Cargo)', 'POD-03 (Scout)'],
            'DEPARTURE BASE': ['HQ: Thiruvananthapuram', 'Kochi Naval Grid', 'Kozhikode Air Base'],
            'DESTINATION ZONE': ['Kochi Naval Grid', 'Kozhikode Air Base', 'Wayanad Outpost'],
            'FLIGHT DIRECTION': ['➡️ NORTH-WEST', '➡️ NORTH', '➡️ EAST'],
            'VELOCITY': [f"{random.randint(600, 750)} km/h", f"{random.randint(450, 550)} km/h", f"{random.randint(800, 950)} km/h"],
            'STATUS': ['EN-ROUTE', 'APPROACHING', 'PATROLLING']
        })
        st.dataframe(air_pod_data, use_container_width=True)

# 🔄 3 സെക്കൻഡ് നിർത്തിയ ശേഷം പേജ് തനിയെ റീഫ്രെഷ് ചെയ്യാനുള്ള വിദ്യ
time.sleep(3)
st.rerun()
