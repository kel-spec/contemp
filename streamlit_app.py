import streamlit as st

# Page Configurations
st.set_page_config(page_title="She Elevates", layout="wide")

# Custom Styles for Aesthetic Appeal
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f7fb;
        color: #33475b;
    }
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #33475b;
        margin-bottom: 20px;
    }
    .sub-title {
        font-size: 28px;
        font-weight: bold;
        color: #5a6d8c;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .content {
        font-size: 18px;
        line-height: 1.6;
        color: #495e73;
    }
    .st-expander {
        background-color: #ffffff;
        border: 1px solid #dde1e7;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
    }
    .impact-box {
        background-color: #edf2f7;
        border: 1px solid #d2d6db;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("She Elevates Navigation")
page = st.sidebar.radio(
    "Explore:",
    ["Home", "Educational Resources", "Success Stories", "Community Resources", "About Us"]
)

# Home Page
if page == "Home":
    st.markdown("<div class='main-title'>Welcome to She Elevates!</div>", unsafe_allow_html=True)
    st.markdown(
        """
        She Elevates is a dynamic platform aimed at empowering women with resources, community support, 
        and inspiring success stories. We’re here to elevate, inspire, and empower!
        """
    )
    st.markdown("---")

    st.markdown("<div class='sub-title'>📢 Share Your Empowerment Story</div>", unsafe_allow_html=True)
    story_input = st.text_area("Tell us about your inspiring journey:")
    if st.button("Submit Your Story"):
        if story_input.strip():
            st.success("Thank you for sharing your story! Check the Success Stories section to see your contribution.")
        else:
            st.error("Please enter a story before submitting.")

    # Impact Section
    st.markdown("<div class='sub-title'>Our Impact</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='impact-box'>
            <b>500+</b> Women Empowered | <b>300+</b> Stories Shared | <b>200+</b> Free Courses Taken
        </div>
        """, 
        unsafe_allow_html=True
    )

# Educational Resources
elif page == "Educational Resources":
    st.markdown("<div class='main-title'>Educational Resources</div>", unsafe_allow_html=True)
    st.write("Expand the sections below to explore resources that can transform your personal and professional journey.")

    with st.expander("🔑 Leadership Skills"):
        st.write(
            """
            Discover actionable tips and strategies to enhance your leadership abilities, communicate effectively, 
            and inspire teams. Leadership is about influence, not just position.
            """
        )
        st.markdown("[Learn More](https://example.com/leadership-skills)")

    with st.expander("⚖️ Understanding Rights"):
        st.write(
            """
            Knowing your rights is key to empowerment. Understand workplace equality, legal protections, and 
            how to advocate for yourself effectively.
            """
        )
        st.markdown("[Read More](https://example.com/know-your-rights)")

    with st.expander("💸 Financial Independence"):
        st.write(
            """
            Take control of your financial future with practical advice on budgeting, investing, and building wealth 
            for long-term stability.
            """
        )
        st.markdown("[Explore Tips](https://example.com/financial-independence)")

# Success Stories
elif page == "Success Stories":
    st.markdown("<div class='main-title'>Inspiring Success Stories</div>", unsafe_allow_html=True)
    st.write("Read stories from women who have overcome challenges and achieved remarkable success.")
    sample_stories = [
        "Jane, a software engineer, shares her journey of breaking into tech and becoming a mentor for others.",
        "Anita, a small business owner, talks about starting her company from scratch and building a community-focused brand.",
        "Maria's story of resilience as she returned to school and earned her degree while raising a family."
    ]
    for story in sample_stories:
        st.markdown(f"- {story}")

# Community Resources
elif page == "Community Resources":
    st.markdown("<div class='main-title'>Community Resources</div>", unsafe_allow_html=True)
    st.write("Explore these valuable tools and communities to connect, grow, and thrive.")

    with st.expander("📚 Books to Empower"):
        st.write(
            """
            - *Lean In* by Sheryl Sandberg: A powerful guide to leadership.
            - *Becoming* by Michelle Obama: A memoir of strength and authenticity.
            """
        )

    with st.expander("🖥️ Online Courses"):
        st.write(
            """
            - [Coursera - Women in Leadership](https://coursera.org): Gain skills to lead effectively.
            - [Udemy - Financial Literacy for Women](https://udemy.com): Take charge of your financial health.
            """
        )

    with st.expander("🤝 Organizations to Join"):
        st.write(
            """
            - [LeanIn.org](https://leanin.org): A global community dedicated to empowering women.
            - [Girls Who Code](https://girlswhocode.com): Building future leaders in tech.
            """
        )

# About Us
elif page == "About Us":
    st.markdown("<div class='main-title'>About She Elevates</div>", unsafe_allow_html=True)
    st.write(
        """
        She Elevates is more than a platform; it’s a mission to inspire, connect, and empower women. Through our resources, 
        we aim to help every woman achieve her full potential.
        """
    )
    st.markdown("<div class='sub-title'>Our Mission</div>", unsafe_allow_html=True)
    st.write(
        """
        To foster growth, resilience, and leadership by providing women with tools and opportunities to thrive.
        """
    )
