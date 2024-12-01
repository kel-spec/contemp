import streamlit as st
from PIL import Image

# Set up the app title and sidebar
st.set_page_config(page_title="Empowering Women", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Articles", "Success Stories", "Resources", "About Us"])

# Load Images
home_image = "home_image.jpg"  # Replace with your image file
leadership_image = "leadership.jpg"  # Replace with your image file
inspiration_image = "inspiration.jpg"  # Replace with your image file
resources_image = "resources.jpg"  # Replace with your image file

# Pages
if page == "Home":
    st.image(home_image, use_column_width=True)
    st.title("Welcome to Empower Women App!")
    st.write("""
        **Empower Women** is a platform dedicated to inspiring and educating individuals about gender equality.
        Here, you'll find:
        - Educational articles on leadership and financial independence.
        - Stories of incredible women who changed the world.
        - Resources to support women in need.
    """)
    st.balloons()  # Add a simple animation for welcoming users.

elif page == "Articles":
    st.title("Educational Articles")
    st.image(leadership_image, caption="Leadership Skills for Women", use_column_width=True)
    st.write("""
        Gain insights from curated articles to empower your journey:
        - **Leadership Skills**: [10 Skills Every Woman Should Master](https://example.com)
        - **Know Your Rights**: [A Comprehensive Guide](https://example.com)
        - **Financial Independence**: [Steps to Take Charge](https://example.com)
    """)
    st.info("💡 *Discover, Learn, and Lead!*")  # Add a callout box for extra emphasis.

elif page == "Success Stories":
    st.title("Inspiring Stories")
    st.image(inspiration_image, caption="Women Who Inspire Us", use_column_width=True)
    st.write("""
        Explore stories of courage, determination, and leadership:
        1. **Marie Curie**: The first woman to win a Nobel Prize.
        2. **Malala Yousafzai**: Global advocate for girls' education.
        3. **Your Story**: Share your inspiring journey with us. We would love to feature it!
    """)
    st.write("👩‍🎓 *Empower yourself with inspiration from these amazing women!*")

elif page == "Resources":
    st.title("Resources for Help")
    st.image(resources_image, caption="Support and Assistance", use_column_width=True)
    st.write("""
        Access support resources and tools for women:
        - **Mental Health Support**: [Find help near you](https://example.com)
        - **Legal Aid**: [Know your rights and get assistance](https://example.com)
        - **Workshops and Webinars**: [Upcoming events for personal growth](https://example.com)
    """)
    st.warning("⚠️ *If you or someone you know needs immediate help, please contact local authorities or a trusted organization.*")

elif page == "About Us":
    st.title("About Empower Women")
    st.write("""
        This app was created to educate, inspire, and connect women worldwide.
        Our mission is to:
        - Promote gender equality.
        - Provide tools for personal and professional growth.
        - Create a supportive community for women everywhere.
    """)
    st.image(home_image, caption="Together, we create change.", use_column_width=True)
    st.markdown("""
        ### Meet the Team
        - **Founder**: Jane Doe - Advocate for women's rights.
        - **Contributors**: Amazing individuals dedicated to empowering women globally.
    """)

# Footer
st.sidebar.write("Made with ❤️ using Streamlit")
