import streamlit as st
import os

st.set_page_config(
    page_title="何晨苗 | He Chenmiao",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ══════════════════════════════════════════════════════════════
#  BILINGUAL CONTENT DICTIONARY
#  PMS 202 · #862633 · RGB(134, 38, 51)
# ══════════════════════════════════════════════════════════════
TEXTS = {
    "zh": {
        # ── Sidebar ──
        "lang_options": ["中文", "English"],
        "lang_label":   "语言 / Language",
        "sidebar_name": "何晨苗 (Meow)",
        "contact_title": "联系方式",
        "email_label":  "📧 邮箱",
        "phone_label":  "📱 电话",

        # ── Hero ──
        "hero_title":   "您好，我是何晨苗 (Meow) 👋",
        "hero_focus":   "**研究方向：** `拳击` `运动表现分析` `循证运动实践` `体育教育`",

        # ── Tabs ──
        "tab_edu":      "🎓 教育背景",
        "tab_exp":      "💼 实践经验",
        "tab_res":      "🔬 科研成果",
        "tab_hon":      "🏅 荣誉与技能",

        # ── Education ──
        "edu_title":    "教育背景",
        "edu": [
            {
                "school":   "北京体育大学",
                "sub":      "Beijing Sport University",
                "period":   "2023.9 — 2026.6",
                "degree":   "体育教育训练学 · 硕士研究生",
                "courses_label": "核心课程",
                "courses":  "运动生理学原理 · 运动训练学原理 · 体育教学论 · 体育科研方法",
            },
            {
                "school":   "春田学院",
                "sub":      "Springfield College · Springfield, MA",
                "period":   "2025.8 — 2026.5",
                "degree":   "体育教育训练学 · 访问学者",
                "courses_label": "核心课程",
                "courses":  "运动科学的数据分析 · 高级统计学 · 循证实践 · 运动技能的发展与评估",
            },
            {
                "school":   "湖南师范大学树达学院",
                "sub":      "Hunan Normal University Shuda College",
                "period":   "2019.9 — 2023.6",
                "degree":   "社会体育指导与管理 · 学士学位",
                "courses_label": "核心课程",
                "courses":  "体育管理学 · 篮球 · 足球 · 羽毛球 · 体育舞蹈 · 空手道",
            },
        ],

        # ── Experience ──
        "exp_title":    "实践经验",
        "exp": [
            {
                "org":      "中国拳击协会",
                "sub":      "China Boxing Association",
                "period":   "2025.5 — 2025.8",
                "role":     "实习生",
                "duties": [
                    "负责全国拳击比赛及教练员培训的组织与管理",
                    "负责国家队外事接待工作",
                ],
            },
            {
                "org":      "春田市拳击队",
                "sub":      "Springfield Boxing Team · Springfield, MA",
                "period":   "2025.9 — 2026.5",
                "role":     "助理教练",
                "duties": [
                    "负责队员体能监测与数据分析",
                    "参与正式比赛裁判工作",
                ],
            },
            {
                "org":      "北京体育大学附属竞技体育学院拳击队",
                "sub":      "BSU Affiliated School of Competitive Sports · Boxing Team",
                "period":   "2023.9 — 2025.5",
                "role":     "助理教练",
                "duties": [
                    "负责拳击队训练的组织与管理",
                    "参与技术分析与体育课程设计",
                ],
            },
        ],

        # ── Research ──
        "res_title":        "科研成果",
        "res_focus_label":  "研究方向",
        "res_focus_body":   "拳击技术动作自动化评估 · 新入职体育教师专业发展支持",
        "conf_label":       "国际会议报告",
        "conferences": [
            "**SHAPE America National Convention**",
            "**ICSPAH 年会** — 主题：拳击技术动作发展序列构建",
            "**哈佛国际教育论坛** — 主题：新入职女性体育教师的职业困境",
        ],
        "ongoing_label":    "进行中的研究项目",
        "ongoing": [
            "**Meta分析**：运动锻炼对电子产品成瘾的干预效果（团队协作，进行中）",
            "**系统综述**：题目待定（独立项目，方案设计阶段）",
        ],

        # ── Honours & Skills ──
        "hon_title":        "荣誉与技能",
        "awards_label":     "学术奖项",
        "awards": [
            "John's Scholarship · 春田学院",
            "二等奖学金 · 北京体育大学",
        ],
        "sports_label":     "竞技体育荣誉",
        "sports": [
            "冠军 · 全国大学生拳击锦标赛",
            "冠军 · 北体大拳击比赛",
            "冠军 · 永州市篮球比赛",
        ],
        "lang_skill_label": "语言能力",
        "lang_skills": [
            "中文 — 母语",
            "英语 — TOEFL iBT 93",
        ],
        "certs_label":      "职业资格证书",
        "certs_sport": [
            "国家二级拳击运动员证",
            "国家二级拳击裁判员证",
            "国家二级羽毛球裁判证",
            "国家三级武术套路裁判员证",
            "国家跳绳社会指导员证",
            "体育教师资格证",
        ],
        "certs_intl": [
            "美国马萨诸塞州体育教师执照",
            "美国拳击协会拳击官员执照",
            "美国体能协会军事体能资格证 (NSCA-TSAC-F)",
            "美国心脏协会心肺复苏与体外除颤急救证书 (AHA CPR/AED)",
            "数据分析师资格证",
        ],
        "data_label":       "数据科学",
        "data_skills": [
            "🐍 Python — 数据处理 / 网页开发",
            "📊 R 语言 — 统计分析 / Meta分析",
            "📈 Streamlit — 数据可视化仪表盘",
        ],
        "certs_cn_title":   "国内证书",
        "certs_intl_title": "国际证书",
    },

    "en": {
        # ── Sidebar ──
        "lang_options": ["中文", "English"],
        "lang_label":   "语言 / Language",
        "sidebar_name": "He Chenmiao (Meow)",
        "contact_title": "Contact",
        "email_label":  "📧 Email",
        "phone_label":  "📱 Phone",

        # ── Hero ──
        "hero_title":   "Hi, I'm He Chenmiao (Meow) 👋",
        "hero_focus":   "**Research Focus:** `Boxing` `Sports Performance Analysis` `Evidence-Based Practice` `Physical Education`",

        # ── Tabs ──
        "tab_edu":      "🎓 Education",
        "tab_exp":      "💼 Experience",
        "tab_res":      "🔬 Research",
        "tab_hon":      "🏅 Honours & Skills",

        # ── Education ──
        "edu_title":    "Education",
        "edu": [
            {
                "school":   "Beijing Sport University",
                "sub":      "北京体育大学",
                "period":   "Sep 2023 — Jun 2026",
                "degree":   "Sport Education & Training · Master's Degree",
                "courses_label": "Core Courses",
                "courses":  "Exercise Physiology · Sport Training Theory · PE Pedagogy · Research Methods in Sport Science",
            },
            {
                "school":   "Springfield College",
                "sub":      "春田学院 · Springfield, MA",
                "period":   "Aug 2025 — May 2026",
                "degree":   "Sport Education & Training · Visiting Scholar",
                "courses_label": "Core Courses",
                "courses":  "Data Analytics in Sport Science · Advanced Statistics · Evidence-Based Practice · Motor Skill Development & Assessment",
            },
            {
                "school":   "Hunan Normal University Shuda College",
                "sub":      "湖南师范大学树达学院",
                "period":   "Sep 2019 — Jun 2023",
                "degree":   "Social Sport Instruction & Management · Bachelor's Degree",
                "courses_label": "Core Courses",
                "courses":  "Sport Management · Basketball · Football · Badminton · Sport Dance · Karate",
            },
        ],

        # ── Experience ──
        "exp_title":    "Professional Experience",
        "exp": [
            {
                "org":      "China Boxing Association",
                "sub":      "中国拳击协会",
                "period":   "May 2025 — Aug 2025",
                "role":     "Intern",
                "duties": [
                    "Organised and managed national boxing competitions and coaching certification programmes",
                    "Coordinated international affairs and delegation reception for the national team",
                ],
            },
            {
                "org":      "Springfield Boxing Team",
                "sub":      "春田市拳击队 · Springfield, MA",
                "period":   "Sep 2025 — May 2026",
                "role":     "Assistant Coach",
                "duties": [
                    "Conducted athlete fitness monitoring and performance data analysis",
                    "Served as a certified official in formal competitive bouts",
                ],
            },
            {
                "org":      "BSU Affiliated School of Competitive Sports · Boxing Team",
                "sub":      "北京体育大学附属竞技体育学院拳击队",
                "period":   "Sep 2023 — May 2025",
                "role":     "Assistant Coach",
                "duties": [
                    "Managed the daily organisation and training of the boxing squad",
                    "Contributed to technical analysis and sport curriculum design",
                ],
            },
        ],

        # ── Research ──
        "res_title":        "Research",
        "res_focus_label":  "Research Focus",
        "res_focus_body":   "Automated assessment of boxing technical movements · Professional support for newly employed PE teachers",
        "conf_label":       "Conference Presentations",
        "conferences": [
            "**SHAPE America National Convention**",
            "**ICSPAH Annual Conference** — Boxing Technical Movement Development Sequence",
            "**Harvard International Education Forum** — Dilemmas of Newly Employed Female PE Teachers",
        ],
        "ongoing_label":    "Ongoing Projects",
        "ongoing": [
            "**Meta-Analysis**: Effect of exercise interventions on electronic device addiction (team project, in progress)",
            "**Systematic Review**: Title in development (independent, protocol stage)",
        ],

        # ── Honours & Skills ──
        "hon_title":        "Honours & Skills",
        "awards_label":     "Academic Awards",
        "awards": [
            "John's Scholarship · Springfield College",
            "Second-Class Scholarship · Beijing Sport University",
        ],
        "sports_label":     "Athletic Honours",
        "sports": [
            "Champion · National Collegiate Boxing Championship",
            "Champion · BSU Boxing Competition",
            "Champion · Yongzhou City Basketball Competition",
        ],
        "lang_skill_label": "Language Proficiency",
        "lang_skills": [
            "Chinese — Native",
            "English — TOEFL iBT 93",
        ],
        "certs_label":      "Professional Certifications",
        "certs_sport": [
            "National Level-2 Boxing Athlete Certificate",
            "National Level-2 Boxing Referee Certificate",
            "National Level-2 Badminton Referee Certificate",
            "National Level-3 Wushu Routines Referee Certificate",
            "National Jump Rope Community Instructor Certificate",
            "Physical Education Teacher Qualification Certificate",
        ],
        "certs_intl": [
            "Massachusetts (USA) Physical Education Teacher License",
            "USA Boxing Officials License",
            "NSCA Tactical Strength & Conditioning Facilitator (TSAC-F)",
            "AHA CPR & AED Certificate",
            "Data Analyst Qualification Certificate",
        ],
        "data_label":       "Data Science",
        "data_skills": [
            "🐍 Python — Data processing / Web development",
            "📊 R — Statistical analysis / Meta-analysis",
            "📈 Streamlit — Data visualisation dashboards",
        ],
        "certs_cn_title":   "Chinese Certificates",
        "certs_intl_title": "International Certificates",
    },
}

# ══════════════════════════════════════════════════════════════
#  GLOBAL CSS  —  PMS 202 · #862633
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.main { background-color: #fdf8f8; }

/* ── Sidebar ── */
[data-testid="stSidebar"] { background: #1c0508; }
[data-testid="stSidebar"] * { color: #f5e8ea !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 0.9rem; padding: 4px 0; }
[data-testid="stSidebar"] hr { border-color: #4a1520 !important; }

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #3d0d12 0%, #6a1e28 55%, #862633 100%);
    border-radius: 14px; padding: 2.2rem 2.6rem; margin-bottom: 1.8rem; color: white;
}
.hero h1 { font-family: 'Lora', serif; font-size: 2.1rem; font-weight: 600; color: white; margin: 0 0 0.5rem 0; }
.hero .focus { font-size: 0.92rem; color: #f5d8db; margin-top: 0.4rem; }

/* ── Section headings ── */
.sec-title {
    font-family: 'Lora', serif; font-size: 1.45rem; font-weight: 600;
    color: #1a0508; border-left: 4px solid #862633;
    padding-left: 12px; margin: 1.6rem 0 1.2rem 0;
}

/* ── Timeline card (edu + exp) ── */
.timeline-card {
    background: #fff; border: 1px solid #edd8da;
    border-left: 4px solid #862633;
    border-radius: 0 10px 10px 0;
    padding: 1.2rem 1.6rem; margin-bottom: 1.1rem;
    box-shadow: 0 2px 8px rgba(134,38,51,0.06);
}
.timeline-card .org { font-size: 1.08rem; font-weight: 700; color: #1a0508; margin: 0; }
.timeline-card .sub { font-size: 0.82rem; color: #8a6670; margin: 1px 0 4px 0; }
.timeline-card .period {
    display: inline-block; background: #fdf0f1; color: #862633;
    border: 1px solid #f0c8cb; border-radius: 20px;
    font-size: 0.76rem; font-weight: 600; padding: 2px 10px; margin-bottom: 6px;
}
.timeline-card .role { font-size: 0.88rem; font-weight: 600; color: #4a1520; margin-bottom: 6px; }
.timeline-card .detail { font-size: 0.88rem; color: #4a5568; line-height: 1.65; }
.timeline-card .course-label { font-size: 0.78rem; font-weight: 700; color: #862633; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 8px; margin-bottom: 3px; }

/* ── Info cards (research / honours) ── */
.info-card {
    background: #fff; border: 1px solid #edd8da; border-radius: 10px;
    padding: 1.2rem 1.5rem; margin-bottom: 1rem;
    box-shadow: 0 2px 6px rgba(134,38,51,0.05);
}
.info-card .label {
    font-size: 0.75rem; font-weight: 700; color: #862633;
    text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;
}
.info-card li { font-size: 0.9rem; color: #2d2d2d; line-height: 1.7; margin-bottom: 2px; }

/* ── Cert chip ── */
.cert-chip {
    display: inline-block; background: #fdf5f6;
    border: 1px solid #e8c5c8; border-radius: 6px;
    font-size: 0.82rem; color: #6a1e27;
    padding: 4px 12px; margin: 3px 4px 3px 0;
}

/* ── Divider ── */
.rdivider { border: none; border-top: 1px solid #f0d8da; margin: 1.2rem 0; }

/* Streamlit tab active color override */
button[data-baseweb="tab"][aria-selected="true"] {
    color: #862633 !important;
    border-bottom: 2px solid #862633 !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  LANGUAGE TOGGLE
# ══════════════════════════════════════════════════════════════
if "lang" not in st.session_state:
    st.session_state.lang = "zh"

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    lang_choice = st.radio(
        "语言 / Language",
        ["中文", "English"],
        index=0 if st.session_state.lang == "zh" else 1
    )
    st.session_state.lang = "zh" if lang_choice == "中文" else "en"
    T = TEXTS[st.session_state.lang]

    st.markdown("---")

    # Photo — graceful fallback if file missing
     st.image("012.psd", caption="何晨苗 (Meow)") 
        st.markdown(
            f"<div style='text-align:center;padding:1.2rem 0;font-size:3.5rem;'>🥊</div>"
            f"<div style='text-align:center;font-size:0.9rem;color:#f0d0d3;'>{T['sidebar_name']}</div>",
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.subheader(f"📍 {T['contact_title']}")
    st.markdown(T["email_label"])
    st.caption("chenmiaohe7@gmail.com")
    st.caption("602471974@qq.com")
    st.markdown(T["phone_label"])
    st.caption("🇨🇳 +86 158-9747-2620")
    st.caption("🇺🇸 +1 (413) 272-5040")

# ── Resolve T after sidebar (in case first render) ──────────
T = TEXTS[st.session_state.lang]

# ══════════════════════════════════════════════════════════════
#  HERO
# ══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="hero">
    <h1>{T["hero_title"]}</h1>
    <div class="focus">{T["hero_focus"]}</div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
#  TABS
# ══════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    T["tab_edu"], T["tab_exp"], T["tab_res"], T["tab_hon"]
])

# ── TAB 1: EDUCATION ─────────────────────────────────────────
with tab1:
    st.markdown(f'<div class="sec-title">{T["edu_title"]}</div>', unsafe_allow_html=True)
    for edu in T["edu"]:
        st.markdown(f"""
        <div class="timeline-card">
            <div class="org">{edu["school"]}</div>
            <div class="sub">{edu["sub"]}</div>
            <span class="period">🗓 {edu["period"]}</span>
            <div class="detail" style="margin-top:4px;">{edu["degree"]}</div>
            <div class="course-label">{edu["courses_label"]}</div>
            <div class="detail">{edu["courses"]}</div>
        </div>
        """, unsafe_allow_html=True)

# ── TAB 2: EXPERIENCE ────────────────────────────────────────
with tab2:
    st.markdown(f'<div class="sec-title">{T["exp_title"]}</div>', unsafe_allow_html=True)
    for exp in T["exp"]:
        duties_html = "".join(f"<li>{d}</li>" for d in exp["duties"])
        st.markdown(f"""
        <div class="timeline-card">
            <div class="org">{exp["org"]}</div>
            <div class="sub">{exp["sub"]}</div>
            <span class="period">🗓 {exp["period"]}</span>
            <div class="role">— {exp["role"]}</div>
            <ul class="detail" style="margin:4px 0 0 0; padding-left:1.2rem;">
                {duties_html}
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ── TAB 3: RESEARCH ──────────────────────────────────────────
with tab3:
    st.markdown(f'<div class="sec-title">{T["res_title"]}</div>', unsafe_allow_html=True)

    # Research focus
    st.markdown(f"""
    <div class="info-card">
        <div class="label">{T["res_focus_label"]}</div>
        <div style="font-size:0.92rem;color:#2d2d2d;line-height:1.7;">{T["res_focus_body"]}</div>
    </div>
    """, unsafe_allow_html=True)

    # Conferences
    conf_items = "".join(f"<li>{c}</li>" for c in T["conferences"])
    st.markdown(f"""
    <div class="info-card">
        <div class="label">{T["conf_label"]}</div>
        <ul>{conf_items}</ul>
    </div>
    """, unsafe_allow_html=True)

    # Ongoing
    ongoing_items = "".join(f"<li>{o}</li>" for o in T["ongoing"])
    st.markdown(f"""
    <div class="info-card">
        <div class="label">{T["ongoing_label"]}</div>
        <ul>{ongoing_items}</ul>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 4: HONOURS & SKILLS ──────────────────────────────────
with tab4:
    st.markdown(f'<div class="sec-title">{T["hon_title"]}</div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        # Academic awards
        awards_items = "".join(f"<li>{a}</li>" for a in T["awards"])
        st.markdown(f"""
        <div class="info-card">
            <div class="label">🎓 {T["awards_label"]}</div>
            <ul>{awards_items}</ul>
        </div>
        """, unsafe_allow_html=True)

        # Athletic honours
        sports_items = "".join(f"<li>{s}</li>" for s in T["sports"])
        st.markdown(f"""
        <div class="info-card">
            <div class="label">🏆 {T["sports_label"]}</div>
            <ul>{sports_items}</ul>
        </div>
        """, unsafe_allow_html=True)

        # Language skills
        lang_items = "".join(f"<li>{l}</li>" for l in T["lang_skills"])
        st.markdown(f"""
        <div class="info-card">
            <div class="label">🌐 {T["lang_skill_label"]}</div>
            <ul>{lang_items}</ul>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        # Chinese certs
        cn_chips = "".join(f'<span class="cert-chip">✅ {c}</span>' for c in T["certs_sport"])
        st.markdown(f"""
        <div class="info-card">
            <div class="label">📜 {T["certs_cn_title"]}</div>
            <div style="margin-top:4px;">{cn_chips}</div>
        </div>
        """, unsafe_allow_html=True)

        # International certs
        intl_chips = "".join(f'<span class="cert-chip">🌏 {c}</span>' for c in T["certs_intl"])
        st.markdown(f"""
        <div class="info-card">
            <div class="label">🌍 {T["certs_intl_title"]}</div>
            <div style="margin-top:4px;">{intl_chips}</div>
        </div>
        """, unsafe_allow_html=True)

        # Data science
        data_items = "".join(f"<li>{d}</li>" for d in T["data_skills"])
        st.markdown(f"""
        <div class="info-card">
            <div class="label">💻 {T["data_label"]}</div>
            <ul>{data_items}</ul>
        </div>
        """, unsafe_allow_html=True)
