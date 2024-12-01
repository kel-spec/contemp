import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

# Function to load Lottie animations from a URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            st.warning(f"Failed to load animation from {url}. Check the URL.")
            return None
        return r.json()
    except Exception as e:
        st.error(f"An error occurred while fetching the animation: {e}")
        return None

# Load Lottie animations
lottie_welcome = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_hxdojphc.json")
lottie_resources = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
lottie_success = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_lz5xrpb1.json")

# Set up the app title and sidebar
st.set_page_config(page_title="Empowering Women", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# Pages
if page == "Home":
    st.title("Welcome to Empower Women App! 🌟")
    if lottie_welcome:
        st_lottie(lottie_welcome, height=300, key="welcome")
    else:
        st.write("Welcome animation could not be loaded.")
    st.write("""
        This app is dedicated to empowering women by providing resources, educational content, and inspiring stories. 
        Our goal is to create a safe and supportive space for women to learn, grow, and connect.
    """)

elif page == "Articles":
    st.title("Educational Articles 📚")
    st.write("""
        Discover articles to educate and empower:
        - **Leadership Skills**: [Read more](https://example.com)
        - **Know Your Rights**: [Read more](https://example.com)
        - **Financial Independence**: [Read more](https://example.com)
        - **Health & Wellness**: [Read more](https://example.com)
        - **Personal Growth**: [Read more](https://example.com)
    """)
    st.write("Stay informed and take charge of your life with these expert-curated articles!")

elif page == "Success Stories":
    st.title("Inspiring Stories 🌟")
    if lottie_success:
        st_lottie(lottie_success, height=300, key="success")
    st.write("""
        Be inspired by the journeys of remarkable women:
        1. **Marie Curie**: Pioneering scientist who broke gender barriers.
        2. **Malala Yousafzai**: Advocate for girls' education and Nobel laureate.
        3. **Rosa Parks**: Civil rights icon who sparked change.
        4. **Your Story**: Share your inspiring journey with us!
    """)
    st.write("Every story matters. Share yours to inspire others!")

elif page == "Resources":
    st.title("Resources for Help 🛠️")
    if lottie_resources:
        st_lottie(lottie_resources, height=300, key="resources")
    st.write("""
        Access essential resources to support and empower yourself:
        - **Mental Health Support**: [Find Support](https://example.com)
        - **Legal Aid Services**: [Get Help](https://example.com)
        - **Workshops and Events**: [Upcoming Events](https://example.com)
        - **Financial Planning Tools**: [Learn More](https://example.com)
    """)
    st.write("Empower yourself with the tools and support you need to thrive!")

elif page == "About Us":
    st.title("About Empower Women 🤝")
    st.write("""
        Our mission is to empower women globally through education, inspiration, and connection. 
        We believe in gender equality and strive to create opportunities for women in all aspects of life.
        
        **Core Values**:
        - Inclusivity
        - Education
        - Empowerment
        - Community
    """)
    st.write("Join us on this journey to make the world a better place for everyone!")

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
