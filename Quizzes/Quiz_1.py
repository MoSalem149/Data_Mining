# Create the following employees information List all employees with salary greater than 50000 and sick days greater than 5. 
#Using seaborne create boxplot for salary attribute. The table: 
#Name Attribute [Graham Chapman, John Cleese, Eric Idle, Terry Jones, Elina Gilliam, Michael Palin] 
#Hired Attribute [3/15/2014, 6/1/2015, 5/12/2014, 11/1/2013, 8/12/2014, 5/23/2013] 
#Salary Attribute [50000, 65000, 45000, 70000, 48000, 66000] Sick Days Attribute [10, 8, 10, 3, 7, 8]

# Import Important Packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Name': ['Graham Chapman', 'John Cleese', 'Eric Idle', 'Terry Jones', 'Elina Gilliam', 'Michael Palin'],
    'Hired': ['3/15/2014', '6/1/2015', '5/12/2014', '11/1/2013', '8/12/2014', '5/23/2013'],
    'Salary': [50000, 65000, 45000, 70000, 48000, 66000],
    'Sick Days': [10, 8, 10, 3, 7, 8]
}

df = pd.DataFrame(data)
print(df)

# Convert Hired to datetime
df['Hired'] = pd.to_datetime(df['Hired'])

# Filter data where Salary > 50000 and Sick Days > 5
filtered_df = df[(df['Salary'] > 50000) & (df['Sick Days'] > 5)]
print("Filtered Employees:")
print(filtered_df)

# Create Boxplot for the Salary attribute
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Salary'])
plt.title('Boxplot of Employee Salaries')
plt.show()