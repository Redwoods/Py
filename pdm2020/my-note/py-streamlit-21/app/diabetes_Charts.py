import streamlit as st
import pandas as pd

# Get the data
df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")

st.subheader('Data Information:')
# Show the data as a table (you can also use st.write(df))
st.dataframe(df)
# Get statistics on the data
st.write(df.describe().T)

st.write('***')
# Show the data as a chart.
chart = st.line_chart(df)

## mid-term practice
## EDA of new data (csv file)




