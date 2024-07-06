from openai import OpenAI
import google.generativeai as genai
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_SECRET_KEY"])
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


def workout_plan_ai(height, body_mass, diet):
    user_input = f"Create a beginner workout plan for someone with a height of {height} cm, body mass of {body_mass} kg, and diet that includes {diet}."
    workout_response = client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "You are a fitness coach."
        }, {
            "role": "user",
            "content": user_input
        }],
        max_tokens=300)

    workout_plan = workout_response.choices[0].message.content
    return workout_plan


def nutrition_plan_ai(height, body_mass, diet):
    user_input = f"Create a nutrition plan for someone with a height of {height} cm, body mass of {body_mass} kg, and diet that includes {diet}."
    nutrition_response = client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "You are a nutritionist."
        }, {
            "role": "user",
            "content": user_input
        }],
        max_tokens=300)

    nutrition_plan = nutrition_response.choices[0].message.content
    return nutrition_plan


def fitness_ai(height, body_mass, diet):
    workout_plan = workout_plan_ai(height, body_mass, diet)
    nutrition_plan = nutrition_plan_ai(height, body_mass, diet)
    return workout_plan, nutrition_plan


def main():
    st.title("AI Workout for Beginner")

    height = st.text_input("Enter your height in cm (e.g., 175):")
    body_mass = st.text_input("Enter your body mass in kg (e.g., 70):")
    diet = st.text_input(
        "Describe your diet (e.g., vegetarian, high protein, etc.):")

    if st.button("Generate Workout and Dietry Plan"):
        if height and body_mass and diet:
            try:
                height = float(height)
                body_mass = float(body_mass)
                workout_plan, nutrition_plan = fitness_ai(
                    height, body_mass, diet)
                st.subheader("Workout Plan")
                st.write(workout_plan)
                st.subheader("Nutrition Plan")
                st.write(nutrition_plan)
            except ValueError:
                st.error(
                    "Please enter valid numeric values for height and body mass."
                )
        else:
            st.error("Please fill out all fields.")


if __name__ == "__main__":
    main()
