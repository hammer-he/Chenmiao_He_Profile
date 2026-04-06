import streamlit as st

# 1. 页面配置
st.set_page_config(
    page_title="何晨苗 (Meow)", 
    page_icon="🥊", 
    layout="wide"
)

# 自定义 CSS 样式
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%; border-radius: 5px; height: 3em;
        background-color: #800000; color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 侧边栏
with st.sidebar:
    # 💡 提示：请确保你的 GitHub 仓库里有一个 012.jpg 文件（PSD格式网页打不开哦）
    st.image("012.psd", caption="何晨苗 (Meow)") 
    st.subheader("📍 联系方式")
    st.markdown("📧 **Email**")
    st.caption("chenmiaohe7@gmail.com")
    st.caption("602471974@qq.com")
    st.markdown("📱 **Phone**")
    st.caption("🇨🇳 +86 15897472620")
    st.caption("🇺🇸 +1 4132725040")

# 3. 主界面
col1, col2 = st.columns([2, 1], gap="large")

with col1: # ✅ 修正：不再缩进
    st.title("您好，我是何晨苗 (Meow) 👋") # ✅ 修正：内部任务需要缩进
    st.markdown("**Focus:** `拳击` `运动表现分析` `循证运动实践` `体育教育`")

with col2:
    st.write("### 📈 个人成长图谱")
    st.write("北京体育大学硕士毕业")
    st.progress(80)
    st.write("申请清华大学体育博士")
    st.progress(30)
    st.write("拳击世界冠军")
    st.progress(20)

st.markdown("---")

# 4. 详细信息
tab1, tab2, tab3, tab4 = st.tabs(["🎓 教育背景", "💼 实践经验", "🔬 科研成果", "🏅 荣誉与技能"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🇨🇳 北京体育大学")
        st.caption("Beijing Sport University")
        st.write("**体育教育训练学 | 硕士研究生**")
        st.markdown("- **核心领域：** 运动生理学、运动训练学、体育教学论、科研方法论")
    with c2:
        st.markdown("### 🇺🇸 Springfield College")
        st.caption("春田学院 (Springfield, MA)")
        st.write("**体育教育训练学 | 访问学者**")
        st.markdown("- **核心领域：** 循证实践 (EBP)、运动技能分析、高级统计学、体育大数据")

with tab2:
    with st.container(border=True):
        p1, p2, p3 = st.columns(3)
        with p1:
            st.markdown("#### 🏗️ 中国拳击协会")
            st.caption("实习生")
            st.write("- 组织协调全国拳击赛事\n- 负责国家队外事接待")
        with p2:
            st.markdown("#### 🏫 春田市拳击队")
            st.caption("助理教练 | 美国春田")
            st.write("- 负责体能监测与数据分析\n- 参与正式比赛裁判工作")
        with p3:
            st.markdown("#### 🥊 拳击俱乐部")
            st.caption("主教练 | 课程研发")
            st.write("- 设计模块化拳击课程\n- 提供高强度私教指导")

with tab3:
    st.markdown("### 🔬 学术发表与会议报告")
    st.info("**核心研究方向：** 拳击技术动作自动化评估，新入职体育教师支持")
    with st.expander("📍 国际会议报告", expanded=True):
        st.markdown("""
        1. **SHAPE America National Convention**
        2. **ICSPAH 年会** - *主题：拳击技术动作发展序列构建*
        3. **哈佛国际教育论坛** - *主题：新入职女性体育教师的困境*
        """)

with tab4:
    h_col, s_col = st.columns([1.5, 1])
    with h_col:
        st.markdown("### 🏆 荣誉奖项")
        with st.expander("🎓 学术奖项", expanded=True):
            st.markdown("- **John's Scholarship** | 春田学院\n- **二等奖学金** | 北京体育大学")
        with st.expander("🥊 竞技体育荣誉", expanded=True):
            st.success("🥇 **全国大学生拳击锦标赛 - 冠军**")
            st.write("- 冠军 | 北体大拳击比赛\n- 冠军 | 永州市篮球比赛")
    with s_col:
        st.markdown("### 🛠️ 专业技能")
        st.write("**语言能力**")
        st.metric(label="TOEFL iBT", value="93") # ✅ 修正了引号
        st.divider()
        st.write("**数据科学**")
        st.markdown("- 🐍 **Python** (网页制作)\n- 📊 **R 语言** (数据分析)")

# 5. 底部互动
st.markdown("---")
st.header("📮 留言与交流")
with st.form("contact"):
    user_name = st.text_input("您的姓名")
    user_msg = st.text_area("您想对我说的话")
    if st.form_submit_button("发送信息"):
        st.balloons()
        st.success(f"收到！谢谢你，{user_name}。我会尽快与您联系。")
