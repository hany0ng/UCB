#import csv & hashlib modules
import csv, hashlib

#Open the contents of UserInfo.csv using the Python CSV Library.
csvfilein = open("UserInfo.csv")
csv_input = csv.reader(csvfilein)

#Utilize the SHA256 hash strategy to mask password and credit card number.
def hash_string(text):
    return hashlib.sha256(bytes(text, 'utf-8')).hexdigest()

#Store the hashed version of the data into a new file titled UserInfo_Hashed.csv.
csvfileout = open("UserInfo_Hashed.csv", "w", newline="")
csv_output = csv.writer(csvfileout)

csv_output.writerow(next(csv_input))
for name, email, password, phone, address, city, zip, country, cc, cvv, balance in csv_input:
    csv_output.writerow([name, email, hash_string(password), phone, address, city, zip, country, hash_string(cc), cvv, balance])

#Close UserInfo.csv and UserInfo_Hashed.csv files.
csvfilein.close()
csvfileout.close()