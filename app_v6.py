import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# AIRPULSE INDIA v4
# Interactive Environmental Intelligence Platform
# ============================================================

st.set_page_config(
    page_title="AirPulse India | Environmental Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ============================================================
# AIRPULSE v6 — PREMIUM PRODUCT UI ENGINE
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --ap-bg: #061113;
    --ap-panel: #0b1b1e;
    --ap-panel-2: #0e2225;
    --ap-border: rgba(148, 255, 237, 0.10);
    --ap-text: #edfafa;
    --ap-muted: #789492;
    --ap-teal: #35e0c2;
    --ap-cyan: #38bdf8;
    --ap-green: #4ade80;
    --ap-yellow: #facc15;
    --ap-orange: #fb923c;
    --ap-red: #f87171;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 12% 8%,
            rgba(53,224,194,.095),
            transparent 25%
        ),
        radial-gradient(
            circle at 88% 14%,
            rgba(56,189,248,.075),
            transparent 23%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(20,184,166,.045),
            transparent 30%
        ),
        var(--ap-bg);
    color: var(--ap-text);
}

/* =========================================================
   APP SHELL
   ========================================================= */

.block-container {
    max-width: 1540px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}

/* Keep Streamlit controls and sidebar accessible */
#MainMenu,
footer {
    visibility: hidden;
}

header {
    visibility: visible;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(7,25,28,.99),
            rgba(4,15,17,.99)
        );
    border-right: 1px solid rgba(255,255,255,.055);
}

section[data-testid="stSidebar"] > div {
    padding: 1.15rem .85rem 1rem;
}

/* Brand */

section[data-testid="stSidebar"]::before {
    content: "";
    display: block;
    position: absolute;
    top: 18px;
    left: 20px;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--ap-teal);
    box-shadow:
        0 0 12px rgba(53,224,194,.9),
        0 0 28px rgba(53,224,194,.45);
    animation: apPulse 2.4s ease-in-out infinite;
}

@keyframes apPulse {
    0%,100% {
        transform: scale(.8);
        opacity: .55;
    }
    50% {
        transform: scale(1.25);
        opacity: 1;
    }
}

/* Navigation radio */

div[data-testid="stRadio"] {
    padding-top: 4px;
}

div[data-testid="stRadio"] > div {
    gap: 5px;
}

div[data-testid="stRadio"] label {
    position: relative;
    border: 1px solid transparent;
    border-radius: 14px;
    padding: 10px 12px !important;
    margin: 2px 0;
    background: transparent;
    transition:
        background .22s ease,
        border-color .22s ease,
        transform .22s ease,
        box-shadow .22s ease;
}

div[data-testid="stRadio"] label:hover {
    background: rgba(53,224,194,.065);
    border-color: rgba(53,224,194,.10);
    transform: translateX(4px);
}

div[data-testid="stRadio"] label p {
    color: #91aaa7 !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    letter-spacing: .1px;
    transition: color .2s ease;
}

div[data-testid="stRadio"] label:hover p {
    color: #d7f7f2 !important;
}

/* =========================================================
   GLOBAL ANIMATION
   ========================================================= */

@keyframes apReveal {
    from {
        opacity: 0;
        transform: translateY(14px);
        filter: blur(3px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}

.main .block-container {
    animation: apReveal .55s cubic-bezier(.2,.8,.2,1);
}

/* =========================================================
   HERO
   ========================================================= */

.ap-hero {
    position: relative;
    overflow: hidden;
    min-height: 330px;
    border-radius: 30px;
    border: 1px solid rgba(255,255,255,.075);
    padding: 44px 48px;
    margin-bottom: 25px;

    background:
        radial-gradient(
            circle at 85% 35%,
            rgba(53,224,194,.16),
            transparent 28%
        ),
        radial-gradient(
            circle at 72% 100%,
            rgba(56,189,248,.08),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #0c272a,
            #081719 70%
        );

    box-shadow:
        0 25px 80px rgba(0,0,0,.28),
        inset 0 1px rgba(255,255,255,.035);
}

.ap-hero::before {
    content: "";
    position: absolute;
    width: 480px;
    height: 480px;
    right: -190px;
    top: -210px;
    border-radius: 50%;
    border: 1px solid rgba(53,224,194,.11);
    box-shadow:
        0 0 0 45px rgba(53,224,194,.025),
        0 0 0 90px rgba(53,224,194,.018),
        0 0 0 135px rgba(53,224,194,.012);
    animation: apOrbit 12s linear infinite;
}

@keyframes apOrbit {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.ap-eyebrow {
    position: relative;
    color: #5eead4;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.ap-hero-title {
    position: relative;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(38px,5vw,68px);
    font-weight: 700;
    line-height: 1.02;
    letter-spacing: -3.5px;
    margin: 0;
    max-width: 920px;
}

.ap-hero-title span {
    background:
        linear-gradient(
            90deg,
            #effffb,
            #6ee7d3 55%,
            #67d7ff
        );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.ap-hero-copy {
    position: relative;
    color: #91aaa7;
    max-width: 760px;
    font-size: 15px;
    line-height: 1.75;
    margin-top: 20px;
}

.ap-live-pill {
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 20px;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(53,224,194,.065);
    border: 1px solid rgba(53,224,194,.18);
    color: #8de9dc;
    font-size: 11px;
    font-weight: 700;
}

.ap-live-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #35e0c2;
    box-shadow: 0 0 12px #35e0c2;
    animation: apPulse 1.7s infinite;
}

/* =========================================================
   SECTION HEADINGS
   ========================================================= */

.ap-section {
    margin: 32px 0 14px;
}

.ap-section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 25px;
    font-weight: 700;
    letter-spacing: -.8px;
    color: #e8f8f5;
}

.ap-section-subtitle {
    color: #6f8b87;
    font-size: 12px;
    margin-top: 4px;
}

/* =========================================================
   PREMIUM METRIC CARDS
   ========================================================= */

.ap-metric {
    position: relative;
    overflow: hidden;
    min-height: 150px;
    padding: 21px;
    border-radius: 21px;
    border: 1px solid rgba(255,255,255,.065);
    background:
        linear-gradient(
            145deg,
            rgba(16,43,46,.96),
            rgba(7,22,25,.96)
        );
    box-shadow:
        0 16px 45px rgba(0,0,0,.18),
        inset 0 1px rgba(255,255,255,.025);
    transition:
        transform .25s cubic-bezier(.2,.8,.2,1),
        border-color .25s ease,
        box-shadow .25s ease;
}

.ap-metric:hover {
    transform: translateY(-5px);
    border-color: rgba(53,224,194,.20);
    box-shadow:
        0 22px 55px rgba(0,0,0,.28),
        0 0 35px rgba(53,224,194,.045);
}

.ap-metric::after {
    content: "";
    position: absolute;
    width: 100px;
    height: 100px;
    right: -50px;
    bottom: -50px;
    border-radius: 50%;
    background: rgba(53,224,194,.045);
}

.ap-metric-label {
    color: #718d89;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
}

.ap-metric-value {
    font-family: 'Space Grotesk', sans-serif;
    color: #f0fffc;
    font-size: 34px;
    line-height: 1;
    font-weight: 700;
    letter-spacing: -1.8px;
    margin-top: 13px;
}

.ap-metric-help {
    color: #5f7b77;
    font-size: 10px;
    margin-top: 9px;
}

/* =========================================================
   AQI STATUS
   ========================================================= */

.ap-aqi {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 14px 16px;
    border-radius: 16px;
    background: rgba(255,255,255,.025);
    border: 1px solid rgba(255,255,255,.055);
}

.ap-aqi-ring {
    width: 47px;
    height: 47px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 3px solid #35e0c2;
    box-shadow: 0 0 18px rgba(53,224,194,.18);
    font-size: 15px;
    font-weight: 800;
}

/* =========================================================
   GLASS PANELS
   ========================================================= */

.ap-panel {
    border-radius: 23px;
    border: 1px solid rgba(255,255,255,.065);
    background:
        linear-gradient(
            145deg,
            rgba(15,39,42,.88),
            rgba(7,21,24,.90)
        );
    padding: 21px;
    box-shadow: 0 18px 55px rgba(0,0,0,.16);
}

/* =========================================================
   INFO / EXPLANATION
   ========================================================= */

.ap-explain {
    border-left: 3px solid #35e0c2;
    border-radius: 0 16px 16px 0;
    padding: 16px 18px;
    background:
        linear-gradient(
            90deg,
            rgba(53,224,194,.065),
            rgba(53,224,194,.012)
        );
    color: #93ada9;
    font-size: 12px;
    line-height: 1.7;
    margin: 16px 0;
}

.ap-explain strong {
    color: #c9eeea;
}

/* =========================================================
   CITY CARDS
   ========================================================= */

.ap-city {
    position: relative;
    overflow: hidden;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,.065);
    padding: 19px;
    background: linear-gradient(
        145deg,
        rgba(15,40,43,.94),
        rgba(7,22,25,.96)
    );
    transition:
        transform .22s ease,
        border-color .22s ease;
}

.ap-city:hover {
    transform: translateY(-4px);
    border-color: rgba(53,224,194,.20);
}

.ap-city-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 700;
}

