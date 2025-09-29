# mailmind_streamlit.py 
import streamlit as st

st.set_page_config(page_title="MailMind", layout="wide")

# ---- Custom CSS for full dark navy + white theme ----
PRIMARY_BG = "#001933"  # very dark navy
ACCENT = "#ffffff"
BOX_BG = "#002244"      # box background
SECTION_BOX = "#001F44" # subtle section distinction

st.markdown(f"""
<style>
/* Hide default Streamlit header & footer */
header {{visibility: hidden;}}
footer {{visibility: hidden;}}

/* Add spacing so top title isn't cut off */
.block-container {{
    padding-top: 4rem !important;
}}

/* Full page background */
body, section.main, .block-container {{
    background-color: {PRIMARY_BG} !important;
    color: {ACCENT} !important;
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
}}

/* Headings and text scaling */
h1 {{ font-size: 50px !important; text-align: center; color: {ACCENT} !important; margin: 8px 0; }}
h2 {{ font-size: 28px !important; text-align: center; color: {ACCENT} !important; margin: 6px 0; }}
h3 {{ font-size: 24px !important; text-align: center; color: {ACCENT} !important; margin: 4px 0; }}
p, span, li {{ font-size: 20px !important; text-align: center; color: {ACCENT} !important; line-height: 1.5; }}

/* Boxes for key sections */
.box {{
    background-color: {BOX_BG};
    padding: 20px;
    border-radius: 12px;
    margin: 15px auto;
    max-width: 900px;
    text-align: left;
}}

/* Section boxes for paragraph distinction */
.section-box {{
    background-color: {SECTION_BOX};
    padding: 20px;
    border-radius: 12px;
    margin: 15px auto;
    max-width: 900px;
    text-align: left;
}}

/* Horizontal rule styling */
hr {{
    border: 1px solid #ffffff55;
    margin: 20px 0;
}}

/* Remove list bullets and spacing */
ul {{
    list-style-type: none;
    padding: 0;
}}
ul li {{
    margin: 10px 0;
}}

/* Key metrics styling */
.key-metrics {{
    display: flex;
    justify-content: center;
    gap: 80px;
    font-size: 22px !important; /* metrics numbers */
    margin: 30px 0;
    text-align: center;
}}
.key-metrics div {{
    text-align: center;
    padding: 15px;
    border-radius: 10px;
    background-color: #001A33;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}}
.key-metrics small {{
    font-size: 16px;
}}
</style>
""", unsafe_allow_html=True)

# ---- HERO SECTION ----
st.title("MailMind")
st.subheader("Email-Native Operational Intelligence")
st.markdown(f"""
<div class="section-box">
<p><b>Emails aren't just communication. They're action waiting to happen.</b></p>
<p>MailMind reads them, understands them, and makes them move.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ---- WATCH DEMO ----
st.markdown("## Watch Live Demo")
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID")  # <-- replace with your actual YT URL
st.markdown("---")

# ---- MARKETING COPY ----
st.markdown("## What is MailMind?")
st.markdown(f"""
<div class="section-box">
<p>Every email is a trigger—an intent to approve, assign, reply, route, or resolve.</p>
<p>Most companies treat email as static noise.</p>
<p><b>MailMind changes that.</b></p>
<p>It reads emails like a human, extracts key data, and kicks off workflows across your stack.</p>
</div>
""", unsafe_allow_html=True)

# ---- OPERATIONAL INTELLIGENCE BOX ----
st.markdown(f"""
<div class="box">
<ul>
<li>Automatically update your CRM</li>
<li>Draft responses and internal alerts</li>
<li>Assign tasks and launch approvals</li>
<li>Escalate follow-ups when ignored</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---- HOW IT WORKS ----
st.markdown("## How It Works")
st.markdown(f"""
<div class="section-box">
<p><b>01 — An email arrives</b><br>A lead, invoice, support request, or escalation.</p>
<p><b>02 — MailMind reads it</b><br>Categorizes the intent and extracts structured fields.</p>
<p><b>03 — It acts, instantly</b><br>Updates systems, routes to teams, or drafts replies.</p>
<p><b>Real-time Processing Pipeline:</b><br>Email Received → AI Analysis → Action Triggered</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ---- COMING SOON MODULES ----
st.markdown("## Coming Soon — Your Command Center for Email-Driven Ops")
st.markdown(f"""
<div class="box">
<ul>
<li><b>Category Config:</b> Design how MailMind thinks. Define your own logic for classifying emails.</li>
<li><b>Integration Hub:</b> Connect MailMind to Slack, Teams, Notion, HubSpot, Zoho, ClickUp, and more.</li>
<li><b>Routing Rules:</b> Automatically assign or escalate based on keywords, sender, attachments, or timing.</li>
<li><b>Action Dashboard:</b> Track everything—extracted, triggered, routed emails in real-time.</li>
<li><b>Bonus Module — Memory Layer:</b> Learns recurring clients, team habits, and org language over time.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---- FINAL CALL ----
st.markdown("## Final Call")
st.markdown(f"""
<div class="section-box">
<p>Don't manage emails. Orchestrate operations.</p>
<p>If you want your inbox to be a system of execution, not just communication—join the waitlist.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")
