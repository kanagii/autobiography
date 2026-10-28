import textwrap
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).parent  # all file paths below are relative to app.py

# ---------------------------------------------------------------------------
# 1. YOUR DETAILS: replace everything in [brackets]
# ---------------------------------------------------------------------------
NAME = "Jim Lord Kim P. Agbon"
PROGRAM = "BS in Computer Science"
YEAR = "Third Year"
SECTION = "BSCS - F2"
TAGLINE = "Bite more than you can chew and figure out how to chew it later."
EMAIL = "jimlordkim@gmail.com"
GITHUB = "https://github.com/kanagii"
LEETCODE_PROFILE = "https://leetcode.com/u/kanagi/"
PHOTO_PATH = BASE / "photo.jpg"  # drop a photo next to app.py to replace the stand-in

ACCENT = "#7C83D6"  # indigo, the main color
ROSE = "#D98BA8"    # soft rose, used sparingly
TEAL = "#6FB7A8"    # muted teal, used sparingly

BIO = {
    "Background": (
        """My journey started in Cebu City before moving to Consolacion, where I grew up with my cousins. I spent my childhood with relatives who lived nearby and even though I don't talk to them much anymore, I still maintain relationships with them despite our distance.

During my childhood, all I did was building stuff from nothing with LEGOs and playing games for a long period of time on my Game Boy before I got internet access when I reached fifth grade. During this time, chess became my favorite game during my childhood years. I never treated chess as a serious game but I enjoyed how its strategic enough to play competitively until I played at the inter-school municipal chess competition.

My entry into tech was fairly organic/common. Spending countless hours on my laptop made me realize how comfortable I felt working with it. While computing can be a love-hate relationship at times, as anyone who code knows, my love for thinking and maybe even problem solving made computer science a natural fit for me."""
    ),
    "Education": """
- **Primary education:** Spent 1st to 4th grade at Punta Princesa Elementary School in Cebu City before transferring to Paraclete Learning Center in Consolacion for 5th and 6th grade.
- **Secondary education:** Went to Jugan National High School (Grades 7 to 10) and Consolacion National High School for Senior High (Grades 11 to 12). In my last year, I joined the Supreme Student Government, which taught me to be more responsible and how to lead others.
- **Biggest academic regret:** I passed the Cebu City Science High School entrance exam but I decided to back out. I still think about it every now and then, thinking that I could've been better if I had attended there. Still, it remains as one of my top motivators to grab opportunities and to always step out of comfort.
- **College:** Moved back to Cebu City for college, where I'm currently a 3rd-year BS Computer Science student at Cebu Institute of Technology – University (CIT-U).
""",
    "Interests": """
- **Games:** I play Tekken, Genshin Impact, and osu!. I main Lili on Tekken as my past self just assumed that she'd be broken judging by her fit. I got too many things to share for Genshin, but for osu!, I once was part of the country's top 100 players. I miss those days </3
- **LeetCode:** I solve problems when I can, usually at night. Favorite problems include binary trees (very easy to solve), and I hate dynamic programming. Though I still try my best to solve those problems.
- **Working out:** Once in every two days, or if I don't have classes the day after.
- **Piano:** I learn songs on the piano, but mostly anime arrangements.
- **Cubing:** I'm not that fast yet, but I'm working on it. Currently trying to improve my OLL to reduce my average solve time.
- **Music:** I'm obsessed with math rock at the moment. My favorite artists for this genre are toe, tide/edit and Covet. If I had to pick a song, it would be shibuya, by Covet.
""",
}

MILESTONES = [
    ("May 2024", "Graduated high school"),
    ("Aug 2024", "Started college, taking Computer Science"),
    ("Nov 2025", "Led and built Swingify, my first ever project"),
    ("Sep 2026", "Joined my first hackathon (Knowles Hackathon)"),
    ("Now", "Still improving and learning"),
]

