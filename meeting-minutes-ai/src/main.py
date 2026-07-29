import os
from summerizer import summarize_transcript

def readfile(absolute_file_path: str ) -> str:
    """ Reads from the file provided and raise error if file is not found """
    if not os.path.exists(absolute_file_path):
        print("File is not found please check the correct path!")
    else:
        with open(absolute_file_path,"r", encoding="utf-8") as file:
            return file.read()


def main():
    content = readfile('../input/transcript.txt')
    #print(content)
    summary = summarize_transcript(content)
    print(summary)

main()