# Familiarizing myself with csv.reader/writer in Python. Received this from
# Pythons docs @ https://docs.python.org/3/library/csv.html

if __name__ == '__main__':

    import csv
    import pandas as pd
    import os
    # Will be using glob to retrieve files/pathnames '.csv'
    import glob
    import pyodbc


    received_files = []
    # Using os.chdir to change the current working directory to 'Received Files'
    # https://stackoverflow.com/questions/39838332
    # /reading-multiple-csv-files-from-different-directories-into-pandas-dataframe
    os.chdir('Received Files')
    # the glob module finds all pathnames matching a specified pattern, in this case '.csv'.
    for files in glob.glob("*.csv"):
        # Appending the files to the list 'fileList'
        received_files.append(files)

    #print(received_files)

    def Organize_CSV(received_files):
        # Using i as an iterative variable within my method.
        i = 0
        #import csv
        # Downloaded and installed Pandas to be used for the data within this script.
        import pandas as pd

        # Setting up some lists to be populated with SKUs, prices and supplier names.
        SKU = []
        price = []
        addName = []


        for x in received_files:
            # Grabbing the filename each time my loop iterates.
            file_name = received_files[i]

            # Strip method:
            # https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
            stripped_path = file_name.strip('.csv')  # Trimming .csv from the string.

            # I am reading in my csv files and assigning them to df.
            df = pd.read_csv(received_files[i])
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
            fileObject = open(received_files[i], 'r')
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

        dict = {'SKU': SKU, 'PRICE': price, 'SUPPLIER': addName}
        # Adding to the dataframe.
        df = pd.DataFrame(dict)
        # Writing to csv.
        # Setting SKU as my index, which removes the indexing column that was before my data.
        df = df.set_index('SKU')
        df.to_csv(r"C:/Users/codyw/PycharmProjects/CSV Project/Final CSV File/newFile.csv")



        return 'Hello'



    print(Organize_CSV(received_files))
    print('Opening acess..')
    print(pyodbc.drivers())

    #import os
    newfile = []
    print(os.getcwd())
    os.chdir("..")
    os.chdir('Final CSV File')


    new_csv_data = pd.read_csv('newFile.csv')
    df = pd.DataFrame(new_csv_data)
    print(df.head())
    # After getting my SQL Server set up I used Boltic & W3 to connect to my database using Python:
    # https://www.boltic.io/blog/python-connect-to-sql-server
    # https://www.w3schools.com/sql/sql_create_table.asp
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=WOODYFOSHO\\MY_TEST_INSTANCE;'
                      'DATABASE=Test;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    #SQLString = "CREATE TABLE Product (ID varchar(20))"
    #insert statement, for loop

    if cursor.tables(table='Product', tableType='TABLE').fetchone():
        print('exists')

    else:
        cursor.execute('''
                    CREATE TABLE Products (
                        SKU varchar(20),
                        PRICE varchar(20),
                        SUPPLIER varchar(30))''')
        for row in df.itertuples():
            cursor.execute(''' INSERT INTO Products (SKU, PRICE, SUPPLIER)
            VALUES (?,?,?)''',row.SKU, row.PRICE, row.SUPPLIER)

    if cursor.tables(table='TableName', tableType='TABLE').fetchone():
        print("exists")

    conn.commit()
    cursor.close()



