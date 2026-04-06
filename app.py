import streamlit as st

# 1. 页面配置：增加了个性化标题和页面布局
st.set_page_config(
    page_title="何晨苗 (Meow)", 
    page_icon="🥊", 
    layout="wide"
)

# 自定义 CSS 样式（让界面更有设计感）
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #800000;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 侧边栏：头像与联系方式
with st.sidebar:
    st.image("https://via.placeholder.com/200x200.png?text=Miao+He", caption="何晨苗 (Miao)")
    st.subheader("📍 联系方式")
    
    st.markdown("📧 **Email**")
    st.caption("chenmiaohe7@gmail.com")
    st.caption("602471974@qq.com")
    
    st.markdown("📱 **Phone**")
    st.caption("🇨🇳 +86 15897472620")
    st.caption("🇺🇸 +1 4132725040")

# 3. 主界面：核心简介
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.title("你好，我是 何晨苗 (Miao) 👋")
    st.markdown("""
    ### **体育教育者 / 数据科学探索者**
    
    我目前就读于 **美国春田学院 (Springfield College)**。我致力于将 **北京体育大学** 扎实的竞技体育理论与国际前沿的 **循证体育科学 (Evidence-based Practice)** 相结合。
    
    我的目标是利用数据驱动的方法优化运动表现，并探索体育教育在不同文化背景下的创新路径。
    """)

with col2:
    st.write("### 📈 个人成长图谱")
    # 这里的进度可以根据你的实际备考/学业进度调整
    st.write("MTEL 备考进度")
    st.progress(75)
    st.write("数据科学技能 (Python/R)")
    st.progress(60)
    st.write("拳击教学资质")
    st.progress(90)

st.markdown("---")

# 4. 详细信息：标签页展示
tab1, tab2, tab3 = st.tabs(["🎓 教育背景", "🏆 专业资质", "📖 教学哲学"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("🇺🇸 Springfield College")
        st.write("**体育教育专业 (Graduate/Undergraduate)**")
        st.write("主要研究：运动生理学、课程设计、特殊体育教育。")
    with c2:
        st.subheader("🇨🇳 北京体育大学")
        st.write("**体育教育专业**")
        st.write("核心经历：系统掌握竞技体育训练法，并在 [具体项目] 表现优异。")

with tab2:
    st.subheader("跨界技能组合")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("#### 🥊 专项技能")
        st.write("- 拳击教学与训练\n- 力量与体适能")
    with col_b:
        st.markdown("#### 💻 技术能力")
        st.write("- Python 数据处理\n- Streamlit 网页构建\n- 运动数据分析")
    with col_c:
        st.markdown("#### 📜 证书")
        st.write("- MTEL (准备中)\n- [其他证书...]")

with tab3:
    st.info("### 我的教学哲学")
    st.write("""
    > “体育不仅是汗水，更是科学。我相信通过数据量化和循证方法，可以为每位学生找到最适合的运动路径。”
    
    作为一名教师，我的使命是连接**科学研究**与**训练场**，让学生在运动中获得自信与健康。
    """)

# 5. 底部互动
st.markdown("---")
st.header("📮 留言与交流")
with st.form("contact"):
    name = st.text_input("你的姓名")
    msg = st.text_area("你想对我说的话")
    if st.form_submit_button("发送信息"):
        st.balloons()
        st.success(f"收到！谢谢你，{name}。我会尽快与你联系。")
