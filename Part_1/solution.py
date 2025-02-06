import os
from datetime import datetime, timedelta
from datetime import date
import statistics

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

        books = parse_in(input_path)
        print(books)



    # Write the output


def parse_in(input_path):


    # Implement processing logic
    f = open(input_path, "r")

    lines = f.readlines()

    for i, line in enumerate(lines):
        lines[i] = line.replace("\n", "")

    n = lines[0]

    title = ""
    books = {}
    newBook = True
    checkout = True

    for i in (range(1, len(lines) - 1)):

        if lines[i] == "":
            newBook = True
            checkout = True
            i += 1
            continue

        if newBook == True:
            title = lines[i]
            books[title] = {}
            books[title]["check_outs"] = []
            books[title]["check_ins"] = []
            newBook = False
        else:
            if checkout == True:
                books[title]["check_outs"].append(string_to_datetime(lines[i]))
                checkout = False
            else:
                books[title]["check_ins"].append(string_to_datetime(lines[i]))
                checkout = True

        i += 1

    books_with_count = count_borrows(books)
    books_with_idle_time = calculate_idle_time(books)

    return books_with_count

def string_to_datetime(date_string):
    date_list = date_string.split("/")
    return date(int(date_list[2]), int(date_list[1]), int(date_list[0]))

def count_borrows(books):
    for book in books.keys():
        books[book]["borrows"] = len(books[book]["check_ins"])

    return books

def calculate_idle_time(books):
    for book in books.keys():
        idle_times = []
        for i, checkin in enumerate(books[book]["check_ins"]):
            if i+1 < len(books[book]["check_outs"]):
                idle_times.append((books[book]["check_outs"][i+1])-checkin)

        books[book]["idle_time"] = sum(idle_times, timedelta(0)) / len(idle_times)
    return books








main()