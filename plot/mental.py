import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def load_data(data_path):
    new_data = pd.read_csv(data_path)
    return new_data

def prepare_data(new_data):
    mean_scores = new_data.groupby(['Skill', 'Scenario', 'Fault Condition'])['Mental Demand'].mean().reset_index()
    operators = mean_scores[mean_scores['Skill'] == 'Operator']
    students = mean_scores[mean_scores['Skill'] == 'Student']
    mean_scores_students = new_data[new_data['Skill'] == 'Student'].groupby(['Study', 'Scenario', 'Fault Condition'])['Mental Demand'].mean().reset_index()
    return operators, students, mean_scores_students

def plot_interaction_scores(operators, students):
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plotting for Operators and Students
    for scenario, color in zip(['LOFW', 'SGTR'], ['blue', 'red']):
        subset_operators = operators[operators['Scenario'] == scenario]
        ax.plot(subset_operators['Fault Condition'], subset_operators['Mental Demand'], label=f'Operators - {scenario}', marker='o', markersize=5, linestyle='--', linewidth=2, color=color)
        
        subset_students = students[students['Scenario'] == scenario]
        ax.plot(subset_students['Fault Condition'], subset_students['Mental Demand'], label=f'Students - {scenario}', marker='o', markersize=5, linestyle='-', linewidth=2, color=color)

    ax.set_title('Mental Demand Scores; Students vs Operators Across Studies')
    ax.set_xlabel('Fault Condition')
    ax.set_ylabel('Mean Mental Demand Score')
    legend_elements = [Line2D([0], [0], color='black', lw=1, label='Operators', linestyle='--'),
                       Line2D([0], [0], color='black', lw=1, label='Students', linestyle='-'),
                       Patch(facecolor='blue', label='LOFW'),
                       Patch(facecolor='red', label='SGTR')]
    ax.legend(handles=legend_elements, title='Skill and Scenario')
    return fig, ax

def plot_mental_demand_scores(mean_scores_students):
    fig, ax = plt.subplots(figsize=(10, 6))
    for study, marker in zip(['Dependency', 'FATR'], ['^', 's']):
        for scenario, color in zip(['LOFW', 'SGTR'], ['blue', 'red']):
            subset = mean_scores_students[(mean_scores_students['Study'] == study) & (mean_scores_students['Scenario'] == scenario)]
            ax.plot(subset['Fault Condition'], subset['Mental Demand'], label=f'{study} - {scenario}', marker=marker, markersize=10, linestyle='-', linewidth=2, color=color)

    ax.set_title('Mental Demand Scores for Students; Normal vs FATR')
    ax.set_xlabel('Fault Condition')
    legend_elements = [
        Line2D([0], [0], marker='^', color='black', label='Dependency', linestyle='None', markersize=10),
        Line2D([0], [0], marker='s', color='black', label='FATR', linestyle='None', markersize=10),
        Patch(facecolor='blue', label='LOFW'),
        Patch(facecolor='red', label='SGTR')]
    ax.legend(handles=legend_elements, title='Study and Scenario')
    return fig, ax

print("mental.py loaded!")
