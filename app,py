import streamlit as st
import pandas as pd
import altair as alt
import requests
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from streamlit_lottie import st_lottie

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FIT Plan AI",
    page_icon="🏋️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#1e3c72,#2a5298);
    color: white;
}
h1, h2, h3 {
    text-align: center;
    color: #FFD700;
}
.name-tag {
    text-align:center;
    font-size:20px;
    color:#ffffff;
    margin-bottom:10px;
}
div.stButton > button {
    background-color: #FF5733;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    return tokenizer, model

tokenizer, model = load_model()

# ---------------- LOTTIE FUNCTION ----------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------- BMI FUNCTION ----------------
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 24.9:
        category = "Normal"
    elif bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category

# ---------------- TITLE ----------------
st.title("🏋️ FIT PLAN AI")
st.subheader("AI Powered Personalized Workout Generator")
st.markdown("---")

# ---------------- SESSION STATE ----------------
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["🏠 Home", "📝 User Details", "📊 BMI Analysis", "💪 Workout Plan"]
)

# ---------------- HOME TAB ----------------
with tab1:
    st.header("🏠 Welcome to FIT Plan AI")
    st.write("""
    - Calculate your BMI  
    - Generate structured 7-day workout plans  
    - Beginner safe programming  
    - Fat-loss focused training  
    """)
    lottie = load_lottie("https://assets2.lottiefiles.com/packages/lf20_2LdLki.json")
    st_lottie(lottie, height=200)

# ---------------- USER DETAILS TAB ----------------
with tab2:
    st.header("📝 Enter Your Fitness Details")

    name = st.text_input("👤 Enter Your Name")

    gender = st.radio("Gender *", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
    height = st.number_input("Height (cm)", min_value=100, max_value=220)

    goal = st.selectbox(
        "🎯 Select Your Goals",
        [
        "Flexible",
        "Weight Loss",
        "Build Muscle",
        "Strength Gaining",
        "Abs Building"
]
    )

    equipment = st.multiselect(
        "🏋️ Available Equipment",
        [    "Dumbbells",
        "Resistance Band",
        "Yoga Mat",
        "No Equipment",
        "Inclined Bench",
        "Treadmill",
        "Cycle",
        "Skipping Rope",
        "Hand Gripper",
        "Pull-ups Bar",
        "Weight Plates",
        "Hula Hoop Ring",
        "Bosu Ball"]
    )

    fitness_level = st.radio(
        "💪 Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    st.session_state.user_data = {
        "name": name,
        "gender": gender,
        "weight": weight,
        "height": height,
        "goal": goal,
        "equipment": equipment,
        "fitness_level": fitness_level
    }

# ---------------- BMI TAB ----------------
with tab3:
    st.header("📊 BMI Analysis")

    if st.session_state.user_data:
        data = st.session_state.user_data
        bmi, category = calculate_bmi(data["weight"], data["height"])

        st.markdown(f"<div class='name-tag'>👤 {data['name']}'s BMI Result</div>", unsafe_allow_html=True)
        st.subheader(f"BMI: {bmi} ({category})")

        df = pd.DataFrame({
            "Category": ["Underweight", "Normal", "Overweight", "Obese"],
            "BMI Range": [18.5, 24.9, 29.9, 35]
        })

        chart = alt.Chart(df).mark_bar().encode(
            x="Category",
            y="BMI Range"
        )

        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Please enter your details in the User Details tab.")

# ---------------- WORKOUT PLAN TAB ----------------
with tab4:
    st.header("💪 Generate Your Detailed Workout Plan")

    # Select number of days (3 to 7)
    selected_days = st.selectbox(
        "📅 Select Number of Workout Days",
        [3, 4, 5, 6, 7]
    )

    if st.button("🔥 Generate Workout Plan"):

        data = st.session_state.user_data
        bmi, category = calculate_bmi(data["weight"], data["height"])

        prompt = f"""
You are a certified strength and conditioning coach.
Create a SAFE and EFFECTIVE {selected_days}-day workout plan.
User Profile:
- Name: {data['name']}
- Gender: {data['gender']}
- BMI: {bmi}
- Goal: {data['goal']}
- Fitness Level: {data['fitness_level']}
- Available Equipment: {data['equipment']}
Important Instructions:
1. Design specifically for a beginner (if beginner selected).
2. Focus on fat loss and improving overall fitness.
3. Each day must include:
   - Warm-up (5–10 minutes)
   - Main workout (4–6 exercises)
   - Sets, reps, and rest time
   - Cool-down/stretching
4. Include at least 2 cardio-focused days if days >= 4.
5. Avoid advanced or high-injury-risk movements.
6. Keep each session under 45 minutes.
7. Clearly label Day 1 to Day {selected_days}.
8. Provide detailed structured formatting.
9. Return ONLY the structured workout plan.
"""

        inputs = tokenizer(prompt, return_tensors="pt")

        outputs = model.generate(
            **inputs,
            max_new_tokens=600,  # Increased for detailed output
            temperature=0.7,
            do_sample=True
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.markdown(
            f"<div class='name-tag'>🏋️ {selected_days}-Day Workout Plan for {data['name']}</div>",
            unsafe_allow_html=True
        )

        st.write(response)

        st.success("Train smart. Stay consistent. Recover well. 🚀")
