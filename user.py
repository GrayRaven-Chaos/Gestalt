import streamlit as st
from PIL import Image

# 设置页面标题和布局
st.set_page_config(page_title="📄个人简历生成器📄", layout="wide")
st.title("📝个人简历生成器📝")
st.text('欢迎创建您的个性化简历')

#设置列容器
col1, col2= st.columns([1, 2])

#第一列代码
with col1:
    st.text('个人信息表单')
    # 分割线
    st.markdown('***')
    name = st.text_input('姓名', autocomplete='name')

    zw = st.text_input('职位：', ' ')

    phone=st.text_input('电话：', value=None)

    Email=st.text_input('邮箱：', placeholder='这是一个占位字符串')

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
                               [],max_selections=2)

    options_3 = st.multiselect('技能(可多选)',
                               ['C语言', 'C++', 'Erlang', 'Go', 'Ruby', 'PHP', 'JavaScript', 'Python', 'Java', 'Perl'],
                               [],max_selections=10)

    my_range = range(0, 31)

    numbers = st.select_slider('工作经验（年）', options=my_range, value=5)

    my_range1 = range(5000, 50001)

    end_money = st.select_slider('期望薪资范围（元）',
                                 options=my_range1,
                                 value=(5000, 10000))
    
    init_text = ""
    summary=st.text_area(label='个人简介：', value=init_text,
            height=200, max_chars=200)

    w1 = st.time_input("每日最佳联系时间段")



    #照片上传
    photo=st.file_uploader('个人照片',type=['jpg','jpeg','png'])
    
      

#第二列代码    
with col2:
    st.text('简历实时预览')
    # 分割线
    st.markdown('***')
    #设置第二列内部的列容器
    col3,col4=st.columns([1, 1])
    #内部第一列代码
    with col3:
        #姓名
        if name:
            st.header(name)
            
        #照片展示
        if photo:
           image = Image.open(photo)
           st.image(image, use_column_width=150)
        else:
           st.text(" ")

        #个人信息
        
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
    #个人简介
    st.subheader("个人简介")
    if summary:
        st.write(summary)
    else:
        st.text('这个人很懒，什么介绍都没有留下')
    #专业技能展示
    st.subheader("专业技能")  
    if options_3:
        st.write(options_3)
        
        
