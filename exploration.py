import pandas as pd
import matplotlib.pyplot as plt

attractionPath = '..\\case_disney_world\\data\\waiting times\\dinosaur.csv'
df = pd.read_csv(attractionPath)

prints = True

if prints:
    print(df.head())
    print('missing values in SACTMIN: ', df['SACTMIN'].isna().sum())
    print('missing values in SPOSTMIN: ', df['SPOSTMIN'].isna().sum())

### Investigating difference between actual and posted waiting time ###

# Add a new column 'both_missing' indicating whether both 'SACTMIN' and 'SPOSTMIN' are missing
df['both_missing'] = df['SACTMIN'].isna() & df['SPOSTMIN'].isna()

# Count how many times both 'SACTMIN' and 'SPOSTMIN' are missing
count_both_missing = df['both_missing'].sum()

# Print the count
if prints:
    print(f"Number of times both 'SACTMIN' and 'SPOSTMIN' are missing: {count_both_missing}")

# Add a new column 'both_filled' indicating whether both 'SACTMIN' and 'SPOSTMIN' are filled in
df['both_filled'] = ~df['SACTMIN'].isna() & ~df['SPOSTMIN'].isna()

# Count how many times both 'SACTMIN' and 'SPOSTMIN' are filled in
count_both_filled = df['both_filled'].sum()

# Print the count
if prints:
    print(f"Number of times both 'SACTMIN' and 'SPOSTMIN' are filled in: {count_both_filled}")

### Investigating actual waiting times and measurement frequency ###

# Create a subset where only 'SACTMIN' is filled in
dfActual = df[~df['SACTMIN'].isna()]

# Print the subset
if prints:
    print(dfActual.head())

# Convert the 'datetime' column to a datetime object
dfActual['datetime'] = pd.to_datetime(dfActual['datetime'])

# Sort the DataFrame based on the 'datetime' column
dfActual = dfActual.sort_values(by='datetime')

# Calculate the time differences between consecutive measurements
dfActual['time_diff'] = dfActual['datetime'].diff()
dfActual['time_diff_seconds'] = dfActual['time_diff'].dt.total_seconds()

# Summary statistics
summary_stats = dfActual['time_diff_seconds'].describe()
if prints:
    print("Summary Statistics for Waiting Times: ", summary_stats)

lim = 0.5e6

plt.figure(figsize=(10, 6))
plt.hist(dfActual['time_diff_seconds'].dropna(), bins=30, range=(0,lim), color='skyblue', edgecolor='black')
plt.title('Distribution of Waiting Times')
plt.xlabel('Waiting Time (minutes)')
plt.ylabel('Frequency')
#plt.show()

# Visualize the time differences
plt.figure(figsize=(10, 6))
plt.plot(dfActual['datetime'], dfActual['time_diff'].dt.total_seconds(), marker='o', linestyle='', color='b')
plt.title('Time Differences Between Consecutive Measurements')
plt.xlabel('Datetime')
plt.ylabel('Time Difference (seconds)')
plt.xticks(rotation=45)
plt.ylim(0, lim)
plt.show()