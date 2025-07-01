## Streamlit 快速入门

#### 环境准备
```shell
pip install virtualenv
Python -m venv streamlit_venv

# 激活 streamlit_venv
source streamlit_venv/bin/activate

pip install streamlit pandas

# 保存环境
pip freeze > requirements.txt
# 恢复环境
pip install -r requirements.txt

# 测试
streamlit hello
```

#### 例子
##### chap02
```shell
# 设置了一个标题
streamlit run Chap02/Product_Recommender/data_app.py
```

##### chap03
```shell
streamlit run Chap03/Product_Recommender/data_app.py
```

##### chap04
+ ex01 不使用layouts和containers
```shell
streamlit run Chap04/ex01.py
```
+ Streamlit App With Layouts and Containers
```shell
streamlit run Chap04/ex02.py
```
+ Application to use the utility features of Streamlit
```shell
streamlit run Chap04/ex03.py
```