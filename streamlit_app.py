import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page config as the first Streamlit command
st.set_page_config(page_title="Empowering Women", layout="wide")

# Load Lottie animation (example from an external source)
def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example Lottie animation URL (replace with your actual URL)
lottie_welcome = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_MlOtA4.json")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# Pages
if page == "Home":
    st.title("Welcome to Empower Women App!")
    st_lottie(lottie_welcome, height=300, key="welcome")
    st.write("""
        This app provides resources, stories, and insights to empower women worldwide.
        Explore articles, find help, and connect with inspiring stories!
    """)

elif page == "Articles":
    st.title("Educational Articles")
    st.write("""
        - **Leadership Skills**: [Read more](https://example.com)
        - **Know Your Rights**: [Read more](https://example.com)
        - **Financial Independence**: [Read more](https://example.com)
    """)

elif page == "Success Stories":
    st.title("Inspiring Stories")
    st.write("""
        1. **Marie Curie**: Pioneering scientist who broke gender barriers.
        2. **Malala Yousafzai**: Advocate for girls' education.
        3. **Your Story**: Share your inspiring journey!
    """)

elif page == "Resources":
    st.title("Resources for Help")
    st.write("""
        - **Mental Health Support**: [Support Organization](https://example.com)
        - **Legal Aid**: [Legal Help](https://example.com)
        - **Workshops**: [Upcoming Events](https://example.com)
    """)

elif page == "About Us":
    st.title("About Empower Women")
    st.write("""
        This app was created to educate, inspire, and connect women globally.
        Our mission is to promote gender equality and empower women in all aspects of life.
    """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
