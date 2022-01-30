def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    score = input("Enter score: ")
    try:
        enteredScore = float(score)
        if (enteredScore < 0):
            print ("Bad score")
        elif (enteredScore > 1):
            print ("Bad score")
        else:
            if (enteredScore >= 0.9):
                print ("A")
            elif (enteredScore >= 0.8):
                print ("B")
            elif (enteredScore >= 0.7):
                print ("C")
            elif (enteredScore >= 0.6):
                print ("D")
            else:
                print ("F")
    except:
        print ("Bad score")
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()