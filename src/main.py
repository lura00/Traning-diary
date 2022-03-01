from numpy import insert
from database import Notepad
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

db = Notepad()


def show_menu():
    print("\n===========================================================")
    print("|                      Welcome champ                      |")
    print("|                                                         |")
    print("|               Would you like to add a user? press .1    |")
    print("|               Would you like to add a workout? press .2 |")
    print("|               Or perhaps see all posts? press .3        |")
    print("|               Edit post? press .4                       |")
    print("|               Delete post? press .5                     |")
    print("|               Exit, press .6                            |")
    print("===========================================================")


while True:

    show_menu()
    choice = int(input("Make our choice: 1 - 6: "))

    if choice == 1:
        name = input("Enter your name: ")
        goal = input("Whats your training goal? ")
        form = input("Enter your current form: ")
        user = (name, goal, form, today)
        db.insert_user(user)

    elif choice == 2:
        training_type = input("Enter training type: ")
        todays_goal = input("Whats your training goal today? ")
        form = input("Enter your current form: ")
        result = input("What is todays result?: ")
        food_before_training = input("What did you eat before? ")
        stomich_state = input("How did your body react?: ")
        user_id = input("Enter your user id: ")
        workout = (training_type, todays_goal, form, result, food_before_training, stomich_state, user_id, today)
        db.insert_workout(workout)

    elif choice == 3:
        choice = input("Show users or workouts? ")
        if choice == "users":
            db.show_all_users()
        else:
            db.show_all_workouts()

    elif choice == 4:
        column = input(
            "What column do you want to edit? First_name, goal or form? ")
        data = input("What is the new data? ")
        id = input("Enter the row ID ")
        db.edit_post(column, data, id)

    elif choice == 5:
        delete_user_id = input("Enter id of user to be deleted: ")
        db.delete_one(delete_user_id)

    elif choice == 6:
        print("Thank you for using my app, your notes have been saved, come back any time!")
        break
    else:
        print("==>Now something went a little bit wrong, try another number<==")