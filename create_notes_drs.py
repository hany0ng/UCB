#Import os, sys (for bonus challenge) modules.
import os, sys

#Define function called main.
def main():
    
    #Bonus Challenge: Add a conditional statement to abort the script if the directory CyberSecurity-Notes already exists.
    #Creates a directory called CyberSecurity-Notes in the current working directory.
    if os.path.exists("CyberSecurity-Notes"):
        print("CyberSecurity-Notes folder already exists!  Aborting script.")
        sys.exit()
    
    else:
        os.mkdir("CyberSecurity-Notes")
    
    #Within the CyberSecurity-Notes directory, creates 24 sub-directories (sub-folders), called Week 1, Week 2, Week 3, and so on until up through Week 24.
    for i in range(1, 25):
        os.mkdir("Cybersecurity-Notes/Week {}".format(i))
    
    #Within each week directory, create 3 sub-directories, called Day 1, Day 2, and Day 3.
        for j in range (1, 4):
            os.mkdir("Cybersecurity-Notes/Week {}/Day {}".format(i, j))

main()