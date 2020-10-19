import streamlit as st
## streamlit charts
## Plotting
# load iris.csv
# https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv
st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd
iris_df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv")
st.subheader('dataframe of iris data')
st.dataframe(iris_df)
#
st.subheader("Matplotlib/Pandas로 차트 그리기")
iris_df[iris_df['variety']=='Virginica']['petal.length'].hist()
st.pyplot()
