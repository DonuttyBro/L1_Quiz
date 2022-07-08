import csv

with open('04_Trivia_Quiz\Horror_Quiz.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f('Column names are {", ".join(row)}'))
            line_count += 1
        print(f('\t{row["Card Name"]} works in the {row["Answer"]} department, and was born in {row["Incorrect 1, Incorrect 2, Incorrect"]}.'))
        line_count += 1
    print(f('Processed {line_count} lines.'))