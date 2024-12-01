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
        - **Leadership Skills**: Building leadership skills is essential for women who want to take charge of their
          careers and lives. Our article provides insights on developing leadership qualities, managing teams,
          and staying resilient in the face of challenges. These are the skills that will set you apart in any field.
          [Read More: Leadership Skills](https://www.forbes.com/sites/forbeshumanresourcescouncil/2020/01/28/five-essential-leadership-skills-every-woman-should-develop/?sh=167a2ff34b93)

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
            ("**Lean In: Women, Work, and the Will to Lead**", "Sheryl Sandberg's groundbreaking book that encourages women to pursue leadership roles and challenges gender inequality in the workplace."),
            ("**The Moment of Lift: How Empowering Women Changes the World**", "Melinda Gates' inspiring call to action for improving women's health, education, and economic opportunities."),
            ("**Women Who Run with the Wolves**", "Clarissa Pinkola Estés shares the powerful stories of wild women and their untamed spirit, encouraging women to reclaim their power."),
            ("**The Power of Now: A Guide to Spiritual Enlightenment**", "Eckhart Tolle's transformative teachings on mindfulness and self-awareness, helping women to focus on the present moment.")
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
st.sidebar.write("Made by Michael Lagunday & Lance Salamanca submitted to GEC003 - Contemporary World")
