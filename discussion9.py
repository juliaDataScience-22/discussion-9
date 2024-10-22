import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Burndown Chart for Your Project")

# User input
num_days = st.number_input("Enter the number of days total for the project:", min_value=1, max_value=999, value=1)

days = []
work_remaining = []

# Loop for the user to input the work remaining for each day
for i in range(1, num_days + 1):
    day_label = f"{i}"
    days.append(day_label)
    
    if num_days > 1:
        default_remaining = int(100 - (100 / (num_days - 1)) * (i - 1))
    else:
        default_remaining = 100  # When there's only one day

    # Input work left to do
    remaining = st.number_input(f"Enter percentage of work remaining for {day_label}:", min_value=0, max_value=100, value=default_remaining)
    work_remaining.append(remaining)

if num_days > 1:
    ideal_progress = [100 - (100 / (num_days - 1)) * i for i in range(num_days)]
else:
    ideal_progress = [100]

df = pd.DataFrame({
    'Day': days,
    'Work Remaining (%)': work_remaining,
    'Ideal Progress (%)': ideal_progress
})

fig, ax = plt.subplots()
ax.plot(df['Day'], df['Work Remaining (%)'], label='Work Remaining', marker='*', color='black')
ax.plot(df['Day'], df['Ideal Progress (%)'], label='Ideal Progress', linestyle=':', color='blue')

ax.set_xlabel('Day')
ax.set_ylabel('Work Remaining (%)')
ax.set_title('Burndown Chart')
ax.legend()

st.pyplot(fig)

st.write("Project Data:")
st.dataframe(df)
