import streamlit as st
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="My Baby - Premium Pregnancy Assistant",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Sidebar
    with st.sidebar:
        st.image("https://placehold.co/600x200", caption="My Baby")
        st.markdown("---")
        selected = st.selectbox(
            "Navigate to",
            ["Home", "Pregnancy Tracker", "Health Monitor", "Educational Resources", "Support"],
            index=0
        )
        st.markdown("---")
        st.markdown("### Quick Links")
        st.button("📝 My Profile")
        st.button("⚕ Find Doctor")
        st.button("🆘 Emergency Contacts")

    # Main content
    if selected == "Home":
        # Welcome section
        st.title("Welcome to My Baby 👶")
        st.subheader("Your AI-Powered Pregnancy Journey Companion")
        
        # Quick stats in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Active Users", value="100K+", delta="↑ 15%")
        with col2:
            st.metric(label="Success Stories", value="50K+", delta="↑ 12%")
        with col3:
            st.metric(label="Expert Doctors", value="1000+", delta="↑ 5%")

        # Main features
        st.markdown("## Key Features")
        feature_col1, feature_col2 = st.columns(2)
        
        with feature_col1:
            with st.container():
                st.markdown("### 🌟 Smart Tracking")
                st.write("AI-powered pregnancy tracking with personalized insights.")
                st.button("Try Smart Tracking")
            
            with st.container():
                st.markdown("### 👩‍⚕ Virtual Support")
                st.write("24/7 access to AI-powered pregnancy support.")
                st.button("Get Support")

        with feature_col2:
            with st.container():
                st.markdown("### 📊 Health Monitor")
                st.write("Comprehensive health monitoring with real-time alerts.")
                st.button("View Health Dashboard")
            
            with st.container():
                st.markdown("### 🎓 Learn")
                st.write("Access to premium pregnancy courses and workshops.")
                st.button("Browse Courses")

        # Recent Updates
        st.markdown("## Recent Updates")
        with st.expander("What's New", expanded=True):
            st.markdown("""
            - 🎉 **New Feature**: Advanced baby size visualization
            - 📱 **App Update**: Improved user interface
            - 🏥 **Partner Network**: Added 100+ new hospitals
            """)

        # Tips Section
        st.markdown("## Today's Tips")
        tip_col1, tip_col2 = st.columns(2)
        
        with tip_col1:
            st.info("💡 Stay hydrated! Aim for 8-10 glasses of water daily.")
        with tip_col2:
            st.info("🧘‍♀ Take short walks to maintain good circulation.")

        # Community Section
        st.markdown("## Community Highlights")
        comm_col1, comm_col2, comm_col3 = st.columns(3)
        
        with comm_col1:
            st.markdown("### 👥 Active Members")
            st.write("Join our growing community")
            st.button("Join Community")
        
        with comm_col2:
            st.markdown("### 📅 Upcoming Events")
            st.write("Check our latest events")
            st.button("View Events")
        
        with comm_col3:
            st.markdown("### 💬 Support Group")
            st.write("Connect with other parents")
            st.button("Join Group")

        # Footer
        st.markdown("---")
        footer_col1, footer_col2, footer_col3 = st.columns(3)
        
        # with footer_col1:
        #     st.markdown("### Contact Us")
        #     st.write("📧 support@mybaby.ai")
        #     st.write("📞 1-800-MYBABY")
        
        # with footer_col2:
        #     st.markdown("### Follow Us")
        #     st.write("Find us on social media")
        #     st.button("Social Media Links")
        
        # with footer_col3:
        #     st.markdown("### Help & Support")
        #     st.write("Need assistance?")
        #     st.button("Get Help")

        # Copyright
        # st.markdown("---")
        st.markdown(
            "<div style='text-align: center'>© 2024 My Baby. All rights reserved.</div>", 
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
