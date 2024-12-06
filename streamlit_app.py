import streamlit as st
import random

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
    
    # Add an introductory banner image or header
    st.image("https://www.cloud-awards.com/wp-content/uploads/2024/03/AdobeStock_415181377-scaled.jpeg", caption="Empowerment in Action", use_column_width=True)
    
    st.write("""
        Welcome to She Elevates, a platform designed to empower and support women worldwide. Our mission is to provide 
        resources, inspiration, and a sense of community to help you thrive personally, professionally, and emotionally.
    """)

    # Create collapsible sections for detailed content
    with st.expander("What We Offer"):
        st.write("""
            - **Leadership Skills**: Resources to help women develop confidence, manage teams, and navigate workplace challenges.
            - **Know Your Rights**: Educational articles about workplace equality, personal safety, and reproductive rights.
            - **Financial Independence**: Practical advice on budgeting, saving, and investing for long-term financial security.
            - **Inspiring Stories**: Real stories from women who turned challenges into opportunities for success.
        """)

    # Add a video section for user engagement
    st.subheader("Get Inspired")
    st.video("https://youtu.be/VF4ZyJRUxk8")  # Replace with a relevant empowerment video

    # Story-sharing interactive feature
    st.subheader("Share Your Story")
    st.write("Your voice matters! Share your empowering story and inspire others.")
    user_story = st.text_area("What's your empowering story?", placeholder="Type your story here...")
    if st.button("Submit Story"):
        if user_story:
            st.session_state.stories.append(user_story)
            st.success("Thank you for sharing your story! It will appear in the Success Stories tab.")
        else:
            st.error("Please write your story before submitting.")

    # Add a motivational quote carousel
    st.subheader("Words to Empower")
    quotes = [
        "“There is no limit to what we, as women, can accomplish.” – Michelle Obama",
        "“I am not free while any woman is unfree, even when her shackles are very different from my own.” – Audre Lorde",
        "“A woman with a voice is, by definition, a strong woman.” – Melinda Gates",
        "“The most courageous act is still to think for yourself. Aloud.” – Coco Chanel"
    ]
    st.info(random.choice(quotes))  # Randomly display one quote per refresh
    
    # CTA button to explore the platform further
    st.write("Ready to start your journey with us?")
    st.button("Explore Articles", on_click=lambda: st.experimental_set_query_params(page="Articles"))
    
elif page == "Articles":
    st.title("Explore Empowering Articles")

    # Add a banner image for the Articles page
    st.image("https://www.stackumbrella.com/wp-content/uploads/2024/07/Women-Empowerment_11zon.jpg", caption="Stay Informed, Stay Empowered", use_column_width=True)

    st.write("""
        Dive into a collection of articles designed to educate, inspire, and empower. Explore topics ranging 
        from leadership to financial independence, and discover insights to elevate your journey.
    """)

    # Add collapsible categories for easier navigation
   st.subheader("Browse Categories")

    with st.expander("Leadership Skills"):
    st.write("""
        Learn about strategies to develop confidence, lead teams effectively, and grow as a professional leader.
        - [Breaking the Glass Ceiling](https://www.inc.com/guides/2010/06/defining-your-leadership-style.html)
        - [Overcoming Workplace Bias](https://www.mckinsey.com/featured-insights/diversity-and-inclusion/why-diversity-matters)
        - [Top Leadership Books for Women](https://www.amazon.com/Best-Sellers-Books-Leadership-Development/zgbs/books/2646)
    """)

    with st.expander("Know Your Rights"):
    st.write("""
        Stay informed about your rights and navigate personal and professional challenges confidently.
        - [Understanding Workplace Rights](https://www.eeoc.gov/what-you-should-know-about-workplace-rights)
        - [Legal Support for Women](https://www.nwlc.org/our-issues/)
        - [Feminist Movements to Know](https://www.theguardian.com/world/2019/jul/16/feminism-global-activism-gender-equality)
    """)

    with st.expander("Financial Independence"):
    st.write("""
        Master your finances with practical advice tailored for women.
        - [Building a Sustainable Budget](https://www.investopedia.com/articles/personal-finance/050515/how-create-budget-you-can-stick.asp)
        - [Smart Investment Strategies](https://www.investopedia.com/articles/financial-advisors/122215/7-best-investment-strategies-women.asp)
        - [Emergency Fund Essentials](https://www.forbes.com/advisor/personal-finance/how-to-build-an-emergency-fund/)
    """)

    # Highlight featured articles with links
    st.subheader("Featured Articles")
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://www.thebalancemoney.com/thmb/k1vstgDS1GTccOgxbbHKuyTxKRQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/top-leadership-skills-2063782_final-5b3e6be646e0fb0036272f42-5bbf7e0246e0fb0026d6416a.png", caption="5 Tips to Elevate Your Leadership Skills")
        st.markdown("[Read Article](https://www.investopedia.com/articles/pf/12/leadership-skils.asp)", unsafe_allow_html=True)
    
    with col2:
        st.image("https://media.licdn.com/dms/image/v2/D5612AQEUFRgI--hEtg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1730472147640?e=2147483647&v=beta&t=geFR7XCLgWoTd0MYszLKVz7QazKokK7Yj8Lz8Brr2Os", caption="Financial Freedom: A Guide for Women")
        st.markdown("[Read Article](https://globalwomanmagazine.com/your-guide-to-financial-freedom/)", unsafe_allow_html=True)

    # Feedback collection for articles
    st.subheader("Your Thoughts Matter")
    st.write("We value your feedback. Let us know how these articles help you or suggest topics you'd like to see.")
    feedback = st.text_area("Write your feedback here...", placeholder="Share your thoughts...")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback! Your input helps us grow.")
        else:
            st.error("Please enter your feedback before submitting.")

