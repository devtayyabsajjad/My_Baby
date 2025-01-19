import streamlit as st
import base64

def team_contact_page():
    # Custom CSS with theme-compatible styling
    st.markdown("""
        <style>
        /* Header styling */
        .team-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
        }
        
        /* Team card styling */
        .team-card {
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            border: 1px solid rgba(128, 128, 128, 0.2);
            background-color: var(--background-color);
        }
        
        /* Profile image styling */
        .profile-img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto;
            border: 3px solid var(--primary-color);
            padding: 3px;
        }
        
        /* Social links container */
        .social-links {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
            flex-wrap: wrap;
        }
        
        /* Social button styling */
        .social-button {
           padding: 8px 15px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 120px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);

        }
        
        .linkedin-button {
           background-color: #0077B5;
            color: white !important;
        }
        
        .github-button {
           background-color: #24292e;
            color: white !important;
        }
        
        .social-button:hover {
               transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            opacity: 0.9;
        }
        /* Icons for buttons */
        .button-icon {
            font-size: 16px;
        }

        
        /* Contact section styling */
        .contact-section {
            padding: 20px;
            border-radius: 15px;
            margin-top: 30px;
            text-align: center;
            border: 1px solid rgba(128, 128, 128, 0.2);
            background-color: var(--background-color);
        }
        
        /* Form styling */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: var(--background-color);
            border: 1px solid rgba(128, 128, 128, 0.2);
            border-radius: 8px;
        }
        
        /* Submit button styling */
        .stButton > button {
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            color: white;
            border: none;
            padding: 0.5rem 2rem;
            border-radius: 50px;
            font-weight: 500;
            width: 100%;
        }
        
        .stButton > button:hover {
            opacity: 0.9;
        }
        
        /* Success message styling */
        .success-message {
            padding: 1rem;
            border-radius: 8px;
            background-color: rgba(0, 200, 0, 0.1);
            border: 1px solid rgba(0, 200, 0, 0.2);
            margin: 1rem 0;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .team-card {
                margin: 10px 0;
            }
            .social-links {
                flex-direction: column;
                align-items: center;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='team-header'>Meet Our Team</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; margin-bottom: 30px; opacity: 0.8;'>
        We're a passionate team dedicated to creating innovative AI solutions. 
        Feel free to reach out to any of us with questions or collaboration ideas.
        </p>
    """, unsafe_allow_html=True)

    # Team members data
    team_members = [
        {
            "name": "Ahmad Fakhar",
            "role": "Data Analyst",
            "github_url": "https://github.com/Ahmad-Fakhar",
            "linkedin_url": "https://www.linkedin.com/in/ahmad-fakhar-357742258/",
            "image_url": "https://github.com/Ahmad-Fakhar.png"
        },
        {
            "name": "Asim Khan",
            "role": "ML Expert",
            "github_url": "https://github.com/Asimbaloch",
            "linkedin_url": "https://www.linkedin.com/in/asim-khan-baloch/",
            "image_url": "https://avatars.githubusercontent.com/u/85347127?v=4"
        },
        {
            "name": "Tayyab Sajjiad",
            "role": "Software Developer",
            "github_url": "https://github.com/devtayyabsajjad",
            "linkedin_url": "http://www.linkedin.com/in/tayyab-sajjad-156ab2267",
            "image_url": "https://avatars.githubusercontent.com/u/124726671?v=4"
        },
        {
            "name": "Muhammad Ibrahim",
            "role": "Data Scientist",
            "github_url": "https://github.com/muhammadibrahim313",
            "linkedin_url": "https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/",
            "image_url": "https://github.com/muhammadibrahim313.png"
        }
    ]

    # Create team member grid
    for i in range(0, len(team_members), 2):
        col1, col2 = st.columns(2)
        
        # First team member in row
        with col1:
            member = team_members[i]
            st.markdown(f"""
                <div class='team-card'>
                    <img src="{member['image_url']}" 
                    class='profile-img' alt='{member["name"]}'>
                    <h3 style='margin: 15px 0;'>{member["name"]}</h3>
                    <p style='margin-bottom: 15px; opacity: 0.8;'>{member["role"]}</p>
                    <div class='social-links'>
                        <a href='{member["linkedin_url"]}' target='_blank' class='social-button linkedin-button'>LinkedIn</a>
                        <a href='{member["github_url"]}' target='_blank' class='social-button github-button'>GitHub</a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Second team member in row (if exists)
        if i + 1 < len(team_members):
            with col2:
                member = team_members[i + 1]
                st.markdown(f"""
                    <div class='team-card'>
                        <img src="{member['image_url']}" 
                        class='profile-img' alt='{member["name"]}'>
                        <h3 style='margin: 15px 0;'>{member["name"]}</h3>
                        <p style='margin-bottom: 15px; opacity: 0.8;'>{member["role"]}</p>
                        <div class='social-links'>
                            <a href='{member["linkedin_url"]}' target='_blank' class='social-button linkedin-button'>LinkedIn</a>
                            <a href='{member["github_url"]}' target='_blank' class='social-button github-button'>GitHub</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("""
        <div class='contact-section'>
            <h2 style='margin-bottom: 15px;'>Get in Touch</h2>
            <p style='margin-bottom: 20px; opacity: 0.8;'>
                Have questions? We'd love to hear from you. Send us a message and we'll respond as soon as possible.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Contact Form
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with col2:
            subject = st.text_input("Subject")
            phone = st.text_input("Phone (optional)")
        
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        
        if submit:
            if name and email and subject and message:
                st.markdown("""
                    <div class='success-message'>
                        Thank you for your message! We'll get back to you soon.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Please fill in all required fields.")

if __name__ == "__main__":
    team_contact_page()
