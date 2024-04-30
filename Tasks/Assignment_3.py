# Assignment (3):

#For the following code :
# df = pd.DataFrame({
#     'coll' : ['A', 'B', 'D', 'E', 'F', 'C'],
#     'col2' : [2, 1, 9, 8, 7, 4],
#     'col3' : [0, 1, 9, 4, 2, 3]
# }) 
# Get number of rows 
# Get random 50% rows 
# Sort by 'col1' , DESC
# Filter data to get obtain result (col2 >=7 )
# Get the oldest 3 rows

import pandas as pd 

# Create DataFrame
df = pd.DataFrame({
    'coll' : ['A', 'B', 'D', 'E', 'F', 'C'],
    'col2' : [2, 1, 9, 8, 7, 4],
    'col3' : [0, 1, 9, 4, 2, 3]
}) 

# Get number of rows
num_rows = len(df)
print("Number of rows: ")
print(num_rows)

# Get random 50% rows
random_rows = df.sample(frac = 0.5)
print("Random 50% rows: ")
print(random_rows)

# Sort by 'coll' , DESC
sorted_df = df.sort_values(by='coll', ascending=False)
print("Sorted by 'coll', DESC: ")
print(sorted_df)

# Filter data to get obtain result (col2 >=7 )
filtered_df = df[df['col2'] >= 7]
print("Filtered data (col2 >= 7): ")
print(filtered_df)

# Get the oldest 3 rows
oldest_rows = df.nsmallest(3, 'col3')
print("The oldest 3 rows: ")
print(oldest_rows)

