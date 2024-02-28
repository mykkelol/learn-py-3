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

    Writing files
        - similar to read but with its own set of methods and when we want to create a whole new file, we still use open('file_name.csv') as it's upsert-like
        - file.write() - write lines within files with lines suffixed with line delimiter (\n) and REMOVES previous content
        
    File modes
        - modes used with open() function and defaults to "r" or read files
        - "w" - write but REMOVES previous file content
        - "a" - write but appends to previous file content
        - "r+" - most common, only works for existing file (i.e. it won't save file like "a" or "w"), and is both read and write (but write is cursor-based and defaults to 0 char so need to leverage seek)

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