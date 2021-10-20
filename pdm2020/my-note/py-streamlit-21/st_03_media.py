import streamlit as st
st.header("Show media") 

## Show image
## PIL : Python Image Library
## (How to install PIL): pip install pillow
from PIL import Image

img = Image.open("files/example_cat.jpeg")
st.image(img, width=400, caption="Image example: Cat")
 
# ## Show videos
vid_file = open("files/example_vid_cat.mp4", "rb").read()
st.video(vid_file, start_time=2)
 
# ## Play audio file.
audio_file = open("files/loop_w_bass.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3", start_time=10)

st.header("Load local image from PC")
#### Load images
# Types of images
imgTypes = ["png", "jpg"]
 
st.info("Upload source image on Streamlit")
# # st.set_option('deprecation.showfileUploaderEncoding', False)
 
source_img_buf = st.file_uploader("Upload source image", type=imgTypes, key='src')
 
if source_img_buf is not None:
    source_img = Image.open(source_img_buf)
    #### Show image
    st.image(source_img)

