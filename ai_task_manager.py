import openai
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- SETUP ---
openai.api_key = "your_openai_api_key"  # Replace with your OpenAI key

# --- TASK PRIORITIZATION ---
def prioritize_tasks(tasks):
    df = pd.DataFrame(tasks)
    df['Priority'] = df['Urgency'] / df['Deadline']  # Simple priority formula
    return df.sort_values(by='Priority', ascending=False)

# --- STREAMLIT DASHBOARD ---
st.title("AI Task Manager")

tasks = st.text_area("Enter tasks (comma-separated)")
if st.button("Prioritize Tasks"):
    task_list = [{'Task': t, 'Deadline': 2, 'Urgency': 5} for t in tasks.split(',')]
    st.write(prioritize_tasks(task_list))