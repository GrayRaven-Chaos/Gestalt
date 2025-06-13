import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它
import time
from PIL import Image
import random
# 设置页面标题以及整体布局
st.set_page_config(page_title="多功能应用平台", layout="wide")
st.image('https://www.gxvnu.edu.cn/images/QQtupian20240701090920_fuben.png', use_column_width=False)
# 创建顶部选项卡
tabs = st.tabs(["📊 数字档案", "🧀 美食探索", "🎼 音乐播放器", "📝 简历生成器"])
#  数字档案板块
with tabs[0]:
    st.title("🕶学生小军-数字档案")
    
    st.header("🔑基础信息")
    st.text("学生ID：NEO-2023-007")
    st.markdown("注册时间：:green[2025-6-4-16:20:48] | 精神状态：✅ 正常 ")
    st.markdown("当前教室：:green[实训301] | 安全等级：:green[普通]")
    
    # 技能矩阵
    st.subheader('📊技能矩阵')
    c1, c2, c3 = st.columns(3)
    c1.metric(label="C语言", value="95%", delta="+2%")
    c2.metric(label="Python", value="87%", delta="-1%")
    c3.metric(label="Java", value="68%", delta="-10%")
    
    # Streamlit课程进度
    st.subheader("🎯 Streamlit课程进度")
    st.text("Streamlit课程进度")
    progress_bar = st.progress(60)  # 假设进度为60%
    
    # 分割线
    st.markdown('***')
    
    # 定义数据,以便创建数据框
    data = {
        '日期':['2023-10-01', '2023-10-05', '2023-10-12'],
        '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
        '状态':['✅完成', '🕒进行中', '❌未完成'],
        '难度':['***', '****', '**'],
    }
    # 定义数据框所用的索引
    index = pd.Series(['0', '1', '2'], name='  ')
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)
    
    st.subheader('📝任务日志')
    st.dataframe(df)
    
    # 分割线
    st.markdown('***')
    
    # 最新代码成果
    st.header('🔐最新代码成果')
    python_code = '''def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stealth_evade()
'''
    st.code(python_code)

