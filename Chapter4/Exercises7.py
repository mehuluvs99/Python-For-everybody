

def computergrade(grade):
        
    if grade < 0 or grade > 1.0:
        print("Score is Out of Range")
    elif grade >=0.9:
        return "Rank : A"
    elif grade >= 0.8:
        return "Rank : B"
    elif grade >= 0.7:
        return "Rank : c"
    elif grade >= 0.6:
        return "Rank : D"
    #elif grade >= 0.5:
    #    print("Rank : E")
    else:
        return "Rank : F"
try:
    grade = float(input("Enter Score: \n"))
    
except:
    print("Bad Score")
    quit()

print(computergrade(grade))