import os
import tarfile
from os import listdir
from os.path import isfile, join
import pandas as pd

def uncompress_data(file_name_path):
    # documentation for tar functions
    # https://docs.python.org/3/library/tarfile.html

    #open tar.gz file
    tar = tarfile.open(file_name_path)

    #extracting files so we can open them
    #missing code to extract files here

    #close original compressed file
    tar.close()

    #we are manually returning the path of the extracted files
    return 'cell_data'


def read_directory_of_files(dir_path):

    #A placeholder varable to store our data
    data = None

    #Documentation on listing all files in a directory
    #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    #loop through the names of each file in the director
    for file_name in onlyfiles:

        #We have to prepend the directory name to the file name to get the full path
        file_name_path = os.path.join(dir_path, file_name)

        #print out the full path we are interested in
        print(file_name_path)

        #Using Pandas open the CSV file
        #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
        #Tutoral to open file
        #https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/

        # Read data from file file_name_path
        # Control delimiters, rows, column names with read_csv
        # missing command to read a csv file into a Pandas dataframe named current_data
        # current_data = [some missing code]
        
        # Preview the first 5 lines of the loaded data
        print(current_data.head())

        if data is None:
            data = current_data
        else:
            data = pd.concat([data,current_data])

    return data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    compressed_data_file_path = 'cell_data.tar.gz'

    #1 uncompress the source data
    #dir_path = uncompress_data(compressed_data_file_path)

    dir_path = 'cell_data'
    #read all files into memory
    data = read_directory_of_files(dir_path)
