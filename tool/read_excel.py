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


#!/bin/bash

# Define the directory to scan
DIR="/path/to/your/location"

# Define the variable to hold file names with accented characters
files_with_accents=""

# Find files with French accented characters
for file in $(grep -l '[éèêëàâäîïôöûüçÉÈÊËÀÂÄÎÏÔÖÛÜÇ]' "$DIR"/*); do
    # Add the file to the list
    files_with_accents+="$file "
done

# Print the list of files
echo "Files with accented characters: $files_with_accents"

# Loop through each file and replace accented characters
for file in $files_with_accents; do
    sed -i 's/é/e/g;s/è/e/g;s/ê/e/g;s/ë/e/g;s/à/a/g;s/â/a/g;s/ä/a/g;s/î/i/g;s/ï/i/g;s/ô/o/g;s/ö/o/g;s/û/u/g;s/ü/u/g;s/ç/c/g;s/É/E/g;s/È/E/g;s/Ê/E/g;s/Ë/E/g;s/À/A/g;s/Â/A/g;s/Ä/A/g;s/Î/I/g;s/Ï/I/g;s/Ô/O/g;s/Ö/O/g;s/Û/U/g;s/Ü/U/g;s/Ç/C/g' "$file"
done

echo "Accented characters replaced with English characters in all files."

