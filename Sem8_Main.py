from os.path import exists
from Sem8_CSV_create import creating
from Sem8_File_writing import writing_scv
from Sem8_File_writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()