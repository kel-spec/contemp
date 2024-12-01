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
        This app is a powerful platform designed to provide a wealth of resources, stories, and insightful guidance aimed at empowering women across the globe. Our mission is to inspire and educate women of all ages and backgrounds, equipping them with the tools and knowledge they need to overcome challenges, unlock their potential, and succeed in every aspect of life. Whether you're seeking to develop strong leadership skills, understand and assert your rights, improve your mental and physical well-being, or simply connect with a community of like-minded women, this app is here to support and guide you.We believe that empowerment begins with education, self-awareness, and access to the right resources. Through empowering articles, success stories of women who have broken barriers, and practical tips for navigating personal and professional challenges, we aim to create an environment where every woman can thrive. We are committed to fostering a space where women can learn, grow, and collaborate, ultimately leading to the creation of a more equitable world where all women are able to achieve their goals, break down societal limitations, and lead fulfilling lives.No matter where you are in your journey, whether you're looking to make informed decisions about your career, health, family, or finances, or seeking motivation from others who have paved the way, you're in the right place. Here, you’ll find everything you need to empower yourself, advocate for your rights, and contribute to a global community of empowered women.
    """)
    st.write("""
        **What We Offer:**
        - **Educational Articles**: Learn about essential topics like financial independence, leadership, and rights.
        - **Success Stories**: Get inspired by stories of incredible women who have broken barriers.
        - **Resources**: Find support through mental health resources, legal aid, and upcoming workshops.
    """)

elif page == "Articles":
    st.title("Educational Articles")
    st.write("""
        We believe that education is the key to empowerment. Here are some insightful articles to help you take charge of your future:
    """)
    st.write("""
        - **Leadership Skills**: Learn the skills that will help you lead in any situation. [Read more](https://example.com)
        - **Know Your Rights**: Understand the legal rights that protect women and how to assert them. [Read more](https://example.com)
        - **Financial Independence**: A guide to managing your finances and achieving financial freedom. [Read more](https://example.com)
        - **Work-Life Balance**: Tips on balancing your career, personal life, and self-care. [Read more](https://example.com)
        - **Mental Health Awareness**: Prioritize your mental health with these resources. [Read more](https://example.com)
    """)

elif page == "Success Stories":
    st.title("Inspiring Stories")
    st.write("""
        Real stories of women who have changed the world and made history! These women serve as an inspiration and reminder
        that we all have the power to break barriers and achieve greatness.
    """)
    st.write("""
        1. **Marie Curie**: Pioneering scientist who was the first woman to win a Nobel Prize and the only person to win
           Nobel Prizes in two different scientific fields.
        2. **Malala Yousafzai**: A Pakistani education activist and the youngest-ever Nobel Prize laureate. Malala advocates for
           girls' education and equality in education across the world.
        3. **Oprah Winfrey**: A media mogul who rose from humble beginnings to become one of the most influential women in the world,
           empowering millions with her media and philanthropic work.
        4. **Your Story**: Share your inspiring journey! Everyone has a story that can inspire others. Let’s build a community of
           women empowering one another.
    """)

elif page == "Resources":
    st.title("Resources for Help")
    st.write("""
        Empowering women goes beyond education. It's also about access to the right resources when needed. Here are some vital
        resources to support women in various aspects of life.
    """)
    st.write("""
        - **Mental Health Support**: Women's mental health is just as important as physical health. Get help through these
           [Support Organizations](https://example.com).
        - **Legal Aid**: Knowledge is power when it comes to protecting your rights. Find assistance through these
           [Legal Help Resources](https://example.com).
        - **Workshops & Networking**: Empowerment often comes through learning and connecting with others. Check out
           [Upcoming Workshops](https://example.com) where you can expand your skills and meet other like-minded women.
        - **Domestic Violence Support**: Find resources and hotlines that offer immediate assistance and long-term help for those in need.
           [Support and Hotline Information](https://example.com).
        - **Career Resources**: Whether you're seeking career advancement or transitioning into a new field, these resources will help.
           [Career Development](https://example.com).
    """)

elif page == "About Us":
    st.title("About Empower Women")
    st.write("""
        Empower Women is a platform designed to educate, inspire, and connect women globally. We believe in the power of knowledge,
        community, and support to overcome the barriers that women face in every part of the world.
    """)
    st.write("""
        **Our Mission**: To create an inclusive space where women can access educational resources, learn their rights, get inspired,
        and find support in overcoming challenges. 
    """)
    st.write("""
        **Why Empower Women?**
        Women all over the world face unique challenges, including social inequalities, limited access to education, and underrepresentation
        in various fields. Our mission is to address these issues by providing information, education, and community that foster empowerment
        for women of all backgrounds.
    """)
    st.write("""
        **How You Can Help:**
        - Share your story to inspire others.
        - Engage with the resources we provide to further your knowledge and well-being.
        - Support others by spreading the word about Empower Women.
    """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
