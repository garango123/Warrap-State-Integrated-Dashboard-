import streamlit as st
import sqlite3
import hashlib
import io
from datetime import datetime
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Warrap State Integrated Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DATABASE
# =========================================================

DB_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def hash_password(password):

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def register_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (username, password, created_at)
            VALUES (?, ?, ?)
            """,
            (
                username,
                hash_password(password),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def authenticate_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username
        FROM users
        WHERE username = ?
        AND password = ?
        """,
        (
            username,
            hash_password(password)
        )
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


create_database()

# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# =========================================================
# PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #f5f7fb;
}

/* Main headings */

h1 {
    font-size: 40px !important;
    font-weight: 800 !important;
}

h2 {
    font-weight: 750 !important;
}

h3 {
    font-weight: 700 !important;
}

/* Metric cards */

div[data-testid="metric-container"] {

    background: white;

    border: 1px solid #e5e7eb;

    border-radius: 18px;

    padding: 22px;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.05);

}

/* Buttons */

.stButton > button,
.stDownloadButton > button {

    border-radius: 12px;

    font-weight: 600;

    min-height: 45px;

}

/* Tables */

[data-testid="stDataFrame"] {

    border-radius: 16px;

    border: 1px solid #e5e7eb;

    overflow: hidden;

}

/* Charts */

.js-plotly-plot {

    background: white !important;

    border-radius: 18px;

    padding: 10px;

    border: 1px solid #e5e7eb;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.04);

}

/* Login card */

.login-card {

    background: white;

    padding: 40px;

    border-radius: 24px;

    border: 1px solid #e5e7eb;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);

}

/* Welcome banner */

.welcome {

    padding: 18px 22px;

    border-radius: 15px;

    background: white;

    border: 1px solid #e5e7eb;

    margin-bottom: 20px;

}

/* Footer */

