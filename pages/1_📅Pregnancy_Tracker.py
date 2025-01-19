# pages/1_pregnancy_tracker.py
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.constants import PREGNANCY_WEEKS
from utils.ai_utils import get_ai_response

def calculate_due_date(last_period):
    return last_period + timedelta(days=280)

def calculate_current_week(last_period):
    today = datetime.now().date()
    pregnancy_start = last_period
    days_pregnant = (today - pregnancy_start).days
    weeks_pregnant = days_pregnant // 7
    return min(max(1, weeks_pregnant), 40)

def pregnancy_tracker_page():
    st.title("🗓 Pregnancy Tracker")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        last_period = st.date_input(
            "When was the first day of your last period?",
            datetime.now().date() - timedelta(weeks=12)
        )
        
        current_week = calculate_current_week(last_period)
        due_date = calculate_due_date(last_period)
        
        # Progress bar
        st.progress(current_week / 40)
        st.markdown(f"### Week {current_week} of 40")
        
        # Baby size visualization
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=current_week,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 40]},
                'bar': {'color': "#ff4b8d"},
                'steps': [
                    {'range': [0, 13], 'color': "lightgray"},
                    {'range': [13, 26], 'color': "gray"},
                    {'range': [26, 40], 'color': "darkgray"}
                ]
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### Your Baby This Week")
        if current_week in PREGNANCY_WEEKS:
            st.write(PREGNANCY_WEEKS[current_week])
            
        st.markdown("### Due Date")
        st.write(f"📅 {due_date.strftime('%B %d, %Y')}")
        
        # AI Insights
        st.markdown("### AI Insights")
        if st.button("Get Personalized Insights"):
            prompt = f"What should a pregnant woman expect and focus on during week {current_week} of pregnancy? Give 3 key points."
            insights = get_ai_response(prompt)
            st.write(insights)
    
    # Milestone Timeline
    st.markdown("---")
    st.markdown("### Pregnancy Milestones")
    
    timeline_data = {
        "First Trimester": ["First ultrasound", "Morning sickness subsides", "End of embryonic period"],
        "Second Trimester": ["Gender reveal possible", "Baby's first movements", "Glucose screening test"],
        "Third Trimester": ["Baby shower", "Birth plan creation", "Pack hospital bag"]
    }
    
    for trimester, milestones in timeline_data.items():
        with st.expander(trimester):
            for milestone in milestones:
                st.checkbox(milestone)

if __name__ == "__main__":
    pregnancy_tracker_page()