.ap-city-value {
    font-size: 31px;
    font-weight: 800;
    margin-top: 10px;
}

.ap-city-meta {
    color: #67817e;
    font-size: 10px;
    margin-top: 5px;
}

/* =========================================================
   STREAMLIT INPUTS
   ========================================================= */

div[data-baseweb="select"] > div {
    background: #0c2427 !important;
    border: 1px solid rgba(255,255,255,.08) !important;
    border-radius: 13px !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: rgba(53,224,194,.30) !important;
}

.stButton > button {
    border-radius: 13px;
    border: 1px solid rgba(53,224,194,.17);
    background: rgba(53,224,194,.055);
    color: #9aece1;
    font-weight: 700;
    transition: all .22s ease;
}

.stButton > button:hover {
    background: rgba(53,224,194,.13);
    border-color: rgba(53,224,194,.40);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(53,224,194,.08);
}

/* =========================================================
   TABS
   ========================================================= */

button[data-baseweb="tab"] {
    color: #6f8986 !important;
    font-weight: 650 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #66e4d3 !important;
}

/* =========================================================
   CHART CONTAINERS
   ========================================================= */

div[data-testid="stPlotlyChart"] {
    border-radius: 20px;
    overflow: hidden;
    animation: apReveal .55s ease;
}

/* =========================================================
   DATAFRAME
   ========================================================= */

div[data-testid="stDataFrame"] {
    border: 1px solid rgba(255,255,255,.06);
    border-radius: 18px;
    overflow: hidden;
}

/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

.stDownloadButton > button {
    border-radius: 12px;
    background: linear-gradient(
        135deg,
        rgba(53,224,194,.12),
        rgba(56,189,248,.08)
    );
}

/* =========================================================
   SCROLLBAR
   ========================================================= */

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #061113;
}

::-webkit-scrollbar-thumb {
    background: #173b3d;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #245c5b;
}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 900px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .ap-hero {
        padding: 30px 25px;
        border-radius: 23px;
    }

    .ap-hero-title {
        letter-spacing: -2px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PATHS
# ============================================================

ROOT = Path(r"D:\AirPollutionProject")
DASH = ROOT / "dashboard"
DATA = DASH / "data"
RAW = Path(r"D:\bda dataset\raw")

# ============================================================
# GLOBAL STYLE
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 5%, rgba(0, 220, 190, 0.10), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(80, 120, 255, 0.08), transparent 25%),
        #061116;
    color: #eefcff;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, #07191e 0%, #061216 100%);
    border-right: 1px solid rgba(100,255,230,0.12);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

.brand {
    padding: 10px 8px 25px 8px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

.brand-title {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -0.8px;
}

.brand-sub {
    color: #7bded1;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 4px;
}

.nav-title {
    color: #64848a;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    margin: 15px 5px 8px;
}

button[kind="secondary"] {
    border-radius: 12px !important;
    border: 1px solid rgba(100,255,230,0.08) !important;
    background: rgba(255,255,255,0.025) !important;
}

button[kind="secondary"]:hover {
    border-color: rgba(100,255,230,0.40) !important;
    background: rgba(0,220,190,0.08) !important;
}

.hero {
    padding: 42px 45px;
    border-radius: 28px;
    background:
        radial-gradient(circle at 80% 20%, rgba(0,255,210,0.18), transparent 30%),
        linear-gradient(135deg, rgba(14,53,61,0.95), rgba(6,20,25,0.98));
    border: 1px solid rgba(100,255,230,0.15);
    box-shadow: 0 25px 80px rgba(0,0,0,0.25);
    margin-bottom: 24px;
}

.hero-kicker {
    color: #58e8d0;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 13px;
}

.hero h1 {
    font-size: clamp(38px, 5vw, 70px);
    line-height: 0.98;
    letter-spacing: -3px;
    margin: 0;
}

.hero h1 span {
    color: #5ef2d7;
}

.hero p {
    color: #a5c0c5;
    max-width: 760px;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 20px;
}

.section-kicker {
    color: #55e5cf;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 2.5px;
    margin-bottom: 6px;
}

.section-title {
    font-size: 30px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 3px;
}

.section-desc {
    color: #769197;
    margin-bottom: 22px;
}

.metric-card {
    background: linear-gradient(145deg, rgba(18,49,57,0.90), rgba(8,25,30,0.95));
    border: 1px solid rgba(100,255,230,0.12);
    border-radius: 18px;
    padding: 20px;
    min-height: 125px;
}

.metric-label {
    color: #78969b;
    font-size: 10px;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    font-weight: 700;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 10px;
    color: #efffff;
}

.metric-note {
    color: #58dfcb;
    font-size: 11px;
    margin-top: 4px;
}

.insight {
    background: linear-gradient(135deg, rgba(15,55,61,0.75), rgba(6,26,31,0.85));
    border: 1px solid rgba(100,255,230,0.10);
    border-radius: 18px;
    padding: 20px;
    margin: 8px 0;
}

.insight-title {
    font-weight: 800;
    color: #dffffa;
    margin-bottom: 7px;
}

.insight-text {
    color: #8da9ae;
    font-size: 13px;
    line-height: 1.6;
}

.status-pill {
    display: inline-block;
    padding: 6px 11px;
    border-radius: 999px;
    background: rgba(77,235,201,0.10);
    color: #61e6cf;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.city-card {
    background: linear-gradient(145deg, rgba(12,47,54,0.9), rgba(6,21,26,0.95));
    border: 1px solid rgba(100,255,230,0.13);
    border-radius: 24px;
    padding: 25px;
    margin-bottom: 18px;
}

.city-name {
    font-size: 34px;
    font-weight: 800;
}

.city-meta {
    color: #6e9097;
    font-size: 12px;
}

.big-number {
    font-size: 40px;
    font-weight: 800;
    color: #65efda;
}

.footer {
    margin-top: 60px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.07);
    color: #557279;
    font-size: 11px;
    text-align: center;
}

