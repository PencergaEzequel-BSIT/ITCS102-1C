username = input("Enter username: ")
password = input("Enter password: ")

correct_username = "negro69"
correct_password = "isakangnigga"


(username < correct_username and print("Wrong input")) or \
(username > correct_username and print("Wrong input")) or \
(password < correct_password and print("Wrong input")) or \
(password > correct_password and print("Wrong input")) or \
(print("Access Granted"))
