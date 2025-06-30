import streamlit as st
import random
import pandas as pd

# Sample product data
products = ['Phone', 'Laptop', 'Headphones', 'Camera', 'Smartwatch', 'Tablet', 'Charger', 'Keyboard', 'Mouse', 'Speaker']

def generate_random_recommendations(selected_products, products, num_recommendations=3):
    """Generate random product recommendations."""
    # 使用列表推导式，从所有商品中筛选出未被用户选择过的商品，生成新的列表
    available_products = [p for p in products if p not in selected_products]

    # 从 available_products 中随机抽取若干商品作为推荐。
    # random.sample 用于无重复地随机抽取元素。
    # 抽取数量为 num_recommendations 和 available_products 长度的较小值，避免商品数量不足时报错。
    recommendations = random.sample(available_products, min(num_recommendations, len(available_products)))
    return recommendations


# 根据传入的推荐商品列表，生成一个包含推荐商品及其购买可能性的 Pandas DataFrame。
def create_recommendation_df(recommendations):
    """Create a DataFrame with recommendations and random likelihood percentages."""

    # 使用列表推导式 [random.randint(50, 99) for _ in recommendations]，为每个推荐商品生成一个 50 到 99 之间的随机整数，表示“购买可能性百分比”。
    likelihoods = [random.randint(50, 99) for _ in recommendations]  # Random likelihood percentages between 50% and 99%
    # 用 pd.DataFrame 创建一个数据框，包含两列：
    return pd.DataFrame({'Recommended Product': recommendations, 'Likelihood of Purchase': likelihoods})

# Streamlit application layout
st.title('Product Recommender')
st.write('Select one or more products to see recommendations.')

# User selects multiple products
selected_products = st.multiselect('Choose products:', products, default=None)

# Generate recommendations if any product is selected
if selected_products:
    recommendations = generate_random_recommendations(selected_products, products)

    # Create and display recommendations DataFrame
    df_recommendations = create_recommendation_df(recommendations)
    st.write('Recommended Products:')
    st.dataframe(df_recommendations,
                 column_config={
                        'Likelihood of Purchase': st.column_config.NumberColumn(
                         'Likelihood of Purchase',
                         help="How likely is user to buy this **product**",
                         min_value=0,
                         max_value=100,
                         step=1,
                         format="%d %%",
                     )},
                 hide_index=True,
                 )
else:
    st.write('Please select at least one product to see recommendations.')