# 美食探索板块
with tabs[1]:
    st.title("🧀 南宁美食探索 🧀")
    
    # 介绍
    st.markdown("""
    探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。
    """)
    
    # 定义数据,以便创建数据框
    data = {
        '店名': ["星艺会尝不忘", "蜜雪冰城", "塔斯汀(火炬路店)", "好友缘", "白妈螺狮粉"],
        "类型": ["中餐", "饮料", "快餐", "自助餐", "中餐"],
        "评分": [4.2, 4.8, 4.5, 4.7, 4.3],
        "价格": [15, 10, 20, 35, 20],
        "位置X": [22.853838, 22.850126,22.835862, 22.809105, 22.839699],
        "位置Y": [108.222177, 108.222890, 108.295162, 108.378664, 108.245804]
    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series([1,2,3,4,5], name='序号')
    # 将新索引应用到数据框上
    df.index = index
    
    # 地图坐标展示
    st.header("📍 南宁美食地图")
    st.map(pd.DataFrame({
        "lat": df["位置X"],
        "lon": df["位置Y"],
        "店名": df["店名"]
    }))
    
    # 餐厅评分条形图
    st.header("⭐ 餐厅评分")
    st.bar_chart(df.set_index('店名')['评分'])
    
    st.header("💰 不同类型餐厅价格走势")
    # 新建一个12个月份的走势数据data2
    data2= {
        '月份':['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
        '星艺会尝不忘':[17,17,16,15,19,18,20,15,18,20,15,18],
        '蜜雪冰城':[7,9,8,10,6,8,10,12,10,10,11,8],
        '塔斯汀(火炬路店)':[17,20,23,25,25,23,20,25,18,19,16,18],
        '好友缘':[37,27,26,25,29,28,30,35,38,30,35,38],
        '白妈螺狮粉':[19,18,22,19,23,18,17,23,28,23,25,22],
    }
    # 新建一个数据框df2作为展示折线图的数据
    df2 = pd.DataFrame(data2)
    df2 = df2.set_index('月份')
    
    # 显示折线图
    st.line_chart(df2)
    
    # 用餐高峰面积图
    st.header("📰 用餐高峰时段")
    # 创建时间数据
    hours = [11, 12, 13, 17, 18, 19]
    crowd_data = pd.DataFrame({
        "时间": hours,
        "星艺会尝不忘": [30, 95, 70, 40, 85, 60],
        "蜜雪冰城": [25, 85, 65, 35, 90, 65],
        "塔斯汀(火炬路店)": [40, 80, 50, 45, 75, 55],
        "好友缘": [50, 70, 60, 55, 95, 40],
        "白妈螺狮粉": [80,50, 40, 30, 100, 45],
    })
    st.area_chart(crowd_data.set_index("时间"))
    
#  音乐播放器板块 
with tabs[2]:
    st.title("🎼简易音乐播放器🎼")
    
    # 模拟音乐库
    music_library = [
        {
            "歌名": "「极地暗流」- Narwhal",
            "歌手": "Vanguard Sound / Haloweak",
            "播放时长": "5:40",
            "封面链接": "http://p1.music.126.net/XCkyfA8o2Sb5qScfNPVRXA==/109951164626741397.jpg",
            "歌曲链接": "https://music.163.com/song/media/outer/url?id=1416730484.mp3"
        },
        {
            "歌名": "Twilight road 暮光之路",
            "歌手": "呦猫UNEKO / Kausz",
            "播放时长": "4:16",
            "封面链接": "http://p2.music.126.net/1JAQZP59A1nVjjcgq2jLnQ==/109951170480262656.jpg",
            "歌曲链接": "https://music.163.com/song/media/outer/url?id=2675193406.mp3"
        },
        {
            "歌名": "Burning Vow 誓焰",
            "歌手": "芝麻Mochi",
            "播放时长": "4:15",
            "封面链接": "http://p1.music.126.net/YK01DLPApdrjapYOUlbvNQ==/109951169835050330.jpg",
            "歌曲链接": "https://music.163.com/song/media/outer/url?id=2613308858.mp3"
        },
        {
            "歌名": "N.A.M.E",
            "歌手": "Punishing Gray Raven",
            "播放时长": "3:46",
            "封面链接": "http://p1.music.126.net/cnYoY9qtf8qYZkyZUPS7QA==/109951166960334103.jpg",
            "歌曲链接": "https://music.163.com/song/media/outer/url?id=1913688116.mp3"
        }
    ]
    
    # 初始化会话状态
    if 'current_song_index' not in st.session_state:
        st.session_state.current_song_index = 0
    if 'is_playing' not in st.session_state:
        st.session_state.is_playing = False
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    
    # 获取当前歌曲信息
    def get_current_song():
        return music_library[st.session_state.current_song_index]
    
    # 播放控制函数
    def play_pause():
        st.session_state.is_playing = not st.session_state.is_playing
    
    def next_song():
        st.session_state.current_song_index = (st.session_state.current_song_index + 1) % len(music_library)
        st.session_state.is_playing = True
        st.session_state.progress = 0
    
    def prev_song():
        st.session_state.current_song_index = (st.session_state.current_song_index - 1) % len(music_library)
        st.session_state.is_playing = True
        st.session_state.progress = 0
    
    # 分割线
    st.markdown("---")
    
    # 当前歌曲信息
    current_song = get_current_song()
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # 专辑封面
        st.image(current_song["封面链接"], width=150, caption="专辑封面")
    
    with col2:
        st.subheader(current_song["歌名"])
        st.markdown(f"**歌手**: {current_song['歌手']}")
        st.markdown(f"**时长**: {current_song['播放时长']}")
    
    # 播放控制按钮
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.button("上一首", on_click=prev_song)
    
    with col2:
        if st.session_state.is_playing:
            st.button("暂停", on_click=play_pause)
        else:
            st.button("播放", on_click=play_pause)
    
    with col3:
        st.button("下一首", on_click=next_song)
    
    # 播放进度显示
    progress_bar = st.progress(st.session_state.progress)
    if st.session_state.is_playing:
        for i in range(100):
            time.sleep(0.1)  # 模拟播放进度
            st.session_state.progress = i + 1
            progress_bar.progress(st.session_state.progress)
            if not st.session_state.is_playing:
                break
        if st.session_state.progress >= 100:
            next_song()
    
    # 音频播放器
    st.audio(current_song["歌曲链接"], format="audio/mp3")
    
    # 歌曲列表
    st.markdown("## 歌曲列表")
    for i, song in enumerate(music_library):
        if st.button(f"{song['歌名']} - {song['歌手']} ({song['播放时长']})", key=f"song_{i}"):
            st.session_state.current_song_index = i
            st.session_state.is_playing = True
            st.session_state.progress = 0
            st.experimental_rerun()
# 简历生成器板块
with tabs[3]:
    st.title("📝个人简历生成器📝")
    st.text('欢迎创建您的个性化简历')
    
    # 设置列容器
    col1, col2 = st.columns([1, 2])
    
    # 第一列代码
    with col1:
        st.text('个人信息表单')
        # 分割线
        st.markdown('***')
        name = st.text_input('姓名', autocomplete='name')
        
        zw = st.text_input('职位：', ' ')
        
        phone = st.text_input('电话：', value=None)
        
        Email = st.text_input('邮箱：', placeholder='这是一个占位字符串')
        
        # value参数默认为None，初始状态为今天
        birth = st.date_input("出生日期：", value=None)
        
        # 设置水平排列
        lunch = st.radio('性别',
                        ['男', '女', '其他'],
                        horizontal=True )
        
        size = st.selectbox('学历',
                           ['小学', '初中', '高中', '专科', '本科'],)
        
        options_2 = st.multiselect('语言能力',
                                  ['中文', '英语', '日语', '俄罗斯语', '法语'],
                                  [], max_selections=2)
        
        options_3 = st.multiselect('技能(可多选)',
                                  ['C语言', 'C++', 'Erlang', 'Go', 'Ruby', 'PHP', 'JavaScript', 'Python', 'Java', 'Perl'],
                                  [], max_selections=10)
        
        my_range = range(0, 31)
        numbers = st.select_slider('工作经验（年）', options=my_range, value=5)
        
        my_range1 = range(5000, 50001)
        end_money = st.select_slider('期望薪资范围（元）',
                                    options=my_range1,
                                    value=(5000, 10000))
        
        init_text = ""
        summary = st.text_area(label='个人简介：', value=init_text,
                               height=200, max_chars=200)
        
        w1 = st.time_input("每日最佳联系时间段")
        
        # 照片上传
        photo = st.file_uploader('个人照片', type=['jpg', 'jpeg', 'png'])
    
    # 第二列代码    
    with col2:
        st.text('简历实时预览')
        # 分割线
        st.markdown('***')
        # 设置第二列内部的列容器
        col3, col4 = st.columns([1, 1])
        # 内部第一列代码
        with col3:
            # 姓名
            if name:
                st.header(name)
                
            # 照片展示
            if photo:
               image = Image.open(photo)
               st.image(image, use_column_width=150)
            else:
               st.text(" ")

            # 个人信息
            if zw:
                st.markdown(f"⚖ 职位:{zw}")
            if phone:
                st.markdown(f"📱 电话: {phone}")
            if Email:
                st.markdown(f"✉ 邮箱: {Email}")
            if birth:
                st.markdown(f"📅 出生日期: {birth.strftime('%Y-%m-%d')}")
        
        with col4:
            if lunch :
                st.markdown(f"👨‍ 性别 👧: {lunch }")
            if size:
                st.markdown(f"‍🎓 学历 ‍🎓: {size}")
            if numbers:
                st.markdown(f"💼 工作经验: {numbers}年")
            if end_money:
                st.markdown(f"💰 期望薪酬: {end_money}元")
            if w1:
                st.markdown(f"⏰ 最佳联系时间: {w1.strftime('%H:%M')}")
            if options_2:
                st.markdown(f"💬 语言能力: {options_2}")
        
        # 分割线
        st.markdown('***')
        # 个人简介
        st.subheader("个人简介")
        if summary:
            st.write(summary)
        else:
            st.text('这个人很懒，什么介绍都没有留下')
        # 专业技能展示
        st.subheader("专业技能")  
        if options_3:
            st.write(options_3)
