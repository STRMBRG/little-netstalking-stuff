import os
import time

# Creating a list of available programs
programs = {
    "1": "DeepScan.py",
    "2": "PortScan.py"
}

# Displaying a message before the script starts
print('Launcher by STRMBRG & OpenAI')
time.sleep(0.8)

# Displaying a list of programs
print("Available programs:")

for key, value in programs.items():
    print(f"{key}. {value}")

# Get the number of the selected program from the user
program_number = input("Enter program number: ")

# Launch the program selected by the user, if it is in the list of available
if program_number in programs:
    program_name = programs[program_number]
    
    # Check the existence of a file with the specified name and run it if it exists
    if os.path.isfile(f"PyProgs/{program_name}"):
        os.system(f"python PyProgs/{program_name}")
        
        print(f"Program {program_name} completed")
    
    else:
        print(f"Error: program {program_name} not found!")
else:
    print("Error: Wrong program number!")