elif page == "Success Stories":
    st.title("Inspiring Success Stories")
    st.write("""
        Welcome to our Success Stories page, where we showcase women who have overcome significant challenges, achieved
        remarkable success, and made a positive impact on their communities and industries. These stories are a testament
        to the strength, resilience, and determination that every woman holds within herself.

        Each story is a powerful reminder that success is not defined by one’s circumstances but by the courage to
        overcome obstacles and pursue one's dreams. Whether it's overcoming financial hardship, breaking societal barriers,
        or making a change in the world, these stories will inspire you to take the next step in your own journey of success.

        *Here are some of the stories we’ve collected so far:*
    """)

    # Display the stories
    if st.session_state.stories:
        for idx, story in enumerate(st.session_state.stories):
            st.write(f"*Story {idx + 1}:* {story}")
    else:
        st.write("No stories yet. Be the first to share your empowering story!")

elif page == "Resources":
    st.title("Resources for Empowerment")
    
    st.write("""
        She Elevates provides a curated list of resources to empower women across various aspects of life. Whether you're
        looking for educational materials, financial advice, or ways to get involved with non-profits, you'll find it here.
    """)

    # Books Section - Collapsible
    with st.expander("Books for Empowerment"):
        st.write("""
            Explore these insightful books that discuss women's empowerment, leadership, financial independence, and more.
        """)

        books = [
            ("*Lean In: Women, Work, and the Will to Lead*", "Sheryl Sandberg's groundbreaking book that encourages women to pursue leadership roles and challenges gender inequality in the workplace."),
            ("*The Moment of Lift: How Empowering Women Changes the World*", "Melinda Gates' inspiring call to action for improving women's health, education, and economic opportunities."),
            ("*Women Who Run with the Wolves*", "Clarissa Pinkola Estés shares the powerful stories of wild women and their untamed spirit, encouraging women to reclaim their power."),
            ("*The Power of Now: A Guide to Spiritual Enlightenment*", "Eckhart Tolle's transformative teachings on mindfulness and self-awareness, helping women to focus on the present moment.")
        ]
        
        for title, description in books:
            st.subheader(title)
            st.write(description)
    
    # Websites Section - Collapsible
    with st.expander("Websites for Support and Resources"):
        st.write("""
            These websites offer valuable resources, advocacy, and education about women's rights, health, and empowerment.
        """)

        websites = [
            ("[UN Women](https://www.unwomen.org)", "The United Nations' global champion for gender equality, providing resources and support for women's empowerment worldwide."),
            ("[National Organization for Women](https://now.org)", "NOW is the largest organization of feminist activists in the United States, advocating for equal rights and justice for women."),
            ("[Global Fund for Women](https://www.globalfundforwomen.org)", "A global champion for the rights of women and girls, funding organizations working on gender equality across the world."),
            ("[Women for Women International](https://www.womenforwomen.org)", "An organization that helps women survivors of war and conflict to rebuild their lives and become leaders in their communities.")
        ]
        
        for site, description in websites:
            st.subheader(site)
            st.write(description)
    
    # Non-Profit Organizations Section - Collapsible
    with st.expander("Non-Profit Organizations Supporting Women"):
        st.write("""
            These non-profits focus on advocacy, education, and empowerment, providing essential services to women in need.
        """)

        nonprofits = [
            ("[Malala Fund](https://www.malala.org)", "The Malala Fund advocates for girls' education and works to eliminate the barriers preventing girls from going to school."),
            ("[The Women's Foundation](https://www.thewomensfoundation.org)", "An organization dedicated to advancing the economic and political power of women."),
            ("[Equal Rights Advocates](https://www.equalrights.org)", "Equal Rights Advocates focuses on advancing gender justice in workplaces and schools, fighting for equal rights for all women."),
            ("[Girls Who Code](https://www.girlswhocode.com)", "An organization dedicated to closing the gender gap in technology by empowering girls to code.")
        ]
        
        for org, description in nonprofits:
            st.subheader(org)
            st.write(description)

    # Online Courses Section - Collapsible
    with st.expander("Online Courses and Learning Platforms"):
        st.write("""
            The following platforms offer courses and resources designed to empower women by providing the skills and knowledge
            needed to succeed in various fields.
        """)

        courses = [
            ("[Coursera - Women in Leadership](https://www.coursera.org/learn/women-leadership)", "A comprehensive course aimed at helping women step into leadership roles in their respective industries."),
            ("[LinkedIn Learning - Personal Branding for Women](https://www.linkedin.com/learning/personal-branding-for-women)", "Learn how to create and communicate your personal brand to succeed in your career and business."),
            ("[EdX - Women in the Workplace](https://www.edx.org/course/women-in-the-workplace)", "This course provides an overview of the challenges and strategies for women to succeed in the corporate world."),
            ("[Udemy - Financial Literacy for Women](https://www.udemy.com/course/financial-literacy-for-women/)", "A course designed to help women gain financial independence and understanding of investment strategies.")
        ]
        
        for course, description in courses:
            st.subheader(course)
            st.write(description)

    # Videos and Documentaries Section - Collapsible
    with st.expander("Inspirational Videos and Documentaries"):
        st.write("""
            Watch these empowering videos and documentaries that feature the stories of women overcoming challenges, breaking barriers,
            and leading the way for gender equality.
        """)

        videos = [
            ("[The Feminist on Cellblock Y](https://www.netflix.com/title/81020607)", "A documentary about the transformative power of feminism and activism inside a women's prison."),
            ("[He Named Me Malala](https://www.youtube.com/watch?v=3J6OuvzZh0Y)", "The powerful story of Malala Yousafzai, who defied the Taliban to advocate for girls' education."),
            ("[RBG](https://www.youtube.com/watch?v=biIRw5tKePQ)", "A documentary that chronicles the life of U.S. Supreme Court Justice Ruth Bader Ginsburg, a pioneer for gender equality."),
            ("[The Mask You Live In](https://www.youtube.com/watch?v=hc45-ptHMxo)", "A film that explores the toxic influences of masculinity, providing insight into the social pressures faced by both men and women.")
        ]
        
        for video, description in videos:
            st.subheader(video)
            st.write(description)

    # Articles Section - Collapsible
    with st.expander("Articles and Blogs"):
        st.write("""
            These articles and blogs provide the latest news, opinions, and insights on women's rights, gender equality, and empowerment.
        """)

        articles = [
            ("[Why Women Empowerment is the Future of Work](https://www.forbes.com/sites/forbeshumanresourcescouncil/2022/03/07/why-women-empowerment-is-the-future-of-work/)", "An article exploring why gender equality and women empowerment will be crucial to the future of work and economic recovery."),
            ("[The Future of Women's Rights](https://www.weforum.org/agenda/2021/03/the-future-of-women-s-rights/)", "An exploration of the current state of women's rights and the progress needed for gender equality."),
            ("[Empowering Women Through Education](https://www.education.com/article/empowering-women-through-education/)", "An article on how education can break cycles of poverty, promote self-reliance, and empower women globally."),
            ("[How to Advocate for Women's Rights](https://www.amnesty.org/en/latest/campaigns/2022/03/how-to-advocate-for-womens-rights/)", "A comprehensive guide on how to become an advocate for women's rights, including actionable steps.")
        ]
        
        for article, description in articles:
            st.subheader(article)
            st.write(description)
            
