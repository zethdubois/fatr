import os
import json
import pandas as pd
import tkinter as tk
from tkinter import ttk
import re


def classify_scenario_and_outcome(events):
    true_fault = 0  # Default to False (0)
    scenario = None
    outcome = None
    time = None

    # Step 1: Determine the "True Fault" attribute based on the first "Fault" event
    for event in events:
        if event.get('EventType') == 'Fault':
            if event.get('Tag') in ['FeedWaterPumpA', 'SGLevelSpoofA']:
                true_fault = 1  # Set True Fault based on specific Tags
            break  # Stop after evaluating the first "Fault" event

    # Step 2: Classify the scenario and other details
    for event in events:
        if 'Settings' in event and 'FaultTarget' in event['Settings']:
            settings = event['Settings']
            if settings.get('FaultTarget') == 'FATR':
                fault_value = settings.get('FaultTargetInitialValue')
                if fault_value == 2:
                    scenario = 'LOFW'
                elif fault_value == 3:
                    scenario = 'SGTR'
                time = event.get('Time')  # Assume time is set here for simplicity

        # Continue with outcome determination logic as before
        if event.get('Tag') == 'ManualReactorTrip' or event.get('Tag') == 'ManualTurbineTrip':
            outcome = 'Manual Activation'
        elif event.get('Tag') == 'FATR':
            if event.get('Command') == 'Continue':
                outcome = 'FATR Execute'
            elif event.get('Command') == 'Abort':
                outcome = 'FATR Cancel'

    if scenario and not outcome:
        outcome = 'FATR Timeout'

    return scenario, outcome, time, true_fault



def process_file(file_path, pid, trial_num):
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line.lower() == "missing":
                return {
                    'PID': pid,
                    'Trial': trial_num,
                    'Scenario': None,
                    'True Fault': None,  # Add placeholder for True Fault
                    'Outcome': None,
                    'Time': None,
                    'FileName': os.path.basename(file_path)
                }

            file.seek(0)  # Reset file pointer to the beginning
            events = []
            for line in file:
                data = json.loads(line)
                if data.get('EventType') in ['ControlAction', 'Alarm', 'Fault']:
                    events.append(data)

        scenario, outcome, time, true_fault = classify_scenario_and_outcome(events)
        return {
            'PID': pid,
            'Trial': trial_num,
            'Scenario': scenario,
            'True Fault': true_fault,  # Include True Fault in the return dictionary
            'Outcome': outcome,
            'Time': time,
            'FileName': os.path.basename(file_path)
        }

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None


    
def extract_pid(directory_name):
    # Extract PID from directory name
    if directory_name.startswith('p') and directory_name[1:].isdigit():
        return int(directory_name[1:]) + 12
    else:
        return None

def search_json_files(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        dir_name = os.path.basename(root)
        pid = extract_pid(dir_name)
        if pid is not None:
            sorted_files = sorted(f for f in files if f.endswith('.json'))
            for trial_num, file in enumerate(sorted_files, start=1):
                result = process_file(os.path.join(root, file), pid, trial_num)
                if result:
                    results.append(result)
    return results

# Function to print each row with background color for even PIDs
def print_with_color(df):
    # Print the header
    header = " | ".join(df.columns)
    print(header)
    print("-" * len(header))  # Print a separator line

    # Print each row
    for index, row in df.iterrows():
        formatted_row = " | ".join(str(item) for item in row)
        if row['PID'] % 2 == 0:
            print("\033[100m" + formatted_row + "\033[0m")  # Dark gray background for even PID
        else:
            print(formatted_row)  # No background color for odd PID

def create_popup_window(df):
    window = tk.Tk()
    window.title("Data Viewer")

    # Creating a frame for the TreeView
    frame = ttk.Frame(window)
    frame.pack(fill='both', expand=True)

    # Define the columns for the Treeview
    columns = list(df.columns)
    
    # Creating the TreeView with the defined columns
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    # Adding the column headings and setting column properties
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Style configuration for alternating background colors
    style = ttk.Style(window)
    style.configure("Treeview", rowheight=25)  # Adjust row height as needed
    tree.tag_configure('evenrow', background='#E0E0E0')  # Light gray color for even rows

    # Adding the data to the TreeView with alternating background colors
    is_even_row = False
    for _, row in df.iterrows():
        row_id = tree.insert('', tk.END, values=list(row))
        if row['PID'] % 2 == 0:  # Check if PID is even
            tree.item(row_id, tags=('evenrow',))
    tree.pack(fill='both', expand=True)

    window.mainloop()

def extract_date(file_name):
    # Extract the date
    date_match = re.search(r'(\d{1,2}-\d{1,2}-\d{4})', file_name)
    return date_match.group(1) if date_match else 'unknown-date'

def extract_copy_number(file_name):
    # Extract the copy number
    copy_match = re.search(r'_Copy\((\d+)\)', file_name)
    return copy_match.group(1).zfill(2) if copy_match else '00'



#--------------------------------------------------
directory = '.'  # Current directory
data = search_json_files(directory)
df = pd.DataFrame(data)
# Specify the file name for the CSV output
csv_file_name = 'classify_fatr_students.csv'

#--------------------------------------------------


# Sort the DataFrame by PID first, then by Trial, both in ascending order
df = df.sort_values(by=['PID', 'Trial'])

#--------------------------------------------------


# Write the DataFrame to a TSV file
df.to_csv(csv_file_name, sep='\t', index=False)

print(f"DataFrame has been saved as '{csv_file_name}'")

# Create and show the popup window
# create_popup_window(df)

# print(df)
