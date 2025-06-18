#导入库
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle # 用来保存模型和 output_uniques 变量

#以下是模型训练代码

# 读取数据集，并将字符编码指定为 gbk，防止中文报错
penguin_df = pd.read_csv('D:/Chapter8_resources/penguins-chinese.csv', encoding='gbk')
# 删除缺失值所在的行
penguin_df.dropna(inplace=True)
# 将企鹅的种类定义为目标输出变量
output = penguin_df['企鹅的种类']
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
# 对特征列进行独热编码
features = pd.get_dummies(features)
# 将目标输出变量转换为离散数值
output_codes, output_uniques = pd.factorize(output)

# 从 features 和 output_codes 这两个数组中将数据集划分为训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

# 构建一个随机森林分类器
rfc = RandomForestClassifier()

# 使用训练集数据 x_train 和 y_train 来拟合（训练）模型
rfc.fit(x_train, y_train)

# 用训练好的模型 rfc 对测试集数据 x_test 进行预测，将预测结果存储在 y_pred 中
y_pred = rfc.predict(x_test)

# 计算测试集上模型的预测准确率
score = accuracy_score(y_test, y_pred)

# 使用 with 语句简化文件操作
# open() 函数和 'wb' 参数用于创建并写入字节流
# pickle.dump() 方法将模型对象转换为字节流
with open('rfc_model.pkl', 'wb') as f:
    pickle.dump(rfc, f)

# 同上
# 将映射变量写入文件中
with open('output_uniques.pkl', 'wb') as f:
    pickle.dump(output_uniques, f)

print('保存成功，已生成相关文件。')

#以下是企鹅分类项目web应用的代码

# 设置页面的标题、图标和布局
st.set_page_config(
    page_title="企鹅分类器", # 页面标题
    page_icon=":penguin:", # 页面图标
    layout='wide',
)
# 使用侧边栏实现多页面显示效果
with st.sidebar:
    st.image('D:/Chapter8_resources/images/rigth_logo.png', width=100)
    st.title('请选择页面')
    page = st.selectbox("请选择页面", ["简介页面", "预测分类页面"], label_visibility='collapsed')
if page == "简介页面":
    st.title("企鹅分类器:penguin:")
    st.header('数据集介绍')
    st.markdown("""帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，也可以作为机器学习入门练习。
    该数据集是由 Gorman 等收集，并发布在一个名为 palmerpenguins 的 R 语言包，以对南极企鹅种类进行分类和研究。
    该数据集记录了 344 行观测数据，包含 3 个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和帽带企鹅的各种信息。""")
    st.header('三种企鹅的卡通图像')
    st.image('D:/Chapter8_resources/images/penguins.png')
elif page == "预测分类页面":
    st.header("预测企鹅分类")
    st.markdown("这个 Web 应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入 6 个信息，就可以预测企鹅的物种，使用下面的表单开始预测吧！")
    # 该页面的列布局设置
col_form, col, col_logo = st.columns([3, 1, 2])
with col_form:
    # 运用表单和表单提交按钮
    with st.form('user_inputs'):
        island = st.selectbox('企鹅栖息的岛屿', options=['托尔森岛', '比斯科群岛', '德里姆岛'])
        sex = st.selectbox('性别', options=['雄性', '雌性'])
        bill_length = st.number_input('喙的长度（毫米）', min_value=0.0)
        bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0)
        flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0)
        body_mass = st.number_input('身体质量（克）', min_value=0.0)
        submitted = st.form_submit_button('预测分类')
# 初始化数据预处理格式中与岛屿相关的变量
island_biscoe, island_dream, island_torgerson = 0, 0, 0
# 根据用户输入的岛屿数据更改对应的值
if island == '比斯科群岛':
    island_biscoe = 1
elif island == '德里姆岛':
    island_dream = 1
elif island == '托尔森岛':
    island_torgerson = 1
# 初始化数据预处理格式中与性别相关的变量
sex_female, sex_male = 0, 0
# 根据用户输入的性别数据更改对应的值
if sex == '雌性':
    sex_female = 1
elif sex == '雄性':
    sex_male = 1
format_data = [bill_length, bill_depth, flipper_length, body_mass,
               island_dream, island_torgerson, island_biscoe, sex_male, sex_female]
# 使用 pickle 的 load 方法从磁盘文件反序列化加载一个之前保存的随机森林模型对象
with open('rfc_model.pkl', 'rb') as f:
    rfc_model = pickle.load(f)
with open('output_uniques.pkl', 'rb') as f:
    output_uniques_map = pickle.load(f)

if submitted:
    format_data_df = pd.DataFrame(data=[format_data], columns=rfc_model.feature_names_in_)
    # 使用模型对格式化后的数据 format_data 进行预测，返回预测的类别代码
    predict_result_code = rfc_model.predict(format_data_df)
    # 将类别代码映射到具体的类别名称
    predict_result_species = output_uniques_map[predict_result_code][0]

    st.write(f'根据您输入的数据，预测该企鹅的物种名称是：**{predict_result_species}**')

with col_logo:
    if not submitted:
        st.image('D:/Chapter8_resources/images/rigth_logo.png', width=300)
    else:
        st.image(f'D:/Chapter8_resources/images/{predict_result_species}.png', width=300)

