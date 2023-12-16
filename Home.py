import base64
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(
    page_title="Waste item classification",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This application is for classification of waste item and it will facilitate waste management ,environment protection ans sources recovery by systematically categorizing. "
    }
) 

title_style = """
        color: #000000;
        font-size: 60px;
        text-align: center;
        width : 100%;
    """
page_bg_img = f"""
<style>
.custom-text {{
    margin-top: 50px;
    background-color: rgba(255, 255, 255, 0.4); /* Adjust the last value for transparency */
    padding: 16px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); /* Optional: Add a shadow effect */

}}
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://blogs.3ds.com/northamerica/wp-content/uploads/sites/4/2019/09/CPG-Bottles_InLine.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
h1 {{
{title_style}
}}
    p {{
        text-align: justify;
        font-size: 25px;
        margin-left: 20px;
}}
.styled-image {{
        border-radius: 10px;
        box-shadow: 2px 2px 5px #888888;
    }}
.example {{
    font-color: rgba(0, 0, 0, 0.5);
    font-weight: 5px;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1)
}}


[data-testid="stMarkdownContainer"] > .main {{  
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;
    }}
</style>
"""

def showimagewithcss(imageurl):
    with stylable_container(
        key="image",
        css_styles="""
        div[data-testid="stImage"]>img {
        border-radius: 10px;
        width: 200px;
        height: 200px;
        }"""
    ):
        st.image(imageurl)
    st.divider()
intro =f"""
<p class="custom-text">Waste has profound implications for both the environment and human health. Improper disposal and management of waste contribute to environmental degradation, air and water pollution, and soil contamination. These factors, in turn, pose significant health risks to communities worldwide. Sustainable waste management practices are crucial not only for preserving ecosystems but also for safeguarding human well-being by minimizing exposure to harmful pollutants and fostering a healthier, more sustainable future.</p>

"""
example="""<p class="example">
These are the examples of improper disposal of waste items.</p>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("WASTE ITEMS CLASSIFICATION")
st.write(intro,unsafe_allow_html=True)
st.write(example,unsafe_allow_html=True)
col1, col2, col3  = st.columns(3)
image1="https://th.bing.com/th/id/OIP.xAirES5DM6UPP9Bb3HdeVgHaFj?w=244&h=183&c=7&r=0&o=5&dpr=1.3&pid=1.7"
image2="https://th.bing.com/th/id/OIP.Vy3t3dIV7Iou-ioWlF8v1wHaEL?w=325&h=183&c=7&r=0&o=5&dpr=1.3&pid=1.7"
image3="https://th.bing.com/th/id/OIP.s6nHDhp_idCI1G5FWxX5sgAAAA?rs=1&pid=ImgDetMain"
image4="https://th.bing.com/th/id/OIP.2czAM4isq1bMCoFZ4Lc6KwHaEK?w=900&h=506&rs=1&pid=ImgDetMain"
imgae5="https://th.bing.com/th/id/OIP.cH5tTejXEQl_4rLxkxIbSQHaEK?w=2560&h=1440&rs=1&pid=ImgDetMain"
image6="https://th.bing.com/th/id/OIP.r51yLW6gMHEhN2tvR3RM4gHaD4?rs=1&pid=ImgDetMain"
with col1:
    showimagewithcss(image1)
    showimagewithcss(image4)
with col2:
    showimagewithcss(image2)
    showimagewithcss(imgae5)
with col3:
    showimagewithcss(image3)
    showimagewithcss(image6)
with stylable_container(
    key="green_button",
    css_styles="""
        button {
            background-color: green;
            color: white;
            border-radius: 20px;
           
        }
        """,
):
    if st.button("let save the world"):
        switch_page("getting_start")

