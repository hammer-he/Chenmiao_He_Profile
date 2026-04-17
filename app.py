import streamlit as st
from io import BytesIO

try:
    import qrcode
    from PIL import Image
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False

st.set_page_config(
    page_title="何晨苗 | He Chenmiao",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ══════════════════════════════════════════════════════════════
#  BILINGUAL CONTENT — 中文版全中文 / English version all English
# ══════════════════════════════════════════════════════════════
TEXTS = {
    "zh": {
        "name":        "何晨苗",
        "tagline":     "运动技能的发展与分析，女性体育教师的发展，拳击专项体能训练",
        "institution": "北京体育大学硕士 / 春田学院访问学者",
        "qr_label":    "扫码访问",
        "lang_zh":     "中文",
        "lang_en":     "English",

        "sec_about":   "简介",
        "about": (
            "专注于运动表现量化分析与循证研究。"
            "研究方向包括拳击技术动作自动化评估、运动干预与行为健康。"
            "国家二级拳击运动员，拥有国内外多项专业执照，"
            "将科研服务于体育实践。"
        ),

        "sec_edu": "教育背景",
        "edu": [
            {
                "org":    "北京体育大学",
                "badge":  "硕士研究生",
                "gold":   False,
                "period": "2023 — 2026",
                "role":   "体育教育训练学",
                "desc":   "运动生理学原理 · 运动训练学原理 · 体育教学论 · 体育科研方法",
            },
            {
                "org":    "春田学院",
                "badge":  "访问学者",
                "gold":   True,
                "period": "2025 — 2026",
                "role":   "体育教育训练学",
                "desc":   "运动科学数据分析 · 高级统计学 · 循证实践 · 运动技能发展与评估",
            },
            {
                "org":    "湖南师范大学树达学院",
                "badge":  "学士学位",
                "gold":   False,
                "period": "2019 — 2023",
                "role":   "社会体育指导与管理",
                "desc":   "体育管理学 · 篮球 · 足球 · 羽毛球 · 体育舞蹈 · 空手道",
            },
        ],

        "sec_exp": "实践经验",
        "exp": [
            {
                "org":    "中国拳击协会",
                "period": "2025.5 — 2025.8",
                "role":   "",
                "desc":   "负责全国拳击比赛及教练员培训的组织与管理，负责国家队外事接待工作",
            },
            {
                "org":    "春田市拳击队",
                "period": "2025.9 — 2026.5",
                "role":   "",
                "desc":   "负责队员体能监测与数据分析，参与正式比赛裁判工作",
            },
            {
                "org":    "北京体育大学附属竞技体育学院拳击队",
                "period": "2023.9 — 2025.5",
                "role":   "",
                "desc":   "负责拳击队训练的组织与管理，参与技术分析与体育课程设计",
            },
        ],

        "sec_research": "科研成果",
        "research_focus_label": "研究方向",
        "research_focus": "拳击技术动作自动化评估 · 新入职体育教师专业发展支持",
        "research_conf_label": "国际会议报告",
        "research_conf": [
            "SHAPE America National Convention",
            "ICSPAH 年会 — 拳击技术动作发展序列构建",
            "哈佛国际教育论坛 — 新入职女性体育教师的职业困境",
        ],

        "sec_honours": "运动经历与奖项",
        "honours": [
            "全国大学生拳击竞标赛冠军",
            "北京体育大学拳击比赛冠军",
            "哈巴罗夫斯克国际拳击邀请赛道德风尚奖",
            "湖南省永州市拳击比赛冠军",
            "湖南省长沙市棒垒球冠军",
            "美国大学生英式橄榄球联赛",
        ],

        "sec_certs": "资质证书",
        "certs_dark": [
            "国家二级拳击运动员证",
            "国家二级拳击裁判员证",
            "国家二级羽毛球裁判证",
            "国家三级武术套路裁判员证",
            "国家跳绳社会指导员证",
            "体育教师资格证",
            "美国拳击协会拳击官员执照",
            "NSCA-TSAC-F",
            "AHA CPR/AED",
            "数据分析师资格证",
        ],
        "certs_light": [
            "托福 iBT 93",
            "中文 — 母语",
        ],

        "contact_email_label": "邮箱",
        "contact_phone_label": "电话",
    },

    "en": {
        "name":        "He Chenmiao (Meow)",
        "tagline":     "Sport Science Researcher · Sports Performance Analysis · Boxing",
        "institution": "Beijing Sport University / Springfield College Visiting Scholar",
        "location":    "Beijing, China · Springfield, MA, USA",
        "qr_label":    "Scan to visit",
        "lang_zh":     "中文",
        "lang_en":     "English",

        "sec_about": "About",
        "about": (
            "Sport science researcher focused on quantitative performance analysis "
            "and evidence-based practice. Research spans automated assessment of boxing "
            "technique, exercise-behavioral health intervention, and physical education policy. "
            "National Level-2 Boxing Athlete holding multiple domestic and international "
            "professional licenses, committed to integrating rigorous research methods "
            "with competitive sport practice."
        ),

        "sec_edu": "Education",
        "edu": [
            {
                "org":    "Beijing Sport University",
                "badge":  "Master's",
                "gold":   False,
                "period": "2023 — 2026",
                "role":   "Sport Education & Training",
                "desc":   "Exercise Physiology · Sport Training Theory · PE Pedagogy · Research Methods in Sport Science",
            },
            {
                "org":    "Springfield College",
                "badge":  "Visiting Scholar",
                "gold":   True,
                "period": "2025 — 2026",
                "role":   "Sport Education & Training",
                "desc":   "Data Analytics in Sport Science · Advanced Statistics · Evidence-Based Practice · Motor Skill Development & Assessment",
            },
            {
                "org":    "Hunan Normal University Shuda College",
                "badge":  "Bachelor's",
                "gold":   False,
                "period": "2019 — 2023",
                "role":   "Social Sport Instruction & Management",
                "desc":   "Sport Management · Basketball · Football · Badminton · Sport Dance · Karate",
            },
        ],

        "sec_exp": "Experience",
        "exp": [
            {
                "org":    "China Boxing Association",
                "badge":  "Intern",
                "gold":   False,
                "period": "May 2025 — Aug 2025",
                "role":   "",
                "desc":   "Organised national boxing competitions and coaching certification programmes; coordinated international affairs and delegation reception for the national team",
            },
            {
                "org":    "Springfield Boxing Team",
                "badge":  "Assistant Coach",
                "gold":   True,
                "period": "Sep 2025 — May 2026",
                "role":   "",
                "desc":   "Conducted athlete fitness monitoring and performance data analysis; served as a certified official in formal competitive bouts",
            },
            {
                "org":    "BSU Affiliated School of Competitive Sports · Boxing Team",
                "badge":  "Assistant Coach",
                "gold":   False,
                "period": "Sep 2023 — May 2025",
                "role":   "",
                "desc":   "Managed daily organisation and training of the boxing squad; contributed to technical analysis and sport curriculum design",
            },
        ],

        "sec_research": "Research",
        "research_focus_label": "Research Focus",
        "research_focus": "Automated assessment of boxing technical movements · Professional support for newly employed PE teachers",
        "research_conf_label": "Conference Presentations",
        "research_conf": [
            "SHAPE America National Convention",
            "ICSPAH Annual Conference — Boxing Technical Movement Development Sequence",
            "Harvard International Education Forum — Dilemmas of Newly Employed Female PE Teachers",
        ],
        "research_ongoing_label": "Ongoing Projects",
        "research_ongoing": [
            "Meta-Analysis: Effect of exercise on electronic device addiction (team project, in progress)",
            "Systematic Review: Title in development (independent, protocol stage)",
        ],

        "sec_honours": "Honours & Awards",
        "honours": [
            "Champion · National Collegiate Boxing Championship",
            "Champion · BSU Boxing Competition",
            "Champion · Yongzhou City Basketball Competition",
            "John's Scholarship · Springfield College",
            "Second-Class Scholarship · Beijing Sport University",
        ],

        "sec_certs": "Certifications",
        "certs_dark": [
            "National L2 Boxing Athlete Certificate",
            "National L2 Boxing Referee Certificate",
            "National L2 Badminton Referee Certificate",
            "National L3 Wushu Routines Referee Certificate",
            "National Jump Rope Instructor Certificate",
            "PE Teacher Qualification Certificate",
            "Massachusetts PE Teacher License",
            "USA Boxing Officials License",
            "NSCA TSAC-F",
            "AHA CPR / AED",
            "Data Analyst Qualification Certificate",
        ],
        "certs_light": [
            "TOEFL iBT 93",
            "English — Professional",
            "Chinese — Native",
        ],

        "contact_email_label": "Email",
        "contact_phone_label": "Phone",
    },
}

# ══════════════════════════════════════════════════════════════
#  CSS — Jarocki style: pure white + dark gray + IBM Plex Mono
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #ffffff;
}
.main { background-color: #ffffff; }
.main .block-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2.5rem 3rem 3rem;
    background: #ffffff;
}

