def password_validator(password):
    digit_counter = 0
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    for i in range(len(password)):
        if password[i].isdigit():
            digit_counter += 1
    if digit_counter == 0 or digit_counter < 2:
        print("Password must have at least 2 digits")
    if 6 <= len(password) <= 10 and password.isalnum() and digit_counter >= 2:
        print("Password is valid")


pswd = input()
password_validator(pswd)
