import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. പേജ് കോൺഫിഗറേഷൻ (ടാബ് ടൈറ്റിലും തീമും സജ്ജമാക്കുന്നു)
st.set_page_config(
    page_title="KERALA CENTRAL COMMAND v2.0",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. സൈൻസ് ഫിക്ഷൻ മിലിട്ടറി ലുക്ക് നൽകാനുള്ള കസ്റ്റം സിഎസ്എസ് (Dark Theme & Neon Blue)
st.markdown("""
    <style>
    .main { background-color: #0B0F19; color: #E0E6ED; }
    h1, h2, h3 { color: #00E5FF !important; font-family: 'Courier New', monospace; font-weight: bold; }
    .stMetric { background-color: #121826; padding: 20px; border-radius: 12px; border: 1px solid #00E5FF; box-shadow: 0 4px 15px rgba(0,229,255,0.1); }
    .stAlert { border-radius: 10px; font-family: monospace; }
    div.stButton > button:first-child { background-color: #00E5FF; color: #0A0F1D; font-weight: bold; border-radius: 8px; border: none; width: 100%; height: 45px; }
    div.stButton > button:first-child:hover { background-color: #00B3CC; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. ഡാഷ്‌ബോർഡ് ഹെഡ്ഡർ
st.title("🚨 KERALA CENTRAL COMMAND & SECURITY GRID")
st.subheader("CHIEF MINISTER'S SECRET DEFENSE INTERFACE | LEVEL: OMNISCIENT")
st.write("---")

# 4. ഒന്നാം നിര: പ്രധാന പ്രൊജക്റ്റുകളുടെ തത്സമയ സ്റ്റാറ്റസ് (Metrics)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="🚀 KALINGA ELEVATOR SPEED", value="MACH 4.5", delta="🚀 VERTICAL ASCENT")
with col2:
    st.metric(label="🐝 CARGO DRONES IN AIR", value="7,240 Units", delta="+340 Active")
with col3:
    st.metric(label="🚡 KOCHI MAGLEV GRID", value="99.2% EFF", delta="🟢 ONLINE")
with col4:
    st.metric(label="🛡️ PROJECT KAVACHAM", value="SECURE", delta="0 THREATS DETECTED")

st.write("---")

# 5. രണ്ടാം നിര: ലൈവ് ചാർട്ടുകളും കമാൻഡ് പാനലും
col_chart, col_control = st.columns([2, 1])

with col_chart:
    st.subheader("📊 Live Infrastructure Metric Streams")
    
    # കഴിഞ്ഞ 30 ദിവസത്തെ പ്രൊജക്റ്റുകളുടെ സ്റ്റെബിലിറ്റി കാണിക്കുന്ന ലൈവ് ഗ്രാഫ് ഡാറ്റ
    chart_data = pd.DataFrame(
        np.random.randint(85, 100, size=(30, 3)),
        columns=['Kalinga Cable Tension (%)', 'Drone Swarm Sync Rate (%)', 'State Grid Power (MW)']
    )
    st.line_chart(chart_data)
    
    # ബയോസിൻ വാലിയിലെ വിവരങ്ങൾ കാണിക്കുന്ന ടേബിൾ
    st.subheader("🧬 Biosyn Valley Underground Containment Registry")
    biosyn_data = pd.DataFrame({
        'Sector Code': ['SEC-A1 (Snow)', 'SEC-B3 (Jungle)', 'SEC-C2 (Ocean)', 'SEC-D5 (Lab)'],
        'Specimen Type': ['Woolly Mammoth', 'Saber-toothed Cat', 'Amphibious Bio-Guards', 'Neural AI Core'],
        'Population': [12, 8, 150, 1],
        'Neural Link Status': ['Synchronized', 'Synchronized', 'Armed & Guarding', 'Adaptive Encryption'],
        'Threat Level': ['Low', 'Low', 'Tactical Guard', 'Safe']
    })
    st.table(biosyn_data)

with col_control:
    st.subheader("🕹️ Strategic Defense & Grid Controls")
    
    st.write("**PERIMETER SECURITY SYSTEM (PROJECT KAVACHAM)**")
    bio_force = st.checkbox("Deploy Bio-Cybernetic Coastal Guards", value=True)
    drone_swarm = st.checkbox("Activate Combat Drone Swarm Grid")
    laser_shield = st.checkbox("Engage Orbital Kalinga Laser Shield")
    
    st.write("---")
    
    # ചെക്ക്ബോക്സുകളുടെ അവസ്ഥ അനുസരിച്ച് സുരക്ഷാ സ്റ്റാറ്റസ് മാറുന്നു
    if bio_force and drone_swarm and laser_shield:
        st.success("⚡ FORTRESS KERALA SHIELD IS 100% IMPENETRABLE! ALL SECTORS LOCKED.")
    elif bio_force or drone_swarm or laser_shield:
        st.warning("⚠️ WARNING: Partial defense grid active. Perimeter vulnerable to heavy stealth attacks.")
    else:
        st.error("🛑 CRITICAL: Perimeter Defense Mode is OFF. State is unprotected!")
        
    st.write("---")
    st.write("**🚨 EMERGENCY PROTOCOLS**")
    
    # ഇന്ററാക്ടീവ് ബട്ടണുകൾ
    lockdown_btn = st.button("INITIATE STATEWIDE LOCKDOWN")
    scramble_btn = st.button("SCRAMBLE ALL COMBAT DRONES")
    
    if lockdown_btn:
        st.error("🚨 EMERGENCY LOCKDOWN ENFORCED BY THE MINISTER! ALL TRANSIT GRIDS HALTED.")
    if scramble_btn:
        st.info("🐝 ALERT: 7,000+ Combat Drones launched to intercept potential air threats.")

# 6. ഫൂട്ടർ
st.write("---")
st.caption("Developed securely by Chief Advisor AI for the Ministry of Future Advancement, Kerala. © 2026.")
