import re

# Define a regular expression pattern to match AutoSys job definitions
pattern = r'^insert_job\s*:\s*(\w+)\s*:\s*'

# Open the .oil file and read its contents
with open('your_autosys_file.oil', 'r') as file:
    file_contents = file.read()

# Find all matches of the pattern in the file contents
matches = re.findall(pattern, file_contents, re.MULTILINE)

# Extract AutoSys job names and commands
autoSysJobs = []
for job_name in matches:
    # Define a new pattern to match the command section of the job definition
    job_pattern = r'^insert_job\s*:\s*{}\s*:(.*?)\n\s*insert_job'.format(job_name)
    job_match = re.search(job_pattern, file_contents, re.DOTALL | re.MULTILINE)
    
    if job_match:
        # Extract the command section and clean it up (remove leading/trailing whitespaces)
        command = job_match.group(1).strip()
        autoSysJobs.append({"job_name": job_name, "command": command})

# Print the extracted AutoSys job names and commands
for job in autoSysJobs:
    print(f"Job Name: {job['job_name']}")
    print(f"Command: {job['command']}\n")
