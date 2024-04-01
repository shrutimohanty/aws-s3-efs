import subprocess
import os

# Define the ranges for x, y, and z
x_values = [50, 100, 500]
y_values = [1, 10, 50, 100]
z_values = ['s3', 'efs']

# Ensure the output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Iterate over all combinations of x, y, and z
for x in x_values:
    for y in y_values:
        for z in z_values:
            # Construct the command to run the Python program with the current x, y, and z
            command = ["python", "program.py", str(x), str(y), z]
            
            # Execute the command and capture the output
            result = subprocess.run(command, capture_output=True, text=True)
            
            # Define the output file name based on current x, y, and z
            output_file = os.path.join(output_dir, f"out-{z}-{x}-{y}.txt")
            
            # Save the output to the file
            with open(output_file, "w") as file:
                file.write(result.stdout)

            print(f"Output saved to {output_file}")

