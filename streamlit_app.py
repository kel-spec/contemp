import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_welcome = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_hxdojphc.json")
lottie_articles = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_vybwn7df.json")
lottie_resources = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_Stt1R9.json")
lottie_about = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_m9frht1p.json")

# Set up the app title and sidebar
st.set_page_config(page_title="Empowering Women", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# Pages
if page == "Home":
    st.title("Welcome to Empower Women App! 🌟")
    st_lottie(lottie_welcome, height=300, key="welcome")
    st.write("""
        This app is dedicated to empowering women by providing resources, educational content, and inspiring stories. 
        Our goal is to create a safe and supportive space for women to learn, grow, and connect.
    """)
    st.subheader("Why Empower Women?")
    st.write("""
        - **Equality**: Empowering women promotes social justice and equal opportunities for all.
        - **Leadership**: When women lead, communities and organizations thrive.
        - **Support**: Build a network of resources to help women achieve their goals.
    """)

elif page == "Articles":
    st.title("Educational Articles 📚")
    st_lottie(lottie_articles, height=250, key="articles")
    st.write("""
        Explore a curated selection of articles aimed at educating and empowering women:
        - **Leadership Skills**: Tips and strategies for women to excel in leadership roles. [Read more](https://example.com)
        - **Know Your Rights**: A guide to understanding your legal rights and protections. [Read more](https://example.com)
        - **Financial Independence**: Practical advice for achieving economic freedom. [Read more](https://example.com)
    """)
    st.write("💡 **Knowledge is power. Start your journey today!**")

elif page == "Success Stories":
    st.title("Inspiring Stories 🌟")
    st.write("""
        Discover the journeys of extraordinary women who made a difference:
        - **Marie Curie**: The first woman to win a Nobel Prize, breaking barriers in science.
        - **Malala Yousafzai**: A powerful advocate for girls' education and the youngest Nobel laureate.
        - **Your Story**: Share your own journey to inspire others and contribute to this community.
    """)
    st.subheader("Share Your Story")
    st.write("""
        We believe every story matters. If you have an inspiring journey, let us know!
        Together, we can amplify voices and create a ripple effect of empowerment.
    """)

elif page == "Resources":
    st.title("Resources for Help 🤝")
    st_lottie(lottie_resources, height=250, key="resources")
    st.write("""
        Access vital resources to support you in various aspects of life:
        - **Mental Health Support**: Connect with counselors and therapists. [Find help](https://example.com)
        - **Legal Aid**: Guidance for navigating legal challenges. [Learn more](https://example.com)
        - **Workshops and Events**: Upcoming opportunities for personal and professional growth. [Join here](https://example.com)
    """)
    st.info("💬 **Have questions? Reach out to these resources for assistance!**")

elif page == "About Us":
    st.title("About Empower Women 💡")
    st_lottie(lottie_about, height=250, key="about")
    st.write("""
        The Empower Women App is built to educate, inspire, and connect women around the world. 
        Our mission is to:
        - Promote **gender equality**.
        - Provide **support and resources** for personal and professional growth.
        - Celebrate the achievements of women in all fields.
    """)
    st.write("💖 **Together, we can create a brighter and more inclusive future.**")

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