/* hide default streamlit chrome */
[data-testid="stSidebar"] { display: none; }
header[data-testid="stHeader"] { background: transparent; }
footer { display: none; }

/* ── Header ── */
.cv-name {
    font-size: 2rem;
    font-weight: 700;
    color: #111111;
    letter-spacing: -0.02em;
    margin: 0 0 0.35rem;
    line-height: 1.1;
}
.cv-tagline {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    color: #444444;
    line-height: 1.6;
    margin: 0 0 0.35rem;
}
.cv-location {
    font-size: 0.78rem;
    color: #888888;
    margin-bottom: 0.8rem;
}
.cv-icon-row {
    display: flex;
    gap: 7px;
    flex-wrap: wrap;
    margin-bottom: 0;
}
.cv-icon-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    border: 1px solid #dddddd;
    border-radius: 4px;
    padding: 3px 10px;
    font-size: 0.75rem;
    color: #444444;
    font-family: 'IBM Plex Mono', monospace;
    text-decoration: none;
    background: #ffffff;
}

/* ── Lang toggle ── */
.lang-row {
    display: flex;
    gap: 6px;
    margin: 1.4rem 0 1.8rem;
}
.lang-btn {
    font-size: 0.78rem;
    font-family: 'IBM Plex Mono', monospace;
    padding: 4px 14px;
    border: 1px solid #dddddd;
    border-radius: 3px;
    color: #888888;
    background: #ffffff;
    cursor: pointer;
}
.lang-btn.active {
    background: #111111;
    color: #ffffff;
    border-color: #111111;
}

