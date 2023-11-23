import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_index = None
    end_index = None

    # Find the first occurrence of the word 'record'
    for i, line in enumerate(lines):
        if 'record' in line:
            start_index = i
            break

    # Find the last occurrence of the word 'end'
    for i in range(len(lines) - 1, -1, -1):
        if 'end' in lines[i]:
            end_index = i
            break

    # If both start and end are found, extract the lines between them
    if start_index is not None and end_index is not None:
        result_lines = lines[start_index + 1:end_index]
        
        # Write the result back to the file
        with open(file_path, 'w') as file:
            file.writelines(result_lines)
    else:
        print(f"Could not find 'record' and/or 'end' in {file_path}")

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            process_file(file_path)

# Replace 'your_folder_path' with the path to your Windows folder
folder_path = r'C:\Windows'
process_files_in_folder(folder_path)
