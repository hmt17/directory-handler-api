"""
    Included is global dict called directory that acts as a tree
    and stores all folder paths.

    Each command's function is included in here.
"""
class DirectoryService:
    def __init__(self):
        self.directory = {}

    def create_directory(self, directory, moved):
        # Used for both creating new folders and for moving a folders
        # moved will either be None if its a create command or a dict of
        # sub folder paths to be moved if it's called from move_directory
        try:
            folders = directory.split('/')
            lastFolderIndex = len(folders)
            directoryTree = self.directory
            for folder in folders:
                lastFolderIndex -= 1
                if folder not in directoryTree:
                    if moved is None:
                        directoryTree[folder] = {}
                    else:
                        directoryTree[folder] = moved
                elif lastFolderIndex == 0:
                    # If folder exists but its the last level folder,
                    # overwrite with moved sub folder
                    directoryTree[folder] = moved

                directoryTree = directoryTree[folder]

        except Exception as e:
            print(f"Error creating directory: {directory} with error: {e}")


    def move_directory(self, source, destination):
        # Assuming source and destination folders exist
        try:
            sourceFolders = source.split('/')
            folderName = sourceFolders[len(sourceFolders)-1]
            destinationWithNewFolder = destination + "/" + folderName
            directoryTree = self.directory

            for folder in sourceFolders:
                if folder in directoryTree:
                    directoryTree = directoryTree[folder]

            # Create new path and include whatever sub folders exist at the old path
            self.create_directory(destinationWithNewFolder, directoryTree)
            # Delete old path
            self.delete_directory(source)

        except Exception as e:
            print(f"Error moving directory: {source} to {destination} with error: {e}")

    def delete_directory(self, directory):
        # Delete only last level folder from directory
        # Exp: /food/fruit/apple - only deletes /apple
        # Uses a list as a stack to track what nested dict exists at each
        # folder level. We push those values each iteration and we only
        # delete the last value from the top of the stack.
        try:
            folders = directory.split('/')
            directoryTree = self.directory
            stackFolders = []

            for folder in folders:
                if folder in directoryTree:
                    stackFolders.append((directoryTree, folder))
                    directoryTree = directoryTree[folder]
                else:
                    # Return message if folder doesn't exist
                    print(f"Cannot delete {directory} - {folder} does not exist")
                    break

            if stackFolders:
                directory, folder = stackFolders.pop()
                del directory[folder]

        except Exception as e:
            print(f"Error deleting directory: {directoryTree} with error: {e}")

    def list_directory(self, directoryTree, indent):
        # Need to recursively traverse through nested dicts of directories
        # Incrementing indentation with each recursive call
        if directoryTree is None:
            directoryTree = self.directory
        for folder, subDirectory in sorted(directoryTree.items()):
            print("  " * indent + f"{folder}")
            self.list_directory(subDirectory, indent + 1)