/* ── Section ── */
.sec-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #111111;
    letter-spacing: -0.01em;
    margin: 0 0 0.75rem;
    padding-bottom: 0.45rem;
    border-bottom: 1px solid #f0f0f0;
}

/* ── About ── */
.about-body {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    color: #444444;
    line-height: 1.75;
}

/* ── Entry (edu / exp) ── */
.entry-wrap {
    margin-bottom: 1.1rem;
}
.entry-top-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 8px;
    margin-bottom: 0.15rem;
}
.entry-org {
    font-size: 0.92rem;
    font-weight: 700;
    color: #111111;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}
.entry-badge {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    font-weight: 400;
    color: #555555;
    background: #f0f0f0;
    border: 1px solid #e0e0e0;
    border-radius: 3px;
    padding: 1px 8px;
}
.entry-badge.gold {
    background: #fef9ee;
    border-color: #e8d090;
    color: #7a5808;
}
.entry-period {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: #888888;
    white-space: nowrap;
    flex-shrink: 0;
}
.entry-role {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: #333333;
    margin-bottom: 0.2rem;
}
.entry-desc {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.77rem;
    color: #666666;
    line-height: 1.65;
}

/* ── Research ── */
.research-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    font-weight: 500;
    color: #888888;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin: 0.8rem 0 0.3rem;
}
.research-focus {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    color: #333333;
    line-height: 1.6;
}
.research-item {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: #555555;
    line-height: 1.7;
    padding-left: 1rem;
    position: relative;
}
.research-item::before {
    content: "—";
    position: absolute;
    left: 0;
    color: #aaaaaa;
}

