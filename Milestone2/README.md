from huggingface_hub import InferenceClient
import os

def query_model(prompt):
    try:
        HF_TOKEN = os.getenv("HF_TOKENN")

        client = InferenceClient(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            token=HF_TOKEN
        )

        response = client.chat_completion(
            messages=[
                {"role": "system", "content": "You are a certified professional fitness trainer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1200,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
        -----------------------------
        Model Name: **google/flan-t5-base**
        --------------------------------------
        ## 📝 Prompt Design Explanation

Prompt engineering plays a key role in generating high-quality fitness plans.

The prompt was structured to:

1. Clearly define the AI role (Certified Fitness Coach)
2. Provide user-specific parameters:
   - Gender
   - Height
   - Weight
   - BMI
   - Fitness Level
   - Goal
3. Specify output structure:
   - 3–7 Day workout plan
   - Warm-up
   - Main exercises
   - Sets and reps
   - Cool-down
   - Diet recommendations

Example Prompt Structure:

"Act as a certified fitness trainer. Create a personalized 7-day workout plan for a Male, 175cm height, 85kg weight, Beginner level, goal is Weight Loss. Include warm-up, main workout, sets/reps, and diet suggestions."

This structured instruction ensures consistent and meaningful outputs.

---

## ⚙️ Steps Performed

### 1️⃣ Model Loading
- Loaded tokenizer using AutoTokenizer
- Loaded model using AutoModelForSeq2SeqLM
- Enabled caching in Streamlit for performance

### 2️⃣ Prompt Creation
- Built dynamic prompt using user input fields
- Ensured structured formatting
- Included role instruction for better output quality

### 3️⃣ Inference Testing
- Tokenized prompt
- Generated output using:
  - max_new_tokens = 500
  - temperature = 0.3
  - do_sample = True
- Decoded generated response
- Displayed output in Streamlit interface

---

## 📊 Sample Generated Output

### 🏋️ Example 1 – Weight Loss Plan (Beginner)

Day 1:
- Warm-up: 5 minutes brisk walking
- Squats – 3 sets × 12 reps
- Push-ups – 3 sets × 10 reps
- Plank – 30 seconds × 3
- Cool-down stretching

Diet Suggestion:
- High protein breakfast
- Avoid sugary drinks
- Increase water intake

---

### 🏋️ Example 2 – Muscle Gain Plan (Intermediate)

Day 1:
- Warm-up: Jump rope 5 minutes
- Bench Press – 4 × 8 reps
- Deadlifts – 4 × 6 reps
- Shoulder Press – 3 × 10 reps

Diet:
- Calorie surplus
- Protein intake 1.6–2g/kg body weight
- Complex carbohydrates

---

