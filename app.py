import streamlit as st
import sqlite3
import hashlib
import secrets
import hmac
import re
import ast
from pathlib import Path
from datetime import datetime
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    LongTable
)


# ============================================================
# STREAMLIT CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Warrap State Integrated Analytics",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.login-container {
    max-width: 500px;
    margin: auto;
}

.app-header {
    padding: 15px;
    border-radius: 12px;
    background: linear-gradient(90deg, #1f4e79, #2874a6);
    color: white;
    text-align: center;
    margin-bottom: 20px;
}

.info-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #f1f5f9;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DATABASE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "users.db"


def init_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


init_database()


# ============================================================
# PASSWORD SECURITY
# ============================================================

def hash_password(password):
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        200000
    )

    return salt.hex() + "$" + password_hash.hex()


def verify_password(password, stored_password):

    try:
        salt_hex, stored_hash = stored_password.split("$")

        salt = bytes.fromhex(salt_hex)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            200000
        ).hex()

        return hmac.compare_digest(password_hash, stored_hash)

    except Exception:
        return False


# ============================================================
# USER FUNCTIONS
# ============================================================

def username_valid(username):

    return bool(
        re.fullmatch(
            r"[A-Za-z0-9_]{3,30}",
            username
        )
    )


def register_user(username, password):

    if not username_valid(username):
        return False, "Username must contain 3–30 letters, numbers or underscores."

    if len(password) < 6:
        return False, "Password must contain at least 6 characters."

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

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
                datetime.now().isoformat()
            )
        )

        connection.commit()

        return True, "Account created successfully."

    except sqlite3.IntegrityError:

        return False, "That username already exists."

    finally:

        connection.close()


def login_user(username, password):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT username, password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return False

    stored_username, stored_password = result

    return verify_password(
        password,
        stored_password
    )


# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# ============================================================
# LOGIN / REGISTRATION SCREEN
# ============================================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <div class="app-header">
            <h1>📊 Warrap State Integrated Analytics</h1>
            <p>Secure Dashboard Access Portal</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='login-container'>",
        unsafe_allow_html=True
    )

    login_tab, register_tab = st.tabs(
        ["🔐 Login", "📝 Create Account"]
    )

    # --------------------------------------------------------
    # LOGIN
    # --------------------------------------------------------

    with login_tab:

        st.subheader("Welcome Back")

        with st.form("login_form"):

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            login_button = st.form_submit_button(
                "🔐 Login",
                use_container_width=True
            )

        if login_button:

            if login_user(username, password):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login successful.")
                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    # --------------------------------------------------------
    # REGISTRATION
    # --------------------------------------------------------

    with register_tab:

        st.subheader("Create Your Account")

        with st.form("registration_form"):

            new_username = st.text_input(
                "Choose Username",
                placeholder="Example: garang123"
            )

            new_password = st.text_input(
                "Create Password",
                type="password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password"
            )

            register_button = st.form_submit_button(
                "📝 Create Account",
                use_container_width=True
            )

        if register_button:

            if new_password != confirm_password:

                st.error("Passwords do not match.")

            else:

                success, message = register_user(
                    new_username,
                    new_password
                )

                if success:

                    st.success(message)
                    st.info(
                        "You can now return to the Login tab."
                    )

                else:

                    st.error(message)

    st.markdown("</div>", unsafe_allow_html=True)

    st.stop()


# ============================================================
# LOGGED-IN SIDEBAR
# ============================================================

with st.sidebar:

    st.success(
        f"👤 Logged in as: {st.session_state.username}"
    )

    st.markdown("---")

    st.markdown("### Dashboard")

    st.markdown(
        """
        **Warrap State Integrated Data Analytics**

        Explore population, healthcare, education,
        livestock, agriculture, climate and county-level
        information.
        """
    )

    st.markdown("---")

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.username = ""

        st.rerun()


# ============================================================
# RUN ORIGINAL DASHBOARD WITHOUT MODIFYING dashboard.py
# ============================================================

def remove_page_config_from_source(source):

    """
    Removes only st.set_page_config() from the code
    while executing it.

    The original dashboard.py file itself is NOT changed.
    """

    tree = ast.parse(source)

    new_body = []

    for node in tree.body:

        if (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
        ):

            function = node.value.func

            if (
                isinstance(function, ast.Attribute)
                and isinstance(function.value, ast.Name)
                and function.value.id == "st"
                and function.attr == "set_page_config"
            ):

                continue

        new_body.append(node)

    tree.body = new_body

    ast.fix_missing_locations(tree)

    return compile(
        tree,
        "dashboard.py",
        "exec"
    )


def run_original_dashboard():

    dashboard_path = BASE_DIR / "dashboard.py"

    if not dashboard_path.exists():

        st.error(
            "dashboard.py was not found. "
            "Please make sure your original dashboard code "
            "is saved as dashboard.py in the same repository."
        )

        st.stop()

    source = dashboard_path.read_text(
        encoding="utf-8"
    )

    compiled_code = remove_page_config_from_source(
        source
    )

    dashboard_namespace = {
        "__name__": "__dashboard__"
    }

    exec(
        compiled_code,
        dashboard_namespace
    )

    return dashboard_namespace


# ============================================================
# RUN DASHBOARD
# ============================================================

dashboard_data = run_original_dashboard()


# ============================================================
# PDF REPORT GENERATOR
# ============================================================

