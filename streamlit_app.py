# streamlit_app.py
import streamlit as st
from pathlib import Path
import base64
import textwrap

# ------------------ Editable profile content ------------------
NAME = "Mohammed Sinwan"
TITLE = "Data Scientist"
SUMMARY = (
    "Data Scientist with hands-on experience in machine learning, web scraping, "
    "data visualization and deploying apps. Comfortable with Python, Streamlit, SQL "
    "and building end-to-end project demos."
)

SKILLS = ["Python", "Pandas", "NumPy", "Scikit-learn", "Streamlit", "Selenium", "SQL", "PowerBI", "Tableau"]
PROJECTS = [
    "PowerPulse: Household Energy Forecast",
    "Data-Driven Stock Analysis Dashboard",
    "Restaurant Recommendation System using clustering/similarity",
    "Web Scraping & Analysis of Transportation Data",
    "Multi-class Image Classification with CNNs",
    "Deployment of News Article Categorization Application Using AWS Services"
]

EXPERIENCE = [
    {"title": "Operation Head", "period": "2019 — 2024", "desc": "Managed operations, sales and process improvements."},
    {"title": "Front Office Assistant", "period": "2017 — 2018", "desc": "Customer handling, scheduling and basic admin tasks."}
]

EDUCATION = [
    {"title": "B.Sc. — PSG College of Arts & Science, Coimbatore", "period": "2013 — 2016", "desc": "Bachelor of Science (Hotel Management)."},
    {"title": "Guvi - incubated with IIT-M", "period": "2024 — 2025", "desc": "Data Science & Machine Learning."}
]

CONTACTS = {
    "email": "sinwanmohammed022@gmail.com",
    "phone": "7550313915",
    "linkedin": "https://www.linkedin.com/in/sinwan-siraj-07b410162/",
    "github": "https://github.com/SinwanSiraj"
}

# ------------------ Files (make sure these exist in same folder) ------------------
RESUME_PATH = Path("sinwan-B14.pdf.pdf")
CODE_PRACTICE_PATH = Path("Codekata-Report-1763797675239.pdf")

# ------------------ Icons ------------------
ICON_LINKEDIN = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
ICON_GITHUB = "https://cdn-icons-png.flaticon.com/512/25/25231.png"
ICON_EMAIL = "https://cdn-icons-png.flaticon.com/512/732/732200.png"
ICON_PHONE = "https://cdn-icons-png.flaticon.com/512/597/597177.png"
ICON_PDF = "https://cdn-icons-png.flaticon.com/512/337/337946.png"

# ------------------ Page setup ------------------
st.set_page_config(page_title=f"{NAME} — Portfolio", layout="wide", initial_sidebar_state="expanded", page_icon="💼")

# ------------------ Helpers ------------------
def file_to_base64(path: Path):
    try:
        data = path.read_bytes()
        return base64.b64encode(data).decode("utf-8")
    except Exception:
        return None

def embed_pdf(path: Path, height=700):
    b64 = file_to_base64(path)
    if not b64:
        st.warning("PDF not available to embed.")
        return
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="{height}" type="application/pdf"></iframe>'
    st.components.v1.html(pdf_display, height=height, scrolling=True)

