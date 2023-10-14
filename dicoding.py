import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title and subheader of your Streamlit app
st.title(
    "Visualizing The Best Performing Revenue by Product Category and Payment Type in E-Commerce Dataset"
)


# Load the cleaned data from a CSV file
data = pd.read_csv("cleaned_data.csv")
st.subheader("Banyaknya order per Product Category")

fig = plt.figure(figsize=[10, 6])
sns.barplot(
    x=data["product_category"].value_counts().values,
    y=data["product_category"].value_counts().index,
    palette="Set2",
)
plt.title("Banyaknya order per Product Category")
plt.xticks(rotation=45)
sns.despine()
st.pyplot(fig)


st.subheader("Banyaknya order per Payment type")

fig = plt.figure(figsize=[10, 6])
sns.barplot(
    x=data["payment_type"].value_counts().values,
    y=data["payment_type"].value_counts().index,
    palette="Set2",
)
plt.title("Banyaknya order per Payment type")
plt.xticks(rotation=45)
sns.despine()
st.pyplot(fig)

# Calculate total revenue per product category
product_category = (
    data.groupby("product_category")[["payment_value"]]
    .sum()
    .sort_values(by="payment_value", ascending=False)
    .reset_index()
)

# Create the second bar chart for total revenue per product category
st.subheader("Total Revenue per Product Category")

fig = plt.figure(figsize=[15, 8])
sns.barplot(
    x=product_category["product_category"],
    y=product_category["payment_value"],
    palette="Set2",
)
plt.title("Total Revenue per Product Category", fontsize=15)
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Revenue per Product Category (Millions)", fontsize=12)
sns.despine()
st.pyplot(fig)


payment_methods = (
    data.groupby("payment_type")[["payment_value"]]
    .sum()
    .sort_values(by="payment_value", ascending=False)
)

st.subheader("Total Revenue per Payment Type")

payment_methods.reset_index(inplace=True)
fig = plt.figure(figsize=[15, 8])
sns.barplot(
    x=payment_methods.payment_type, y=payment_methods.payment_value, palette="Set2"
)
plt.title("Total Revenue per payment type", fontsize=15)
plt.xlabel("Payment Type", fontsize=12)
plt.ylabel("Revenue per Payment type (Millions)", fontsize=12)
sns.despine()
st.pyplot(fig)
