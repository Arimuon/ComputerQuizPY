import csv
import pandas as pd
import time as t
from question_reader import question
import random as rdm

read_questions = pd.read_csv("700_Questions.csv", encoding="windows-1258", delimiter=";", keep_default_na=False)
questions = []

for index, row in read_questions.iterrows():
        questions.append(question(
            question_number=row['Question_Number'],
            type=row['Type_of_Question'],
            topic=row['Unit'],
            question=row['Question'],
            answer=row['Answer'],
            distractor1=row['Distractor1'],
            distractor2=row['Distractor2'],
            distractor3=row['Distractor3'],
            is_category=row['Question_Number'] == ""
        ))


def test():
    for question in questions:
        print("Question Number:", question.question_number)
        print("Type of Question:", question.type)
        print("Topic:", question.topic)
        print("Question:", question.question)
        print("Answer:", question.answer)
        print("Distractor 1:", question.options)
        print("Distractor 2:", question.options)
        print("Distractor 3:", question.options)
        print("\n")


def score_write(username, score, filename = "scores.csv"):
    '''Firstly, the code checks if the username already exists in the file
    if it does then the score will be appended to the correct username instead of just creating new
    usernames for the same person'''
    existing_user = []
    with open(filename, "r", newline='') as file:
        reader = csv.reader(file)
        # Ignores the header
        next(reader, None)
        existing_user = [row for row in reader]

    # Check if the username already exists in the file
    username_exists = next((i for i, row in enumerate(existing_user) if row[0] == username), None)

    # If the usernames exists only update the score
    if username_exists is not None:
        existing_user[username_exists][1] = str(int(existing_user[username_exists][1]) + int(score))
    else:
        # If the username doesn't already exist create a new username and score
        existing_user.append([username, str(score)])
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Score'])
        writer.writerows(existing_user)


def score_viewer(username, filename = "scores.csv"):
    '''Firstly, the code checks if the username already exists in the file
    if it does then the score stored in a variable then printed with a f-string, if the username doesn't exist an error will
    be printed'''
    valid_user = False
    while valid_user == False:
        final_username = username
        existing_user = []
        with open(filename, "r", newline='') as file:
            reader = csv.reader(file)
            # Ignores the header
            next(reader, None)
            existing_user = [row for row in reader]

        # Check if the username already exists in the file
        username_exists = next((i for i, row in enumerate(existing_user) if row[0] == username), None)

        # If the usernames exists assign it to a the existing_user_score variable
        if username_exists is not None:
            existing_user_score = int(existing_user[username_exists][1])
        else:
            existing_user_score = 0
    
        if existing_user_score == 0:
            print("This username does not exist, please pick another username. ")
            t.sleep(1) # Adds a delay for better user experience
            username = input("Please enter your username >> ")
        elif existing_user_score !=0:
            print("") # Adding extra spacing for a cleaner interface
            print(f"The score for {final_username} is, {existing_user_score} points!")
            break

def menu():
    chosen = False
    while chosen == False:
        choice = input("Please select if you are a student or staff >> ").lower() # Converting all inputs to lowercase for useability
        if choice == "student":
            # Student menu is displayed
            student_Menu()
            break # Exits to the loop
        elif choice == "staff":
            # Staff menu is displayed
            staff_Menu()
            break # Exits to the loop
        else:
            print("Invalid choice, please try again.")
            t.sleep(1) # Adds a delay for better user experience


def student_Menu():
    chosen = False
    while chosen == False:
        print()
        print("Please select from the following options:")
        print("1. Take the quiz")
        print("2. View my score")
        choice = int(input())

        # Checks what option the student picked
        if choice == 1:
            pass
        elif choice == 2:
            username = input("Please enter your username >> ")
            score_viewer(username)
            break # Exits the loop
        else:
            pass


def staff_Menu():
    pass

# Main
menu()
