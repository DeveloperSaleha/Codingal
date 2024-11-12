def shutdown(input_value):
    if input_value.lower() == "yes":
        print("Shutting down...")
    elif input_value.lower() == "no":
        print("Abort shut down.")
    else:
        print("Sorry.")

user_input = input("Do you want to shut down? (Yes/No): ")
shutdown(user_input)