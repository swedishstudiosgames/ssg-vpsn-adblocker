# Import the requests, platform and re modules
import requests
import platform
import re

# Define a function to process a line of input
def process_line(line):
    # Use a regular expression to replace the prefix "0.0.0.0 " with "@@||"
    line = re.sub(r"^0\.0\.0\.0 ", "@@||", line)
    # Use a regular expression to add the suffix "^" to the end of the line
    line = re.sub(r"$", "^", line)
    # Return the processed line
    return line

# Define a function to get the letter after the "%" from a line
def get_letter(line):
    # Use a regular expression to find the letter after the "%"
    match = re.search(r"%(\w)", line)
    # If there is a match, return the letter
    if match:
        return match.group(1)
    # Otherwise, return a default value that will sort after all letters
    else:
        return "z"

# Get the data from the URL as a text
data = requests.get("https://raw.githubusercontent.com/swedishstudiosgames/ssg-vpsn-adblocker/master/allowlist.txt").text
# Split the data into lines
lines = data.splitlines(keepends=False)
# Process each line using the function defined above
lines = [process_line(line) for line in lines]
# Sort the list by the letter after the "%" using the function defined above
lines.sort(key=get_letter)

# Get the platform information using the platform module
system = platform.system() # The system/OS name
release = platform.release() # The system's release version
machine = platform.machine() # The machine type
processor = platform.processor() # The platform processor

# Print the platform information
print(f"The script is running on {system} {release} with {machine} and {processor}")

# Use the requests module to write the output file to the current working directory
with requests.Session() as session:
    # Create a stream to write the output file
    stream = session.post("output.txt", stream=True)
    # Write each line to the output file
    for line in lines:
        stream.write(line)
