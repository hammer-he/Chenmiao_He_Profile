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
    st.image("012.psd", caption="何晨苗 (Meow)")
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
    st.title("您好，我是何晨苗 (Meow) 👋")
    # 使用反引号 ` 将关键词包围，会呈现出代码标签的效果
    st.markdown("**Focus:** `拳击` `运动表现分析` `循证运动实践` `体育教育`")

with col2:
    st.write("### 📈 个人成长图谱")
    # 这里的进度可以根据你的实际备考/学业进度调整
    st.write("北京体育大学硕士毕业")
    st.progress(80)
    st.write("申请清华大学体育博士")
    st.progress(30)
    st.write("拳击世界冠军")
    st.progress(20)

st.markdown("---")

# 4. 详细信息：标签页展示
tab1, tab2, tab3, tab4 = st.tabs(["🎓 教育背景", "💼 实践经验", "🔬 科研成果", "🏅 荣誉与技能"])

# --- Tab 1: 教育背景 ---
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🇨🇳 北京体育大学")
        st.caption("Beijing Sport University")
        st.write("**体育教育训练学 | 硕士研究生**")
        st.markdown("""
        - **核心领域：** 运动生理学、运动训练学、体育教学论、科研方法论
    
        """)
    
    with col2:
        st.markdown("### 🇺🇸 Springfield College")
        st.caption("春田学院 (Springfield, MA)")
        st.write("**体育教育训练学 | 访问学者**")
        st.markdown("""
        - **核心领域：** 循证实践 (EBP)、运动技能分析、高级统计学、体育大数据
        """)

# --- Tab 2: 实践经验 ---
with tab2:
    # 使用 container 让内容更有层次感
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("#### 🏗️ 中国拳击协会")
            st.caption("实习生 ")
            st.write("""
            - 负责全国拳击赛事及教练员培训班的**组织协调**
            - 协助国家队出访比赛注册及外籍裁判**外事接待**
            """)
        
        with c2:
            st.markdown("#### 🏫 春田市拳击队")
            st.caption("助理教练 | 美国春田")
            st.write("""
            - 负责队员月度体能监测与**技术数据分析**
            - 参与正式比赛的**执法裁判**与教学工作
            """)
        
        with c3:
            st.markdown("#### 🥊 拳击俱乐部")
            st.caption("主教练 | 课程研发")
            st.write("""
            - 设计针对不同水平段的**模块化拳击课程**
            - 提供高强度私教指导及团队训练管理
            """)

# --- Tab 3: 科研经验 ---
with tab3:
    st.markdown("### 🔬 学术发表与会议报告")
    
    # 将原本单调的列表改为更具含金量的展示
    st.info("**核心研究方向：** 拳击技术动作自动化评估，新入职体育教师支持")
    
    with st.expander("📍 国际会议报告 (Conference Presentations)", expanded=True):
        st.markdown("""
        1. **SHAPE America National Convention**
        2. **国际华人体育健康学会 (ICSPAH) 年会**
           - *主题：拳击技术动作发展序列构建*
        3. **哈佛国际教育论坛 **
           - *主题：新入职女性体育教师的困境*
        """)
        # --- Tab 4: 荣誉与技能 ---
with tab4:
    # 采用 1.5 : 1 的比例，左边放荣誉（内容多），右边放技能（精简）
    col_honors, col_skills = st.columns([1.5, 1])

    with col_honors:
        st.markdown("### 🏆 荣誉奖项")
        
        # 使用 expander 区分学术和体育，让界面更整洁
        with st.expander("🎓 学术奖项 (Academic Honors)", expanded=True):
            st.markdown("""
            - **John's Scholarship** | Springfield College  
              *春田学院奖学金*
            - **二等奖学金** | 北京体育大学  
             
            """)

        with st.expander("🥊 竞技体育荣誉 (Athletic Achievements)", expanded=True):
            # 使用加粗和 Emoji 突出含金量
            st.success("🥇 **全国大学生拳击锦标赛 - 冠军**")
            st.markdown("""
            - **冠军** | 北京体育大学拳击比赛
            - **冠军** | 湖南省永州市篮球比赛
            - **第四名** | 北京体育大学网球比赛
            """)

    with col_skills:
        st.markdown("### 🛠️ 专业技能")
        
        # 1. 语言能力展示 - 使用 metric 显得很专业
        st.write("**语言能力**")
        st.metric(label="TOEFL iBT", value="93",")
        
        st.divider()

        # 2. 技术栈展示
        st.write("**数据科学**")
        # 使用进度条或简单的标签云
        st.markdown("""
        - 🐍 **Python** (网页制作)
        - 📊 **R 语言** (数据分析与可视化)
      
        """)
        
     

# 5. 底部互动
st.markdown("---")
st.header("📮 留言与交流")
with st.form("contact"):
    name = st.text_input("您的姓名")
    msg = st.text_area("您想对我说的话")
    if st.form_submit_button("发送信息"):
        st.balloons()
        st.success(f"收到！谢谢你，{name}。我会尽快与您联系。")
