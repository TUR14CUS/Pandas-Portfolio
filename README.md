# Streamlit Website

## Overview

This Streamlit-powered website displays information from a CSV file, presenting content in a user-friendly and visually appealing manner. The website showcases a combination of text, images, and links to source code.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Streamlit
- Pandas

Install the required packages using the following command:

```bash
pip install streamlit pandas
```

### Running the Website

To run the website, execute the following command in your terminal:

```bash
streamlit run your_script.py
```

Replace `your_script.py` with the name of your Python script.

## Structure

The website is organized into different sections using Streamlit's layout features. Here's a breakdown:

### Header

- A wide layout is configured using `st.set_page_config(layout="wide")`.
- Two columns (`col1` and `col2`) are defined to hold an image and a title with accompanying text.

```python
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("lorem ipsum")
    # Additional content goes here
```

### Main Content

- The main content is divided into two columns (`col3` and `col4`), separated by an empty column (`empty_col`).
- Each column displays information from the CSV file, including headers, descriptions, images, and source code links.

```python
col3, empty_col, col4 = st.columns([2, 1, 2])

with col3:
    # Display information from the first half of the CSV file
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    # Display information from the second half of the CSV file
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
```

### Additional Content

- Additional content, outside the main columns, can be added using `st.write()`.

```python
content2 = """
lore ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
"""
st.write(content2)
```

## Customization

Feel free to customize the website by modifying the provided script and updating the CSV file with your own data. Adjust the layout, styling, and content to suit your preferences.

---

Make sure to replace placeholders such as `your_script.py`, `images/photo.jpg`, and `data.csv` with the actual file names and paths used in your project.
