import streamlit as st
import streamlit.components.v1 as components
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

        **What We Offer:**
        - **Leadership Skills:** Whether you're starting your career or looking to enhance your leadership abilities,
          we provide resources to help you lead with confidence.
        - **Know Your Rights:** Understanding your rights is the first step to securing your safety and well-being.
          Our articles help you navigate the complexities of your legal rights.
        - **Financial Independence:** Achieving financial independence is empowering, and we share tips and guidance
          to help you take control of your finances.
        - **Inspiring Stories:** Read empowering stories from women who have overcome challenges, broken barriers,
          and made a difference. These stories serve as a source of inspiration for all.
        
        **Join Us!**
        Empowerment is not just about knowledge, but about community. Join other women in this journey of
        self-discovery, leadership, and resilience. Together, we rise.
    """)

    # Button to share a story
    st.subheader("Share Your Story")
    user_story = st.text_area("What's your empowering story?", placeholder="Type your story here...")

    if st.button("Submit Story"):
        if user_story:
            st.session_state.stories.append(user_story)
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
          [Read More: Leadership Skills](https://www.imd.org/blog/leadership/women-in-leadership/)

        - **Know Your Rights**: Knowledge is power. Understanding your rights in different contexts, from the workplace
          to personal matters, is key to maintaining control over your life. In this section, we explore the importance
          of legal awareness and how knowing your rights can safeguard you against potential challenges.
          [Read More: Know Your Rights](https://www.aclu.org/issues/womens-rights)

        - **Financial Independence**: Financial independence is crucial for women, as it provides the freedom to make
          choices, invest in your future, and live life on your own terms. We offer actionable steps, resources, and
          advice to help you achieve financial security, from budgeting tips to investment strategies.
          [Read More: Financial Independence](https://www.investopedia.com/financial-literacy-for-women-5182212)

        - **Overcoming Gender Bias**: Gender bias is still a significant challenge in many aspects of life, especially in
          professional settings. Learn about strategies to combat unconscious bias, promote equality, and help break
          down barriers that hold women back.
          [Read More: Overcoming Gender Bias](https://www.womenforwomen.org/learn/gender-bias)

        - **Work-Life Balance**: Achieving work-life balance can be particularly challenging for women, especially in high
          demanding jobs or family settings. In this article, we provide tips for managing work, personal life, and
          self-care to ensure long-term well-being.
          [Read More: Work-Life Balance](https://www.forbes.com/sites/forbeshumanresourcescouncil/2021/02/23/five-strategies-for-improving-your-work-life-balance/?sh=65eb6c9a6f4e)

        - **Breaking the Glass Ceiling**: The glass ceiling is a term used to describe the invisible barriers that prevent
          women from advancing to the highest levels in their careers. This article discusses how women can break these
          barriers and reach their full potential.
          [Read More: Breaking the Glass Ceiling](https://www.mckinsey.com/featured-insights/gender-equality/why-women-are-still-underrepresented-in-leadership-positions)

        - **Self-Care for Women**: Self-care is not selfish; it’s essential. Women often take on many roles, and it can be
          easy to forget about personal well-being. This article highlights the importance of self-care, offering tips on
          physical, mental, and emotional health.
          [Read More: Self-Care for Women](https://www.psychologytoday.com/us/basics/self-care)

        - **Building a Support Network**: A strong support network is essential for personal and professional growth. Learn
          how to build relationships with mentors, colleagues, and other women who can offer support, advice, and
          encouragement.
          [Read More: Building a Support Network](https://www.inc.com/guides/2010/06/defining-your-support-system.html)
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

        **Our Mission:**
        To empower women with the knowledge, skills, and resources they need to live fulfilling and successful lives.
        By providing educational content, legal advice, financial resources, and mental health support, we aim to
        create a more equal and just world for women.

        **Why We Do It:**
        Empowering women means creating a world where women have equal opportunities to succeed, make choices, and
        contribute to society in meaningful ways. Through She Elevates, we hope to inspire a global movement where
        women support and uplift each other.

        Join us in making the world a better place for women everywhere!
    """)

components.html("""
    <html>
        <head>
            <style>
                body {
                    background-color: #f0f0f0;
                }
                .fade {
                    opacity: 0;
                    transition: opacity 1s ease-in-out;
                }
                .fade.show {
                    opacity: 1;
                }
            </style>
        </head>
        <body>
            <div id="content" class="fade">Your content here</div>
            <script>
                window.onload = () => {
                    document.getElementById('content').classList.add('show');
                };
            </script>
        </body>
    </html>
""", height=600)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
