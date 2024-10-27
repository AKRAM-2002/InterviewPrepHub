# File I/O in Python

File I/O (Input/Output) is essential for working with files in Python. It enables reading, writing, and manipulating data stored in files, allowing you to process large datasets, store logs, or manage configuration files.

This section covers basic to advanced file operations in Python and provides interview questions and exercises to build your expertise.

## Key Concepts

- **File Handling**: Opening, reading, writing, and closing files.
- **Text vs Binary Files**: Understanding different file types and their handling.
- **Buffered I/O**: Efficiently reading and writing large files.
- **Standard Input/Output**: Working with `sys.stdin` and `sys.stdout` for flexible file handling.

## Interview Questions

1. **Basic File I/O Operations**
   - **Q1**: Write a Python program that reads from standard input and prints each line in uppercase.
   - **Q2**: Given a large text file, how would you read and process it line by line without loading the entire file into memory?
   - **Q3**: How would you count the number of lines in a file without using the `len()` function on a list?

2. **Advanced File Manipulation**
   - **Q4**: Explain how you would handle file access errors and ensure files are properly closed after processing.
   - **Q5**: Describe a situation where you’d use binary file reading instead of text reading.
   - **Q6**: How would you manage reading and writing of large files to optimize memory usage?

## Exercises

1. **Basic File Reading and Writing**
   - Implement a Python script that reads a log file line by line and prints only lines containing the word "ERROR".

2. **Memory-Efficient Data Processing**
   - Given a stream of integer values, create a function that calculates the running average of the numbers read so far.

3. **Complex Processing**
   - Write a script that counts the frequency of each word in a file and outputs the result to a new file.

4. **Custom Filtering**
   - Create a Python script that reads a text file and outputs only the lines containing a specific keyword provided by the user.

5. **Line Count without Loading Entire File**
   - Write a function that counts the total number of lines in a file without loading it fully into memory.

## Code Samples

For sample solutions and reference code, visit the [code_samples](code_samples/) folder in this directory.

---

## Additional Resources

- [Python’s `open()` Function](https://docs.python.org/3/library/functions.html#open)
- [File Handling in Python](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

Happy coding! Practice these qu