elif page == "About Us":
    st.title("About She Elevates")
    st.write("""
        She Elevates is more than just a platform—it's a movement. We are dedicated to empowering women through
        education, inspiration, and community support. Our mission is to provide resources, share empowering stories,
        and create a space where women can come together to support and uplift one another.

        *Our Mission:*
        At She Elevates, we believe that empowering women is the key to creating a more just and equal world. Through
        education, we help women develop the skills they need to succeed in all areas of life. Whether it's gaining financial
        independence, learning to advocate for their rights, or developing leadership skills, we provide the tools for women
        to thrive. Our mission is to provide a platform that allows women to not only access valuable resources but to
        also feel supported and empowered by a community of like-minded individuals.

        *Why We Do It:*
        We believe that empowering women leads to stronger families, communities, and societies. By providing women with
        the resources they need to succeed, we help them make informed choices, become leaders, and live fulfilling lives.
        She Elevates is committed to creating a global movement where women rise together, breaking barriers and achieving
        their full potential.
    """)

    # Interactive Poll
    st.subheader("What Matters Most to You in Women's Empowerment?")
    empowerment_choice = st.radio(
        "Select one or more options that matter most to you:",
        ("Leadership", "Financial Independence", "Legal Rights", "Mental Health Support", "Education", "Community Support")
    )
    st.write(f"You chose: {empowerment_choice}. Your input helps us understand what matters most to the women in our community.")
    
    # Quote of the Day
    st.subheader("Quote of the Day")
    quotes = [
        "“There is no limit to what we, as women, can accomplish.” – Michelle Obama",
        "“I am not free while any woman is unfree, even when her shackles are very different from my own.” – Audre Lorde",
        "“A woman with a voice is, by definition, a strong woman.” – Melinda Gates",
        "“The most courageous act is still to think for yourself. Aloud.” – Coco Chanel"
    ]
    st.write(random.choice(quotes))  # This line works now with the random module imported

    # Empowerment Pledge (Users can make a commitment)
    st.subheader("Make Your Empowerment Pledge")
    pledge = st.text_input("What pledge would you like to make in the fight for women's rights?")
    if st.button("Submit Pledge"):
        if pledge:
            st.success(f"Thank you for your pledge: '{pledge}'! Together, we can make a difference.")
        else:
            st.error("Please enter your pledge before submitting.")

    # Impact Tracker
    st.subheader("Track Our Collective Impact")
    st.write("""
        Every time you interact with She Elevates, you contribute to a growing movement of empowerment. Together, we
        can inspire change and create opportunities for women everywhere. Here's how you are making an impact:
    """)
    st.write(f"Total Pledges Made: {random.randint(100, 1000)}")
    st.write(f"Total Empowerment Quiz Scores: {random.randint(500, 5000)}")

# Footer
st.sidebar.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f4f4f9;  
            padding: 20px;
        }
        .title {
            font-size: 20px;
            font-weight: bold;
            color: #424874;  
        }
        .authors {
            font-size: 16px;
            font-style: monospace;
            color: #424874;
        }
        .course {
            font-size: 14px;
            color: #424874;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Stylish message in the sidebar
with st.sidebar.expander("Developers"):
    st.markdown("""
    - **Michael Lagunday**  
    - **Lance Salamanca**  
    
    *Submitted for GEC003 - Contemporary World*  
    """)
