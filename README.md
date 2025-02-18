# directory-handler-api
Repository handles creating, moving, and deleting directories based on commands
passed through in a text file

For testing purposes, a text file of the commands given are in the testing
folder, and you can run the command below to see the output

python3 app/directory.py

Originally I wanted to break each command into APIs hence the "handler-api" in
the repo name, but for the sake of simplicity to read in a text file and print
the results to command line I broke down the commands into functions in
the DirectoryService class.

I included a test suite, and although there's not much to include currently
since all the results are just printed. If our functions were returning or
saving values to a database then there would be more to assert on. To make this
prod ready I would also have included more command files covering different edge
cases.
