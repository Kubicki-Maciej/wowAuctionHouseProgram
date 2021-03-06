import csv


""" 
run it if is new row in items csv
file will be sorted alphabetical 
 """


def sort_csv(file_name):
    """ sort alphabetical"""

    with open(file_name, 'r', newline='') as f_input:
        csv_input = csv.DictReader(f_input)
        data = sorted(csv_input, key=lambda row: (row["name item"], row['id']))

    with open(file_name, 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
        csv_output.writeheader()
        csv_output.writerows(data)