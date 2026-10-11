Students_Name = input("Enter the Students Name: ")
while True:
    try:
        Amount_of_Subjects = int(input("Enter the Amount of Subjects: "))
        if Amount_of_Subjects <= 0:
            print("Please enter a valid number of subjects.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

Subjects = []
Subjects_and_Scores = {}
for i in range(Amount_of_Subjects):
    subject = input(f"Enter the name of subject {i + 1}: ")
    Subjects.append(subject.title())
    while True:
        try:
            Score = float(input(f"Enter the score for {subject}: "))
                
            # Check if score is within range (0 to 100)
            if 0 <= Score <= 100:
                break  # Score is valid! Exit the while loop
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
                    
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    Subjects_and_Scores[subject.title()] = Score  # Store the score in the dictionary with the subject as the key
total_score = sum(Subjects_and_Scores.values())
Average_Score = total_score / Amount_of_Subjects

print("\n--- Student Report ---")
print(f"Student Name: {Students_Name}")
print(f"Total Score: {total_score}")
print(f"Average Score: {Average_Score}")
if Average_Score >= 90:
    print(f"Overall Grade for {Students_Name}: A")
elif Average_Score >= 80:
    print(f"Overall Grade for {Students_Name}: B")
elif Average_Score >= 70:
    print(f"Overall Grade for {Students_Name}: C")
elif Average_Score >= 60:
    print(f"Overall Grade for {Students_Name}: D")
else:
    print(f"Overall Grade for {Students_Name}: F")

highest_score_subject = max(Subjects_and_Scores, key=Subjects_and_Scores.get)
lowest_score_subject = min(Subjects_and_Scores, key=Subjects_and_Scores.get)
highest_score = Subjects_and_Scores[highest_score_subject]
lowest_score = Subjects_and_Scores[lowest_score_subject]
print(f"{highest_score_subject} is the subject with the highest score, with a score of {highest_score}.")
print(f"{lowest_score_subject} is the subject with the lowest score, with a score of {lowest_score}.")