[data-testid="stMetric"] {
    background: rgba(10,35,41,0.65);
    border: 1px solid rgba(100,255,230,0.10);
    padding: 15px;
    border-radius: 15px;
}

[data-testid="stMetricValue"] {
    color: #efffff;
}

.stSelectbox > div > div {
    border-radius: 12px;
}

div[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPERS
# ============================================================

def locate_file(name):
    candidates = [
        DATA / name,
        RAW / name,
        DATA / (name.replace(".csv", "")),
        RAW / (name.replace(".csv", ""))
    ]

    for p in candidates:
        if p.exists():
            return p

    matches = []
    for folder in [DATA, RAW]:
        if folder.exists():
            matches.extend(folder.glob(name + "*"))

    return matches[0] if matches else None


@st.cache_data(show_spinner=False)
def load_csv(path):
    if path is None:
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def get_col(df, possibilities):
    if df.empty:
        return None

    lower = {str(c).lower().strip(): c for c in df.columns}

    for p in possibilities:
        if p.lower() in lower:
            return lower[p.lower()]

    for c in df.columns:
        lc = str(c).lower().strip()
        for p in possibilities:
            if p.lower() in lc:
                return c

    return None


def metric_card(label, value, note=""):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def section(kicker, title, description=""):
    st.markdown(f'<div class="section-kicker">{kicker}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

    if description:
        st.markdown(f'<div class="section-desc">{description}</div>', unsafe_allow_html=True)


def chart_layout(fig, height=450):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#cce1e5"),
        margin=dict(l=20, r=20, t=55, b=20),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#b9d0d4")
        ),
        xaxis=dict(
            gridcolor="rgba(255,255,255,0.07)",
            zerolinecolor="rgba(255,255,255,0.08)"
        ),
        yaxis=dict(
            gridcolor="rgba(255,255,255,0.07)",
            zerolinecolor="rgba(255,255,255,0.08)"
        )
    )
    return fig


def category(aqi):
    if pd.isna(aqi):
        return "Unknown"
    if aqi <= 50:
        return "Good"
    if aqi <= 100:
        return "Satisfactory"
    if aqi <= 200:
        return "Moderate"
    if aqi <= 300:
        return "Poor"
    if aqi <= 400:
        return "Very Poor"
    return "Severe"


# ============================================================
# CITY COORDINATES
# ============================================================

CITY_COORDS = {
    "Ahmedabad": (23.0225, 72.5714),
    "Aizawl": (23.7271, 92.7176),
    "Amaravati": (16.5062, 80.6480),
    "Amritsar": (31.6340, 74.8723),
    "Bengaluru": (12.9716, 77.5946),
    "Bhopal": (23.2599, 77.4126),
    "Brajrajnagar": (21.8167, 83.9167),
    "Chandigarh": (30.7333, 76.7794),
    "Chennai": (13.0827, 80.2707),
    "Coimbatore": (11.0168, 76.9558),
    "Delhi": (28.6139, 77.2090),
    "Ernakulam": (9.9816, 76.2999),
    "Gurugram": (28.4595, 77.0266),
    "Guwahati": (26.1445, 91.7362),
    "Hyderabad": (17.3850, 78.4867),
    "Jaipur": (26.9124, 75.7873),
    "Jorapokhar": (23.7167, 86.4167),
    "Kochi": (9.9312, 76.2673),
    "Kolkata": (22.5726, 88.3639),
    "Lucknow": (26.8467, 80.9462),
    "Mumbai": (19.0760, 72.8777),
    "Patna": (25.5941, 85.1376),
    "Shillong": (25.5788, 91.8933),
    "Talcher": (20.9500, 85.2167),
    "Thiruvananthapuram": (8.5241, 76.9366),
    "Visakhapatnam": (17.6868, 83.2185)
}

# ============================================================
# LOAD CORE DATA
# ============================================================

pred = load_csv(locate_file("predictions_2020.csv"))
forecast = load_csv(locate_file("forecast_2026.csv"))
performance = load_csv(locate_file("model_performance.csv"))
importance = load_csv(locate_file("feature_importance.csv"))
city_summary = load_csv(locate_file("city_forecast_summary.csv"))
monthly_forecast = load_csv(locate_file("monthly_forecast_summary.csv"))

weather = load_csv(locate_file("weather_india.csv"))
vehicle = load_csv(locate_file("vehicle_dataset.csv"))
citydetails = load_csv(locate_file("citydetails.csv"))

# ============================================================
# NORMALIZE CORE DATA
# ============================================================

if not pred.empty:
    pc = get_col(pred, ["City"])
    pdte = get_col(pred, ["Date"])
    pa = get_col(pred, ["AQI", "ActualAQI", "actual"])
    pp = get_col(pred, ["prediction", "PredictedAQI", "Predicted", "prediction_aqi"])

    if pc:
        pred["City_std"] = pred[pc].astype(str)
    if pdte:
        pred["Date_std"] = pd.to_datetime(pred[pdte], errors="coerce")
    if pa:
        pred["Actual_std"] = pd.to_numeric(pred[pa], errors="coerce")
    if pp:
        pred["Predicted_std"] = pd.to_numeric(pred[pp], errors="coerce")

