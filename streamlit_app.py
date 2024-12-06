import streamlit as st
import random

# Set up the app title and sidebar
st.set_page_config(page_title="She Elevates", layout="wide", page_icon="🌟")

# Custom CSS for aesthetics
st.markdown("""
    <style>
        body {
            background-color: #f9f7fc;
        }
        .title {
            font-family: 'Helvetica', sans-serif;
            font-size: 40px;
            color: #4c1d95;  
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .quote {
            font-style: italic;
            font-size: 20px;
            text-align: center;
            color: #6d28d9;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: #9ca3af;
        }
        .btn {
            background-color: #6d28d9;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #4c1d95;
        }
        .success-story {
            background-color: #e0e7ff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌟 Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "Community", "About Us"])

# Store user pledges and quiz scores (for simplicity, in session state)
if "stories" not in st.session_state:
    st.session_state.stories = []
if "pledges" not in st.session_state:
    st.session_state.pledges = []
if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = []

# Pages
if page == "Home":
    st.markdown('<div class="title">Welcome to She Elevates!</div>', unsafe_allow_html=True)
    st.write("""
        🌟 Empowering women worldwide through education, inspiration, and community engagement. Let's rise together!
    """)

    # Quote of the Day
    st.markdown('<div class="quote">"Empowered women empower the world." – Unknown</div>', unsafe_allow_html=True)

    # Daily Empowerment Challenge
    challenges = [
        "Write down 3 things you're grateful for today.",
        "Read an article from our resources section.",
        "Share an empowering story with a friend.",
        "Set a small goal to achieve today.",
        "Compliment another woman today."
    ]
    st.subheader("🌟 Daily Challenge")
    st.write(random.choice(challenges))

elif page == "Articles":
    st.title("📚 Educational Articles")
    st.write("""
        Discover articles on leadership, financial independence, and overcoming societal barriers.
        [Visit our curated list of articles](#resources).
    """)

elif page == "Success Stories":
    st.title("💪 Inspiring Success Stories")
    st.write("Celebrate the achievements of incredible women.")

    # Display user-submitted stories
    if st.session_state.stories:
        for idx, story in enumerate(st.session_state.stories):
            st.markdown(f'<div class="success-story"><strong>Story {idx + 1}:</strong> {story}</div>', unsafe_allow_html=True)
    else:
        st.write("No stories yet. Be the first to share your empowering story!")

    # Share your story
    st.subheader("📝 Share Your Story")
    user_story = st.text_area("What's your empowering story?", placeholder="Type your story here...")
    if st.button("Submit Story"):
        if user_story:
            st.session_state.stories.append(user_story)
            st.success("Thank you for sharing your story! It will appear above.")
        else:
            st.error("Please write your story before submitting.")

elif page == "Resources":
    st.title("🔗 Resources for Empowerment")
    st.write("""
        A curated list of books, courses, and organizations to inspire and support you.
    """)

elif page == "Community":
    st.title("🤝 Community Engagement")
    st.write("Join challenges, take quizzes, and share pledges.")

    # Quiz
    st.subheader("📝 Empowerment Quiz")
    question = "Which leadership quality resonates with you the most?"
    options = ["Empathy", "Confidence", "Vision", "Resilience"]
    choice = st.radio(question, options)
    if st.button("Submit Quiz Answer"):
        st.session_state.quiz_scores.append(choice)
        st.success(f"Thank you for participating! You chose: {choice}.")

    # Pledges
    st.subheader("🌟 Make Your Empowerment Pledge")
    pledge = st.text_input("What pledge would you like to make?")
    if st.button("Submit Pledge"):
        if pledge:
            st.session_state.pledges.append(pledge)
            st.success(f"Thank you for your pledge: '{pledge}'!")
        else:
            st.error("Please enter your pledge before submitting.")

    # Display pledges
    st.write("💬 **Recent Pledges:**")
    if st.session_state.pledges:
        for idx, p in enumerate(st.session_state.pledges[-5:], 1):
            st.write(f"{idx}. {p}")
    else:
        st.write("No pledges yet. Be the first to make one!")

elif page == "About Us":
    st.title("💡 About She Elevates")
    st.write("""
        Empowering women to achieve their fullest potential through education and community support.
    """)

    # Team Acknowledgment
    st.write("**Team:** Michael Lagunday & Lance Salamanca")
