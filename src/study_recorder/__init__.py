import json
import os

def main():
    filename = "study_sessions.json"
    
    # Load existing sessions if the file exists
    if os.path.exists(filename):
        with open(filename, "r") as f:
            all_sessions = json.load(f)
    else:
        all_sessions = []
        
    print("Previous sessions loaded:", all_sessions)

    # Input loop
    while True:
        answer = input("Would you like to log a study session? (y/n): ")
        if answer.lower() == "n":
            break
        elif answer.lower() == "y":
            topic = input("What topic did you study today? ")
            minutes = int(input("How many minutes did you study? "))
            
            session = {
                "topic": topic,
                "minutes": minutes
            }
            all_sessions.append(session)

    # Save updated list back to the file
    with open(filename, "w") as f:
        json.dump(all_sessions, f, indent=4)

    print("\nUpdated session list saved successfully:")
    print(all_sessions)

if __name__ == "__main__":
    main()