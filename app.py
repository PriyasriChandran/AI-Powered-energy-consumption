import streamlit as st
import mysql.connector
import random
import pandas as pd

# ---------------- DATABASE ----------------
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="energy_system",
        charset="utf8"
    )

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="⚡ Smart Energy System", layout="wide")

# ---------------- GLOBAL DESIGN ----------------
st.markdown("""
<style>

/* FULL PAGE GRADIENT BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1f1c2c, #928dab, #00c6ff);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

/* ANIMATION */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* MAIN TITLE */
.title {
    font-size: 55px;
    font-weight: 900;
    text-align: center;
    color: #ffffff;
    text-shadow: 2px 2px 20px rgba(0,0,0,0.5);
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #e0f7fa;
    margin-bottom: 30px;
}

/* GLASS CARD EFFECT */
.card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.3);
    transition: 0.4s;
}
.card:hover {
    transform: translateY(-10px) scale(1.05);
}

/* FEATURE BOX */
.feature {
    background: linear-gradient(135deg, #ff6a00, #ee0979);
    padding: 20px;
    border-radius: 15px;
    color: white;
    font-weight: 500;
    margin: 10px 0;
}

/* BUTTON STYLE */
.stButton button {
    width: 100%;
    height: 70px;
    border-radius: 15px;
    font-size: 18px;
    font-weight: bold;
    color: white;
    border: none;
    background: linear-gradient(to right, #ff512f, #dd2476);
    box-shadow: 0px 5px 20px rgba(0,0,0,0.3);
}
.stButton button:hover {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    transform: scale(1.05);
}

/* SECTION TITLES */
.section {
    font-size: 28px;
    font-weight: bold;
    color: white;
    margin-top: 30px;
}

/* TEXT */
p, li {
    color: #f1f5f9;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* FORM CONTAINER */
.form-box {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(18px);
    padding: 40px;
    border-radius: 25px;
    width: 50%;
    margin: auto;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.4);
}

/* INPUT FIELDS */
input {
    border-radius: 10px !important;
}

/* FORM TITLE */
.form-title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* TOP HEADER BAR */
.top-bar {
    width: 80%;
    margin: auto;
    margin-top: 40px;
    padding: 25px;
    border-radius: 30px;
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(20px);
    box-shadow: 0px 10px 40px rgba(0,0,0,0.3);
    text-align: center;
}

/* HEADER TEXT */
.top-text {
    font-size: 36px;
    font-weight: bold;
    color: white;
}

/* FORM BOX */
.form-box {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(18px);
    padding: 40px;
    border-radius: 25px;
    width: 55%;
    margin: auto;
    margin-top: 30px;
    box-shadow: 0px 10px 40px rgba(0,0,0,0.4);
}

/* INPUT */
input {
    border-radius: 10px !important;
}

/* BUTTON */
.stButton button {
    width: 100%;
    height: 65px;
    border-radius: 15px;
    font-size: 17px;
    font-weight: bold;
    color: white;
    background: linear-gradient(to right, #ff512f, #dd2476);
}
.stButton button:hover {
    background: linear-gradient(to right, #00c6ff, #0072ff);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* DASHBOARD CARD BUTTON */
.dashboard-card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
    transition: 0.3s;
    height: 180px;
}
.dashboard-card:hover {
    transform: scale(1.05);
}

/* TITLE */
.card-title {
    font-size: 20px;
    font-weight: bold;
}

/* DESCRIPTION */
.card-desc {
    font-size: 14px;
    margin-top: 10px;
    color: #e0f7fa;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* SECTION BOX */
.section-box {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(15px);
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

/* METRIC CARD */
.metric-card {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-weight: bold;
}

/* SUB TITLES */
.sub-title {
    font-size: 22px;
    font-weight: bold;
    color: white;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* COMPARISON CARD */
.compare-card {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-weight: bold;
    color: #333;
}

/* OVERRIDE BOX */
.override-box {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)
# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME ----------------
if st.session_state.page == "home":

    st.markdown('<div class="title">⚡ Smart Energy System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-Powered Energy Prediction & HVAC Optimization Platform</div>', unsafe_allow_html=True)

    st.write("")

    # ---------------- HERO ----------------
    st.markdown('<div class="section">🌍 Intelligent Energy Management for Smart Buildings</div>', unsafe_allow_html=True)

    st.write("""
This platform integrates **IoT, Machine Learning, and Reinforcement Learning** to deliver a next-generation smart energy solution.

It enables real-time monitoring, predictive analytics, and intelligent HVAC control for efficient building management.
""")

    # ---------------- FEATURES ----------------
    st.markdown('<div class="section">🚀 Core Features</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">📡<br><b>Real-Time Monitoring</b><br>Track live sensor data and energy usage.</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">🔮<br><b>Energy Prediction</b><br>LSTM predicts future energy consumption.</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">⚙<br><b>HVAC Optimization</b><br>RL controls HVAC efficiently.</div>', unsafe_allow_html=True)

    # ---------------- WORKFLOW ----------------
    st.markdown('<div class="section">🔄 System Workflow</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="feature">
Sensors → MQTT → InfluxDB → Grafana → LSTM → RL → HVAC → Dashboard
</div>
""", unsafe_allow_html=True)

    # ---------------- BENEFITS ----------------
    st.markdown('<div class="section">💡 Benefits</div>', unsafe_allow_html=True)

    st.write("""
• ⚡ Reduce energy consumption  
• ❄ Maintain comfort levels  
• 🤖 Fully automated system  
• 📊 Real-time analytics  
• 🌱 Sustainable smart building solution  
""")

    # ---------------- LOGIN ----------------
    st.markdown('<div class="section">🔐 Access System</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        if st.button("👨‍💼 Building Manager Login"):
            st.session_state.page = "admin_login"

    with c2:
        if st.button("🛠 Technician Login"):
            st.session_state.page = "tech_login"

# ---------------- REGISTER ----------------
elif st.session_state.page == "register":

    st.markdown("""
    <div class="top-bar">
        <div class="top-text">📝 Building Manager Registration</div>
    </div>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email")
        mobile = st.text_input("📱 Mobile")

    with col2:
        building = st.text_input("🏢 Building Name")
        username = st.text_input("👨‍💻 Username")
        password = st.text_input("🔒 Password", type="password")

    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("🚀 Register"):
            db = get_db()
            cursor = db.cursor()
            cursor.execute("""
            INSERT INTO building_managers 
            (name,email,mobile,building_name,username,password)
            VALUES (%s,%s,%s,%s,%s,%s)
            """, (name,email,mobile,building,username,password))
            db.commit()
            st.success("✅ Account Created Successfully!")

    with c2:
        if st.button("⬅ Back to Login"):
            st.session_state.page = "admin_login"

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- LOGIN ----------------
elif st.session_state.page == "admin_login":

    st.markdown("""
    <div class="top-bar">
        <div class="top-text">🔐 Building Manager Login</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    username = st.text_input("👨‍💻 Username")
    password = st.text_input("🔒 Password", type="password")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 Login"):
            db = get_db()
            cursor = db.cursor()
            cursor.execute(
                "SELECT * FROM building_managers WHERE username=%s AND password=%s",
                (username, password)
            )
            user = cursor.fetchone()

            if user:
                st.session_state.admin_id = user[0]
                st.success("✅ Login Successful!")
                st.session_state.page = "dashboard"
            else:
                st.error("❌ Invalid Username or Password")

    with col2:
        if st.button("📝 Register"):
            st.session_state.page = "register"

# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":

    st.markdown('<div class="title">📊 Smart Energy Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Control, Monitor and Optimize Building Energy Efficiently</div>', unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    # ---------------- ADD TECHNICIAN ----------------
    with c1:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">➕ Add Technician</div>
            <div class="card-desc">
            Create and manage technician accounts for system maintenance.<br>
            Allows controlled access to monitoring and backend operations.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Technician Panel"):
            st.session_state.page = "add_tech"

    # ---------------- MONITOR ----------------
    with c2:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">📈 Monitor System</div>
            <div class="card-desc">
            View real-time environmental and appliance energy data.<br>
            Track system performance and energy consumption live.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Monitoring"):
            st.session_state.page = "monitor"

    # ---------------- COMPARE ----------------
    with c3:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">📊 Compare Energy</div>
            <div class="card-desc">
            Analyze energy usage before and after optimization.<br>
            Helps evaluate system efficiency and savings.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Comparison"):
            st.session_state.page = "compare"

    # ---------------- HVAC ----------------
    with c4:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">❄ HVAC Control</div>
            <div class="card-desc">
            Manually override HVAC system when required.<br>
            Provides control during special conditions or emergencies.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open HVAC Control"):
            st.session_state.page = "override"

    st.write("")
    st.write("")

    # ---------------- LOGOUT ----------------
    col1, col2, col3 = st.columns([1,1,1])

    with col2:
        if st.button("🚪 Logout"):
            st.session_state.page = "home"

# ---------------- ADD TECH ----------------
elif st.session_state.page == "add_tech":

    # 🔷 TOP HEADER BAR (same as login/register)
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">➕ Add Technician</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # 🔷 CENTER FORM
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        c1, c2 = st.columns(2)

        with c1:
            name = st.text_input("👤 Full Name")
            email = st.text_input("📧 Email")
            mobile = st.text_input("📱 Mobile")

        with c2:
            username = st.text_input("👨‍💻 Username")
            password = st.text_input("🔒 Password", type="password")

        st.write("")

        b1, b2 = st.columns(2)

        # 🔷 ADD BUTTON
        with b1:
            if st.button("🚀 Add Technician"):
                db = get_db()
                cursor = db.cursor()
                cursor.execute("""
                INSERT INTO technicians (name,username,password,created_by)
                VALUES (%s,%s,%s,%s)
                """, (name,username,password,st.session_state.admin_id))
                db.commit()
                st.success("✅ Technician Added Successfully!")

        # 🔷 BACK BUTTON
        with b2:
            if st.button("⬅ Back to Dashboard"):
                st.session_state.page = "dashboard"


# ---------------- MONITOR ----------------
elif st.session_state.page == "monitor":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">📈 Smart Monitoring Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ---------------- APPLIANCE DATA ----------------
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">⚡ Appliance Energy Usage</div>', unsafe_allow_html=True)

    appliances = {
        "Fan": round(random.uniform(0.05, 0.1), 3),
        "Tubelight": round(random.uniform(0.02, 0.05), 3),
        "Television": round(random.uniform(0.1, 0.2), 3),
        "AC": round(random.uniform(1.0, 2.5), 3),
        "Heater": round(random.uniform(1.5, 3.0), 3),
        "Refrigerator": round(random.uniform(0.2, 0.5), 3),
        "Washing Machine": round(random.uniform(0.5, 1.5), 3),
        "Motor Pump": round(random.uniform(1.0, 3.0), 3),
        "Air Cooler": round(random.uniform(0.2, 0.8), 3),
        "Computers": round(random.uniform(0.3, 1.0), 3)
    }

    df = pd.DataFrame(appliances.items(), columns=["Appliance", "Power (kW)"])
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- ENVIRONMENT DATA ----------------
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">🌡 Environmental Conditions</div>', unsafe_allow_html=True)

    temp = random.randint(25, 35)
    humidity = random.randint(50, 80)
    energy = round(random.uniform(2, 5), 2)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f'<div class="metric-card">🌡 Temp<br>{temp} °C</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f'<div class="metric-card">💧 Humidity<br>{humidity} %</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(f'<div class="metric-card">⚡ Energy<br>{energy} kWh</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- PREDICTION ----------------
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    if st.button("🔮 Run AI Prediction"):

        predicted = round(energy + random.uniform(0.3, 1.0), 2)

        st.markdown('<div class="sub-title">🔮 Energy Prediction Result</div>', unsafe_allow_html=True)
        st.success(f"Predicted Energy (Next Hour): {predicted} kWh")

        # Explanation
        st.markdown("### 📘 Prediction Explanation")
        st.info(f"""
        • The system analyzes current temperature ({temp}°C), humidity ({humidity}%), and appliance load conditions.  
        • High temperature and appliance usage increase HVAC demand, leading to higher energy consumption.  
        • Based on learned patterns, the model predicts a rise in energy usage in the next hour.
        """)

        # Recommendation
        st.markdown("### 💡 Energy Recommendation")
        st.warning("""
        • Reduce unnecessary appliance usage during peak hours.  
        • Maintain temperature between 22°C–26°C for efficiency.  
        • Use energy-efficient devices to minimize consumption.
        """)

        # ---------------- OPTIMIZATION ----------------
        action = random.choice(["Cooling Level 1", "Cooling Level 2", "Cooling Level 3"])
        optimized = round(predicted - random.uniform(0.2, 0.5), 2)
        new_temp = temp - random.randint(3, 6)

        st.markdown('<div class="sub-title">⚙ HVAC Optimization Result</div>', unsafe_allow_html=True)
        st.success(f"Recommended HVAC Action: {action}")
        st.write(f"Optimized Energy: {optimized} kWh")
        st.write(f"Temperature After Optimization: {new_temp} °C")

        # Optimization Explanation
        st.markdown("### 📘 Optimization Explanation")
        st.info(f"""
        • The reinforcement learning model selects {action} based on current environmental conditions.  
        • It balances energy consumption and comfort by reducing temperature efficiently.  
        • The system improves decisions continuously using previous outcomes.
        """)

        # Optimization Recommendation
        st.markdown("### 💡 Optimization Recommendation")
        st.warning("""
        • Avoid using maximum cooling unless necessary.  
        • Ensure proper airflow and ventilation.  
        • Regular HVAC maintenance improves efficiency and reduces energy waste.
        """)

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- BACK ----------------
    st.write("")
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"

# ---------------- COMPARE ----------------
elif st.session_state.page == "compare":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">📊 Energy Comparison Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 🔷 DATA GENERATION (UNCHANGED LOGIC)
    before = round(random.uniform(3,5),2)
    after = round(before - random.uniform(0.3,1.0),2)

    df = pd.DataFrame({
        "Stage":["Before Optimization","After Optimization"],
        "Energy (kWh)":[before,after]
    })

    # 🔷 GRAPH SECTION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📊 Energy Comparison (Before vs After)</div>', unsafe_allow_html=True)

    st.bar_chart(df.set_index("Stage"))

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 RESULT CARDS
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f'<div class="compare-card">⚡ Before<br>{before} kWh</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f'<div class="compare-card">✅ After<br>{after} kWh</div>', unsafe_allow_html=True)

    st.success(f"Energy Reduced from {before} → {after} kWh")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 EXPLANATION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 Comparison Explanation")
    st.info("""
• This comparison shows the effectiveness of AI-based HVAC optimization.  
• Energy consumption decreases after applying intelligent control strategies.  
• Helps building managers evaluate system performance improvements.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 BACK
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"

# ---------------- OVERRIDE ----------------
elif st.session_state.page == "override":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">❄ HVAC Override Control</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 🔷 CONTROL BOX
    st.markdown('<div class="override-box">', unsafe_allow_html=True)

    st.markdown("### ⚙ Manual HVAC Control")

    option = st.selectbox("Select Level",["OFF","Level 1","Level 2","Level 3"])

    st.write("")

    if st.button("🚀 Apply Override"):
        st.success(f"HVAC set to {option}")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 INFO SECTION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 Override Explanation")
    st.info("""
• Manual override allows admin control over HVAC.  
• Useful during special conditions or emergencies.  
• Overrides AI temporarily.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 BACK
    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"

# ---------------- TECH LOGIN ----------------
elif st.session_state.page == "tech_login":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">🛠 Technician Login</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # 🔷 CENTER FORM
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("👨‍💻 Username")
        password = st.text_input("🔒 Password", type="password")

        st.write("")

        c1, c2 = st.columns(2)

        with c1:
            if st.button("🚀 Login"):
                db = get_db()
                cursor = db.cursor()
                cursor.execute(
                    "SELECT * FROM technicians WHERE username=%s AND password=%s",
                    (username, password)
                )
                if cursor.fetchone():
                    st.success("✅ Login Successful!")
                    st.session_state.page = "tech_dashboard"
                else:
                    st.error("❌ Invalid Login")

        with c2:
            if st.button("⬅ Back"):
                st.session_state.page = "home"


# ---------------- TECH DASHBOARD ----------------
elif st.session_state.page == "tech_dashboard":

    st.markdown("""
    <div class="top-bar">
        <div class="top-text">🛠 Technician Control Panel</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="subtitle">Monitor system infrastructure, IoT flow, and backend services</div>', unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    # MQTT
    with c1:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">📡 MQTT Monitor</div>
            <div class="card-desc">
            Monitor real-time communication between sensors and system.<br>
            Ensures reliable IoT data transmission.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open MQTT Monitor"):
            st.session_state.page = "mqtt"

    # SENSOR
    with c2:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">🌡 Sensor Status</div>
            <div class="card-desc">
            Track environmental data from sensors.<br>
            Ensures real-time data collection accuracy.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Sensor Status"):
            st.session_state.page = "sensor"

    # TOPICS
    with c3:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">📊 MQTT Topics</div>
            <div class="card-desc">
            View live MQTT topic data streams.<br>
            Helps analyze system data flow.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Topics"):
            st.session_state.page = "topics"

    st.write("")

    c4, c5 = st.columns(2)

    # INFLUX
    with c4:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">🗄 InfluxDB</div>
            <div class="card-desc">
            Monitor time-series data storage.<br>
            Verify database performance and logging.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open InfluxDB"):
            st.session_state.page = "influx"

    # GRAFANA
    with c5:
        st.markdown("""
        <div class="dashboard-card">
            <div class="card-title">📈 Grafana</div>
            <div class="card-desc">
            Visualize real-time system data.<br>
            Analyze trends and performance metrics.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Grafana"):
            st.session_state.page = "grafana"

    st.write("")

    if st.button("🚪 Logout"):
        st.session_state.page = "home"

elif st.session_state.page == "mqtt":

    st.markdown("""
    <div class="top-bar">
        <div class="top-text">📡 MQTT Broker Monitoring</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # STATUS BOX
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    status = random.choice(["Connected", "Stable", "High Traffic"])
    st.success(f"Broker Status: {status}")

    st.write("📌 Active Topics:")
    st.write("• building/temperature")
    st.write("• building/energy")

    st.markdown('</div>', unsafe_allow_html=True)

    # EXPLANATION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 MQTT Explanation")
    st.info("""
• MQTT enables real-time communication between sensors and system.  
• Mosquitto broker ensures efficient and low-latency data transfer.  
• Supports scalable IoT-based architecture.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "tech_dashboard"


# ---------------- SENSOR ----------------
elif st.session_state.page == "sensor":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">🌡 Sensor Monitoring Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 🔷 SENSOR DATA
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📡 Live Sensor Data</div>', unsafe_allow_html=True)

    temp = random.randint(25,35)
    humidity = random.randint(50,80)
    co2 = random.randint(400,1000)
    occupancy = random.randint(0,10)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f'<div class="metric-card">🌡 Temp<br>{temp} °C</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f'<div class="metric-card">💧 Humidity<br>{humidity} %</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(f'<div class="metric-card">🫁 CO₂<br>{co2} ppm</div>', unsafe_allow_html=True)

    with c4:
        st.markdown(f'<div class="metric-card">👥 Occupancy<br>{occupancy}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 STATUS
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.success("📡 Sensors are actively streaming real-time data")
    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 EXPLANATION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 Sensor System Explanation")
    st.info("""
• Sensors collect environmental and occupancy data continuously.  
• Data is transmitted in real-time to the MQTT broker.  
• Enables accurate monitoring and supports AI-based predictions.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 BACK
    if st.button("⬅ Back to Technician Dashboard"):
        st.session_state.page = "tech_dashboard"


# ---------------- TOPICS ----------------
elif st.session_state.page == "topics":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">📊 MQTT Topic Data Streams</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 🔷 TOPIC DATA
    st.markdown('<div class="sub-title">📡 Live MQTT Topics</div>', unsafe_allow_html=True)

    topics = {
        "temperature": random.randint(25,35),
        "humidity": random.randint(50,80),
        "occupancy": random.randint(0,10),
        "energy": round(random.uniform(2,5),2)
    }

    st.json(topics)

    # 🔷 VISUAL METRICS
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📊 Topic Metrics Overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f'<div class="metric-card">🌡 Temp<br>{topics["temperature"]} °C</div>', unsafe_allow_html=True)

    with c2:
        st.markdown(f'<div class="metric-card">💧 Humidity<br>{topics["humidity"]} %</div>', unsafe_allow_html=True)

    with c3:
        st.markdown(f'<div class="metric-card">👥 Occupancy<br>{topics["occupancy"]}</div>', unsafe_allow_html=True)

    with c4:
        st.markdown(f'<div class="metric-card">⚡ Energy<br>{topics["energy"]} kWh</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 EXPLANATION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 MQTT Topics Explanation")
    st.info("""
• MQTT topics store structured IoT data streams.  
• Each parameter is published independently in real-time.  
• Enables modular, scalable, and efficient communication.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 BACK
    if st.button("⬅ Back to Technician Dashboard"):
        st.session_state.page = "tech_dashboard"

# ---------------- INFLUXDB ----------------
elif st.session_state.page == "influx":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">🗄 InfluxDB Time-Series Monitoring</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 🔷 STATUS BOX
    st.success("📡 Database Connected | Writing Live Data")

    # 🔷 DATA GENERATION (UNCHANGED)
    time_range = pd.date_range(end=pd.Timestamp.now(), periods=12, freq='5min')

    temp = [random.randint(26, 32) for _ in range(12)]
    energy = [round(random.uniform(2.5, 4.5), 2) for _ in range(12)]
    humidity = [random.randint(50, 75) for _ in range(12)]

    df = pd.DataFrame({
        "Time": time_range,
        "Temperature": temp,
        "Energy": energy,
        "Humidity": humidity
    })

    # 🔷 TABLE SECTION
    st.markdown('<div class="sub-title">📊 Time-Series Data (Last 1 Hour)</div>', unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 GRAPH SECTION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">📈 Data Trends</div>', unsafe_allow_html=True)

    st.line_chart(df.set_index("Time"))

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 EXPLANATION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 InfluxDB Explanation")
    st.info("""
• InfluxDB stores continuous time-series data from IoT sensors.  
• Data is recorded at fixed intervals (every 5 minutes).  
• Enables historical analysis, monitoring, and predictive modeling.
""")

    st.markdown('</div>', unsafe_allow_html=True)

    # 🔷 BACK
    if st.button("⬅ Back to Technician Dashboard"):
        st.session_state.page = "tech_dashboard"


# ---------------- GRAFANA ----------------
elif st.session_state.page == "grafana":

    # 🔷 HEADER
    st.markdown("""
    <div class="top-bar">
        <div class="top-text">📈 Grafana Visualization Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # 🔷 STATUS
    st.success("📡 Live Dashboard Connected")

    # 🔷 DATA (UNCHANGED)
    time_range = pd.date_range(end=pd.Timestamp.now(), periods=12, freq='5min')

    temp = [random.randint(26, 32) for _ in range(12)]
    energy = [round(random.uniform(2.5, 4.5), 2) for _ in range(12)]
    occupancy = [random.randint(1, 10) for _ in range(12)]

    df = pd.DataFrame({
        "Time": time_range,
        "Temperature": temp,
        "Energy": energy,
        "Occupancy": occupancy
    })

    # 🔷 GRAPH 1
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">🌡 Temperature Trend</div>', unsafe_allow_html=True)
    st.line_chart(df.set_index("Time")["Temperature"])

    # 🔷 GRAPH 2
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">⚡ Energy Consumption</div>', unsafe_allow_html=True)
    st.line_chart(df.set_index("Time")["Energy"])

    # 🔷 GRAPH 3
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">👥 Occupancy Analysis</div>', unsafe_allow_html=True)
    st.area_chart(df.set_index("Time")["Occupancy"])

    # 🔷 GRAPH 4
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">🔄 Combined Analytics</div>', unsafe_allow_html=True)
    st.line_chart(df.set_index("Time"))

    # 🔷 EXPLANATION
    st.markdown('<div class="section-box">', unsafe_allow_html=True)

    st.markdown("### 📘 Grafana Explanation")
    st.info("""
• Grafana visualizes real-time and historical data from InfluxDB.  
• Multiple graphs display trends in temperature, energy, and occupancy.  
• Helps identify peak loads and optimize energy usage efficiently.
""")


    # 🔷 BACK
    if st.button("⬅ Back to Technician Dashboard"):
        st.session_state.page = "tech_dashboard"
