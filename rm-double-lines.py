input_file = 'inp.txt'
output_file = 'outp.txt'

# Open the input file for reading
with open(input_file, 'r') as file:
    # Read the lines from the file and store them in a list
    lines = file.readlines()

# Remove duplicates from the list
lines = list(set(lines))

# Open the output file for writing
with open(output_file, 'w') as file:
    # Write the unique lines to the output file
    file.writelines(lines)

# Close the files
file.close()

print("Done")
