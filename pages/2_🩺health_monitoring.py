# pages/2_health_monitoring.py
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utils.ai_utils import get_ai_response

def health_monitoring_page():
    st.title("🏥 Health Monitoring")
    
    tabs = st.tabs(["Physical Health", "Mental Health", "Symptom Checker"])
    
    # Physical Health Tab
    with tabs[0]:
        st.subheader("Track Your Physical Health")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Weight Tracking
            st.markdown("### Weight Tracking")
            weight = st.number_input("Enter today's weight (kg)", min_value=0.0, max_value=200.0)
            if st.button("Log Weight"):
                # Here you would normally save to a database
                st.success("Weight logged successfully!")
            
            # Create sample weight data for demonstration
            dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
            weights = [65 + i * 0.1 + np.random.normal(0, 0.2) for i in range(len(dates))]
            weight_df = pd.DataFrame({'Date': dates, 'Weight': weights})
            
            # Plot weight trend
            fig = px.line(weight_df, x='Date', y='Weight', title='Weight Trend')
            st.plotly_chart(fig)
        
        with col2:
            # Blood Pressure Tracking
            st.markdown("### Blood Pressure")
            col3, col4 = st.columns(2)
            with col3:
                systolic = st.number_input("Systolic", min_value=0, max_value=200)
            with col4:
                diastolic = st.number_input("Diastolic", min_value=0, max_value=150)
            
            if st.button("Log Blood Pressure"):
                st.success("Blood pressure logged successfully!")
    
    # Mental Health Tab
    with tabs[1]:
        st.subheader("Mental Wellness Tracker")
        
        # Mood Tracker
        st.markdown("### Today's Mood")
        mood = st.select_slider(
            "How are you feeling today?",
            options=["😔", "😕", "😐", "🙂", "😊"],
            value="😐"
        )
        
        # Stress Level
        stress_level = st.slider("Stress Level (0-10)", 0, 10, 5)
        
        # Sleep Quality
        sleep_hours = st.number_input("Hours of sleep last night", 0, 24, 8)
        
        if st.button("Get Mental Health Tips"):
            prompt = f"I'm {mood} today with a stress level of {stress_level}/10 and slept {sleep_hours} hours. Give me 3 mental health tips for pregnancy."
            tips = get_ai_response(prompt)
            st.markdown("### AI-Generated Tips")
            st.write(tips)
        
        # Meditation Timer
        st.markdown("### Quick Meditation")
        meditation_time = st.select_slider(
            "Select meditation duration",
            options=[1, 2, 3, 5, 10],
            value=3,
            format_func=lambda x: f"{x} minutes"
        )
        if st.button("Start Meditation"):
            # Here you would normally implement a timer
            st.balloons()
    
    # Symptom Checker Tab
    with tabs[2]:
        st.subheader("Symptom Checker")
        
        # Common pregnancy symptoms checklist
        symptoms = {
            "Morning Sickness": ["Nausea", "Vomiting"],
            "Pain": ["Headache", "Back Pain", "Pelvic Pain"],
            "Digestive": ["Heartburn", "Constipation", "Bloating"],
            "Other": ["Fatigue", "Dizziness", "Swelling"]
        }
        
        selected_symptoms = []
        for category, symptom_list in symptoms.items():
            st.markdown(f"### {category}")
            for symptom in symptom_list:
                if st.checkbox(symptom):
                    selected_symptoms.append(symptom)
        
        severity = st.select_slider(
            "Symptom Severity",
            options=["Mild", "Moderate", "Severe"],
            value="Moderate"
        )
        
        if st.button("Check Symptoms"):
            if selected_symptoms:
                prompt = f"I'm experiencing {', '.join(selected_symptoms)} with {severity.lower()} severity during pregnancy. What should I know and when should I contact a healthcare provider?"
                advice = get_ai_response(prompt)
                st.markdown("### AI Assessment")
                st.write(advice)
                
                if severity == "Severe":
                    st.warning("⚠ Please consult your healthcare provider immediately for severe symptoms.")
            else:
                st.info("Please select at least one symptom to check.")

if __name__ == "__main__":
    health_monitoring_page()
