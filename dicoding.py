import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title and subheader of your Streamlit app
st.title('Visualizing The Best Performing Revenue by Product Category and Payment Type in E-Commerce Dataset')


# Load the cleaned data from a CSV file
data = pd.read_csv("cleaned_data.csv")

# Calculate product category sales and sort the values
product_category_revenue = data.groupby('product_category')[['payment_value']].sum().sort_values(by='payment_value', ascending=False)
payment_type_revenue = data.groupby('payment_type')[['payment_value']].sum().sort_values(by='payment_value', ascending=False)
# Display the plots in Streamlit
st.subheader('Payment Type Revenue')

st.bar_chart(payment_type_revenue)
st.subheader('Product Category Revenue')

st.bar_chart(product_category_revenue)