.footer {

    text-align: center;

    color: #6b7280;

    padding: 30px;

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    st.markdown(
        "<h1 style='text-align:center;'>📊 Warrap State</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>Integrated Data Analytics Dashboard</h3>",
        unsafe_allow_html=True
    )

    st.write("")

    left, center, right = st.columns(
        [1, 2, 1]
    )

    with center:

        st.markdown(
            "<div class='login-card'>",
            unsafe_allow_html=True
        )

        login_tab, register_tab = st.tabs(
            ["🔐 Login", "📝 Create Account"]
        )

        # =================================================
        # LOGIN
        # =================================================

        with login_tab:

            st.subheader("Welcome Back")

            username = st.text_input(
                "Username",
                placeholder="Enter your username",
                key="login_username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
                key="login_password"
            )

            if st.button(
                "🔐 Login",
                use_container_width=True
            ):

                if not username or not password:

                    st.warning(
                        "Please enter your username and password."
                    )

                elif authenticate_user(
                    username,
                    password
                ):

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.rerun()

                else:

                    st.error(
                        "Incorrect username or password."
                    )

        # =================================================
        # REGISTER
        # =================================================

        with register_tab:

            st.subheader("Create Your Account")

            new_username = st.text_input(
                "Username",
                placeholder="Choose a username",
                key="new_username"
            )

            new_password = st.text_input(
                "Password",
                type="password",
                placeholder="Minimum 8 characters",
                key="new_password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                key="confirm_password"
            )

            if st.button(
                "📝 Create Account",
                use_container_width=True
            ):

                if not new_username or not new_password:

                    st.warning(
                        "Please complete all fields."
                    )

                elif len(new_password) < 8:

                    st.warning(
                        "Password must contain at least 8 characters."
                    )

                elif new_password != confirm_password:

                    st.error(
                        "Passwords do not match."
                    )

                elif register_user(
                    new_username.strip(),
                    new_password
                ):

                    st.success(
                        "Account created successfully!"
                    )

                    st.info(
                        "Please switch to the Login tab."
                    )

                else:

                    st.error(
                        "That username already exists."
                    )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    st.stop()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("📊 Warrap Analytics")

    st.markdown("---")

    st.success(
        f"👤 {st.session_state.username}"
    )

    st.markdown("### Dashboard")

    navigation = st.radio(
        "Navigate",
        [
            "🏠 Dashboard",
            "📄 PDF Report",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()

    st.markdown("---")

    st.caption(
        "Warrap State Integrated\n"
        "Data Analytics Platform"
    )

# =========================================================
# DASHBOARD
# =========================================================

if navigation == "🏠 Dashboard":

    st.markdown(
        f"""
        <div class="welcome">
        <b>Welcome, {st.session_state.username} 👋</b><br>
        Explore integrated development indicators for Warrap State.
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # QUICK INDICATORS
    # -----------------------------------------------------

    st.title(
        "Warrap State Integrated Data Analytics Dashboard"
    )

    st.markdown(
        """
        Explore population, healthcare, education,
        livestock, agriculture, climate and county-level
        development information.
        """
    )

    st.markdown("---")

    q1, q2, q3, q4 = st.columns(4)

    q1.metric(
        "Population",
        "1.7M"
    )

    q2.metric(
        "Health Facilities",
        "108"
    )

    q3.metric(
        "Primary Schools",
        "1,286"
    )

    q4.metric(
        "Counties",
        "6"
    )

    st.markdown("---")

    # -----------------------------------------------------
    # COUNTY FILTER
    # -----------------------------------------------------

    st.subheader("🔎 County Explorer")

    counties = [
        "All Counties",
        "Gogrial West",
        "Twic",
        "Gogrial East",
        "Tonj North",
        "Tonj South",
        "Tonj East"
    ]

    selected_county = st.selectbox(
        "Select a county",
        counties
    )

    if selected_county != "All Counties":

        st.info(
            f"You are viewing information related to "
            f"**{selected_county} County**."
        )

    # -----------------------------------------------------
    # LOAD ORIGINAL DASHBOARD
    # -----------------------------------------------------

    # IMPORTANT:
    # dashboard.py is your original code.
    # DO NOT MODIFY IT.

    dashboard_file = Path("dashboard.py")

    if dashboard_file.exists():

        # Execute the original dashboard.
        # Its code remains completely unchanged.

        with open(
            dashboard_file,
            "r",
            encoding="utf-8"
        ) as file:

            dashboard_code = file.read()

        exec(
            compile(
                dashboard_code,
                "dashboard.py",
                "exec"
            )
        )

    else:

        st.error(
            "dashboard.py was not found. "
            "Please make sure your original dashboard code "
            "is saved as dashboard.py."
        )

# =========================================================
# PDF REPORT
# =========================================================

elif navigation == "📄 PDF Report":

    st.title("📄 Professional Dashboard Report")

    st.markdown(
        """
        Generate a downloadable PDF report containing
        key Warrap State development indicators.
        """
    )

    st.markdown("---")

    st.subheader("Report Information")

    report_col1, report_col2 = st.columns(2)

    with report_col1:

        st.write(
            f"**Prepared for:** "
            f"{st.session_state.username}"
        )

        st.write(
            "**Region:** Warrap State, South Sudan"
        )

    with report_col2:

        st.write(
            "**Report Type:** Integrated Analytics"
        )

        st.write(
            f"**Date:** "
            f"{datetime.now().strftime('%d %B %Y')}"
        )

    # =====================================================
    # PDF GENERATOR
    # =====================================================

    def create_pdf():

        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            Table,
            TableStyle,
            PageBreak
        )

        from reportlab.lib import colors

        from reportlab.lib.styles import (
            getSampleStyleSheet,
            ParagraphStyle
        )

        from reportlab.lib.enums import TA_CENTER

        buffer = io.BytesIO()

        document = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=45,
            bottomMargin=45
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "DashboardTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            fontSize=20,
            leading=25,
            spaceAfter=20
        )

        section_style = ParagraphStyle(
            "Section",
            parent=styles["Heading2"],
            fontSize=15,
            leading=20,
            spaceBefore=15,
            spaceAfter=10
        )

        normal_style = ParagraphStyle(
            "Normal",
            parent=styles["BodyText"],
            fontSize=10,
            leading=15
        )

        story = []

        # -------------------------------------------------
        # COVER
        # -------------------------------------------------

        story.append(
            Spacer(1, 50)
        )

        story.append(
            Paragraph(
                "WARRAP STATE",
                title_style
            )
        )

        story.append(
            Paragraph(
                "Integrated Data Analytics Dashboard",
                title_style
            )
        )

        story.append(
            Spacer(1, 25)
        )

        story.append(
            Paragraph(
                "Professional Regional Development Report",
                normal_style
            )
        )

        story.append(
            Spacer(1, 15)
        )

        story.append(
            Paragraph(
                f"Prepared for: "
                f"{st.session_state.username}",
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"Generated: "
                f"{datetime.now().strftime('%d %B %Y, %H:%M')}",
                normal_style
            )
        )

        story.append(
            Spacer(1, 50)
        )

        story.append(
            Paragraph(
                "This report summarizes selected population, "
                "healthcare, education, livestock, agriculture "
                "and climate indicators for Warrap State.",
                normal_style
            )
        )

        story.append(
            PageBreak()
        )

        # -------------------------------------------------
        # EXECUTIVE SUMMARY
        # -------------------------------------------------

        story.append(
            Paragraph(
                "Executive Summary",
                section_style
            )
        )

        summary = """
        Warrap State Integrated Data Analytics Dashboard
        provides a consolidated view of important regional
        development indicators. The dashboard covers
        population, healthcare infrastructure, education,
        livestock, agriculture, climate stressors and
        county-level information.
        """

        story.append(
            Paragraph(
                summary,
                normal_style
            )
        )

        # -------------------------------------------------
        # POPULATION
        # -------------------------------------------------

        story.append(
            Paragraph(
                "1. Population",
                section_style
            )
        )

        population_table = Table([
            ["Indicator", "Value"],
            ["Estimated Population", "1.7 Million"],
            ["Number of Counties", "6"]
        ], colWidths=[280, 180])

        population_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            population_table
        )

        # -------------------------------------------------
        # HEALTHCARE
        # -------------------------------------------------

        story.append(
            Paragraph(
                "2. Healthcare Infrastructure",
                section_style
            )
        )

        health_table = Table([
            ["Indicator", "Value"],
            ["PHCCs", "23"],
            ["PHCUs", "85"],
            ["Referral Hospitals", "4"],
            ["Total Facilities", "108"]
        ], colWidths=[280, 180])

        health_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            health_table
        )

        # -------------------------------------------------
        # EDUCATION
        # -------------------------------------------------

        story.append(
            Paragraph(
                "3. Education Infrastructure",
                section_style
            )
        )

        education_table = Table([
            ["Indicator", "Value"],
            ["Primary Schools", "1,286"],
            ["Secondary Schools", "86"],
            ["CEC Centers", "6"],
            ["TVET Centers", "3"]
        ], colWidths=[280, 180])

        education_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            education_table
        )

        # -------------------------------------------------
        # LIVESTOCK
        # -------------------------------------------------

        story.append(
            Paragraph(
                "4. Livestock Economy",
                section_style
            )
        )

        story.append(
            Paragraph(
                "Estimated cattle population: "
                "7 Million Head.",
                normal_style
            )
        )

        # -------------------------------------------------
        # AGRICULTURE
        # -------------------------------------------------

        story.append(
            Paragraph(
                "5. Agricultural Production",
                section_style
            )
        )

        crop_table = Table([
            ["Crop", "Production Index"],
            ["Sorghum", "95"],
            ["Groundnuts", "80"],
            ["Maize", "75"],
            ["Sesame", "60"],
            ["Millet", "55"]
        ], colWidths=[280, 180])

        crop_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            crop_table
        )

        # -------------------------------------------------
        # CLIMATE
        # -------------------------------------------------

        story.append(
            Paragraph(
                "6. Climate and System Stressors",
                section_style
            )
        )

        climate_table = Table([
            ["Stress Factor", "Impact Level"],
            ["Flooding", "90"],
            ["Disease", "75"],
            ["Water Competition", "65"],
            ["Crop Damage", "80"],
            ["Grazing Pressure", "70"]
        ], colWidths=[280, 180])

        climate_table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ])
        )

        story.append(
            climate_table
        )

        # -------------------------------------------------
        # METHODOLOGY
        # -------------------------------------------------

        story.append(
            Paragraph(
                "7. Methodology",
                section_style
            )
        )

        methodology = """
        Data were organized and presented using Python,
        Pandas, Plotly and Streamlit. Where direct
        county-level data were unavailable, derived
        estimates should be interpreted as estimates
        rather than directly published official figures.
        """

        story.append(
            Paragraph(
                methodology,
                normal_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        story.append(
            Paragraph(
                "Data may vary by year, methodology and "
                "reporting period.",
                normal_style
            )
        )

        document.build(story)

        buffer.seek(0)

        return buffer.getvalue()

    # =====================================================
    # DOWNLOAD BUTTON
    # =====================================================

    pdf_data = create_pdf()

    st.download_button(
        label="⬇️ Download Professional PDF Report",
        data=pdf_data,
        file_name=(
            "Warrap_State_Integrated_Dashboard_Report.pdf"
        ),
        mime="application/pdf",
        use_container_width=True
    )

# =========================================================
# ABOUT
# =========================================================

elif navigation == "ℹ️ About":

    st.title("ℹ️ About the Dashboard")

    st.markdown(
        """
        ### Warrap State Integrated Data Analytics Dashboard

        This platform brings together regional development
        indicators into a single interactive analytics
        environment.

        #### Main Areas

        - 👥 Population
        - 🏥 Healthcare
        - 🎓 Education
        - 🐄 Livestock
        - 🌾 Agriculture
        - 🌦️ Climate
        - 🏘️ County-level development

        #### Technology

        The platform is built using:

        - Python
        - Streamlit
        - Pandas
        - Plotly
        - SQLite
        - ReportLab

        #### Purpose

        The dashboard is designed to make regional data
        easier to explore, understand and communicate.
        """
    )

    st.markdown("---")

    st.info(
        "Data should always be interpreted according to "
        "its source, reporting year and methodology."
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        © 2026 Warrap State Integrated Data Analytics Dashboard<br>
        Built with Python and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
