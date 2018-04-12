import os
import csv


def split(path: str,
          delimiter=',',
          row_limit=500,
          output_name_template='output_%s.csv',
          output_path='.',
          keep_headers=True):
    """
    A function that split a large csv file to chunks.
    """

    filehandler = open(path, 'r', encoding='utf8')
    reader = csv.reader(filehandler, delimiter=delimiter)
    
    piece_curr = 1
    current_out_path = os.path.join(output_path,
                                    output_name_template % 
                                    piece_curr)
    current_out_writer = csv.writer(
        open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.__next__()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            
            piece_curr += 1
            current_limit = row_limit * piece_curr
            current_out_path = os.path.join(
                output_path, output_name_template % 
                piece_curr)
            current_out_writer = csv.writer(
                open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


if __name__ == "__main__":

    large_file = 'diabetes_dataset.csv'
    split(large_file, output_name_template=large_file.split('.')[0]+"_%s.csv")
