import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.sidebar.header('EDA: Cleveland Heart Disease, clean data') 
st.sidebar.subheader('Visualization using seaborn and plotly by pdm16')

# Get the data
df0 = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/heart.csv")

# Clean the data : zero2median()
# 1. Check zeros in features with Pregnancies, Outcome excluded.
# 2. Replace zero with NaN 
# 3. Replace NaN with the median of the corresponding featurs
# def zero2median(df):
#     columns_with_zero = df.columns[(df==0).sum() > 0][1:-1]
#     # Index(['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'], dtype='object')
#     df[columns_with_zero]=df[columns_with_zero].replace(0,np.nan)
#     for feature in columns_with_zero:
#         df[feature].fillna(df[feature].median(),inplace=True)
    
#     return df

# Start with cleaned dataframe (이미 전처리 되었음.)
df = df0  # zero2median(df0)

# 정상인(noHD), 환자(HD) 구분은 'target' 변수
# [hint] 'Outcome' => 'target'
# [hint] 'noDM' => 'noHD'  ,    'DM' => 'HD'
df['target'] = df['target'].apply(lambda x: 'HD' if x == 1 else 'noHD')

classes=df.target
noDB,DB=classes.value_counts()
st.sidebar.write('non-Heart-Disease(noHD):',noDB)
st.sidebar.write('Heart-Disease(HD):',DB)

# plotly batchart
# https://towardsdatascience.com/step-by-step-bar-charts-using-plotly-express-bb13a1264a8b
df1 = df.groupby(["target"]).count().reset_index()
fig0 = px.bar(df1, 
              y=df.groupby(["target"]).size(),
              x="target", 
              width=350, height=300, 
              labels={'y':'Number'}, 
              color='target', 
              color_discrete_map=dict(noHD = 'green', HD = 'red'))
st.sidebar.write(fig0)
# pi-chart
fig1=px.pie(df, values=df.target.value_counts(), 
            width=350, height=300, 
            names=['noHD','HD'], color=['noHD','HD'], 
            color_discrete_map=dict(noHD = 'green', HD = 'red')) 
st.sidebar.write(fig1)

st.subheader(f'Clean Data Information: shape = {df.shape}')
st.write("##### [Data cleaning] Zeores in data were replaced with the median.")
st.subheader('features and classes')
st.write(f'##### features = {list(df.columns)[:-1]}')
st.write(f'##### classes = {pd.unique(classes)}')
st.write('***')
# Show the data as a table (you can also use st.write(df))
st.dataframe(df)
# Get statistics on the data
# st.write(df.describe())

# histogram with plotly
st.header("Histogram")
## multi-column layput
row0_1, row0_space2, row0_2, set_hist_color = st.beta_columns(
    (1, .1, 1, 1))

with row0_1: 
    hist_x = st.selectbox("Select a feature", options=df.columns, index=df.columns.get_loc("age"))
        
with row0_2: 
    bar_mode = st.selectbox("Select barmode", ["relative", "group"], 0)

with set_hist_color:
    hist_color = st.selectbox('Select categorical color option', ["sex", 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal', 'target'], 0)

hist_bins = st.slider(label="Histogram bins", min_value=5, max_value=50, value=25, step=1, key='h1')
# hist_cats = df['Outcome'].sort_values().unique()
hist_cats = df[hist_x].sort_values().unique()
hist_fig1 = px.histogram(df, x=hist_x, nbins=hist_bins, 
                         title="Histogram of " + hist_x,
                         template="plotly_white", 
                         color=f'{hist_color}', 
                         barmode=bar_mode, 
                         color_discrete_map=dict(noDM = 'green', DM = 'red'),  
                         category_orders={hist_x: hist_cats}) 
st.write(hist_fig1)


# boxplots
st.header("Boxplot")
st.subheader("With a categorical variable - Outcome [noDM, DM]")
## multi-column layput
row1_1, row1_space2, row1_2 = st.beta_columns(
    (1, .1, 1))

with row1_1: 
    box_x = st.selectbox("Boxplot variable", ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca'], 0)
        
with row1_2: 
    box_cat = st.selectbox("Categorical variable", ["sex", 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal', 'target'], 0)

st.write("Hint - try comparison w.r.t Categories")
box_fig = px.box(df, x=box_cat, y=box_x, title="Box plot of " + box_x, color=f'{box_cat}', 
                        color_discrete_map=dict(noDM = 'green', DM = 'red'), 
                        template="plotly_white", 
                        points="all") 
st.write(box_fig)

# Correlations
## multi-column layput
st.header("Correlations")
row2_1, row2_space2, row2_2, set_corr_color = st.beta_columns((1, .1, 1, 1))

with row2_1: 
    corr_x = st.selectbox("Correlation - X variable", options=df.columns, index=df.columns.get_loc("age"))
        
with row2_2: 
    corr_y = st.selectbox("Correlation - Y variable", options=df.columns, index=df.columns.get_loc("age"))

with set_corr_color:
    corr_color = st.selectbox('Select color option', options=df.columns, index=df.columns.get_loc("age"))

corr2_fig = px.scatter(df, x=corr_x, y=corr_y, 
                            color=f'{corr_color}', 
                            color_discrete_map=dict(noDM = 'green', DM = 'red'), 
                            template="plotly_white")
st.write(corr2_fig)

# heatmap
st.subheader('Heatmap of correlation')
fig4 = plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),annot=True, vmin=-1, vmax=1, cmap='coolwarm')
st.pyplot(fig4)
# st.write(fig4)

# correlation heatmap
st.subheader('Heatmap of selected parameters')
fig5 = plt.figure(figsize=(10,10))
hmap_params = st.multiselect("Select parameters to include on heatmap", options=list(df.columns), default=[p for p in df.columns if "Outcome" not in p])
sns.heatmap(df[hmap_params].corr(), annot=True, vmin=-1, vmax=1, cmap='coolwarm')
st.pyplot(fig5)

#############################################################
st.markdown('***')
st.header('Heatmap')
st.subheader('Strongly correlated or anti-correlated parameters')

df_corr = pd.concat([df.pop(x) for x in ['age', 'cp', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']], axis=1)

fig6 = plt.figure(figsize=(10,10))
sns.heatmap(df_corr.corr(),annot=True, vmin=-1, vmax=1, cmap='coolwarm')
st.pyplot(fig6)