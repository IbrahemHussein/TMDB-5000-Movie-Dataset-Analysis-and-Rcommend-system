<<<<<<< HEAD
import streamlit as st

st.set_page_config(
    page_title='About Movie Recommendations App',
    page_icon="📖",
    layout='wide',
    initial_sidebar_state='expanded'
)

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 36px;
        color: #1a73e8;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #ff6347;
        margin-bottom: 10px;
    }
    .content {
        font-size: 18px;
        color: #333333;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    .link {
        font-size: 18px;
        color: #1a73e8;
        text-decoration: none;
    }
    .link:hover {
        text-decoration: underline;
    }
    .footer {
        font-size: 16px;
        color: #666666;
        text-align: center;
        margin-top: 20px;
    }
    .image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='title'>About Movie Recommendations App</div>", unsafe_allow_html=True)

st.markdown("""
    <img src='https://th.bing.com/th/id/OIG1.gpvDmllFSWOG9_yBo2AG?pid=ImgGn' class='image'>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Project Overview</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    The Movie Recommendations App is designed to help users find movies they might enjoy based on their preferences. 
    By leveraging collaborative filtering techniques, the app can suggest movies similar to those the user has liked in the past.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Objectives</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    - Provide personalized movie recommendations.<br>
    - Enhance user experience by suggesting popular and highly rated movies.<br>
    - Continuously improve recommendation algorithms based on user feedback and new data.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>How to Use the App</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    1. Select a movie from the dropdown menu.<br>
    2. Click on the 'Recommend' button to see a list of recommended movies.<br>
    3. Browse through the recommendations and click on the movie titles to get more information.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Learn More</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    For more information about the project, visit our 
    <a href='https://github.com/your-repo' target='_blank' class='link'>GitHub repository</a>.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2024 Movie Recommendations App. All rights reserved.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
=======
import streamlit as st

st.set_page_config(
    page_title='About Movie Recommendations App',
    page_icon="📖",
    layout='wide',
    initial_sidebar_state='expanded'
)

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 36px;
        color: #1a73e8;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #ff6347;
        margin-bottom: 10px;
    }
    .content {
        font-size: 18px;
        color: #333333;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    .link {
        font-size: 18px;
        color: #1a73e8;
        text-decoration: none;
    }
    .link:hover {
        text-decoration: underline;
    }
    .footer {
        font-size: 16px;
        color: #666666;
        text-align: center;
        margin-top: 20px;
    }
    .image {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='title'>About Movie Recommendations App</div>", unsafe_allow_html=True)

st.markdown("""
    <img src='https://th.bing.com/th/id/OIG1.gpvDmllFSWOG9_yBo2AG?pid=ImgGn' class='image'>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Project Overview</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    The Movie Recommendations App is designed to help users find movies they might enjoy based on their preferences. 
    By leveraging collaborative filtering techniques, the app can suggest movies similar to those the user has liked in the past.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Objectives</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    - Provide personalized movie recommendations.<br>
    - Enhance user experience by suggesting popular and highly rated movies.<br>
    - Continuously improve recommendation algorithms based on user feedback and new data.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>How to Use the App</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    1. Select a movie from the dropdown menu.<br>
    2. Click on the 'Recommend' button to see a list of recommended movies.<br>
    3. Browse through the recommendations and click on the movie titles to get more information.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Learn More</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='content'>
    For more information about the project, visit our 
    <a href='https://github.com/your-repo' target='_blank' class='link'>GitHub repository</a>.
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2024 Movie Recommendations App. All rights reserved.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
>>>>>>> e1ddd1ea8b1198d4cd20417f4165fa0c77a36171
