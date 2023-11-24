import pandas as pd

# Load the Excel file into a DataFrame
excel_file = 'data.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Group the DataFrame by ID and aggregate the sum of values in column D
grouped = df.groupby('ID')['Value'].sum().reset_index()

# Iterate over each unique ID and create a file for each with the aggregated value
for _, row in grouped.iterrows():
    id_value = row['ID']
    sum_value = row['Value']
    
    # Create a file named "<id>.txt" and write the sum value to it
    file_name = f"{id_value}.txt"
    with open(file_name, 'w') as file:
        file.write(f"ID: {id_value}\nSum of Values in Column D: {sum_value}")

print("Files created successfully.")
