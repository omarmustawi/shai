import pandas as pd

# Load the dataset
salaries_df = pd.read_csv('./Salaries.csv')

# Identify the number of rows and columns
num_rows, num_columns = salaries_df.shape

# Determine the data types of each column
data_types = salaries_df.dtypes

# Check for missing values in each column
missing_values = salaries_df.isnull().sum()

# Display the results
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
print("\nData Types:")
print(data_types)
print("\nMissing Values:")
print(missing_values)
# Calculate basic statistics
basic_stats = salaries_df.describe()

# Determine the range of salaries
salary_range = salaries_df['TotalPay'].max() - salaries_df['TotalPay'].min()

# Find the standard deviation of salaries
salary_std_dev = salaries_df['TotalPay'].std()

# Display the results
print("\nDescriptive Statistics:")
print(basic_stats)
print(f"\nRange of Salaries: {salary_range}")
print(f"Standard Deviation of Salaries: {salary_std_dev}")
# Drop rows with missing values
salaries_df_cleaned = salaries_df.dropna()


import matplotlib.pyplot as plt

# Create a histogram to visualize the distribution of salaries
plt.hist(salaries_df['TotalPay'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Salaries')
plt.xlabel('Total Pay')
plt.ylabel('Frequency')
plt.show()

# Create a pie chart to represent the proportion of employees in different departments
department_counts = salaries_df['JobTitle'].value_counts()
top_departments = department_counts.head(5)  # Displaying the top 5 departments
plt.pie(top_departments, labels=top_departments.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Employees in Top 5 Departments')
plt.show()
# Group the data by job title and calculate average salaries
average_salaries_by_job = salaries_df.groupby('JobTitle')['TotalPay'].mean()

# Display the results
print("\nAverage Salaries by Job Title:")
print(average_salaries_by_job)


# Identify correlation between salary and another numerical column (e.g., OvertimePay)
correlation = salaries_df['TotalPay'].corr(salaries_df['OvertimePay'])

# Plot a scatter plot to visualize the relationship
plt.scatter(salaries_df['OvertimePay'], salaries_df['TotalPay'])
plt.title('Scatter Plot: OvertimePay vs TotalPay')
plt.xlabel('Overtime Pay')
plt.ylabel('Total Pay')
plt.show()

# Display the correlation coefficient
print(f"\nCorrelation between TotalPay and OvertimePay: {correlation}")

