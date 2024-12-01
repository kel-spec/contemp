import streamlit as st

# Set up the app title and sidebar
st.set_page_config(page_title="Empowering Women", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# Pages
if page == "Home":
    st.title("Welcome to Empower Women App!")
    st.write("""
        This app is a powerful platform designed to provide a wealth of resources, stories, and insightful guidance aimed at empowering women across the globe. 
        Our mission is to inspire and educate women of all ages and backgrounds, equipping them with the tools and knowledge they need to overcome challenges, unlock their potential, 
        and succeed in every aspect of life. Whether you're seeking to develop strong leadership skills, understand and assert your rights, improve your mental and physical well-being, 
        or simply connect with a community of like-minded women, this app is here to support and guide you.

        We believe that empowerment begins with education, self-awareness, and access to the right resources. Through empowering articles, success stories of women who have broken barriers, 
        and practical tips for navigating personal and professional challenges, we aim to create an environment where every woman can thrive. We are committed to fostering a space where 
        women can learn, grow, and collaborate, ultimately leading to the creation of a more equitable world where all women are able to achieve their goals, break down societal limitations, 
        and lead fulfilling lives.

        No matter where you are in your journey, whether you're looking to make informed decisions about your career, health, family, or finances, or seeking motivation from others who have paved the way, 
        you're in the right place. Here, you’ll find everything you need to empower yourself, advocate for your rights, and contribute to a global community of empowered women.
    """)

elif page == "Articles":
    st.title("Educational Articles")
    st.write("""
        - **Leadership Skills**: A comprehensive guide on how to build leadership qualities and make an impact.
        - **Know Your Rights**: Learn about your legal rights and how to assert them in personal and professional settings.
        - **Financial Independence**: Practical advice on managing finances, building wealth, and achieving financial freedom.
    """)

elif page == "Success Stories":
    st.title("Inspiring Stories")
    st.write("""
        1. **Marie Curie**: Pioneering scientist who broke gender barriers and made groundbreaking contributions to science.
        2. **Malala Yousafzai**: Advocate for girls' education who fought for the right of all children to receive an education.
        3. **Your Story**: Share your inspiring journey and be a role model for other women around the world.
    """)

elif page == "Resources":
    st.title("Resources for Help")
    st.write("""
        - **Mental Health Support**: Learn about organizations and services available to support your mental health.
        - **Legal Aid**: Discover the legal resources available to women in need of assistance.
        - **Workshops**: Find events, seminars, and workshops that can help you develop new skills and connect with others.
    """)

elif page == "About Us":
    st.title("About Empower Women")
    st.write("""
        This app was created to educate, inspire, and connect women globally. Our mission is to promote gender equality and empower women in all aspects of life.
        We aim to break down barriers, provide education, and inspire women to take charge of their futures, one step at a time. Through access to resources, articles, success stories, and a vibrant 
        community, we hope to make a meaningful impact in the lives of women everywhere.
    """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
