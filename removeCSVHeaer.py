#! python3
# removeCSVHeader.py - Remove the header from all CSV files in the current working
# directory.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# loop through every file in the current working directory.
for csvfile in os.listdir('.'):
    if not csvfile.endswith('.csv'):
        continue
    print('Removing header from ' + csvfile + '...')
    
    # Read the csv file in (skipping the first row)
    csvRows = []
    csvFileObj = open(csvfile)
    reader = csv.reader(csvFileObj)
    for row in reader:
        if reader.line_num == 1:
            continue
        csvRows.append(row)
        
    csvFileObj.close()

    # Write out the csv file
    csvFileObj = open(os.path.join('headerRemoved', csvfile), 'w', newline='')
    writer = csv.writer(csvFileObj)
    for row in csvRows:
        writer.writerow(row)

    csvFileObj.close()
    
