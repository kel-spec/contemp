import streamlit as st
import random

# Set up the app title and custom layout
st.set_page_config(page_title="She Elevates", layout="wide")

# Apply custom styles for aesthetics
st.markdown("""
    <style>
    body {
        font-family: 'Verdana', sans-serif;
        background-color: #f7f8fa;
        color: #424874;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #2e2e54;
        margin-bottom: 15px;
    }
    .subsection-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        color: #424874;
    }
    .content {
        font-size: 18px;
        line-height: 1.6;
    }
    .sidebar {
        background-color: #fafafa;
        padding: 20px;
    }
    .st-expander {
        background-color: #ffffff;
        border: 1px solid #dedede;
        border-radius: 10px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Learn", "Success Stories", "Resources", "About Us"])

# Story storage
if "stories" not in st.session_state:
    st.session_state.stories = []

if page == "Home":
    st.markdown("<div class='title'>Welcome to She Elevates!</div>", unsafe_allow_html=True)
    st.write("""
        She Elevates is a platform dedicated to empowering women through knowledge, community, and inspiration. 
        Explore resources, connect with stories of resilience, and take the first step toward self-empowerment. 
        Together, let's rise to new heights!
    """)
    st.markdown("---")

    st.markdown("<div class='subsection-title'>Share Your Story</div>", unsafe_allow_html=True)
    user_story = st.text_area("What empowering story would you like to share?", placeholder="Type your story here...")
    if st.button("Submit Story"):
        if user_story.strip():
            st.session_state.stories.append(user_story.strip())
            st.success("Thank you for sharing your story! It will appear in the Success Stories section.")
        else:
            st.error("Please write your story before submitting.")

elif page == "Learn":
    st.markdown("<div class='title'>Educational Articles</div>", unsafe_allow_html=True)
    st.write("Expand the topics below to learn more.")

    with st.expander("Leadership Skills"):
        st.write("""
            Developing leadership skills is key for women to excel in their personal and professional lives. Learn 
            strategies to build confidence, manage teams, and navigate challenges.
            """)
        st.write("[Read Full Article](https://www.forbes.com/sites/forbeshumanresourcescouncil/2020/01/28/five-essential-leadership-skills-every-woman-should-develop/?sh=167a2ff34b93)")

    with st.expander("Know Your Rights"):
        st.write("""
            Empower yourself by understanding your rights in areas such as workplace equality, safety, and legal protections.
            """)
        st.write("[Learn More](https://www.aclu.org/issues/womens-rights)")

    with st.expander("Financial Independence"):
        st.write("""
            Gain control of your finances with budgeting tips, investment strategies, and advice on long-term financial planning.
            """)
        st.write("[Explore Financial Tips](https://www.investopedia.com/financial-literacy-for-women-5182212)")

elif page == "Success Stories":
    st.markdown("<div class='title'>Inspiring Success Stories</div>", unsafe_allow_html=True)
    if st.session_state.stories:
        for idx, story in enumerate(st.session_state.stories):
            st.write(f"**Story {idx + 1}:** {story}")
    else:
        st.write("No stories yet. Be the first to share your empowering journey!")

elif page == "Resources":
    st.markdown("<div class='title'>Resources for Empowerment</div>", unsafe_allow_html=True)
    st.write("Expand the sections below to access books, courses, and organizations dedicated to empowering women.")

    with st.expander("Books for Empowerment"):
        st.write("""
        - **Lean In** by Sheryl Sandberg: A guide to achieving leadership and breaking barriers in the workplace.
        - **The Moment of Lift** by Melinda Gates: Insights on the transformative power of empowering women globally.
        """)

    with st.expander("Courses & Learning Platforms"):
        st.write("""
        - [Coursera - Women in Leadership](https://www.coursera.org/learn/women-leadership): Develop skills to lead in any industry.
        - [Udemy - Financial Literacy for Women](https://www.udemy.com/course/financial-literacy-for-women/): Learn to take charge of your financial future.
        """)

elif page == "About Us":
    st.markdown("<div class='title'>About She Elevates</div>", unsafe_allow_html=True)
    st.write("""
        She Elevates is more than a platform; it's a movement dedicated to uplifting women worldwide. Through education, 
        inspiration, and community, we aim to help women unlock their full potential.
    """)
    st.markdown("---")
    st.markdown("<div class='subsection-title'>Mission</div>", unsafe_allow_html=True)
    st.write("""
        Our mission is to empower women through actionable resources and a supportive network that fosters growth, 
        resilience, and leadership.
    """)
    st.markdown("<div class='subsection-title'>Impact Tracker</div>", unsafe_allow_html=True)
    st.write(f"Pledges Taken: {random.randint(100, 1000)}")
    st.write(f"Stories Shared: {len(st.session_state.stories)}")
