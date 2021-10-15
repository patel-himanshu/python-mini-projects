# File to Format (CLI-based)

This program returns the file format of the file given as its input. It searches a list of 185 file signatures (magic numbers) and compares them with the signature of the input file, and if a match is found, then it returns back the extension of the matched file format. 

## Usage

Executing the command without any arguments, prints the extensions of the files present inside the `samples` directory.

    Sample command: `python file2format.py`

Executing the command with arguments, prints the extensions of the input files. It returns an error, in case the file path is invalid.

    Sample commands:
    `python file2format.py file1.gif`
    `python file2format.py file2.pdf file3.iso`
