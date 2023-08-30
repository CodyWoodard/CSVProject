# Familiarizing myself with csv.reader/writer in Python. Received this from
# Pythons docs @ https://docs.python.org/3/library/csv.html
if __name__ == '__main__':

    import os
    # This block of code was built using:
    # https://stackoverflow.com/questions/10149263/extract-a-part-of-the-filepath-a-directory-in-python
    Bobs_Path = os.path.abspath('BobsParts.csv')
    Insta_Path = os.path.abspath('Instamonia.csv')
    Vanilla_Path = os.path.abspath('VanillaAndCanolaSpecialists.csv')

    List_Of_Files = [Bobs_Path, Insta_Path, Vanilla_Path]  # Populating a list.

    def path_stripper(List_Of_Files):
        i = 0
        Parsed_Filenames = []
        for x in List_Of_Files:

            parent_directory, directory_name = os.path.split(List_Of_Files[i])
            stripped_path = directory_name.strip('.csv')
            #print(stripped_path)
            Parsed_Filenames.append(stripped_path)
            #print(Parsed_Filenames[i])
            i += 1
        return Parsed_Filenames

    #print(path_stripper(List_Of_Files))



