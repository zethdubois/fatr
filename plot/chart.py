import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def load_data(data_path):
    data = pd.read_csv(data_path)
    return data

def prepare_data(data,group_iv,g1,g2,iv1,iv2,dv1):
    g1_mean, g2_mean, mean_scores_students = [],[],[]
    mean_scores = data.groupby([group_iv, iv1, iv2])[dv1].mean().reset_index()
    # print(group_iv)
    # print(g1)
    # print(mean_scores)
    g1_mean = mean_scores[mean_scores[group_iv] == g1]
    g2_mean = mean_scores[mean_scores['Expertise'] == 'Student']
    # mean_scores_students = new_data[new_data['Expertise'] == 'Student'].groupby(['Study', 'Scenario', 'Fault Condition'])[dv].mean().reset_index()
    return g1_mean, g2_mean, mean_scores_students

def plot_interaction_scores(operators, students, iv1, iv2, dv1, tit1, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    # Use the provided ax for plotting
    for scenario, color in zip(['LOFW', 'SGTR'], ['blue', 'red']):
        # Operators
        subset_operators = operators[operators['Scenario'] == scenario]
        ax.plot(subset_operators['Fault Condition'], subset_operators[dv1], label=f'Operators - {scenario}', marker='o', markersize=5, linestyle='--', linewidth=2, color=color)
        # Students
        subset_students = students[students['Scenario'] == scenario]
        ax.plot(subset_students['Fault Condition'], subset_students[dv1], label=f'Students - {scenario}', marker='o', markersize=5, linestyle='-', linewidth=2, color=color)

    ax.set_title(tit1)
    ax.set_xlabel(iv2)
    ax.set_ylabel(iv1)
    legend_elements = [Line2D([0], [0], color='black', lw=1, label='Operators', linestyle='--'),
                   Line2D([0], [0], color='black', lw=1, label='Students', linestyle='-'),
                   Patch(facecolor='blue', label='LOFW'),
                   Patch(facecolor='red', label='SGTR')]
    ax.legend(handles=legend_elements)

def plot_mental_demand_scores(mean_scores_students, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    # Plotting logic using ax
    for study, marker in zip(['Dependency', 'FATR'], ['^', 's']):
        for scenario, color in zip(['LOFW', 'SGTR'], ['blue', 'red']):
            subset = mean_scores_students[(mean_scores_students['Study'] == study) & (mean_scores_students['Scenario'] == scenario)]
            ax.plot(subset['Fault Condition'], subset[dv1], label=f'{study} - {scenario}', marker=marker, markersize=10, linestyle='-', linewidth=2, color=color)

    ax.set_title('Mental Demand Scores for Students; Normal vs FATR')
    ax.set_xlabel('Fault Condition')
    legend_elements = [
        Line2D([0], [0], marker='^', color='black', label='Dependency', linestyle='None', markersize=10),
        Line2D([0], [0], marker='s', color='black', label='FATR', linestyle='None', markersize=10),
        Patch(facecolor='blue', label='LOFW'),
        Patch(facecolor='red', label='SGTR')]
    ax.legend(handles=legend_elements)

print("chart.py loaded!")
