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
        # print(books)

        sorted_list = sort_books(books)
        parse_out(output_path, sorted_list)

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
    books_with_total_borrow_time = sum_borrow_time(books)

    return books_with_total_borrow_time

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
        books[book]["min_idle_time"] = min(idle_times)
    return books

def sum_borrow_time(books):
    for book in books.keys():
        borrow_times = []
        for i, checkout in enumerate(books[book]["check_outs"]):
            if i < len(books[book]["check_ins"]):
                borrow_times.append( (books[book]["check_ins"][i]) - checkout )

        books[book]["total_borrow_time"] = sum(borrow_times, timedelta(0))
        books[book]["longest_borrow"] = max(borrow_times)
    return books


def sort_books(books):
    sorting_list = []
    for book in books.keys():
        sorting_list.append((book, books[book]["borrows"], books[book]["min_idle_time"]))

    sorted_by_borrows_idletime_alpha = sorted(sorting_list, key=lambda tup: (tup[1], tup[2], tup[0]))

    sorted_list = []
    for book in sorted_by_borrows_idletime_alpha:
        sorted_list.append((book[0], books[book[0]]))

    print(sorted_list)
    return sorted_list

def parse_out(output_path, sorted_list):
    f = open(output_path, "w")
    f.write("")
    f.close()

    f = open(output_path, "a")
    f.write("Book Name:In/Out Pairs,Idle Time,Total Borrowed,Longest Borrow,Shortest Idle\n")
    for i in range(0, len(sorted_list)):
        f.write(f'{sorted_list[i][0]}: {sorted_list[i][1]["borrows"]}, {int(sorted_list[i][1]["idle_time"].days)}, {int(sorted_list[i][1]["total_borrow_time"].days)}, {int(sorted_list[i][1]["longest_borrow"].days)}, {int(sorted_list[i][1]["min_idle_time"].days)} \n')

    f.close()

main()