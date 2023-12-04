import re

# Define a regular expression pattern to match AutoSys job definitions
pattern = r'insert_job:\s+(\w+)\s+(?:.*?command:\s+(.*?)\s+|$)'

# Open the .oil file and read its contents
with open('your_autosys_file.oil', 'r') as file:
    file_contents = file.read()

# Find all matches of the pattern in the file contents
matches = re.findall(pattern, file_contents, re.MULTILINE | re.DOTALL)

# Extract AutoSys job names and commands
autoSysJobs = []

for match in matches:
    job_name = match[0].strip()
    command = match[1].strip() if len(match) > 1 else None  # Capture the command if present
    if job_name and command:
        autoSysJobs.append({"job_name": job_name, "command": command})

# Print the extracted AutoSys job names and commands
for job in autoSysJobs:
    print(f"Job Name: {job['job_name']}")
    print(f"Command: {job['command']}\n")
