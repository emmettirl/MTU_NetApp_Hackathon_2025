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

        title = ""
        books = {}
        newBook = True

        for i in (range (1, len(lines)-1)):

            if lines[i] == "":
                newBook = True
                i+=1
                continue

            if newBook == True:
                title = lines[i]
                books[title] = []
                newBook = False
            else:
                books[title].append(lines[i])

            i += 1

        print (books)



        # Write the output



main()