import streamlit as st
from streamlit_folium import folium_static
import folium
from PIL import Image

st.set_page_config(page_title="streamlit-folium demo")

# Sidebar
st.sidebar.write("# streamlit-folium")
st.sidebar.subheader('Inje Univ. Map')
img = Image.open("ai_iju2.png")
st.sidebar.image(img, width=320, caption="IJU 2020 Fall, AI-made by NST")
st.sidebar.markdown(
    "- [Try NST(Neural style transfer) with your photos](http://life21c.inje.ac.kr:8503)")

"## Code snippet"

with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import folium

    # center on Inje University
    m = folium.Map(location=[35.249164, 128.901881],
                   zoom_start=16, width=600, height=450)

    # add marker for Inje University
    tooltip = "Inje University"
    folium.Marker(
        [35.249164, 128.901881], popup="Inje University", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)
