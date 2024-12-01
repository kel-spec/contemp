import streamlit as st
import json
import os

# Set up the app title and sidebar
st.set_page_config(page_title="She Elevates", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# File path for storing stories
STORY_FILE = "stories.json"

# Load stories from the file if it exists
def load_stories():
    if os.path.exists(STORY_FILE):
        with open(STORY_FILE, "r") as f:
            return json.load(f)
    return []

# Save stories to the file
def save_stories(stories):
    with open(STORY_FILE, "w") as f:
        json.dump(stories, f)

# Load stories at the start
if "stories" not in st.session_state:
    st.session_state.stories = load_stories()

# Pages
if page == "Home":
    st.title("Welcome to She Elevates!")
    st.write(""" 
        This app provides resources, stories, and insights to empower women worldwide. Our goal is to
        inspire and educate, fostering an environment where women can thrive in all aspects of life. Whether
        you're looking to build leadership skills, understand your rights, or connect with other women, you're
        in the right place.
        """)
    
    # Button to share a story
    st.subheader("Share Your Story")
    user_story = st.text_area("What's your empowering story?", placeholder="Type your story here...")

    if st.button("Submit Story"):
        if user_story:
            st.session_state.stories.append(user_story)
            save_stories(st.session_state.stories)  # Save stories to file
            st.success("Thank you for sharing your story! It will appear in the Success Stories tab.")
        else:
            st.error("Please write your story before submitting.")

elif page == "Success Stories":
    st.title("Inspiring Success Stories")
    st.write("""
        These are the stories of women who have overcome challenges, achieved greatness, and made a difference.
        Whether it's in business, education, or activism, these stories show that with determination and courage, women
        can achieve anything. Feel free to share your own story and inspire others!
        """)

    # Display the stories
    if st.session_state.stories:
        for idx, story in enumerate(st.session_state.stories):
            st.write(f"**Story {idx + 1}:** {story}")
    else:
        st.write("No stories yet. Be the first to share your empowering story!")

elif page == "Articles":
    st.title("Educational Articles")
    st.write(""" 
        - **Leadership Skills**: Building leadership skills is essential for women who want to take charge of their
          careers and lives. Our article provides insights on developing leadership qualities, managing teams,
          and staying resilient in the face of challenges. These are the skills that will set you apart in any field.
        - **Know Your Rights**: Knowledge is power. Understanding your rights in different contexts, from the workplace
          to personal matters, is key to maintaining control over your life. In this section, we explore the importance
          of legal awareness and how knowing your rights can safeguard you against potential challenges.
        - **Financial Independence**: Financial independence is crucial for women, as it provides the freedom to make
          choices, invest in your future, and live life on your own terms. We offer actionable steps, resources, and
          advice to help you achieve financial security, from budgeting tips to investment strategies.
    """)

elif page == "Resources":
    st.title("Resources for Help")
    st.write(""" 
        - **Mental Health Support**: Mental well-being is an essential part of overall health. We've compiled a list
          of organizations and resources that provide mental health support to women, including hotlines, counseling
          services, and online platforms for emotional well-being.
        - **Legal Aid**: Knowing where to turn for legal support can make all the difference. We provide resources for
          legal aid services, from family law and harassment cases to employment discrimination. Empower yourself with
          the knowledge of your legal options.
        - **Workshops and Events**: Attend workshops, webinars, and events that promote women's empowerment, skill-building,
          and personal growth. These resources are designed to equip women with the tools they need to thrive in
          various aspects of life, including professional development, self-care, and leadership.
    """)

elif page == "About Us":
    st.title("About She Elevates")
    st.write(""" 
        She Elevates is a platform created with the vision of empowering women across the globe. We strive to create
        a world where women feel supported, educated, and inspired. Our mission is to provide valuable resources,
        share inspiring stories, and foster an environment where women can lead, achieve, and thrive.
        """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
