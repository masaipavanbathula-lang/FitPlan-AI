import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="FIT Plan AI – Personalized Fitness Plan Generator",
    layout="centered"
)
# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
 return pipeline(
 "text-generation",
 model="google/flan-t5-base"
 ) 
generator = load_model()

# ---------------- TITLE ----------------
st.title("🏋️ FIT Plan AI – Personalized Fitness Plan Generator")

# ---------------- PERSONAL INFORMATION ----------------
st.header("👤 Personal Information")

name = st.text_input("Name *")

height_cm = st.number_input(
    "Height in centimeters *",
    min_value=0.0,
    step=0.1
)

weight_kg = st.number_input(
    "Weight in kilograms *",
    min_value=0.0,
    step=0.1
)

# ---------------- FITNESS DETAILS ----------------
st.header("💪 Fitness Details")

goals = st.multiselect(
    "Select Your Goals",
    [
        "Flexible",
        "Weight Loss",
        "Build Muscle",
        "Strength Gaining",
        "Abs Building"
    ]
)

equipment = st.multiselect(
    "Available Equipment",
    [
        "Dumbbells",
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
        "Bosu Ball"
    ]
)

fitness_level = st.selectbox(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# ---------------- BMI FUNCTIONS ----------------
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# ---------------- SUBMIT BUTTON ----------------
if st.button("Calculate BMI & Submit"):

    # ---------------- VALIDATION ----------------
    if not name.strip():
        st.error("❌ Name is required")
    elif height_cm <= 0:
        st.error("❌ Height must be greater than zero")
    elif weight_kg <= 0:
        st.error("❌ Weight must be greater than zero")
    elif not goals:
        st.error("❌ Please select at least one goal")
    elif not equipment:
        st.error("❌ Please select at least one equipment")
    else:
        # ---------------- CALCULATE BMI ----------------
        bmi = calculate_bmi(weight_kg, height_cm)
        category = bmi_category(bmi)

        # ---------------- DISPLAY OUTPUT ----------------
        st.success("✅ BMI calculated successfully!")

        st.subheader("📊 BMI Result")
        st.write(f"**Name:** {name}")
        st.write(f"**Height:** {height_cm} cm")
        st.write(f"**Weight:** {weight_kg} kg")
        st.write(f"**BMI:** {bmi}")
        st.write(f"**BMI Category:** {category}")

        st.subheader("💪 Fitness Details")
        st.write(f"**Fitness Level:** {fitness_level}")
        st.write(f"**Goals:** {', '.join(goals)}")
        st.write(f"**Equipment:** {', '.join(equipment)}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("💡 *BMI is a screening tool. Combine it with proper training and diet for best results.*")
