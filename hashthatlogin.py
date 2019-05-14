#Import csv & hashlib modules
import csv, hashlib

#Open the contents of UserInfo_Hashed.csv using the Python CSV Library.
csv_file = open("UserInfo_Hashed.csv")
csv_contents = csv.reader(csv_file)

print("Welcome to HackSafe Bank.  The Safest Bank on the Planet.")
print("---------------------------------------------------------\n")
print("To login, please provide the requested information.")

#Prompt users for their email address and password.
user_email = input("What is your email address? ")
user_pw = input("What is your password? ")

#Hash the password provided using the SHA256 strategy.
hash_pw = hashlib.sha256(bytes(user_pw, 'utf-8')).hexdigest()

#Compare the email and password provided against all records in the csv.
for name, email, password_hashed, phone, address, city, zip, country, cc_hashed, cvv, balance in csv_contents:

#If a match is found, the user should be greeted with their name, address, and bank balance.
    if user_email in email and hash_pw in password_hashed:
        print("\nWelcome back", name + "!")
        print("Your address on file is:", address + ",", city + ",", country + ",", zip)
        print("Your balance is:", balance)
        break

#If no match is found, the user should be informed that their login attempt was invalid.
    elif user_email not in email and hash_pw not in password_hashed:
        continue
else:
    print("\nLogin invalid.  Try again.")
        
#Close UserInfo_Hashed.csv
csv_file.close()

#       nascetur.ridiculus@scelerisqueneque.ca
#       TJK56AAR9FZ