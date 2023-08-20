import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Set the title of the web app
st.title("Iris Dataset Visualization")

# Load the Iris dataset
iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Sidebar with options
st.sidebar.header("Visualization Options")
plot_type = st.sidebar.selectbox("Select plot type:", ["Pair Plot", "Scatter Plot", "Histogram"])

# Visualize based on user selection
if plot_type == "Pair Plot":
    st.subheader("Pair Plot")
    hue_option = st.sidebar.checkbox("Color by species")
    
    plt.figure(figsize=(10, 8))
    if hue_option:
        plt.scatter(iris['sepal_length'], iris['sepal_width'], c=iris['species'].astype('category').cat.codes, cmap='viridis')
    else:
        plt.scatter(iris['sepal_length'], iris['sepal_width'], cmap='viridis')
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title("Scatter Plot")
    plt.colorbar(label="Species")
    st.pyplot()

elif plot_type == "Scatter Plot":
    st.subheader("Scatter Plot")
    x_axis = st.sidebar.selectbox("Select X-axis feature:", iris.columns[:-1])
    y_axis = st.sidebar.selectbox("Select Y-axis feature:", iris.columns[:-1])

    plt.figure(figsize=(10, 8))
    plt.scatter(iris[x_axis], iris[y_axis], c=iris['species'].astype('category').cat.codes, cmap='viridis')
    plt.xlabel(x_axis.capitalize())
    plt.ylabel(y_axis.capitalize())
    plt.title("Scatter Plot")
    plt.colorbar(label="Species")
    st.pyplot()

elif plot_type == "Histogram":
    st.subheader("Histogram")
    selected_feature = st.sidebar.selectbox("Select a feature:", iris.columns[:-1])
    
    plt.figure(figsize=(10, 8))
    plt.hist(iris[selected_feature], bins=20, edgecolor="k")
    plt.xlabel(selected_feature.capitalize())
    plt.ylabel("Frequency")
    plt.title("Histogram")
    st.pyplot()
