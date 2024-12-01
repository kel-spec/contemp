import streamlit as st

# Set up the app title and sidebar
st.set_page_config(page_title="She Elevates", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# Story storage (for simplicity, we use session state)
if "stories" not in st.session_state:
    st.session_state.stories = []

# Pages
if page == "Home":
    st.title("Welcome to She Elevates!")
    st.write("""
        Welcome to She Elevates, a platform designed to empower and support women worldwide. We are dedicated to providing
        resources, inspiration, and a sense of community that can help you thrive personally, professionally, and emotionally.

        **What We Offer:**
        - **Leadership Skills**: Leadership is crucial for women to excel in any field. Our resources cover the key aspects of
          leadership, from developing confidence to managing teams and navigating obstacles in the workplace. Whether you're
          looking to lead in your career, community, or personal life, we provide the tools you need to succeed.
        
        - **Know Your Rights**: Understanding your rights as a woman is empowering. Our educational articles explain legal rights
          in areas such as workplace equality, personal safety, and reproductive rights. Knowledge of your rights equips you to
          protect yourself and advocate for positive change in your life and society.
        
        - **Financial Independence**: Financial freedom gives women the power to make informed choices and live life on their
          terms. We provide practical advice on budgeting, saving, investing, and managing debt to help you achieve long-term
          financial independence. You can take control of your financial future, whether you're just starting or planning for
          retirement.
        
        - **Inspiring Stories**: Stories from other women can inspire, motivate, and show us that overcoming obstacles is
          possible. Our collection of success stories highlights women who have turned adversity into triumph, whether in
          business, education, or personal achievements. These stories offer invaluable insights into resilience, determination,
          and the power of perseverance.
        
        **Join Our Movement:**
        At She Elevates, we believe that empowering women goes beyond information—it’s about creating a supportive network.
        Together, we can overcome challenges and lift each other up to reach new heights. Let’s rise as one!
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

elif page == "Articles":
    st.title("Educational Articles")
    st.write("""
        This section is dedicated to providing you with informative articles that can help you develop important skills,
        gain knowledge about your rights, and lead a financially independent life.

        - **Leadership Skills**: Effective leadership is essential for women who want to achieve their goals and make an impact.
          Our article on leadership skills covers various strategies to build confidence, inspire others, and manage challenges
          in leadership positions. By learning from successful female leaders, you'll discover how to navigate challenges and
          unlock your leadership potential.

        - **Know Your Rights**: Women's rights are fundamental to ensuring equality and fairness in society. This article
          delves into various legal rights that every woman should be aware of, including workplace protections, family and
          reproductive rights, and personal safety laws. Knowing your rights helps you navigate life with confidence and
          empowers you to stand up for yourself and others.

        - **Financial Independence**: Achieving financial independence is a transformative step towards personal empowerment.
          This article offers practical advice on budgeting, saving, and investing. It provides insight into how you can
          create a financial plan that allows you to live independently and confidently. Whether you're just starting or
          seeking to enhance your financial literacy, this article will guide you in making informed financial decisions.
    """)
    
    # Adding sample articles with links
    st.subheader("Featured Articles:")
    st.markdown("""
        - [The Importance of Women in Leadership Roles](https://www.example.com/article1) - This article explores the
          impact of women in leadership positions, discussing the benefits and challenges of female leadership.
        - [How to Achieve Financial Independence](https://www.example.com/article2) - A step-by-step guide to becoming
          financially independent, from saving to investing smartly.
        - [Understanding Your Legal Rights](https://www.example.com/article3) - A comprehensive overview of the legal
          rights women should know to protect themselves in various life situations.
    """)

elif page == "Success Stories":
    st.title("Inspiring Success Stories")
    st.write("""
        Welcome to our Success Stories page, where we showcase women who have overcome significant challenges, achieved
        remarkable success, and made a positive impact on their communities and industries. These stories are a testament
        to the strength, resilience, and determination that every woman holds within herself.

        Each story is a powerful reminder that success is not defined by one’s circumstances but by the courage to
        overcome obstacles and pursue one's dreams. Whether it's overcoming financial hardship, breaking societal barriers,
        or making a change in the world, these stories will inspire you to take the next step in your own journey of success.

        **Here are some of the stories we’ve collected so far:**
    """)

    # Display the stories
    if st.session_state.stories:
        for idx, story in enumerate(st.session_state.stories):
            st.write(f"**Story {idx + 1}:** {story}")
    else:
        st.write("No stories yet. Be the first to share your empowering story!")

elif page == "Resources":
    st.title("Resources for Help")
    st.write("""
        We understand that empowerment also requires access to resources. Whether you're seeking mental health support,
        legal aid, or financial advice, this page is dedicated to providing you with the tools and organizations that
        can help you take the next steps towards achieving your goals.

        - **Mental Health Support**: Mental health is a crucial aspect of overall well-being, and taking care of your
          emotional health is essential. This section offers a list of hotlines, counseling services, and online platforms
          dedicated to supporting women's mental health. From managing stress to dealing with life changes, these resources
          are here to help you maintain emotional balance and resilience.
        
        - **Legal Aid**: Legal support is vital for women facing discrimination, harassment, or family issues. We provide a
          comprehensive list of organizations that offer legal advice and services for women in need. These resources can
          help you navigate legal challenges, understand your rights, and find the appropriate legal representation when
          necessary.

        - **Workshops and Events**: Personal development and skill-building are essential components of empowerment. We
          highlight workshops, events, and webinars that offer opportunities for learning, growth, and networking. These
          events cover a wide range of topics, including leadership development, financial literacy, and self-care, helping
          women access the knowledge and connections they need to thrive.
    """)

elif page == "About Us":
    st.title("About She Elevates")
    st.write("""
        She Elevates is more than just a platform—it's a movement. We are dedicated to empowering women through
        education, inspiration, and community support. Our mission is to provide resources, share empowering stories,
        and create a space where women can come together to support and uplift one another.

        **Our Mission:**
        At She Elevates, we believe that empowering women is the key to creating a more just and equal world. Through
        education, we help women develop the skills they need to succeed in all areas of life. Whether it's gaining financial
        independence, learning to advocate for their rights, or developing leadership skills, we provide the tools for women
        to thrive. Our mission is to provide a platform that allows women to not only access valuable resources but to
        also feel supported and empowered by a community of like-minded individuals.

        **Why We Do It:**
        We believe that empowering women leads to stronger families, communities, and societies. By providing women with
        the resources they need to succeed, we help them make informed choices, become leaders, and live fulfilling lives.
        She Elevates is committed to creating a global movement where women rise together, breaking barriers and achieving
        their full potential.
    """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
