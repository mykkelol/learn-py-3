""" 
    Reading files
        - open(file_name, file mode) - in py, we have the open function to open any file and it'd return us a file object which contains its metadata and methods for the file
        - file.read() - one of the open file methods is read, which returns all lines of data within the file if character_num is not specified
            - cursor - after .read() is called, py places cursor at the end of the file so it'd appear as if data is different after each read
        - file.seek(character_num) - to navigate and manipualte the cursor, we can use seek method
        - file.readline() - to read the file line by line instead of the whole file
        - file.readlines() - return all lines as a list which each line as an element
        - file.close() - similar to GUI, we should close files after work is completed
        - with - statement that ties all the above together and close() automatically if file is malformed or unhandled error (see example A)
            - while this allows us to nest with and open multiple files at once, we want to avoid abusing it as ideally we should close if we're not using the file anymore

    Writing files
        - similar to read but with its own set of methods and when we want to create a whole new file, we still use open('file_name.csv') as it's upsert-like
        - file.write() - write lines within files with lines suffixed with line delimiter (\n) and REMOVES previous content
        
    File modes
        - modes used with open() function and defaults to "r" or read files
        - "w" - write but REMOVES previous file content
        - "a" - write but appends to previous file content
        - "r+" - most common, only works for existing file (i.e. it won't save file like "a" or "w"), and is both read and write (but write is cursor-based and defaults to 0 char so need to leverage seek)

    "from csv import ..." module
        - while we can use read/write methods within open, it's best to use CSV module with open to process csv
        - since we still use py open function, all file modes remains (see example D)
        - reader(file, delimiter=",") - converts csv to iterator to let us iterate over rows of csv (this means we can use next() to skip header row!)
        - DictReader(file) - converts csv to iterator to let us iterate over rows of csv as OrderedDicts with headers as keys and row values as values
        - writer(file) - creates a writer object for writing to csv using list (see example B)
        - .writerow() - writer() method to write a row in list
        - DictWriter(file) - creates a writer object for writing to csv using dict (see example C)
        - .writeheader() - DictWriter() method to write header row in dict
        - .writerow() - DictWriter() method to write a row in dict

    "import pickle ..." module
        - sometimes we don't need csv and tabular data but we do need to store something in memory for processing
        - pickle module allows us to store data in .pickle file where it'll serialize the data, converting it into byte stream (see example E)
        - once serialized, we can unpickling our data and works similarly to how we store pickle in a jar and grab it whenever we're ready 
        - what's amazing is we can store class instances, tuple, etc. and load it for processing again later
        - there's also a custom module "from jsonpickle ..." that allows pickling with JSON instead of binary

    "import json ..." module
        - allows us to do json.dump(), json.load() etc. like example E but with JSON
        - however, it converts everything into jsonsting (e.g. none as Null, tuple as array, etc.)
        - class instances won't work and we'd have to convert it to an object first with vars() or my_class_instance.__dict__ before dumping

"""

# example A: create a function that accept old filename, word to replace, replacement word, and create a new file
# the function should also return a dict of number of characters, words, and lines within the new file

def file_io(old_filename, new_filename, find_word, replace_word):
    with open(old_filename) as file:
        text = file.read()
        new_text = text.replace(find_word, replace_word)

    with open(new_filename, 'w') as new_file:
        new_file.write(new_text)
        new_file.truncate() # important if new_text is shorter than original
    
    with open(new_filename, 'r') as new_file:
        lines = new_file.readlines()
    
    return {
        'lines': len(lines),
        'words': sum(len(line.split(' ')) for line in lines),
        'characters': sum(len(line) for line in lines)
    }

# example B: create a function that accepts old and new filenames to copy a file but the copy is all cap
def scream_copy(old_filename, new_filename):
    from csv import reader, writer
    with open(old_filename) as file:
        csv_reader = reader(file)
        with open(new_filename, 'w') as file: # not great to nest and could explode memory by not saving to memory and closing after
            csv_writer = writer(file)
            for row in csv_reader:
                csv_writer.writerow([field.upper() for field in row])

#scream_copy('../practice.csv', '../new_practice.csv')

# example C: create a function that accepts old and new filenames to copy a file but the copy is renames a header
def change_header_copy(old_filename, new_filename):
    from csv import DictReader, DictWriter
    with open(old_filename) as file:
        csv_reader = DictReader(file)
        data = list(csv_reader)
    
    with open(new_filename, 'w') as file:
        headers = ('Name', 'Country', 'Height')
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow({
                'Name': row['Name'],
                'Country': row['Country'],
                'Height': row['Height (in cm)'],
            })

# change_header_copy('../practice.csv', '../new_practice.csv')

# example D: create a function that adds a row into a given file
def add_user(name, country, height):
    from csv import writer
    with open('../practice.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([name, country, height])

# add_user('Panda', 'China', 277)
        
# example E: create a function that uses pickle module to store a class instance for quick processing and load it back
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name} is alive again!'
    
    def login(self):
        print(f'{self.name} logged in!')


def use_pickle():
    import pickle

    random_purple_blue = User('random_purple_blue')
    with open('../my_pickle.pickle', 'wb') as file: # wb as write binary since all pickles are byte streams
        pickle.dump(random_purple_blue, file) # creates a pickle file with class instance stored in binary

    with open('../my_pickle.pickle', 'rb') as file:
        resurrected = pickle.load(file) # we 'revived' the pickle/class instance and took it out the jar :)
        print(resurrected)
        resurrected.login()
    
# use_pickle()
        
# create a function that update users' name and return the count of users updated
def update_users(name, new_name):
    from csv import reader, writer
    count = 0

    with open('../practice.csv') as file:
        csv_reader = reader(file)
        rows = list(csv_reader)
    
    with open('../practice.csv', 'w') as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == name:
                count += 1
                csv_writer.writerow([new_name, row[1], row[2]])
            else:
                csv_writer.writerow(row)

    return count

print(update_users('Panda', 'PANDA'))