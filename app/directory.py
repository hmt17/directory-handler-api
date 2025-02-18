from DirectoryService import DirectoryService

"""
    Retrieves text file with list of commands, assuming commands are spelled
    correctly and capitalized, and for each command will call one of the
    four different service functions.
"""
def text_parser(file):
    directories = DirectoryService()

    if file is None:
        # Can update this file to test the edge case files I included in test folder
        file = "test/commands.txt"

    try:
        with open(file, "r") as commands_file:
            for line in commands_file:
                if line is None: break
                else:
                    command_args = line.split()
                    print(line)
                    if command_args[0] == "CREATE":
                        directories.create_directory(command_args[1], None)
                    elif command_args[0] == "MOVE":
                        directories.move_directory(command_args[1], command_args[2])
                    elif command_args[0] == "DELETE":
                        directories.delete_directory(command_args[1])
                    elif command_args[0] == "LIST":
                        directories.list_directory(None, 0)
    except Exception as e:
        print(f"Error reading commands file: {e}")

if __name__ == "__main__":
    text_parser(None)