SKILLS = pd.DataFrame(
    {
        "Skill": ["Java", "Python", "C++", "C", "JavaScript", "PHP", "MySQL"],
        "Category": ["Language", "Language", "Language", "Language", "Language", "Language", "Database"],
        "Used for": [
            "My main project language",
            "Projects and LeetCode",
            "Data structures and LeetCode",
            "My first language",
            "Mostly forgot about it </3",
            "Not quite experienced",
            "Currently learning",
        ],
        "Level": [85, 77, 68, 57, 30, 40, 44],
    }
)

LC_COUNTS = {"Easy": 138, "Medium": 78, "Hard": 5}  # update as you solve more

PROJECTS = [
    {
        "title": "Kodo",
        "role": "Solo developer",
        "tools": ["Python", "Django"],
        "outcome": "A data structures and algorithms visualizer. Work in progress.",
        "details": "Kodo is a data structures and algorithms visualizer built using Django and Python. Although the frontend visualization engine and complex backend components are still actively in development, I have successfully engineered a custom Python code interpreter to parse and execute user input scripts. Working on Kodo has significantly deepened my understanding of interpreter design, code execution flows, and full-stack system layout.",
        "link": "https://github.com/kanagii/kodo",
    },
    {
        "title": "Swingify",
        "role": "Project lead and developer",
        "tools": ["Java", "Java Swing"],
        "outcome": "A Spotify-inspired music app. My first real project.",
        "details": "Swingify was the first major project I ever built and led to completion. Inspired by Spotify, this desktop music application was built in Java using Java Swing for the user interface. Designing Swingify allowed me to apply core Object-Oriented Programming principles in a real application. It also served as my hands-on introduction to multi-threading concepts, giving me a solid head start on asynchronous execution before we covered it in our coursework.",
        "link": "https://github.com/kim-afk1/Swingify-Music",
    },
    {
        "title": "Orca",
        "role": "Project manager",
        "tools": ["PHP", "MySQL", "JavaScript"],
        "outcome": "A proposed RFID payment system for CIT, built along with a friend.",
        "details": "Orca is a proposed cashless payment system designed to process cashless transactions at CIT. Together with my friend, we came up with various ideas and built the system using JavaScript for interactions, PHP for logic, and SQL for database stuff.",
        "link": "https://github.com/kanagii/Orca",
    },
]

# ---------------------------------------------------------------------------
# 2. PAGE SETUP AND STYLE
# ---------------------------------------------------------------------------
ICON = BASE / "images" / "icon.png"
st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon=str(ICON) if ICON.exists() else "🎹",
    layout="wide",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300..700&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..600&display=swap');