/* ── Honours ── */
.honour-item {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: #444444;
    line-height: 1.7;
    padding-left: 1rem;
    position: relative;
}
.honour-item::before {
    content: "—";
    position: absolute;
    left: 0;
    color: #aaaaaa;
}

/* ── Cert chips ── */
.chips-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}
.chip-dark {
    background: #111111;
    color: #ffffff;
    border-radius: 4px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    padding: 4px 11px;
}
.chip-light {
    background: #f5f5f5;
    color: #333333;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    padding: 4px 11px;
}

/* ── Divider ── */
.cv-divider {
    border: none;
    border-top: 1px solid #f0f0f0;
    margin: 1.6rem 0;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  LANGUAGE STATE
# ══════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "zh"

# ══════════════════════════════════════════════════════════════
#  QR CODE GENERATOR
# ══════════════════════════════════════════════════════════════
YOUR_URL = " https://chenmiaoheprofile-keephungry.streamlit.app"  # ← 替换成你的实际网址

@st.cache_data
def make_qr(url: str):
    if not QR_AVAILABLE:
        return None
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=6,
            border=2,
        )
        qr.add_data(url)
        qr.make(fit=True)
        return qr.make_image(fill_color="#111111", back_color="#ffffff").convert("RGB")
    except Exception:
        return None

# ══════════════════════════════════════════════════════════════
#  RENDER HELPERS
# ══════════════════════════════════════════════════════════════
def entry_html(item: dict) -> str:
    badge_class = "entry-badge gold" if item.get("gold") else "entry-badge"
    role_html = f'<div class="entry-role">{item["role"]}</div>' if item.get("role") else ""
    return f"""
    <div class="entry-wrap">
        <div class="entry-top-row">
            <div class="entry-org">
                {item["org"]}
                <span class="{badge_class}">{item["badge"]}</span>
            </div>
            <div class="entry-period">{item["period"]}</div>
        </div>
        {role_html}
        <div class="entry-desc">{item["desc"]}</div>
    </div>
    """

def chips_html(dark: list, light: list) -> str:
    d = "".join(f'<span class="chip-dark">{c}</span>' for c in dark)
    l = "".join(f'<span class="chip-light">{c}</span>' for c in light)
    return f'<div class="chips-wrap">{d}{l}</div>'

def research_items(items: list) -> str:
    return "".join(f'<div class="research-item">{i}</div>' for i in items)

def honour_items(items: list) -> str:
    return "".join(f'<div class="honour-item">{i}</div>' for i in items)

# ══════════════════════════════════════════════════════════════
#  MAIN LAYOUT
# ══════════════════════════════════════════════════════════════
T = TEXTS[st.session_state.lang]

# ── Header: name/tagline left  |  photo + QR right ──────────
col_left, col_right = st.columns([3, 1], gap="large")

