import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv", sep=";")

for index, row in df.iterrows():
    print(row["title"])

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("lorem ipsum")
    content = """
    lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
    """
    st.write(content)
    
content2 = """
lore ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
"""
st.write(content2)


col3, empty_col , col4 = st.columns([2, 1, 2])


with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])  # corrected here
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])  # corrected here
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")