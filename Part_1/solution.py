import os
import datetime

def main():
    input_folder = "input_files"
    output_folder = "output_files"

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Dynamically find all input files
    input_files = sorted(f for f in os.listdir(input_folder) if f.startswith("input") and f.endswith(".txt"))

    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, input_file.replace("input", "output"))

        # Implement processing logic
        f = open(input_path, "r")

        lines = f.readlines()

        for i, line in enumerate(lines):
            lines[i] = line.replace("\n", "")

        n = lines[0]

        for i in (range (0, len(lines)-1)):
            i += 1

            if lines[i] == "":
                break
            print (lines[i])


        # Write the output



main()