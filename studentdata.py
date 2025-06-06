import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

st.title("🕶学生小军-数字档案")
st.header("🔑基础信息")
st.text("学生ID：NEO-2023-007")
st.markdown("注册时间：:green[2025-6-4-16:20:48] |精神状态：✅ 正常 ")
st.markdown ("当前教室：:green[实训301]|安全等级：:green[普通]")

#技能矩阵
st.subheader('📊技能矩阵')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="c语言", value="95%", delta="+2%")
c2.metric(label="Python", value="87%", delta="-1%")
c3.metric(label="java", value="68%", delta="-10%")

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

# 分割线
st.markdown('***')

# 系统信息
st.markdown(':green[>>>SYSTEM MESSAGE: ]下一个任务目标已解锁...')
st.markdown(':green[>>>TARGET: ]课程管理系统')
st.markdown(':green[>>>COUNTDOWN: ]2025-06-03 15:24:58')
st.markdown('系统状态：在线 连接状态:已加密')