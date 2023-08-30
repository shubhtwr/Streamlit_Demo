import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config("Shubham Tiwari", ":smiling_face_with_halo:", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#adding assets
lottie = load_lottie("https://lottie.host/6decf46b-999d-441a-b82f-d586ef512d4a/orjHbSbGDi.json")

# Header Sec
with st.container():
    st.subheader("Hi! I am Shubham :wave:")
    st.title("An architect from India.")
    st.write(
        "Along with my core area of study, I've also explored diverse fields like marketing and content creation "
        "through "
        "internships.\nAs a result, I've developed a T-shaped knowledge base, giving me a unique perspective on "
        "interdisciplinary fields. With a highly creative mindset, I strive to bring innovation and fresh ideas to "
        "everything I do.")
    st.write("[Visit my Blog >](https://shubhtwr.medium.com)")

#what i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("Welcome to my corner of the internet! I'm Shubham Tiwari, a passionate and innovative Python "
                 "developer with a knack for crafting elegant solutions to complex problems. With a strong foundation "
                 "in software engineering and a love for clean code, I thrive in turning ideas into reality through "
                 "the power of technology.")
        st.header("Python Development")
        st.write("Python is my playground! From building web applications to automating repetitive tasks, I leverage "
                 "the versatility of Python to create efficient and robust software solutions. Whether it's developing "
                 "data-driven applications, designing APIs, or crafting intelligent algorithms, I find joy in pushing"
                 "the boundaries of what Python can do.")
        st.header("Web Development")
        st.write("Web development is where art meets technology. I specialize in creating dynamic and user-centric "
                 "web experiences that leave a lasting impression. By blending my expertise in frontend and backend"
                 "technologies, I bring web applications to life that are not only visually appealing but also perform "
                 "seamlessly.")
        st.header("Problem Solving")
        st.write("At the heart of software development is problem-solving. I thrive in dissecting complex challenges "
                 "and architecting elegant solutions. Through careful analysis, creative thinking, and meticulous "
                 "implementation, I tackle problems head-on and deliver results that exceed expectations.")
        st.header("Continuous Learning")
        st.write("The tech landscape is ever-evolving, and I'm committed to staying ahead of the curve. I have an "
                 "insatiable appetite for learning, which drives me to explore new technologies and methodologies. "
                 "Whether it's mastering a new framework or staying updated with industry trends, I'm always up for "
                 "the challenge.")
    with right_column:
        st_lottie(lottie)