:root { --bg:#0F1014; --surface:#16171D; --line:#24262F; --text:#E7E7EA; --muted:#8C8E99; --accent:#7C83D6; --rose:#D98BA8; --teal:#6FB7A8; }

.stApp {
    background:
        radial-gradient(1200px 640px at 10% -10%, rgba(124,131,214,0.10), transparent 62%),
        radial-gradient(900px 560px at 100% 38%, rgba(217,139,168,0.05), transparent 65%),
        var(--bg);
}

.stApp, .stApp p, .stApp li, .stApp label, .stApp a, .stApp button p, .stApp input, .stApp textarea,
[data-testid="stWidgetLabel"] p, [data-testid="stCaptionContainer"] {
    font-family: 'Manrope', sans-serif;
}

.stMarkdown a { color: #E0A3C2; }
.stMarkdown p, .stMarkdown li { font-size: 1.02rem; line-height: 1.7; letter-spacing: 0.005em; }
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
.block-container { max-width: 1080px; padding-top: 4.5rem; padding-bottom: 5rem; }

.stApp h1, .stApp h2, .stApp h3 {
    font-family: 'Newsreader', serif !important;
    font-weight: 400 !important;
    letter-spacing: -0.01em;
    color: var(--text);
}

.stApp h1 [data-testid="stHeaderActionElements"] { display: none; }

.st-key-stats { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 1.6rem 0; margin-top: 1.5rem; }
.st-key-stats [data-testid="stColumn"] + [data-testid="stColumn"] { border-left: 1px solid var(--line); }
.st-key-stats [data-testid="stColumn"]:first-child [data-testid="stMetricValue"] {
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 0.6rem;
}
.st-key-stats [data-testid="stColumn"]:first-child [data-testid="stMetricValue"]::after {
    content: "and counting";
    font-family: 'Manrope', sans-serif;
    font-weight: 400;
    font-size: 0.95rem;
    letter-spacing: 0.01em;
    color: var(--muted);
}
.stApp h1 { font-size: 3.5rem !important; line-height: 1.02; padding: 0 0 0.4rem 0; }
.stApp h2 { font-size: 2.4rem !important; margin-top: 4.5rem; padding-bottom: 0.2rem; }
.stApp h3 { font-size: 1.6rem !important; }
.tagline { font-family: 'Newsreader', serif; font-style: italic; font-size: 1.7rem; color: #B9BBE8; line-height: 1.3; margin: 0 0 1.2rem 0; }

section[data-testid="stSidebar"] { background: #0C0D11; border-right: 1px solid var(--line); }
section[data-testid="stSidebar"] a { color: var(--text); text-decoration: none; }
section[data-testid="stSidebar"] a:hover { color: var(--accent); }

[class*="st-key-card_"], .st-key-detail_panel {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 1.3rem 1.3rem 1.1rem 1.3rem;
}

[data-testid="stMetric"] { display: flex; flex-direction: column; align-items: center; text-align: center; padding: 0.4rem 0; }
[data-testid="stMetricLabel"] { justify-content: center; }
[data-testid="stMetricLabel"] p { color: var(--muted); }
[data-testid="stMetricValue"] { font-family: 'Newsreader', serif; font-size: 2.6rem; }

.stButton button, .stDownloadButton button, .stLinkButton a {
    background: transparent; border: 1px solid var(--line); border-radius: 8px; color: var(--text);
    transition: border-color .15s ease, color .15s ease;
}
.stButton button:hover, .stDownloadButton button:hover, .stLinkButton a:hover {
    border-color: var(--accent); color: var(--accent);
}
.stFormSubmitButton button { background: var(--accent); color: #0F1014; border: none; border-radius: 8px; font-weight: 500; }
.stFormSubmitButton button:hover { background: #9399E3; color: #0F1014; }

div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] > div { border-radius: 8px; }
.stTabs [data-baseweb="tab-highlight"] { background: var(--accent); }
[data-testid="stImage"] img { border-radius: 14px; border: 1px solid var(--line); }
hr { border-color: var(--line); }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# 3. HELPERS AND SESSION STATE
# ---------------------------------------------------------------------------
if "selected" not in st.session_state:
    st.session_state.selected = None
if "inbox" not in st.session_state:
    st.session_state.inbox = []


def art(path, caption=None):
    """Show an image or GIF from the images folder. Skipped if the file is missing."""
    path = BASE / path
    if path.exists():
        st.image(str(path), caption=caption)


def photo():
    """Your photo if photo.jpg exists, otherwise a labeled initials stand-in."""
    if PHOTO_PATH.exists():
        return str(PHOTO_PATH), NAME
    size = 560
    img = Image.new("RGB", (size, size), (22, 23, 29))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.load_default(size=size // 4)
    except TypeError:
        font = ImageFont.load_default()
    initials = "".join(w[0] for w in NAME.split()[:2]).upper() or "YN"
    draw.text((size / 2, size / 2), initials, fill=(124, 131, 214), font=font, anchor="mm")
    return img, "Stand-in photo. Add photo.jpg next to app.py to replace it."


def bio_markdown():
    parts = [f"# {NAME}", f"{PROGRAM}, {YEAR}", f"{SECTION}", ""]
    for heading, text in BIO.items():
        parts += [f"## {heading}", textwrap.dedent(text).strip(), ""]
    parts.append("## Milestones")
    parts += [f"- {year}: {text}" for year, text in MILESTONES]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# 4. SIDEBAR
# ---------------------------------------------------------------------------
with st.sidebar:
    st.subheader(NAME)
    st.caption(f"{PROGRAM}, {YEAR}")
    st.caption(SECTION)
    st.markdown(
        "[About](#about)  \n[Skills](#skills)  \n[LeetCode](#leetcode)  \n"
        "[Projects](#projects)  \n[Contact](#contact)"
    )
    st.divider()
    show_details = st.checkbox("Show project details", value=True)
    st.download_button("Download my bio", bio_markdown(), file_name="bio.md", mime="text/markdown")

# ---------------------------------------------------------------------------
# 5. HERO
# ---------------------------------------------------------------------------
hero_text, hero_photo = st.columns([3, 2], gap="large", vertical_alignment="center")
with hero_text:
    st.title(NAME)
    st.markdown(f"<p class='tagline'>{TAGLINE}</p>", unsafe_allow_html=True)
    st.write(f"{PROGRAM}, {YEAR}")
    st.caption(SECTION)
    b1, b2, _ = st.columns([1, 1, 3], gap="small")
    b1.link_button("GitHub", GITHUB)
    b2.link_button("LeetCode", LEETCODE_PROFILE)
with hero_photo:
    img, _ = photo()
    st.image(img)

with st.container(key="stats"):
    q1, q2, q3 = st.columns(3)
    q1.metric("LeetCode solved", sum(LC_COUNTS.values()))
    q2.metric("Main language", "Java, Python")
    q3.metric("Focusing on", "MySQL")

# ---------------------------------------------------------------------------
# 6. ABOUT
# ---------------------------------------------------------------------------
st.header("About", anchor="about")
about_left, about_right = st.columns([3, 2], gap="large")

with about_left:
    tabs = st.tabs(list(BIO.keys()))
    for tab, (heading, text) in zip(tabs, BIO.items()):
        with tab:
            st.write(text)
            if heading == "Interests":
                art("images/interests.jpg", caption="Art by @inoitoh on X")
with about_right:
    st.subheader("Milestones")
    for year, text in MILESTONES:
        c1, c2 = st.columns([2, 3])
        c1.markdown(f"<span style='color:{ROSE}; font-weight:600'>{year}</span>", unsafe_allow_html=True)
        c2.write(text)

# ---------------------------------------------------------------------------
# 7. SKILLS
# ---------------------------------------------------------------------------
st.header("Skills", anchor="skills")
st.write(
    "Java is where I am most comfortable with, as I have used it in building most of my projects. I use C++ for data structures "
    "and LeetCode, Python for projects and practice, and C is where I started. "
    "I'm currently focusing on MySQL."
)

f1, f2 = st.columns(2)
category = f1.radio("Show", ["All"] + sorted(SKILLS["Category"].unique()), horizontal=True)
min_level = f2.slider("Minimum level", 0, 100, 0, step=5)

skills_view = SKILLS if category == "All" else SKILLS[SKILLS["Category"] == category]
skills_view = skills_view[skills_view["Level"] >= min_level]

if skills_view.empty:
    st.info("No skills match these filters. Lower the minimum level or pick another category.")
else:
    t_col, c_col = st.columns([5, 4], gap="large")
    with t_col:
        st.dataframe(
            skills_view,
            hide_index=True,
            column_order=["Skill", "Used for", "Level"],
            height=(len(skills_view) + 1) * 35 + 3,
            column_config={
                "Skill": st.column_config.TextColumn("Skill", width=80),
                "Used for": st.column_config.TextColumn("Used for", width=230),
                "Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d", width=150),
            },
        )
    with c_col:
        skills_chart = (
            alt.Chart(skills_view)
            .mark_bar(cornerRadiusEnd=3, size=22)
            .encode(
                y=alt.Y("Skill", sort="-x", title=None),
                x=alt.X("Level", scale=alt.Scale(domain=[0, 100]), title=None),
                color=alt.Color(
                    "Category",
                    scale=alt.Scale(domain=["Language", "Database"], range=[ACCENT, TEAL]),
                    legend=alt.Legend(orient="top", title=None),
                ),
            )
            .properties(height=len(skills_view) * 40 + 110)
        )
        st.altair_chart(skills_chart)

# ---------------------------------------------------------------------------
# 8. LEETCODE
# ---------------------------------------------------------------------------
st.header("LeetCode", anchor="leetcode")
lc = pd.DataFrame({"Difficulty": list(LC_COUNTS.keys()), "Solved": list(LC_COUNTS.values())})
total = int(lc["Solved"].sum())

m1, m2, m3, m4 = st.columns(4)
m1.metric("Solved", total)
m2.metric("Easy", LC_COUNTS["Easy"])
m3.metric("Medium", LC_COUNTS["Medium"])
m4.metric("Hard", LC_COUNTS["Hard"])

st.write("")
lc_chart, lc_text = st.columns([2, 3], gap="large")
with lc_chart:
    chart = (
        alt.Chart(lc)
        .mark_bar(cornerRadiusEnd=3)
        .encode(
            x=alt.X("Difficulty", sort=["Easy", "Medium", "Hard"], axis=alt.Axis(labelAngle=0, title=None)),
            y=alt.Y("Solved", title=None),
            color=alt.Color(
                "Difficulty",
                scale=alt.Scale(domain=["Easy", "Medium", "Hard"], range=[TEAL, ACCENT, ROSE]),
                legend=None,
            ),
        )
        .properties(height=260)
    )
    st.altair_chart(chart)
with lc_text:
    st.write(
        f"I currently have {total} problems solved so far. I mostly practice in C++ and Python, "
        "which is where I practice and refresh my knowledge with data structures."
    )
    st.link_button("View my LeetCode profile", LEETCODE_PROFILE)

# ---------------------------------------------------------------------------
# 9. PROJECTS
# ---------------------------------------------------------------------------
st.header("Projects", anchor="projects")
all_tools = sorted({tool for p in PROJECTS for tool in p["tools"]})
tool_filter = st.selectbox("Filter by tool", ["All"] + all_tools)
shown = [(i, p) for i, p in enumerate(PROJECTS) if tool_filter == "All" or tool_filter in p["tools"]]

cols = st.columns(3, gap="medium")
for col, (i, p) in zip(cols, shown):
    with col:
        with st.container(key=f"card_{i}"):
            st.subheader(p["title"])
            st.caption(f"Role: {p['role']}")
            st.write(p["outcome"])
            st.caption("Tools: " + ", ".join(p["tools"]))
            a, b = st.columns(2)
            if a.button("Details", key=f"details_{i}"):
                st.session_state.selected = i
            b.link_button("View", p["link"])

selected = st.session_state.selected
if show_details and selected is not None:
    p = PROJECTS[selected]
    st.write("")
    with st.container(key="detail_panel"):
        st.subheader(p["title"])
        st.write(p["details"])
        if st.button("Close", key="close_details"):
            st.session_state.selected = None
            st.rerun()

# ---------------------------------------------------------------------------
# 10. CONTACT
# ---------------------------------------------------------------------------
st.header("Contact", anchor="contact")
art("images/contact.jpg")
form_col, info_col = st.columns([3, 2], gap="large")

with form_col:
    with st.form("contact_form"):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        topic = st.selectbox("Topic", ["Feedback on the site", "Project collaboration", "Just saying hi"])
        message = st.text_area("Message", height=140)
        sent = st.form_submit_button("Send message")

    if sent:
        if not name.strip() or "@" not in email or len(message.strip()) < 10:
            st.error("Add your name, a valid email, and a message of at least 10 characters.")
        else:
            st.session_state.inbox.append({"name": name, "topic": topic})
            st.success(f"Thanks, {name}. Your message about “{topic.lower()}” was received.")
            st.toast("Message sent")
    st.caption("This form confirms on the page only. Nothing is emailed.")

with info_col:
    st.subheader("Elsewhere")
    st.write(f"Email: {EMAIL}")
    st.write(f"[GitHub]({GITHUB})  \n[LeetCode]({LEETCODE_PROFILE})")
    if st.session_state.inbox:
        st.caption(f"Messages sent in this session: {len(st.session_state.inbox)}")

st.divider()
st.caption(f"{NAME}, {SECTION}")