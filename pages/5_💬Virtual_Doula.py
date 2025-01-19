# pages/5_virtual_doula.py
import streamlit as st
from utils.ai_utils import get_ai_response
import plotly.express as px
from datetime import datetime, timedelta

def virtual_doula_page():
    st.title("👩‍⚕ Virtual Doula")
    
    tabs = st.tabs(["Birth Plan", "Labor Preparation", "Postpartum Care"])
    
    # Birth Plan Tab
    with tabs[0]:
        st.subheader("Create Your Birth Plan")
        
        # Birth preferences
        preferences = {
            "Birth Environment": st.multiselect(
                "Preferred birth environment",
                ["Hospital", "Birth Center", "Home Birth"]
            ),
            "Pain Management": st.multiselect(
                "Pain management preferences",
                ["Natural", "Epidural", "Nitrous Oxide", "Hydrotherapy"]
            ),
            "Support Team": st.multiselect(
                "Who would you like present?",
                ["Partner", "Doula", "Family Member", "Midwife"]
            ),
            "Interventions": st.multiselect(
                "Intervention preferences",
                ["Only if medically necessary", "Prefer to avoid", "Open to all options"]
            )
        }
        
        if st.button("Generate Birth Plan"):
            prompt = f"""
            Create a detailed birth plan based on these preferences:
            Birth Environment: {', '.join(preferences['Birth Environment'])}
            Pain Management: {', '.join(preferences['Pain Management'])}
            Support Team: {', '.join(preferences['Support Team'])}
            Interventions: {', '.join(preferences['Interventions'])}
            """
            birth_plan = get_ai_response(prompt)
            st.markdown("### Your Personalized Birth Plan")
            st.write(birth_plan)
            
            if st.button("Download Birth Plan"):
                st.download_button(
                    "Download as PDF",
                    birth_plan,
                    file_name="birth_plan.pdf",
                    mime="application/pdf"
                )

    # Labor Preparation Tab
    with tabs[1]:
        st.subheader("Labor Preparation Guide")
        
        # Contraction Timer
        st.markdown("### Contraction Timer")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Start Contraction"):
                st.session_state.contraction_start = datetime.now()
                st.info("Timing contraction...")
            
            if st.button("End Contraction"):
                if hasattr(st.session_state, 'contraction_start'):
                    duration = (datetime.now() - st.session_state.contraction_start).seconds
                    if 'contractions' not in st.session_state:
                        st.session_state.contractions = []
                    st.session_state.contractions.append({
                        'time': datetime.now(),
                        'duration': duration
                    })
                    st.success(f"Contraction recorded: {duration} seconds")
        
        with col2:
            if hasattr(st.session_state, 'contractions') and st.session_state.contractions:
                df = pd.DataFrame(st.session_state.contractions)
                fig = px.line(df, x='time', y='duration', title='Contraction Pattern')
                st.plotly_chart(fig)
        
        # Labor Positions
        st.markdown("### Recommended Labor Positions")
        positions = {
            "Early Labor": ["Walking", "Resting", "Gentle Swaying"],
            "Active Labor": ["Birth Ball", "Squatting", "Hands and Knees"],
            "Transition": ["Supported Squat", "Side-Lying", "Leaning Forward"]
        }
        
        selected_stage = st.selectbox("Select Labor Stage", list(positions.keys()))
        st.write("Try these positions:")
        for position in positions[selected_stage]:
            st.markdown(f"- {position}")
            
        if st.button("Get Position Tips"):
            prompt = f"Provide detailed instructions for the {selected_stage} positions: {', '.join(positions[selected_stage])}"
            tips = get_ai_response(prompt)
            st.write(tips)

    # Postpartum Care Tab
    with tabs[2]:
        st.subheader("Postpartum Recovery & Care")
        
        # Recovery Timeline
        st.markdown("### Recovery Timeline")
        weeks = st.slider("Weeks Postpartum", 0, 12, 0)
        
        if st.button("Get Recovery Info"):
            prompt = f"What should a new mother expect and focus on during week {weeks} postpartum? Include physical recovery, emotional well-being, and baby care tips."
            recovery_info = get_ai_response(prompt)
            st.write(recovery_info)
        
        # Self-Care Checklist
        st.markdown("### Daily Self-Care Checklist")
        self_care_items = [
            "Rested for at least 2 hours",
            "Eaten 3 nutritious meals",
            "Taken prescribed medications/vitamins",
            "Done basic hygiene routine",
            "Had support person help with baby",
            "Moved body gently/stretched",
            "Connected with another adult",
            "Hydrated well (8+ glasses of water)"
        ]
        
        completed_items = []
        for item in self_care_items:
            if st.checkbox(item):
                completed_items.append(item)
        
        progress = len(completed_items) / len(self_care_items)
        st.progress(progress)
        st.write(f"You've completed {int(progress * 100)}% of your self-care tasks today")
        
        # Mood Tracker
        st.markdown("### Mood Tracker")
        mood = st.select_slider(
            "How are you feeling today?",
            options=["😔", "😕", "😐", "🙂", "😊"]
        )
        
        if mood in ["😔", "😕"]:
            st.warning("Remember, it's normal to have ups and downs. Consider talking to your healthcare provider if you're feeling down frequently.")
            if st.button("Get Support Resources"):
                prompt = "Provide resources and coping strategies for postpartum mood concerns."
                resources = get_ai_response(prompt)
                st.write(resources)

if __name__ == "__main__":
    virtual_doula_page()
