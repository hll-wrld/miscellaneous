import csv

dat_file = 'input.dat'
csv_file = 'output.csv'

# Open the .dat file for reading with the correct encoding
with open(dat_file, 'r', encoding='ISO-8859-1') as file:
    # Read the contents of the .dat file
    contents = file.read()

# Split the contents into rows
rows = contents.split('\n')

# Split each row into individual data elements and write to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        data = row.split()  # Adjust this line if your data is separated by a different delimiter
        writer.writerow(data)