# ------------------ CSS: sticky navbar + styles ------------------
st.markdown(
    f""" <style> 
    /* Reset body background for clean look */ 
    .stApp {{ 
    background-image: url(https://raw.githubusercontent.com/Shuying-exquisite/streamlit-app/main/刷步数/image.jpg); 
    background-size: 100% 100%; 
    background-repeat: no-repeat; 
    background-attachment: fixed; }}
    /* Sticky top navbar */
    .topnav {{
        position: sticky;
        top: 0;
        Z-index: 9999;
        background: #1e3a8a; /* indigo */
        padding: 10px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        box-shadow: 0 6px 18px rgba(16,24,40,0.12);
    }}
    .nav-left {{ display:flex; align-items:center; gap:12px; }}
    .brand-name {{ color: #fff; font-weight:700; font-size:18px; text-decoration:none; }}
    .nav-links {{ display:flex; gap:8px; }}
    .nav-links button {{
        background: transparent;
        border: none;
        color: #e6eefb;
        padding: 8px 12px;
        border-radius: 8px;
        font-weight:600;
        cursor:pointer;
        transition: all 0.12s ease-in-out;
    }}
    .nav-links button:hover {{
        background: rgba(255,255,255,0.06);
        transform: translateY(-1px);
        color: #fff;
        box-shadow: 0 4px 10px rgba(14, 27, 84, 0.18);
    }}
    .cta-icons img {{ margin-left:10px; vertical-align: middle; border-radius:6px; }}
    /* Profile / card timeline styles */
    .profile-box {{ text-align:center; padding:14px; border-radius:12px; background:#fff; box-shadow: 0 6px 18px rgba(2,6,23,0.06); }}
    .section-head {{ font-size:20px; font-weight:700; margin-top:12px; margin-bottom:8px; }}
    .timeline {{ margin-top:8px; }}
    .card-item {{
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 6px 18px rgba(2,6,23,0.06);
        padding: 18px;
        margin: 12px 0;
        border-left: 6px solid #2563eb;
    }}
    .card-title {{ font-size: 18px; font-weight:700; margin-bottom:6px; }}
    .card-period {{ color: #6b7280; font-size: 13px; margin-bottom:10px; }}
    .skill-badge {{ display:inline-block; padding:6px 10px; margin:6px 6px 6px 0; border-radius:999px; border:1px solid #e6eefb; font-size:14px; background: #ffffff; }}
    footer{{ text-align:center; color:#6b7280; padding:18px 0; }}
    @media (max-width: 640px) {{
        .nav-links button {{ padding:8px 8px; font-size:14px; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------ Top navigation (ensure session state) ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Build nav buttons (must match dispatcher names exactly)
pages = ["Home", "My Journey", "Skills", "Projects", "Experience", "Education", "Code Practice", "Certifications"]
cols = st.columns([1]*len(pages), gap="small")
for c, p in zip(cols, pages):
    with c:
        if st.button(p):
            st.session_state.page = p

# Floating CTA icons moved to bottom of the page (fixed position)
st.markdown(
    f"""
    <div style="position:fixed; bottom:20px; left:50%; transform:translateX(-50%); z-index:9999;
                display:flex; gap:12px; align-items:center; background:rgba(255,255,255,0.9);
                padding:8px 12px; border-radius:10px; box-shadow:0 6px 18px rgba(2,6,23,0.08);">
        {'<a href="mailto:'+CONTACTS['email']+'"><img src="'+ICON_EMAIL+'" width="28" alt="email"></a>' if CONTACTS.get('email') else ''}
        {'<a href="tel:'+CONTACTS['phone']+'"><img src="'+ICON_PHONE+'" width="28" alt="phone"></a>' if CONTACTS.get('phone') else ''}
        {'<a href="'+CONTACTS['linkedin']+'" target="_blank"><img src="'+ICON_LINKEDIN+'" width="28" alt="linkedin"></a>' if CONTACTS.get('linkedin') else ''}
        {'<a href="'+CONTACTS['github']+'" target="_blank"><img src="'+ICON_GITHUB+'" width="28" alt="github"></a>' if CONTACTS.get('github') else ''}
        {f'<a href="#" onclick="window.location.reload();"><img src=\"{ICON_PDF}\" width=\"28\" alt=\"resume\"></a>' if RESUME_PATH.exists() else ''}
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------ Page renderers ------------------
def render_home():
    st.markdown(
        """
        <div style='text-align:center; margin-top:80px; margin-bottom:10px;'>
            <h1 style='font-size:40px; font-weight:800; margin-bottom:10px;'>
                Mohammed Sinwan
            </h1>
            <p style='font-size:28px; color:#374151; margin-top:-10px;'>
                Data Scientist
            </p>
        </div>

        <div style='text-align:center; margin-top:50px;'>
            <p style='font-size:28px; font-weight:500; color:#111827; line-height:0.2;
                      font-family:Georgia, serif;'>
                “Life reshaped by loss, rebuilt by discipline, and driven by curiosity.”
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_my_journey():
    st.header("My Journey")
    story = textwrap.dedent("""
        Some stories are written in libraries.
        Mine was written on busy hotel lobbies, lonely highways, quiet farms, and in the silent spaces after loss.

        From 2013 to 2024, my life was less like a straight line
        and more like a movie with unexpected twists—
        each chapter teaching me what no classroom ever could.

        I wasn't a topper.
        As a below-average student, I completed my UG with more dreams than direction.
        But one thing stayed with me:
        **I always acted on whatever I believed in—immediately, fearlessly.**
        Failure never frightened me back then, because I never imagined what consequences meant.

        My first job at **Black Thunder Resort** looked simple on the surface—
        a Front Office Assistant greeting guests and checking bookings.
        But it became the **first page of my real education**.

        Front Office is the face of any luxury hotel.
        That responsibility shaped me fast.
        For the first time, I learned to give **100% with care, discipline, and precision**.
        And life rewarded me—
        I fulfilled my first desire and bought an **Indica car for ₹65,000**.

        Everything felt stable…
        until life decided to flip to its darkest chapter.

        **December 26, 2018 — 3:30 AM.**
        The man who smiled at me every night when I returned from work—
        my father, my hero—
        took his last breath.

        No movie prepares you for that silence.
        Life splits into two parts right there:
        **before dad and after dad.**

        2019 didn’t begin with celebrations;
        it began with responsibilities that weren’t mine, but had no one else to carry them.
        Suddenly I became a **Co-Founder of his restaurant**,
        a **Farmer**,
        and a student of the harshest teacher—life.

        I learned more than business:
        human behavior, problem-solving, money flow, customer experience, team dynamics, discipline, and emotional strength.

        In 2021, I stepped into transport and started goods & vegetable delivery with my own load van.
        In 2022, I bought two cows to deliver pure milk — with zero marketing, people trusted me.

        Meanwhile at the restaurant:
        - Revenue increased by **25–30% yearly**
        - On-time delivery improved
        - Stock-outs reduced
        - Costs optimized
        - Success rate increased by **15–20%**

        Curiosity became my compass.
        Knowledge became my backbone.
        But peace… peace slowly faded away.

        Even with all these wins,
        I discovered the uncomfortable truth—
        our financial state was the **same as the beginning**.
        And I finally understood my father's warning:

        **"Study. Learn. Skill up.**
        Life can take away everything—except what’s inside you."**

        One by one, nature pressed the reset button:
        the restaurant building was reclaimed,
        my van met with an accident from a flyover,
        and every business I ran slowly dissolved.

        But this time, I wasn't afraid.
        I had a new belief:

        **Unexpected events can destroy what you built,
        but they can never destroy who you become.**

        In June 2024, I closed the shop,
        sold the van,
        and made the bravest decision of my life—
        to rebuild myself, not my business.

        I searched for a field that needs curiosity, discipline, logic, and problem-solving—
        a career where thinking *is* the job.
        That's when I discovered **Data Science**.

        I joined GUVI and began learning.
        It looked simple—until projects arrived.
        Reality hit—coding wasn't typing;
        it was thinking, falling, breaking, retrying.

        It took **one full year** of practice to understand Python deeply.
        But I didn't stop.
        I couldn't stop.

        Today, I walk a new path—
        not as the student I once was,
        but as the man life shaped me into:

        **Curious.
        Disciplined.
        Skilled.
        And ready for the next chapter.**

        This isn't a story of someone who had it easy.
        It's the story of someone who refused to stop learning,
        no matter how brutal the plot twist.

        And my journey continues from here—
        with a mind that's curious,
        a heart that's steady,
        and a purpose that finally makes sense.
    """)
    st.markdown(f"<div style='font-size:16px; line-height:1.7;'>{story}</div>", unsafe_allow_html=True)
    st.markdown("----")

def render_skills():
    st.header("Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='margin-top:15px;'>

            <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=matplotlib&logoColor=black"><br><br>
            <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
            
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style='margin-top:15px;'>

            <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Machine%20Learning-009688?style=for-the-badge&logo=keras&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"><br><br>
            <img src="https://img.shields.io/badge/Computer%20Vision-3D3D3D?style=for-the-badge&logo=opencv&logoColor=white">

            </div>
            """,
            unsafe_allow_html=True,
        )


def render_projects():
    st.header("Projects")
    for p in PROJECTS:
        st.subheader(p)
        st.write(f"http://github.com/Sinwansiraj/{p.replace(' ', '_')}.")
        st.markdown("---")

def render_experience():
    st.header("Experience")
    for e in EXPERIENCE:
        st.markdown(f"**{e['title']}**  —  {e.get('period','')}")
        st.write(e.get('desc',''))
        st.markdown("---")

def render_education():
    st.header("Education")
    for ed in EDUCATION:
        st.markdown(f"**{ed['title']}**  —  {ed.get('period','')}")
        st.write(ed.get('desc',''))
        st.markdown("---")
def render_code_practice():
        st.header("Code Practice — Practice Reports & Solutions")
        st.write("Below is the Code Practice PDF showcasing my problem-solving skills and coding exercises.")
        if CODE_PRACTICE_PATH.exists():
            try:
                b64 = file_to_base64(CODE_PRACTICE_PATH)
                if b64:
                    # Use <object> with a download fallback; often more reliable than iframe/data-urls in some browsers
                    pdf_html = f"""
                    <div style="width:100%; height:800px; overflow:auto; background:#fff; border-radius:8px; padding:6px;">
                    <object data="data:application/pdf;base64,{b64}" type="application/pdf" width="100%" height="100%">
                    <p style="font-size:16px;">
                    This browser cannot display PDFs inline. You can
                    <a href="data:application/pdf;base64,{b64}" download="{CODE_PRACTICE_PATH.name}">download the PDF</a>.
                    </p>
                    </object>
                    </div>
                    """
                    st.components.v1.html(pdf_html, height=820, scrolling=True)
                    # Also offer a download button as fallback
                    with open(CODE_PRACTICE_PATH, "rb") as f:
                        st.download_button("Download Code Practice PDF", f, file_name=CODE_PRACTICE_PATH.name)
                else:
                    st.warning("Failed to read the PDF for embedding. Please use the download button below.")
                    with open(CODE_PRACTICE_PATH, "rb") as f:
                        st.download_button("Download Code Practice PDF", f, file_name=CODE_PRACTICE_PATH.name)
            except Exception as err:
                st.warning(f"Could not embed PDF (error: {err}). You can download it below.")
                with open(CODE_PRACTICE_PATH, "rb") as f:
                    st.download_button("Download Code Practice PDF", f, file_name=CODE_PRACTICE_PATH.name)
            else:
                st.warning(f"Code Practice PDF not found at {CODE_PRACTICE_PATH}")

def render_certifications():
    st.header("Certifications")

    st.markdown("### Verified Certificates & Job Simulations")
    st.markdown("---")

    certs = [
        {
            "title": "AWS Solutions Architecture Job Simulation – Forage",
            "img": "/mnt/data/AWS.png",
            "date": "June 26th, 2025",
            "issuer": "AWS x Forage",
            "credential_id": "wptzZ2hztQ7AcLmT8",
            "credential_url": "https://www.theforage.com/completion-certificates/pmnMSL4QiQ9JCgE3W/kkE9HyeNcw6rwCRGw_pmnMSL4QiQ9JCgE3W_BGpQhcqPtdi6x2yqp_1750906880079_completion_certificate.pdf"
        },
        {
            "title": "British Airways – Data Science Job Simulation",
            "img": "/mnt/data/British_airways.png",
            "date": "June 15th, 2025",
            "issuer": "British Airways x Forage",
            "credential_id": "NWb29Qp5iCJztuqGz",
            "credential_url":"https://www.theforage.com/completion-certificates/tMjbs76F526fF5v3G/NjynCWzGSaWXQCxSX_tMjbs76F526fF5v3G_BGpQhcqPtdi6x2yqp_1749997682838_completion_certificate.pdf"
        },
        {
            "title": "Master Data Science Program – GUVI / IITM Pravartak",
            "img": "/mnt/data/IITM_Data_science certificate.png",
            "date": "Sep 2024 – Feb 2025",
            "issuer": "GUVI, IITM Pravartak",
            "credential_id": "dR4q94e2y3t07516L1",
            "credential_url": "https://www.guvi.in/share-certificate/dR4q94e2y3t07516L1"
        },
        {
            "title": "TATA – Data Visualisation Job Simulation",
            "img": "/mnt/data/TATA_visuals.png",
            "date": "July 6th, 2025",
            "issuer": "TATA x Forage",
            "credential_id": "pfZtLCnG6BzkMQjQr",
            "credential_url": "https://www.theforage.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_BGpQhcqPtdi6x2yqp_1751811661385_completion_certificate.pdf"
        }
    ]

    col1, col2 = st.columns(2)

    # Split 2 certificates in each column
    for i, cert in enumerate(certs):
        with (col1 if i < 2 else col2):
            st.markdown(
                f"""
                <div style=
                    background: #2c3e50;
                    padding: 18px;
                    margin-bottom: 20px;
                    border-radius: 12px;
                    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.25);
                '>
                    <img src='{cert["img"]}' width='100%' style='border-radius:8px;'>
                    <h4 style='margin-top:15px;'>{cert["title"]}</h4>
                    <p><strong>Issued:</strong> {cert["date"]}</p>
                    <p><strong>Issuer:</strong> {cert["issuer"]}</p>
                    <p><strong>Credential ID:</strong> {cert["credential_id"]}</p>
                    <a href="{cert['credential_url']}" target="_blank">
                        <button style="
                            background:#1e3a8a;
                            color:white;
                            padding:8px 14px;
                            border:none;
                            border-radius:6px;
                            cursor:pointer;
                            margin-top:6px;
                        ">
                            View Credential
                        </button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------ Dispatcher ------------------
page = st.session_state.get("page", "Home")

if page == "Home":
    render_home()
elif page == "My Journey":
    render_my_journey()
elif page == "Skills":
    render_skills()
elif page == "Projects":
    render_projects()
elif page == "Experience":
    render_experience()
elif page == "Education":
    render_education()
elif page == "Code Practice":
    render_code_practice()
elif page == "Certifications":
    render_certifications()
else:
    render_home()










# ------------------ Footer ------------------

st.markdown(
    """
    <footer>
        <p>© 2025 Mohammed Sinwan. All rights reserved.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)