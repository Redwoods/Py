import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# import io
from PIL import Image

# st.set_option('deprecation.showfileUploaderEncoding', False)

#### Load images
# Types of images
imgTypes = ["png", "jpg"]

st.info("Upload source image on Streamlit")
source_img_buf = st.file_uploader("Upload source image", type=imgTypes, key='src')

if source_img_buf is not None:
    source_img = Image.open(source_img_buf)
    st.success("Source image uploaded!")

st.info("Upload style image on Streamlit")
style_img_buf = st.file_uploader("Upload style image", type=imgTypes, key='style')
if style_img_buf is not None:
    style_img = Image.open(style_img_buf)
    st.success("Style image uploaded!")

st.info("Check here to see source and style images:")
if st.checkbox("Show source and style images", key='raw'):
  fig = plt.figure(figsize=(12, 6))
  plt.subplot(1, 2, 1)
  plt.imshow(source_img)
  plt.title('Source Image')
  plt.subplot(1, 2, 2)
  plt.imshow(style_img)
  plt.title('Style Image')
  st.pyplot(fig)
  st.success("Completed!")

# New way to show images in columns (New features of streamlit)
st.info("Check here to show images:source, style in cloumns")
if st.checkbox("Show source and style images", key='column'):
    col1, col2 = st.beta_columns(2)
    col1.header("Source iamge")
    col1.image(source_img, use_column_width=True)
    col2.header("Style image")
    col2.image(style_img, use_column_width=True)
    st.success("Column images, Completed!")