if not forecast.empty:
    fc = get_col(forecast, ["City"])
    fd = get_col(forecast, ["Date"])
    fa = get_col(forecast, ["AQI", "prediction", "PredictedAQI"])
    fb = get_col(forecast, ["AQI_Bucket", "Category"])

    if fc:
        forecast["City_std"] = forecast[fc].astype(str)
    if fd:
        forecast["Date_std"] = pd.to_datetime(forecast[fd], errors="coerce")
    if fa:
        forecast["ForecastAQI"] = pd.to_numeric(forecast[fa], errors="coerce")
    if fb:
        forecast["ForecastCategory"] = forecast[fb].astype(str)

# ============================================================
# DERIVED CITY INTELLIGENCE
# ============================================================

if not pred.empty and "City_std" in pred.columns:
    city_map = (
        pred.groupby("City_std")
        .agg(
            Observed_AQI=("Actual_std", "mean"),
            Predicted_AQI=("Predicted_std", "mean"),
            Maximum_AQI=("Actual_std", "max"),
            Records=("City_std", "size")
        )
        .reset_index()
    )

    city_map["Error"] = city_map["Predicted_AQI"] - city_map["Observed_AQI"]

    if not forecast.empty and "City_std" in forecast.columns:
        fc_avg = (
            forecast.groupby("City_std")["ForecastAQI"]
            .mean()
            .reset_index()
            .rename(columns={"ForecastAQI": "Forecast_2026"})
        )
        city_map = city_map.merge(fc_avg, on="City_std", how="left")
    else:
        city_map["Forecast_2026"] = np.nan

    city_map["Latitude"] = city_map["City_std"].map(
        lambda x: CITY_COORDS.get(x, (np.nan, np.nan))[0]
    )
    city_map["Longitude"] = city_map["City_std"].map(
        lambda x: CITY_COORDS.get(x, (np.nan, np.nan))[1]
    )
    city_map["AQI_Category"] = city_map["Observed_AQI"].apply(category)

else:
    city_map = pd.DataFrame(
        columns=[
            "City_std", "Observed_AQI", "Predicted_AQI",
            "Maximum_AQI", "Records", "Forecast_2026",
            "Latitude", "Longitude", "AQI_Category"
        ]
    )

CITIES = sorted(city_map["City_std"].dropna().unique().tolist())

if not CITIES:
    CITIES = sorted(CITY_COORDS.keys())

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Command Center"

pages = [
    ("⌂", "Command Center"),
    ("◉", "City Intelligence"),
    ("◌", "Historical AQI"),
    ("⌁", "ML Predictions"),
    ("◇", "2026 Forecast"),
    ("✦", "Weather Intelligence"),
    ("▣", "Vehicle Intelligence"),
    ("◈", "Model Intelligence"),
    ("⬡", "Big Data Architecture"),
]

