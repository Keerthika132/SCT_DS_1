import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px

# Function to load data from a CSV (or can be adapted for other formats)
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None

# Sample dataset (Could be replaced with dynamic loading, e.g. from CSV)
data = {
    'Gender': ['Male', 'Female', 'Non-binary', 'Other', 'Male', 'Female', 'Male', 'Female', 'Non-binary', 'Other'],
    'Count': [45, 55, 5, 3, 60, 50, 55, 45, 7, 6]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total count and percentages dynamically
total_count = df['Count'].sum()
df['Percentage'] = (df['Count'] / total_count) * 100

# Advanced Visualization with Seaborn to make a more sophisticated plot
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Create bar plot with color palette and display percentages on bars
barplot = sns.barplot(x='Gender', y='Count', data=df, palette="Set2")

# Adding percentage text above each bar
for p in barplot.patches:
    barplot.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center', fontsize=12, color='black', fontweight='bold', xytext=(0, 5),
                     textcoords='offset points')

# Customize title, axis labels, and ticks
plt.title('Gender Distribution in Population (Advanced Visualization)', fontsize=18, fontweight='bold')
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# Show grid on the y-axis for better readability
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()
plt.show()

# --- Interactive Plot with Plotly --- #
# Plotly for interactive chart
fig = px.bar(df, x='Gender', y='Count', text='Percentage', color='Gender', 
             title='Interactive Gender Distribution in Population', 
             labels={'Count': 'Population Count', 'Gender': 'Gender Categories'})

# Update layout for better visibility of percentage
fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside', marker=dict(line=dict(width=2, color='Black')))
fig.update_layout(showlegend=False)

# Show interactive plot
fig.show()