with col_left:
    st.markdown(f"""
    <div class="cv-name">{T["name"]}</div>
    <div class="cv-tagline">{T["tagline"]}<br>{T["institution"]}</div>
    <div class="cv-icon-row">
        <a class="cv-icon-chip" href="mailto:chenmiaohe7@gmail.com">✉ chenmiaohe7@gmail.com</a>
        <a class="cv-icon-chip" href="mailto:602471974@qq.com">✉ 602471974@qq.com</a>
        <span class="cv-icon-chip">📱 +86 158-9747-2620</span>
        <span class="cv-icon-chip">📱 +1 (413) 272-5040</span>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    # Photo
    try:
        st.image("012.psd", use_container_width=True)
    except Exception:
        st.markdown(
            "<div style='width:100%;aspect-ratio:1;background:#f0f0f0;"
            "border:1px solid #ddd;border-radius:8px;display:flex;"
            "align-items:center;justify-content:center;font-size:1.4rem;"
            "color:#aaa;'>何</div>",
            unsafe_allow_html=True
        )
    # QR code
    qr_img = make_qr(YOUR_URL)
    if qr_img is not None:
        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        buf.seek(0)
        st.image(buf, use_container_width=True)
        st.markdown(
            f"<div style='text-align:center;font-family:IBM Plex Mono,monospace;"
            f"font-size:0.65rem;color:#999;margin-top:-6px;'>{T['qr_label']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align:center;font-size:0.65rem;color:#999;"
            f"font-family:IBM Plex Mono,monospace;padding:6px 0;'>"
            f"<a href='{YOUR_URL}' style='color:#999;'>{T['qr_label']}</a></div>",
            unsafe_allow_html=True
        )

# ── Language toggle (functional buttons styled as Jarocki toggle) ──
st.markdown("""
<style>
/* target the two lang toggle buttons specifically */
div[data-testid="stHorizontalBlock"]:has(button[kind="secondary"]) button[kind="secondary"] {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.78rem !important;
    border: 1px solid #dddddd !important;
    border-radius: 3px !important;
    color: #888888 !important;
    background: #ffffff !important;
    padding: 4px 14px !important;
    height: auto !important;
    min-height: unset !important;
}
</style>
""", unsafe_allow_html=True)

col_zh, col_en, _ = st.columns([1, 1, 8])
with col_zh:
    zh_style = "background:#111;color:#fff;border:1px solid #111;" if st.session_state.lang == "zh" else ""
    if st.button(T["lang_zh"], key="btn_zh", use_container_width=True):
        st.session_state.lang = "zh"
        st.rerun()
with col_en:
    if st.button(T["lang_en"], key="btn_en", use_container_width=True):
        st.session_state.lang = "en"
        st.rerun()

# Re-resolve T after possible lang change
T = TEXTS[st.session_state.lang]

st.markdown("<hr class='cv-divider'>", unsafe_allow_html=True)

# ── About ────────────────────────────────────────────────────
st.markdown(f'<div class="sec-title">{T["sec_about"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="about-body">{T["about"]}</div>', unsafe_allow_html=True)

st.markdown("<hr class='cv-divider'>", unsafe_allow_html=True)

# ── Education ────────────────────────────────────────────────
st.markdown(f'<div class="sec-title">{T["sec_edu"]}</div>', unsafe_allow_html=True)
for item in T["edu"]:
    st.markdown(entry_html(item), unsafe_allow_html=True)

st.markdown("<hr class='cv-divider'>", unsafe_allow_html=True)

# ── Experience ───────────────────────────────────────────────
st.markdown(f'<div class="sec-title">{T["sec_exp"]}</div>', unsafe_allow_html=True)
for item in T["exp"]:
    st.markdown(entry_html(item), unsafe_allow_html=True)

st.markdown("<hr class='cv-divider'>", unsafe_allow_html=True)

# ── Research ─────────────────────────────────────────────────
st.markdown(f'<div class="sec-title">{T["sec_research"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="research-label">{T["research_focus_label"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="research-focus">{T["research_focus"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="research-label">{T["research_conf_label"]}</div>', unsafe_allow_html=True)
st.markdown(research_items(T["research_conf"]), unsafe_allow_html=True)
st.markdown(f'<div class="research-label">{T["research_ongoing_label"]}</div>', unsafe_allow_html=True)
st.markdown(research_items(T["research_ongoing"]), unsafe_allow_html=True)

st.markdown("<hr class='cv-divider'>", unsafe_allow_html=True)

# ── Honours ──────────────────────────────────────────────────
st.markdown(f'<div class="sec-title">{T["sec_honours"]}</div>', unsafe_allow_html=True)
st.markdown(honour_items(T["honours"]), unsafe_allow_html=True)

st.markdown("<hr class='cv-divider'>", unsafe_allow_html=True)

# ── Certifications ───────────────────────────────────────────
st.markdown(f'<div class="sec-title">{T["sec_certs"]}</div>', unsafe_allow_html=True)
st.markdown(chips_html(T["certs_dark"], T["certs_light"]), unsafe_allow_html=True)
