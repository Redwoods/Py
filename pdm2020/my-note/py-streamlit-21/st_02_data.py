import streamlit as st
st.header("Show data") 

## Load data
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
st.write(iris.data)
st.write(iris['target'])
st.write(iris.feature_names)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target']
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))
 
## Return table/dataframe
# table
st.table(iris_df) #.head())
 
# dataframe
st.dataframe(iris_df)
 
st.write(iris_df)

st.header('Load diabetes data')
diabetes_df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")
st.dataframe(diabetes_df)