def dataframe_to_longtable(
    dataframe,
    title,
    max_rows=None
):

    if dataframe is None:
        return []

    df = dataframe.copy()

    if max_rows is not None:
        df = df.head(max_rows)

    df = df.fillna("")

    data = [list(df.columns)]

    for row in df.astype(str).values.tolist():
        data.append(row)

    elements = []

    elements.append(
        Paragraph(
            title,
            ParagraphStyle(
                "SectionTitle",
                fontSize=13,
                leading=16,
                spaceAfter=8
            )
        )
    )

    table = LongTable(
        data,
        repeatRows=1,
        splitByRow=1
    )

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1f4e79")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                7
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.grey
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP"
            ),
            (
                "ROWBACKGROUNDS",
                (0, 1),
                (-1, -1),
                [
                    colors.white,
                    colors.HexColor("#f3f6f9")
                ]
            ),
        ])
    )

    elements.append(table)
    elements.append(Spacer(1, 15))

    return elements


def create_pdf_report(username, data):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4),
        rightMargin=30,
        leftMargin=30,
        topMargin=35,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1f4e79"),
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=11,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=15,
        textColor=colors.HexColor("#1f4e79"),
        spaceBefore=10,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13
    )

    story = []

    # --------------------------------------------------------
    # COVER
    # --------------------------------------------------------

    story.append(
        Spacer(1, 60)
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
        Paragraph(
            "Comprehensive Data Report",
            subtitle_style
        )
    )

    story.append(
        Paragraph(
            f"Generated for: {username}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"Generated on: "
            f"{datetime.now().strftime('%d %B %Y, %H:%M')}",
            body_style
        )
    )

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            "This report summarizes the information presented "
            "in the Warrap State Integrated Data Analytics Dashboard.",
            body_style
        )
    )

    story.append(
        PageBreak()
    )

    # --------------------------------------------------------
    # DATA TABLES
    # --------------------------------------------------------

    sections = [
        (
            "population_df",
            "Population by County"
        ),
        (
            "hospital_df",
            "Healthcare Facilities by County"
        ),
        (
            "referral_hospitals_df",
            "Referral Hospital Directory"
        ),
        (
            "facility_df",
            "Healthcare Facility Directory"
        ),
        (
            "education_df",
            "Education Infrastructure"
        ),
        (
            "livestock_df",
            "Livestock and Economic Importance"
        ),
        (
            "crop_df",
            "Agricultural Crop Production Index"
        ),
        (
            "climate_df",
            "Climate Impact Indicators"
        ),
        (
            "county_df",
            "County Economic Overview"
        )
    ]

    for variable_name, title in sections:

        dataframe = data.get(variable_name)

        if dataframe is not None:

            story.extend(
                dataframe_to_longtable(
                    dataframe,
                    title
                )
            )

    # --------------------------------------------------------
    # DATA SOURCES
    # --------------------------------------------------------

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Data Sources and Methodology",
            heading_style
        )
    )

    story.append(
        Paragraph(
            """
            The dashboard integrates information from relevant
            government, statistical, health, education,
            humanitarian and regional sources. The dashboard
            is designed to support integrated analysis of
            population, healthcare, education, agriculture,
            livestock, climate and county-level development
            indicators.
            """,
            body_style
        )
    )

    story.append(Spacer(1, 15))

    sources = [
        ["Source", "Description"],
        [
            "Warrap State Government",
            "State-level administrative and development information"
        ],
        [
            "National Bureau of Statistics",
            "Population projections and statistical information"
        ],
        [
            "Ministry of Health",
            "Healthcare infrastructure information"
        ],
        [
            "Education Sector Updates",
            "Education infrastructure and school information"
        ],
        [
            "Humanitarian and Regional Assessments",
            "Agriculture, livestock and climate-related information"
        ]
    ]

    source_table = Table(
        sources,
        repeatRows=1,
        colWidths=[2.5 * inch, 7 * inch]
    )

    source_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1f4e79")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.grey
            ),
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                8
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP"
            )
        ])
    )

    story.append(source_table)

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "End of Report",
            subtitle_style
        )
    )

    # --------------------------------------------------------
    # PAGE NUMBER
    # --------------------------------------------------------

    def add_page_number(canvas, document):

        canvas.saveState()

        canvas.setFont(
            "Helvetica",
            8
        )

        canvas.drawRightString(
            landscape(A4)[0] - 30,
            18,
            f"Page {document.page}"
        )

        canvas.restoreState()

    document.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )

    buffer.seek(0)

    return buffer.getvalue()


# ============================================================
# PDF DOWNLOAD SECTION
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div class="app-header">
        <h2>📄 Download Dashboard Report</h2>
        <p>Generate a professional PDF version of the dashboard data.</p>
    </div>
    """,
    unsafe_allow_html=True
)

try:

    pdf_file = create_pdf_report(
        st.session_state.username,
        dashboard_data
    )

    st.download_button(
        label="📥 Download Complete Dashboard PDF",
        data=pdf_file,
        file_name=(
            "Warrap_State_Integrated_Analytics_Report.pdf"
        ),
        mime="application/pdf",
        use_container_width=True
    )

    st.success(
        "Your PDF report is ready."
    )

except Exception as error:

    st.warning(
        "The dashboard is working, but the PDF report "
        f"could not be generated: {error}"
    )
