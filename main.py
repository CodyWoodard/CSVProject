# Familiarizing myself with csv.reader/writer in Python. Received this from
# Pythons docs @ https://docs.python.org/3/library/csv.html
if __name__ == '__main__':

    import os
    import csv
    import pandas as pd
    from csv import writer
    # This block of code was built using:
    # https://stackoverflow.com/questions/10149263/extract-a-part-of-the-filepath-a-directory-in-python
    Bobs_Path = os.path.abspath('BobsParts.csv')
    Insta_Path = os.path.abspath('Instamonia.csv')
    Vanilla_Path = os.path.abspath('VanillaAndCanolaSpecialists.csv')
    #Test_Path = os.path.abspath('Test.csv')

    List_Of_Files = [Bobs_Path, Insta_Path, Vanilla_Path]  # Populating a list with the filepaths.
    #print(Bobs_Path)
    # path_stripper is a function that takes in my list of filepaths,
    # extracts the filename, and populates a new list with the filename which will be used later.
    headerlist = ['SKU', 'PRICE', 'SUPPLIER']

    with open('newFile.csv', 'w', newline='') as csvOutput:
        newfile = csv.DictWriter(csvOutput, delimiter=',', fieldnames=headerlist)
        newfile.writeheader()


    def Organize_CSV(List_Of_Files):
        i = 0
        import csv
        import pandas as pd

        Parsed_Filenames = []
        csvFilenames = []
        SKU = []
        price = []
        addName = []
        for x in List_Of_Files:
            #
            parent_directory, directory_name = os.path.split(List_Of_Files[i])
            print(directory_name)
            # Learning about the strip method:
            # https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
            stripped_path = directory_name.strip('.csv')  # Trimming .csv from the string.
            #print(stripped_path)

            csvFilenames.append(directory_name)
            Parsed_Filenames.append(stripped_path)  # Appending the suppliers name to a new list.
            #print(Parsed_Filenames[i])
            df = pd.read_csv(List_Of_Files[i])
            #SKU = df.iloc[:0]
            #df[df.columns[0]]
            #df = pd.read_csv(List_Of_Files[i])
            #matrix2 = df[df.columns[0]]
            #SKU.append(matrix2.tolist())
            # Retrieving the column  named 'PRICE' and appending to a list.
            filename = open(List_Of_Files[i], 'r')
            file = csv.DictReader(filename)
            for col in file:
                price.append(col["PRICE"])

            newSKU = df[df.columns[0]].values.tolist()
            SKU.extend(newSKU)
            #for col in file:
             #   SKU.append(col['PN'])

            csvInfo = []
            #newSKU = []
            #newPrice = []

            #newPrice.append(price[i])
            #newSKU.append(SKU[i])
            addName.append(Parsed_Filenames[i])
            # directory_name = csvFilenames[k]
            # reading each csv file.
            # Watched this video on reading and writing csv files in Python:
            # https://www.youtube.com/watch?v=q5uM4VKywbA

            # Rather than adding to a Csv file,
            # this is erasing the new file each iteration and rewriting.
            #from csv import writer
            #print(directory_name)
            #with open(directory_name, 'r') as csvfile:
             #   csvreader = csv.reader(csvfile)
              #  rows = list(csvreader)
                #next(csvreader, None)

            #for row in rows:
             #   row.append(price)

            #with open('newFile.csv', 'w', newline='') as f:
             #   writer = csv.writer(f)
              #  writer.writerow(rows[3])

            # with open('newFile.csv', 'a') as fileObject:
                   # writerObject = writer(fileObject)
                    #for row in csvreader:
                     #   writerObject.writerow(row + addName)
                      #  print(row)

            i += 1


        print(SKU)
        print(price)
        print(addName)
        #print(List_Of_Files)
        ExtractedData = [SKU, price, addName]
        dict = {'SKU': SKU, 'PRICE': price}
        df = pd.DataFrame(dict)
        df.to_csv('newFile.csv')
        #i = 0
        #j = 0


        #for x in List_Of_Files:
            # Retrieving the first column in my new csv files.

         #   i += 1
        #k = 0

        #print(directory_name)
        #for x in Parsed_Filenames:

         #   with open('newFile.csv', 'a') as fileObject:
          #      writerObject = writer(fileObject)

           #     for row in newfile.csv:
            #        writerObject.writerow(row + addName)



            #with open('newFile.csv', 'a') as fileObject:
             #   writerobject = writer(fileObject)
              #  for row in csvreader:

        #for x in List_Of_Files[k-1]:
         #   from csv import writer
          #  with open('newFile.csv', 'a') as fileObject:

           #     writerObject = writer(fileObject)
            #    writerObject.writerow(row + addName)
             #   fileObject.close()

        #k += 1


        #print(row)
        #print(SKU)
        #print(price)
        #print(addName)
        #print(csvInfo)
        return ExtractedData


# Creating a method that will read & write csv files dynamically.
    def list_of_csv_file_file(List_Of_Files):
        i = 0

        newcsvfiles = []
        import csv
        import pandas as pd
        for x in List_Of_Files:
            # Getting my filename.csv assigned to directory_name
            parent_directory, directory_name = os.path.split(List_Of_Files[i])
            print(directory_name)
            stripped_path = directory_name.strip('.csv')
            i += 1
            filenameslist = []
            filenameslist.append(stripped_path)

            # reading each csv file.
            # Watched this video on reading and writing csv files in Python:
            # https://www.youtube.com/watch?v=q5uM4VKywbA
            with open(directory_name, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                with open('new' + directory_name, 'w') as csvOutput:
                    newfile = csv.writer(csvOutput)
                    for line in csvreader:
                        # Appending the filename to a new column.
                        newfile.writerow(line + filenameslist)


            newcsvfiles.append('new' + directory_name)
            filenameslist.remove(stripped_path)

        return newcsvfiles




        # Once I learn how to save columns to a list I will save the first column
        # In each csv file to be used later to populate my final csv fle.
        # Taking inspiration from this solution on Stack overflow:
        # https://stackoverflow.com/questions/22806792/append-columns-of-a-csv-file-to-lists



# Will use this method to save the desired data (SKU, PRICE, SUPLIER)
    # from the current csv files, Write to one new one.
    #def organize_csvfiles(newcsvfiles):
        # saved all items under the header PRICE using,
        # https://www.geeksforgeeks.org/python-read-csv-columns-into-list/
     #   import csv
      #  import pandas as pd


    #print(list_of_csv_file_file(List_Of_Files,))
    print(Organize_CSV(List_Of_Files))
    #print(organize_csvfiles(list_of_csv_file_file(List_Of_Files)))

    #def organize_csv(List_of):
     #   columns = []
      #  for row in csv.reader(infile, delimiter="\t"):
       #     columns.append(row[1])  # here row[1] is the second column

