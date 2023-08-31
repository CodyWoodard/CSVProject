# Familiarizing myself with csv.reader/writer in Python. Received this from
# Pythons docs @ https://docs.python.org/3/library/csv.html
if __name__ == '__main__':

    import os
    # This block of code was built using:
    # https://stackoverflow.com/questions/10149263/extract-a-part-of-the-filepath-a-directory-in-python
    Bobs_Path = os.path.abspath('BobsParts.csv')
    Insta_Path = os.path.abspath('Instamonia.csv')
    Vanilla_Path = os.path.abspath('VanillaAndCanolaSpecialists.csv')

    List_Of_Files = [Bobs_Path, Insta_Path, Vanilla_Path]  # Populating a list with the filepaths.

    # path_stripper is a function that takes in my list of filepaths,
    # extracts the filename, and populates a new list with the filename which will be used later.
    def path_stripper(List_Of_Files):
        i = 0
        Parsed_Filenames = []
        for x in List_Of_Files:
            #
            parent_directory, directory_name = os.path.split(List_Of_Files[i])
            #print(directory_name)
            # Learning about the strip method:
            # https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
            stripped_path = directory_name.strip('.csv')  # Trimming .csv from the string.
            #print(stripped_path)
            Parsed_Filenames.append(stripped_path)  # Appending the suppliers name to a new list.
            #print(Parsed_Filenames[i])
            i += 1
        return Parsed_Filenames

# Creating a method that will read & write csv files dynamically.
    def list_of_csv_file_file(List_Of_Files):
        i = 0
        import csv
        for x in List_Of_Files:
            # Getting my filename.csv assigned to directory_name
            parent_directory, directory_name = os.path.split(List_Of_Files[i])
            print(directory_name)
            i += 1
            # reading each csv file.
            # Watched this video on reading and writing csv files in Python:
            # https://www.youtube.com/watch?v=q5uM4VKywbA
            with open(directory_name, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for line in csvreader:
                    print(line)

        # Once I learn how to save columns to a list I will save the first column
        # In each csv file to be used later to populate my final csv fle.
        # Taking inspiration from this solution on Stack overflow:
        # https://stackoverflow.com/questions/22806792/append-columns-of-a-csv-file-to-lists
        columns = []
        for row in csv.reader(directory_name, delimiter=','):
            columns.append(row[0])

        return columns

    print(list_of_csv_file_file(List_Of_Files))
    #print(path_stripper(List_Of_Files))

    #def organize_csv(List_of):
     #   columns = []
      #  for row in csv.reader(infile, delimiter="\t"):
       #     columns.append(row[1])  # here row[1] is the second column

