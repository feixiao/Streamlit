

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# the first iteration without the use of layouts and containers


# Title
st.title('Streamlit App Without Layouts and Containers')


# User Input
user_input = st.text_input("Enter some text")
number_input = st.number_input("Enter a number")


# Button
if st.button('Click Me'):
    st.write('Button clicked!')


# Plotting a simple line chart
# 解释下下面代码

# 生成一个包含20行2列的随机数数据，列名为'A'和'B'
data = pd.DataFrame(np.random.randn(20, 2), columns=['A', 'B'])

# 使用st.line_chart()函数绘制线图
st.line_chart(data)


# Displaying some text
st.write("Here's some text below the chart.")