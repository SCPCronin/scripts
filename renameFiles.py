import os

# Returns a list of all files or directories based on the path provided, essentially running 'ls'
def getListOfFilesBasedOnDirectory(directoryPath):
    return os.listdir(directoryPath)

# Removes the file extension, and any brackets that preceed it
def removeFileExtensionAndRegionFromFileName(fileName):
    return fileName.split("(")[0].rstrip(". _")

# If a filename uses underscores instead of spaces, this function replaces them
def replaceUnderscoresWithSpaces(fileName):
    tempFileName = str(fileName)
    if(len(fileName.split("_")) > len(fileName.split(" "))):
        tempFileName =  " ".join(tempFileName.split("_"))
    return tempFileName

# Calls on above functions to turn a file name into the desired format
def determineNameOfFile(fileName):
    fileNameWithNoExtension = removeFileExtensionAndRegionFromFileName(fileName)
    fileNameWithSpaces = replaceUnderscoresWithSpaces(fileNameWithNoExtension)
    return fileNameWithSpaces

# For every file in a specific directory, update the file name
def cleanUpFileNamesBasedOnDirectory(directoryPath):
    os.chdir(directoryPath)
    listOfFiles = getListOfFilesBasedOnDirectory("./")
    for file in listOfFiles:
        updatedNameOfFile = determineNameOfFile(file)
        # If the filename doesn't exist, updat the fileName
        if(updatedNameOfFile not in listOfFiles):
            os.rename(file, updatedNameOfFile)
        else:
            print(f"File already exists for {updatedNameOfFile}")
        # Updates the list to catch duplicate files
        listOffiles = getListOfFilesBasedOnDirectory("./")

# Future Proofing in case I accidentally remove zip extensions from files again ( ͡° ͜ʖ ͡°)
def reappendZipExtensionToFilesByDirectory(directoryPath):
    os.chdir(directoryPath)
    listOfFiles = getListOfFilesBasedOnDirectory("./")
    for file in listOfFiles:
        os.rename(file, f"{file}.zip")

# Run 
def cleanUpAllFilesInRootFolder():
    listOfDirectories = getListOfFilesBasedOnDirectory("./")
    for directory in listOfDirectories:
        cleanUpFileNamesBasedOnDirectory(f"./{directory}")


def main():
    cleanUpAllFilesInRootFolder()

if __name__ == "__main__": 
    main()