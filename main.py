# Familiarizing myself with csv.reader/writer in Python. Received this from
# Pythons docs @ https://docs.python.org/3/library/csv.html

if __name__ == '__main__':

    import os
    import csv
    import pandas as pd
    from csv import writer
    # Assigning csv filenames to variables
    Bobs = 'BobsParts.csv'
    Insta = 'Instamonia.csv'
    Vanilla = 'VanillaAndCanolaSpecialists.csv'
    Test = 'Test.csv'

    List_Of_Files = [Bobs, Insta, Vanilla, Test]  # Populating a list with the csv files.


    def Organize_CSV(list_of_files):
        # Using i as an iterative variable within my method.
        i = 0
        import csv
        # Downloaded and installed Pandas to be used for the data within this script.
        import pandas as pd

        # Setting up some lists to be populated with SKUs, prices and supplier names.
        SKU = []
        price = []
        addName = []




        for x in list_of_files:
            # Grabbing the filename each time my loop iterates.
            file_name = List_Of_Files[i]

            # Strip method:
            # https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
            stripped_path = file_name.strip('.csv')  # Trimming .csv from the string.

            # I am reading in my csv files and assigning them to df.
            df = pd.read_csv(List_Of_Files[i])
            # newSKU is a list to hold the contents of column[0] (SKUs), however, without the
            # .values method I couldn't write the contents of newSKU to a new file correctly
            # because I was creating a list of lists, when I only needed the values of column 0 to populate a list
            # at each iteration.
            newSKU = df[df.columns[0]].values.tolist()
            # The append method wouldn't work here because of the list of lists issue. Once I figured out that I could
            # use .extend instead of append my newFile started populating correctly.
            SKU.extend(newSKU)

            # I used a simple for loop to give me an iteration of lines in each file,
            # (if the file had 13 lines in BobsParts, than BobsParts was loaded into the addName list 13 times.)
            # Used later in the program to write to a new csv file.
            for l in newSKU:
                addName.append(stripped_path)

            # I am certain there is a better way to do this using Pandas, but this does work.
            # Reading the csv file in and assigning it to fileObject.
            fileObject = open(List_Of_Files[i], 'r')
            # DictReader is mapping the information in each row to a dict,
            # whose keys are given by the optional fieldnames parameter.
            # https://docs.python.org/3/library/csv.html#csv.DictReader
            # https://www.geeksforgeeks.org/python-read-csv-columns-into-list/
            file = csv.DictReader(fileObject)
            for col in file:
                # Retrieving the column  named 'PRICE' and appending to the price list.
                price.append(col["PRICE"])

            i += 1

        # Created a dictionary with my lists
        # https://www.geeksforgeeks.org/python-save-list-to-csv/
        # Okay, 'SKU' 'PRICE' & 'SUPPLIER' are my keys, which will be used to populate the corresponding columns.

        dict = {'SKU': SKU, 'PRICE': price,'SUPPLIER': addName}
        # Adding to the dataframe.
        df = pd.DataFrame(dict)
        # Writing to csv.
        # Setting SKU as my index, which removes the indexing column that was before my data.
        df = df.set_index('SKU')
        df.to_csv('newFile.csv')


        return "Done, check out 'newFile.csv'"

    print(Organize_CSV(List_Of_Files))

