# pages/3_nutrition_exercise.py
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from utils.ai_utils import get_ai_response
from utils.constants import NUTRITION_TIPS, EXERCISE_RECOMMENDATIONS

def nutrition_exercise_page():
    st.title("🥗 Nutrition & Exercise")
    
    tabs = st.tabs(["Meal Planner", "Exercise Guide", "Progress Tracker"])
    
    # Meal Planner Tab
    with tabs[0]:
        st.subheader("Personalized Meal Planner")
        
        # User preferences
        col1, col2 = st.columns(2)
        with col1:
            trimester = st.selectbox(
                "Current Trimester",
                ["First Trimester", "Second Trimester", "Third Trimester"]
            )
            dietary_restrictions = st.multiselect(
                "Dietary Restrictions",
                ["Vegetarian", "Vegan", "Gluten-free", "Dairy-free", "None"]
            )
        
        with col2:
            calories_target = st.slider(
                "Daily Calorie Target",
                1500, 2500, 2000
            )
            
        # Generate meal plan
        if st.button("Generate Meal Plan"):
            prompt = f"""
            Create a one-day meal plan for a pregnant woman in {trimester} 
            with {', '.join(dietary_restrictions)} dietary restrictions, 
            targeting {calories_target} calories. Include breakfast, lunch, dinner, and 2 snacks.
            """
            meal_plan = get_ai_response(prompt)
            st.markdown("### Your Personalized Meal Plan")
            st.write(meal_plan)
        
        # Nutrition tips
        st.markdown("### Essential Nutrients")
        nutrients = {
            "Folic Acid": "800 mcg/day",
            "Iron": "27 mg/day",
            "Calcium": "1000 mg/day",
            "Vitamin D": "600 IU/day",
            "DHA": "200-300 mg/day"
        }
        
        for nutrient, requirement in nutrients.items():
            st.metric(nutrient, requirement)
    
    # Exercise Guide Tab
    with tabs[1]:
        st.subheader("Safe Exercise Guide")
        
        # Exercise preferences
        fitness_level = st.select_slider(
            "Fitness Level",
            options=["Beginner", "Intermediate", "Advanced"],
            value="Intermediate"
        )
        
        exercise_time = st.slider(
            "Available time for exercise (minutes)",
            15, 60, 30
        )
        
        # Generate exercise plan
        if st.button("Get Exercise Plan"):
            prompt = f"""
            Create a safe {exercise_time}-minute pregnancy exercise routine for a {fitness_level.lower()} level
            person in {trimester}. Include warm-up and cool-down.
            """
            exercise_plan = get_ai_response(prompt)
            st.markdown("### Your Exercise Plan")
            st.write(exercise_plan)
        
        # Exercise safety guidelines
        st.markdown("### Safety Guidelines")
        safety_tips = [
            "Listen to your body and don't overexert",
            "Stay hydrated during exercise",
            "Avoid exercises that risk falling or injury",
            "Stop if you feel pain or discomfort",
            "Keep heart rate below 140 bpm"
        ]
        
        for tip in safety_tips:
            st.info(tip)
    
    # Progress Tracker Tab
    with tabs[2]:
        st.subheader("Track Your Progress")
        
        # Activity logging
        st.markdown("### Log Today's Activities")
        
        col1, col2 = st.columns(2)
        with col1:
            water_intake = st.number_input("Water Intake (glasses)", 0, 20, 8)
            exercise_minutes = st.number_input("Exercise Duration (minutes)", 0, 180, 30)
        
        with col2:
            meals_logged = st.number_input("Meals Eaten Today", 0, 6, 3)
            steps_taken = st.number_input("Steps Taken", 0, 20000, 5000)
        
        if st.button("Log Progress"):
            st.success("Progress logged successfully!")
            
            # Create sample progress data
            dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
            water_data = [8 + np.random.normal(0, 1) for _ in range(len(dates))]
            steps_data = [5000 + np.random.normal(0, 500) for _ in range(len(dates))]
            
            # Plot progress charts
            col3, col4 = st.columns(2)
            with col3:
                water_df = pd.DataFrame({'Date': dates, 'Water (glasses)': water_data})
                fig1 = px.line(water_df, x='Date', y='Water (glasses)', title='Water Intake Trend')
                st.plotly_chart(fig1)
            
            with col4:
                steps_df = pd.DataFrame({'Date': dates, 'Steps': steps_data})
                fig2 = px.line(steps_df, x='Date', y='Steps', title='Daily Steps Trend')
                st.plotly_chart(fig2)

if __name__ == "__main__":
    nutrition_exercise_page()
