import os
from summerizer import summarize_transcript
from reader import read_transcript

def readfile(absolute_file_path: str ) -> str:
    """ Reads from the file provided and raise error if file is not found """
    if not os.path.exists(absolute_file_path):
        print("File is not found please check the correct path!")
    else:
        with open(absolute_file_path,"r", encoding="utf-8") as file:
            return file.read()

def display_summary(summary: dict) -> None:
    """Pring the meeting Summary on console"""
    title = summary["meeting_title"]
    print(title)
    print("=" * 60)
    meeting = summary["meeting_summary"]
    print("Meeting Summary:")
    print(meeting)
    print("=" * 60)
    action_items = summary["action_items"]
    print("Action Items:")
    for a in action_items:
        print(f"{a["owner"]} - {a["task"]}, {a["status"]}, {a["due_date"]}")
    print("=" * 60)
    pending_items = summary["pending_items"]
    print("Pending Items:")
    for p in pending_items:
        print(f"{p}")
    print("=" * 60)
    decisions = summary["decisions"]
    print("Decisions Taken:")
    for d in decisions:
        print(f"{d}")
    print("=" * 60)
    participants = summary["participants"]
    print("Participants:")
    for p in participants:
        print(f"{p}")


def main():
    content = read_transcript("C:/Users/U6080302/Downloads/DBA Daily Standup_30Jul_2026.docx")
    #print(content)
    summary = summarize_transcript(content)
    display_summary(summary)
    #print(summary)


if __name__ == "__main__":
    main()