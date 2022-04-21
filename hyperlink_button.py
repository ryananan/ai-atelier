from bokeh.models.widgets import Div
import streamlit as st

#https://discuss.streamlit.io/t/how-to-link-a-button-to-a-webpage/1661/19

if st.button('Go to Streamlit'):
    js = "window.open('https://www.streamlit.io/')"  # New tab or window
    # js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

fid = 'xxxxxx'
url='https://drive.google.com/drive/folders/'+fid
if st.button('View your gallery on Google Drive'):
    js = "window.open('" + url + "')"  # New tab or window
    print(js)
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)