with st.sidebar:
    st.markdown("""
    <div class="brand">
        <div class="brand-title">🌍 AirPulse India</div>
        <div class="brand-sub">ENVIRONMENTAL INTELLIGENCE</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-title">EXPLORE</div>', unsafe_allow_html=True)

    for icon, label in pages:
        if st.button(
            f"{icon}  {label}",
            key=f"nav_{label}",
            width="stretch"
        ):
            st.session_state.page = label
            st.rerun()

    st.markdown("---")

    st.markdown('<div class="nav-title">SYSTEM STATUS</div>', unsafe_allow_html=True)

    st.markdown(
        '<span class="status-pill">● HDFS DATA LAYER</span>',
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        '<span class="status-pill">● APACHE SPARK</span>',
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        '<span class="status-pill">● SPARK ML</span>',
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown(
        '<span class="status-pill">● INTERACTIVE ANALYTICS</span>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("AirPulse India • Big Data Environmental Intelligence")
    st.caption("Historical observations: 2015–2020")
    st.caption("2026 output: baseline forecast")

# ============================================================
# COMMAND CENTER
# ============================================================

def command_center():

    st.markdown("""
    <div class="hero">
        <div class="hero-kicker">INDIA • AIR QUALITY • BIG DATA • MACHINE LEARNING</div>
        <h1>From pollution data<br><span>to environmental intelligence.</span></h1>
        <p>
        AirPulse India combines large-scale air-quality observations,
        Apache Spark processing, Random Forest prediction, weather intelligence
        and vehicle trends to understand pollution patterns across 26 monitored cities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    avg_actual = pred["Actual_std"].mean() if not pred.empty else 0
    avg_pred = pred["Predicted_std"].mean() if not pred.empty else 0
    test_rows = len(pred)
    forecast_rows = len(forecast)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Observed AQI", f"{avg_actual:.2f}", "2020 test period")

    with c2:
        metric_card("ML Estimated AQI", f"{avg_pred:.2f}", "Random Forest")

    with c3:
        metric_card("Cities Monitored", "26", "Indian cities")

    with c4:
        metric_card("Forecast Records", f"{forecast_rows:,}", "2026 baseline")

    st.write("")

    section(
        "SPATIAL INTELLIGENCE",
        "India pollution landscape",
        "Explore the monitored cities. Hover for a full city profile or select a point to inspect it."
    )

    if not city_map.empty:

        map_df = city_map.dropna(subset=["Latitude", "Longitude"]).copy()

        fig = px.scatter_map(
            map_df,
            lat="Latitude",
            lon="Longitude",
            size="Observed_AQI",
            color="Observed_AQI",
            color_continuous_scale=[
                [0.00, "#27d7c1"],
                [0.20, "#77e65b"],
                [0.40, "#ffe04b"],
                [0.60, "#ffad42"],
                [0.80, "#ff5c5c"],
                [1.00, "#b53cff"]
            ],
            size_max=28,
            zoom=4.15,
            center={"lat": 22.5, "lon": 79.0},
            map_style="open-street-map",
            hover_name="City_std",
            hover_data={
                "Observed_AQI": ":.2f",
                "Predicted_AQI": ":.2f",
                "Maximum_AQI": ":.0f",
                "Records": ":,.0f",
                "Forecast_2026": ":.2f",
                "AQI_Category": True,
                "Latitude": False,
                "Longitude": False
            },
            labels={
                "Observed_AQI": "Observed AQI",
                "Predicted_AQI": "ML Prediction",
                "Maximum_AQI": "Maximum",
                "Records": "Records",
                "Forecast_2026": "2026 Baseline",
                "AQI_Category": "Category"
            }
        )

        fig.update_layout(
            height=650,
            margin=dict(l=0, r=0, t=0, b=0),
            coloraxis_colorbar=dict(
                title="AQI",
                tickfont=dict(color="#cde5e8")
            )
        )

        event = st.plotly_chart(
            fig,
            width="stretch",
            key="india_air_map",
            on_select="rerun",
            selection_mode="points",
            config={
                "scrollZoom": True,
                "displaylogo": False,
                "responsive": True
            }
        )

        # Map point selection
        try:
            points = event.selection.points
            if points:
                selected = points[0].get("customdata")
                if selected:
                    st.session_state["selected_city"] = selected[0]
        except Exception:
            pass

    st.write("")

    # City spotlight
    default_city = st.session_state.get(
        "selected_city",
        "Delhi" if "Delhi" in CITIES else CITIES[0]
    )

    if default_city not in CITIES:
        default_city = CITIES[0]

    selected_city = st.selectbox(
        "CITY SPOTLIGHT",
        CITIES,
        index=CITIES.index(default_city),
        key="command_city"
    )

    row = city_map[city_map["City_std"] == selected_city]

    if not row.empty:
        r = row.iloc[0]

        st.markdown(
            f"""
            <div class="city-card">
                <div class="section-kicker">CITY PROFILE</div>
                <div class="city-name">{selected_city}</div>
                <div class="city-meta">
                    Historical observations • ML estimate • 2026 baseline
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        a, b, c, d, e = st.columns(5)

        with a:
            st.metric("Observed AQI", f"{r.Observed_AQI:.2f}")

        with b:
            st.metric("ML Prediction", f"{r.Predicted_AQI:.2f}")

        with c:
            st.metric("Maximum", f"{r.Maximum_AQI:.0f}")

        with d:
            st.metric("2026 Baseline", f"{r.Forecast_2026:.2f}")

        with e:
            st.metric("Records", f"{int(r.Records):,}")

        st.markdown(
            f"""
            <div class="insight">
                <div class="insight-title">
                    {selected_city} — {category(r.Observed_AQI)}
                </div>
                <div class="insight-text">
                    The dashboard combines observed AQI with the Random Forest estimate
                    and the model-generated 2026 baseline. Use City Intelligence for
                    the detailed pollutant and temporal profile.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # City landscape
    st.write("")
    section(
        "CITY COMPARISON",
        "Observed AQI across monitored cities",
        "A visual comparison of average observed AQI in the 2020 test-period data."
    )

    if not city_map.empty:
        bar = city_map.sort_values("Observed_AQI").copy()

        fig = px.bar(
            bar,
            x="Observed_AQI",
            y="City_std",
            orientation="h",
            color="Observed_AQI",
            color_continuous_scale=[
                "#36d8c3", "#8be55b", "#ffe04b",
                "#ff9b3d", "#ff5555", "#a43dff"
            ],
            labels={
                "Observed_AQI": "Average AQI",
                "City_std": ""
            }
        )

        fig = chart_layout(fig, 650)
        fig.update_layout(coloraxis_showscale=False)

        st.plotly_chart(fig, width="stretch")

# ============================================================
# CITY INTELLIGENCE
# ============================================================

def city_intelligence():

    section(
        "CITY INTELLIGENCE",
        "Understand one city from multiple angles",
        "Choose a city to connect its pollution history, ML estimates and 2026 baseline."
    )

    city = st.selectbox("SELECT CITY", CITIES, key="city_intelligence_select")

    cdata = pred[pred["City_std"] == city].copy() if not pred.empty else pd.DataFrame()
    fdata = forecast[forecast["City_std"] == city].copy() if not forecast.empty else pd.DataFrame()

    if not cdata.empty:
        observed = cdata["Actual_std"].mean()
        predicted = cdata["Predicted_std"].mean()
        maximum = cdata["Actual_std"].max()
        records = len(cdata)
    else:
        observed = predicted = maximum = 0
        records = 0

    baseline = fdata["ForecastAQI"].mean() if not fdata.empty else 0

    st.markdown(
        f"""
        <div class="city-card">
            <div class="section-kicker">SELECTED CITY</div>
            <div class="city-name">{city}</div>
            <div class="city-meta">
                Integrated pollution intelligence profile
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    a, b, c, d, e = st.columns(5)

    with a:
        st.metric("Observed", f"{observed:.2f}")

    with b:
        st.metric("ML Estimate", f"{predicted:.2f}")

    with c:
        st.metric("Maximum", f"{maximum:.0f}")

    with d:
        st.metric("2026 Baseline", f"{baseline:.2f}")

    with e:
        st.metric("Records", f"{records:,}")

    st.write("")

    if not cdata.empty:
        cdata = cdata.sort_values("Date_std")

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=cdata["Date_std"],
                y=cdata["Actual_std"],
                mode="lines",
                name="Observed AQI",
                line=dict(color="#57e8d1", width=2)
            )
        )

        fig.add_trace(
            go.Scatter(
                x=cdata["Date_std"],
                y=cdata["Predicted_std"],
                mode="lines",
                name="ML Prediction",
                line=dict(color="#ff7a92", width=2)
            )
        )

        fig = chart_layout(fig, 470)
        fig.update_layout(title=f"{city} — observed vs ML estimated AQI")

        st.plotly_chart(fig, width="stretch")

        left, right = st.columns(2)

        with left:
            monthly = (
                cdata.assign(Month=cdata["Date_std"].dt.month)
                .groupby("Month")["Actual_std"]
                .mean()
                .reset_index()
            )

            fig2 = px.bar(
                monthly,
                x="Month",
                y="Actual_std",
                color="Actual_std",
                color_continuous_scale=["#40d9c3", "#ffe04b", "#ff5b61"],
                labels={"Actual_std": "Average AQI"}
            )
            fig2 = chart_layout(fig2, 380)
            fig2.update_layout(coloraxis_showscale=False, title="Seasonal AQI pattern")
            st.plotly_chart(fig2, width="stretch")

        with right:
            cdata["Error"] = cdata["Predicted_std"] - cdata["Actual_std"]

            fig3 = px.histogram(
                cdata,
                x="Error",
                nbins=35,
                color_discrete_sequence=["#63e7d3"],
                labels={"Error": "Prediction error"}
            )
            fig3 = chart_layout(fig3, 380)
            fig3.update_layout(title="Prediction error distribution")
            st.plotly_chart(fig3, width="stretch")

# ============================================================
# HISTORICAL AQI
# ============================================================

def historical_page():

    section(
        "HISTORICAL ANALYTICS",
        "What did the pollution data reveal?",
        "Explore temporal patterns, distributions and city-level differences."
    )

    if pred.empty:
        st.warning("2020 prediction data is not available.")
        return

    c1, c2 = st.columns([1, 3])

    with c1:
        city = st.selectbox(
            "CITY",
            ["All Cities"] + CITIES,
            key="historical_city"
        )

    data = pred.copy()

    if city != "All Cities":
        data = data[data["City_std"] == city]

    data["Year"] = data["Date_std"].dt.year
    data["Month"] = data["Date_std"].dt.month

    a, b, c, d = st.columns(4)

    with a:
        metric_card("Records", f"{len(data):,}", "Selected period")

    with b:
        metric_card("Average AQI", f"{data.Actual_std.mean():.2f}", "Observed")

    with c:
        metric_card("Peak AQI", f"{data.Actual_std.max():.0f}", "Maximum")

    with d:
        metric_card("AQI Std. Dev.", f"{data.Actual_std.std():.2f}", "Variability")

    st.write("")

    left, right = st.columns(2)

    with left:
        daily = (
            data.groupby("Date_std")["Actual_std"]
            .mean()
            .reset_index()
        )

        fig = px.line(
            daily,
            x="Date_std",
            y="Actual_std",
            labels={"Date_std": "Date", "Actual_std": "AQI"}
        )
        fig = chart_layout(fig, 430)
        fig.update_layout(title="AQI movement over time")
        st.plotly_chart(fig, width="stretch")

    with right:
        fig = px.histogram(
            data,
            x="Actual_std",
            nbins=45,
            color_discrete_sequence=["#63e7d3"],
            labels={"Actual_std": "AQI"}
        )
        fig = chart_layout(fig, 430)
        fig.update_layout(title="AQI distribution")
        st.plotly_chart(fig, width="stretch")

    monthly = (
        data.groupby("Month")["Actual_std"]
        .mean()
        .reset_index()
    )

    fig = px.area(
        monthly,
        x="Month",
        y="Actual_std",
        markers=True,
        labels={"Actual_std": "Average AQI"}
    )
    fig = chart_layout(fig, 420)
    fig.update_layout(title="Monthly pollution pattern")
    st.plotly_chart(fig, width="stretch")

# ============================================================
# ML PREDICTIONS
# ============================================================

def ml_page():

    section(
        "MACHINE LEARNING",
        "How closely did the model reproduce observed AQI?",
        "Random Forest regression trained on historical pollution and temporal features."
    )

    rmse = 31.18
    mae = 17.875
    r2 = 0.8604

    if not performance.empty:
        for _, row in performance.iterrows():
            text = " ".join(str(x) for x in row.values)
            low = text.lower()

            if "rmse" in low:
                nums = pd.to_numeric(
                    row.astype(str).str.extract(r"([-+]?\d*\.?\d+)")[0],
                    errors="coerce"
                ).dropna()
                if len(nums):
                    rmse = float(nums.iloc[-1])

            if "mae" in low:
                nums = pd.to_numeric(
                    row.astype(str).str.extract(r"([-+]?\d*\.?\d+)")[0],
                    errors="coerce"
                ).dropna()
                if len(nums):
                    mae = float(nums.iloc[-1])

            if "r2" in low or "r²" in low:
                nums = pd.to_numeric(
                    row.astype(str).str.extract(r"([-+]?\d*\.?\d+)")[0],
                    errors="coerce"
                ).dropna()
                if len(nums):
                    r2 = float(nums.iloc[-1])

    a, b, c, d = st.columns(4)

    with a:
        metric_card("RMSE", f"{rmse:.2f}", "Test set")

    with b:
        metric_card("MAE", f"{mae:.2f}", "Test set")

    with c:
        metric_card("R²", f"{r2:.4f}", "Explained variance")

    with d:
        metric_card("Test Rows", f"{len(pred):,}", "2020")

    st.write("")

    if not pred.empty:
        sample = pred.dropna(
            subset=["Actual_std", "Predicted_std"]
        ).copy()

        sample["Error"] = sample["Predicted_std"] - sample["Actual_std"]
        sample["Absolute_Error"] = sample["Error"].abs()

        fig = px.scatter(
            sample,
            x="Actual_std",
            y="Predicted_std",
            color="Absolute_Error",
            hover_name="City_std",
            hover_data={
                "Actual_std": ":.2f",
                "Predicted_std": ":.2f",
                "Error": ":.2f",
                "Absolute_Error": ":.2f"
            },
            color_continuous_scale=[
                "#42dfc4", "#ffe04c", "#ff5d61"
            ],
            labels={
                "Actual_std": "Observed AQI",
                "Predicted_std": "ML Prediction",
                "Absolute_Error": "Absolute error"
            }
        )

        maxv = max(
            sample["Actual_std"].max(),
            sample["Predicted_std"].max()
        )

        fig.add_trace(
            go.Scatter(
                x=[0, maxv],
                y=[0, maxv],
                mode="lines",
                name="Perfect prediction",
                line=dict(
                    color="#ffffff",
                    dash="dash",
                    width=2
                )
            )
        )

        fig = chart_layout(fig, 550)
        fig.update_layout(title="Observed AQI vs Random Forest prediction")

        st.plotly_chart(fig, width="stretch")

        left, right = st.columns(2)

        with left:
            fig2 = px.histogram(
                sample,
                x="Error",
                nbins=50,
                color_discrete_sequence=["#ff7a92"],
                labels={"Error": "Prediction error"}
            )
            fig2 = chart_layout(fig2, 400)
            fig2.update_layout(title="Model error distribution")
            st.plotly_chart(fig2, width="stretch")

        with right:
            top = (
                sample.groupby("City_std")["Absolute_Error"]
                .mean()
                .sort_values(ascending=False)
                .head(12)
                .reset_index()
            )

            fig3 = px.bar(
                top,
                x="Absolute_Error",
                y="City_std",
                orientation="h",
                color="Absolute_Error",
                color_continuous_scale=["#40dcc5", "#ffe24d", "#ff5a60"],
                labels={"Absolute_Error": "Mean absolute error"}
            )
            fig3 = chart_layout(fig3, 400)
            fig3.update_layout(title="City-level prediction error")
            st.plotly_chart(fig3, width="stretch")

# ============================================================
# 2026 FORECAST
# ============================================================

def forecast_page():

    section(
        "FORECAST INTELLIGENCE",
        "2026 pollution baseline",
        "A model-based baseline generated from historical city/month pollutant patterns. It is not measured 2026 pollution."
    )

    if forecast.empty:
        st.warning("2026 forecast data is not available.")
        return

    city = st.selectbox(
        "CITY",
        ["All Cities"] + CITIES,
        key="forecast_city"
    )

    data = forecast.copy()

    if city != "All Cities":
        data = data[data["City_std"] == city]

    a, b, c, d = st.columns(4)

    with a:
        metric_card("Forecast Rows", f"{len(data):,}", "2026")

    with b:
        metric_card("Average AQI", f"{data.ForecastAQI.mean():.2f}", "Baseline")

    with c:
        metric_card("Maximum", f"{data.ForecastAQI.max():.2f}", "Projected peak")

    with d:
        metric_card("Cities", f"{data.City_std.nunique()}", "Coverage")

    st.write("")

    if city != "All Cities":

        daily = (
            data.groupby("Date_std")["ForecastAQI"]
            .mean()
            .reset_index()
        )

        fig = px.area(
            daily,
            x="Date_std",
            y="ForecastAQI",
            labels={"ForecastAQI": "Baseline AQI"}
        )
        fig = chart_layout(fig, 450)
        fig.update_layout(title=f"{city} — 2026 baseline trajectory")
        st.plotly_chart(fig, width="stretch")

    else:

        city_avg = (
            data.groupby("City_std")["ForecastAQI"]
            .mean()
            .sort_values()
            .reset_index()
        )

        fig = px.bar(
            city_avg,
            x="ForecastAQI",
            y="City_std",
            orientation="h",
            color="ForecastAQI",
            color_continuous_scale=[
                "#39d8c0", "#85e65c", "#ffe04a",
                "#ff9d3f", "#ff5555"
            ],
            labels={"ForecastAQI": "2026 baseline AQI"}
        )
        fig = chart_layout(fig, 650)
        fig.update_layout(
            title="Average 2026 baseline by city",
            coloraxis_showscale=False
        )
        st.plotly_chart(fig, width="stretch")

    if "Date_std" in data.columns:
        monthly = (
            data.assign(Month=data["Date_std"].dt.month)
            .groupby("Month")["ForecastAQI"]
            .mean()
            .reset_index()
        )

        fig2 = px.line(
            monthly,
            x="Month",
            y="ForecastAQI",
            markers=True,
            labels={"ForecastAQI": "Average baseline AQI"}
        )
        fig2 = chart_layout(fig2, 400)
        fig2.update_layout(title="2026 monthly baseline pattern")
        st.plotly_chart(fig2, width="stretch")

    with st.expander("View detailed forecast records"):
        st.dataframe(
            data.sort_values(["City_std", "Date_std"]),
            width="stretch",
            height=420
        )

        st.download_button(
            "Download filtered forecast CSV",
            data=data.to_csv(index=False).encode("utf-8"),
            file_name="airpulse_2026_forecast.csv",
            mime="text/csv",
            width="stretch"
        )

# ============================================================
# WEATHER INTELLIGENCE
# ============================================================

def weather_page():

    section(
        "ATMOSPHERIC CONDITIONS",
        "Weather intelligence",
        "NASA POWER weather variables are connected to the same city/date framework used by the pollution analysis."
    )

    if weather.empty:
        st.error(
            "Weather dataset could not be loaded from D:\\bda dataset\\raw."
        )
        return

    wc = get_col(weather, ["City"])
    wd = get_col(weather, ["Date"])

    if wc:
        weather["City_std"] = weather[wc].astype(str)

    if wd:
        weather["Date_std"] = pd.to_datetime(
            weather[wd],
            errors="coerce"
        )

    city = st.selectbox(
        "CITY",
        sorted(weather["City_std"].dropna().unique()),
        key="weather_city"
    )

    w = weather[weather["City_std"] == city].copy()

    st.markdown(
        f"""
        <div class="city-card">
            <div class="section-kicker">ATMOSPHERIC PROFILE</div>
            <div class="city-name">{city}</div>
            <div class="city-meta">
                {len(w):,} weather observations available
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    numeric = [
        ("T2M", "Temperature"),
        ("RH2M", "Relative Humidity"),
        ("PRECTOTCORR", "Precipitation"),
        ("WS2M", "Wind Speed"),
        ("PS", "Surface Pressure")
    ]

    available = [(c, label) for c, label in numeric if c in w.columns]

    cols = st.columns(len(available))

    for col, (name, label) in zip(cols, available):
        with col:
            metric_card(
                label,
                f"{pd.to_numeric(w[name], errors='coerce').mean():.2f}",
                "mean"
            )

    st.write("")

    if available:
        long = w[["Date_std"] + [x[0] for x in available]].copy()
        long = long.melt(
            id_vars="Date_std",
            var_name="Variable",
            value_name="Value"
        )

        fig = px.line(
            long,
            x="Date_std",
            y="Value",
            facet_row="Variable",
            labels={"Value": ""}
        )

        fig = chart_layout(fig, max(450, 150 * len(available)))
        fig.update_layout(title=f"{city} — weather timeline")
        fig.for_each_annotation(
            lambda a: a.update(text=a.text.split("=")[-1])
        )

        st.plotly_chart(fig, width="stretch")

    # AQI + weather relationship
    if not pred.empty and "City_std" in pred.columns:
        p = pred[pred["City_std"] == city].copy()

        if not p.empty and "Date_std" in p.columns:

            merged = p.merge(
                w,
                on=["City_std", "Date_std"],
                how="inner"
            )

            if len(merged) > 10:

                variable = st.selectbox(
                    "COMPARE AQI WITH",
                    [x[0] for x in available],
                    key="weather_compare"
                )

                merged[variable] = pd.to_numeric(
                    merged[variable],
                    errors="coerce"
                )

                merged["Actual_std"] = pd.to_numeric(
                    merged["Actual_std"],
                    errors="coerce"
                )

                merged = merged.dropna(
                    subset=[variable, "Actual_std"]
                )

                fig = px.scatter(
                    merged,
                    x=variable,
                    y="Actual_std",
                    color="Actual_std",
                    color_continuous_scale=[
                        "#42ddc4", "#ffe04b", "#ff5b5e"
                    ],
                    labels={
                        variable: variable,
                        "Actual_std": "Observed AQI"
                    }
                )

                fig = chart_layout(fig, 450)
                fig.update_layout(
                    title=f"{city} — {variable} vs observed AQI"
                )

                st.plotly_chart(fig, width="stretch")

# ============================================================
# VEHICLE INTELLIGENCE
# ============================================================

def vehicle_page():

    section(
        "MOBILITY INTELLIGENCE",
        "Vehicle registration trends",
        "Explore the completed city-level vehicle dataset and its year-to-year movement."
    )

    if vehicle.empty:
        st.error(
            "Vehicle dataset could not be loaded from D:\\bda dataset\\raw."
        )
        return

    vc = get_col(vehicle, ["City"])
    if vc:
        vehicle["City_std"] = vehicle[vc].astype(str)

    city = st.selectbox(
        "CITY",
        sorted(vehicle["City_std"].dropna().unique()),
        key="vehicle_city"
    )

    row = vehicle[vehicle["City_std"] == city].copy()

    year_cols = []
    for y in range(2015, 2021):
        c = get_col(row, [str(y)])
        if c:
            year_cols.append((str(y), c))

    if not year_cols:
        st.warning("No 2015–2020 vehicle columns were detected.")
        st.dataframe(row, width="stretch")
        return

    vals = []
    for y, c in year_cols:
        value = pd.to_numeric(row[c], errors="coerce").iloc[0]
        vals.append({"Year": int(y), "Vehicles": value})

    vd = pd.DataFrame(vals).dropna()

    if vd.empty:
        st.warning("Vehicle values are unavailable.")
        return

    start = vd["Vehicles"].iloc[0]
    end = vd["Vehicles"].iloc[-1]
    growth = ((end - start) / start * 100) if start else 0

    a, b, c, d = st.columns(4)

    with a:
        metric_card("2015", f"{start:,.0f}", "registrations")

    with b:
        metric_card("2020", f"{end:,.0f}", "registrations")

    with c:
        metric_card("Change", f"{end-start:,.0f}", "vehicles")

    with d:
        metric_card("Growth", f"{growth:.1f}%", "2015 → 2020")

    st.write("")

    fig = px.area(
        vd,
        x="Year",
        y="Vehicles",
        markers=True,
        labels={"Vehicles": "Vehicle registrations"}
    )

    fig = chart_layout(fig, 450)
    fig.update_layout(title=f"{city} — vehicle registration trajectory")

    st.plotly_chart(fig, width="stretch")

    st.write("")

    # City comparison
    comparison = []

    for city_name in sorted(vehicle["City_std"].dropna().unique()):
        r = vehicle[vehicle["City_std"] == city_name]

        first = pd.to_numeric(r[year_cols[0][1]], errors="coerce").iloc[0]
        last = pd.to_numeric(r[year_cols[-1][1]], errors="coerce").iloc[0]

        comparison.append({
            "City": city_name,
            "2015": first,
            "2020": last,
            "Growth": ((last-first)/first*100) if first else np.nan
        })

    comp = pd.DataFrame(comparison).dropna()

    fig2 = px.bar(
        comp.sort_values("Growth"),
        x="Growth",
        y="City",
        orientation="h",
        color="Growth",
        color_continuous_scale=[
            "#39d9c0", "#ffe04b", "#ff5b60"
        ],
        labels={"Growth": "Growth %"}
    )

    fig2 = chart_layout(fig2, 650)
    fig2.update_layout(
        title="Vehicle registration growth by city",
        coloraxis_showscale=False
    )

    st.plotly_chart(fig2, width="stretch")

    st.dataframe(vd, width="stretch")

# ============================================================
# MODEL INTELLIGENCE
# ============================================================

def model_page():

    section(
        "MODEL INTELLIGENCE",
        "What drove the AQI prediction?",
        "Random Forest feature importance reveals which engineered inputs contributed most strongly to the model."
    )

    if importance.empty:
        st.warning("Feature importance data is unavailable.")
        return

    fc = get_col(
        importance,
        ["Feature", "feature", "FeatureName", "Name"]
    )

    ic = get_col(
        importance,
        ["Importance", "importance", "Value"]
    )

    if fc is None or ic is None:
        st.dataframe(importance, width="stretch")
        return

    imp = importance[[fc, ic]].copy()
    imp.columns = ["Feature", "Importance"]

    imp["Importance"] = pd.to_numeric(
        imp["Importance"],
        errors="coerce"
    )

    imp = imp.dropna().sort_values("Importance")

    fig = px.bar(
        imp,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale=[
            "#38d9c1", "#76e45c", "#ffe149", "#ff5a61"
        ],
        labels={"Importance": "Feature importance"}
    )

    fig = chart_layout(fig, 650)
    fig.update_layout(
        title="Random Forest feature importance",
        coloraxis_showscale=False
    )

    st.plotly_chart(fig, width="stretch")

    top = imp.sort_values("Importance", ascending=False).head(5)

    st.markdown(
        '<div class="section-kicker">TOP MODEL SIGNALS</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    for col, (_, r) in zip(cols, top.iterrows()):
        with col:
            metric_card(
                str(r["Feature"]),
                f"{r['Importance']:.4f}",
                "importance"
            )

    st.write("")

    st.dataframe(
        imp.sort_values("Importance", ascending=False),
        width="stretch"
    )

# ============================================================
# BIG DATA ARCHITECTURE
# ============================================================

def architecture_page():

    section(
        "BIG DATA ENGINEERING",
        "How the intelligence pipeline works",
        "The dashboard is the presentation layer on top of the Hadoop, Spark and machine-learning pipeline."
    )

    stages = [
        ("01", "RAW DATA", "City AQI • Weather • Vehicles • City metadata"),
        ("02", "HDFS", "Distributed storage layer"),
        ("03", "APACHE SPARK", "Cleaning • aggregation • transformation"),
        ("04", "FEATURE ENGINEERING", "Pollutants • time features • ML vectors"),
        ("05", "SPARK ML", "Random Forest regression"),
        ("06", "VALIDATION", "2019 validation • 2020 test"),
        ("07", "FORECAST", "2026 city/month baseline"),
        ("08", "INTELLIGENCE", "Interactive environmental dashboard")
    ]

    for i, (num, title, desc) in enumerate(stages):

        c1, c2, c3 = st.columns([1, 3, 6])

        with c1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{num}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">PIPELINE STAGE</div>
                    <div class="metric-value" style="font-size:20px">{title}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">PROCESS</div>
                    <div style="font-size:14px;margin-top:15px;color:#a8c4c8">
                        {desc}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        if i < len(stages)-1:
            st.markdown(
                '<div style="text-align:center;color:#3edac2;font-size:20px">↓</div>',
                unsafe_allow_html=True
            )

    st.write("")

    section(
        "PROJECT SCALE",
        "Numbers behind the pipeline",
        "These values come from the completed Spark and ML stages."
    )

    a, b, c, d = st.columns(4)

    with a:
        metric_card("Cleaned AQI Rows", "29,531", "Spark processed")

    with b:
        metric_card("ML Rows", "24,850", "valid AQI")

    with c:
        metric_card("Test Rows", "4,421", "2020")

    with d:
        metric_card("2026 Forecast", "9,490", "26 × 365")

    st.write("")

    st.markdown("""
    <div class="insight">
        <div class="insight-title">Why this is a Big Data project</div>
        <div class="insight-text">
        The dashboard is not the core computation. The analytical workload is performed
        through Hadoop HDFS and Apache Spark, followed by Spark ML Random Forest regression.
        Streamlit is the visualization and interaction layer that exposes those results
        to an end user.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# ROUTER
# ============================================================

page = st.session_state.page

if page == "Command Center":
    command_center()

elif page == "City Intelligence":
    city_intelligence()

elif page == "Historical AQI":
    historical_page()

elif page == "ML Predictions":
    ml_page()

elif page == "2026 Forecast":
    forecast_page()

elif page == "Weather Intelligence":
    weather_page()

elif page == "Vehicle Intelligence":
    vehicle_page()

elif page == "Model Intelligence":
    model_page()

elif page == "Big Data Architecture":
    architecture_page()

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <b>AirPulse India</b> • Big Data Environmental Intelligence<br>
    Hadoop HDFS • Apache Spark • Spark ML • Random Forest • Streamlit • Plotly<br>
    Historical observations and model-based 2026 baseline analysis
</div>
""", unsafe_allow_html=True)


