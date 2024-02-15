import os
import re
from os.path import join as _join, split as _split, basename
import pandas as pd
from collections import Counter
import csv
from glob import glob

# Regular expression to find numeric sequences in the filenames
numeric_part_re = re.compile(r'\d+')

def numeric_order(file_name):
    """
    Extracts all numeric parts from the file name and returns a tuple of integers.
    This is used for sorting files numerically based on these numbers.
    """
    numbers = numeric_part_re.findall(file_name)
    return tuple(int(num) for num in numbers)

ts_fns = glob('*/*.csv')
# Sort files by numeric order using the custom sorting function
ts_fns.sort(key=numeric_order)

trial_counter = Counter()
def process(ts_fn):
    head, tail = _split(ts_fn)
    tail_no_ext = tail.replace('.csv', '')
    meta = tail_no_ext.split('_')
    meta = meta[0]
    meta = meta.split('-')
    pid = head[1:]
    trial_counter[pid] += 1
    trial_num = trial_counter[pid]
    
    if len(meta) > 3:
        fault = meta[3]
    else:
        fault = "True"
    
    df = pd.read_csv(ts_fn)
    last_row = df.iloc[-1].to_dict()
    
    time_str = last_row['PlantElapsedTIme']
    h, m, s = time_str.split(':')
    time_in_seconds = int(h) * 3600 + int(m) * 60 + float(s)
    
    trip_df = df.loc[df['GovernorValve'] == 0]
    if not trip_df.empty:
        diagnosis_time = str(trip_df.iloc[0]['PlantElapsedTIme'])
        h, m, s = diagnosis_time.split(':')
        diagnosis_time = int(h) * 3600 + int(m) * 60 + float(s)
    else:
        diagnosis_time = time_in_seconds
        
    return dict(pid=pid, trial_num=trial_num, 
                fault=fault, time=time_in_seconds, 
                mode=int(last_row['ModeValue']) / 5,
                diagnosis_time=diagnosis_time,
                filename=tail_no_ext)

# Get the current working directory's name
directory_name = basename(os.getcwd())

# Format the output file name according to the specified format
output_file_name = f'timeseries_{directory_name}.csv'

fp = open(output_file_name, 'w', newline='', encoding='utf-8')

fieldnames = []

for i, ts_fn in enumerate(ts_fns):
    print(ts_fn)
    d = process(ts_fn)
    if i == 0:
        fieldnames = list(d.keys())
        wtr = csv.DictWriter(fp, fieldnames=fieldnames)
        wtr.writeheader()
        
    wtr.writerow(d)

fp.close()
