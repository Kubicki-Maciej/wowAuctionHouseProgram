import csv
import pandas as pd

""" run it if is new row in items csv """
def sort_csv():
    with open('items.csv', 'r', newline='') as f_input:
        csv_input = csv.DictReader(f_input)
        data = sorted(csv_input, key=lambda row: (row["name item"], row['id']))

    with open('items.csv', 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
        csv_output.writeheader()
        csv_output.writerows(data)

# with open('items.csv', newline='') as csvfile:
