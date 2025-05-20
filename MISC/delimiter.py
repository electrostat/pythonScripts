import csv
import os
import re

def delimitFile(newDirectory, filename, delimiter, fileOutputName):
    # get the current working directory
    current_working_directory = os.getcwd()

    # print output to the console
    print(current_working_directory)
    # Change the working directory
    os.chdir(newDirectory)

    # Verify that the directory has changed
    print("New working directory:", os.getcwd())

    try:
        with open(filename, 'r', encoding='latin-1') as infile, open(fileOutputName, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile, delimiter=delimiter)

            content = infile.read()
            trimmed_content = content[2:]

            new_text = re.sub(r"\s+", delimiter, trimmed_content)
            split = new_text.split(delimiter)
            final_merge = "\n".join([delimiter.join(split[i:i+3]) for i in range(0,len(split),3)])

            outfile.write(final_merge)
    except Exception as e:
        print("Error Occurred: ")
        print(e)


#