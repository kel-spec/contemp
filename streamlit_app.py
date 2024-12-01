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
        **Leadership Skills**: 
        Leadership is one of the most crucial skills for personal and professional success. In this article, we dive deep into the importance of leadership qualities such as confidence, communication, and resilience. 
        Learn how to develop a growth mindset, inspire others, and become a true leader in your community and workplace. 

        **Know Your Rights**: 
        Understanding your legal rights is essential in all aspects of life. Whether in the workplace, at home, or in your personal life, knowing your rights ensures that you can protect yourself and seek justice when needed. 
        This article covers key areas such as workplace equality, reproductive rights, and protection from harassment, helping you understand how to navigate legal systems and assert your rights effectively.

        **Financial Independence**: 
        Achieving financial independence is a major milestone for many women, offering the freedom to make choices based on your desires and not on financial necessity. This article provides practical tips for budgeting, saving, investing, and building long-term wealth. 
        We’ll also explore how to break the gender pay gap and make confident financial decisions for a secure future.
    """)

elif page == "Success Stories":
    st.title("Inspiring Stories")
    st.write("""
        **Marie Curie**: 
        A pioneering scientist who not only made groundbreaking contributions to science but also defied societal expectations in a male-dominated field. Marie Curie’s resilience and dedication led her to become the first woman to win the Nobel Prize and the only person to win the Nobel Prize in two different scientific fields—Physics and Chemistry. Her story continues to inspire women in STEM fields today.

        **Malala Yousafzai**: 
        A passionate advocate for girls’ education and the youngest recipient of the Nobel Peace Prize. Malala’s story is one of incredible courage and determination, as she fought for her right to education despite facing grave danger and adversity. Her commitment to improving the lives of girls around the world has made her an icon of resilience and hope.

        **Your Story**: 
        Every woman has a story of triumph, resilience, and strength. Your experiences—whether in overcoming personal challenges, achieving goals, or breaking societal barriers—are powerful and inspiring. 
        Share your journey and connect with others who are walking similar paths. By sharing our stories, we support and uplift one another.
    """)

elif page == "Resources":
    st.title("Resources for Help")
    st.write("""
        **Mental Health Support**: 
        Mental health is a critical aspect of overall well-being. This section provides information on mental health services, counseling, support groups, and self-care practices. Whether you're seeking professional help or looking for ways to manage stress, anxiety, or depression, these resources can guide you toward healing and empowerment.

        **Legal Aid**: 
        Knowing where to turn for legal help is vital for every woman. This section offers guidance on how to access legal resources, including pro bono legal services, organizations that advocate for women’s rights, and advice on how to navigate legal issues such as domestic violence, discrimination, and child custody.

        **Workshops**: 
        Workshops are a fantastic way to gain new skills, build confidence, and network with other like-minded women. This section highlights upcoming workshops, seminars, and online courses that focus on personal growth, leadership development, and financial literacy. Stay tuned for opportunities to enhance your life and career.
    """)

elif page == "About Us":
    st.title("About Empower Women")
    st.write("""
        Empower Women is a global initiative created with the goal of educating, inspiring, and connecting women across the world. Our platform is dedicated to promoting gender equality and supporting women in all aspects of their lives, including career development, personal growth, mental health, and social change.

        We understand the importance of access to knowledge, opportunities, and community, which is why we provide resources such as articles, success stories, and practical tools designed to help women overcome barriers and achieve their full potential. 
        Our mission is to break down the societal limitations that hold women back and create an environment where every woman can thrive and contribute to a more equal world.

        Together, we can uplift one another and build a future where gender equality is not just a dream but a reality. Join us in this important movement as we work to create a world where all women have the resources, support, and opportunities they need to live fulfilling lives.
    """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
