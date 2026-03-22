def shutdown(user_input):
    if user_input == "Yes" or "yes":
        print("Shutting down")
    elif user_input == "No" or "no":
        print("Abort ! Shut down")
    else:
        print("Sorry")


choice = input("Do you want to shutdown? (Yes/No): ")


shutdown(choice)