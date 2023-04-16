try:
    grade = float(input("Enter Score: \n"))
    
except:
    print("Bad Score")
    quit()

if grade < 0 or grade > 1.0:
    print("Score is Out of Range")
elif grade >=0.9:
    print("Rank : A")
elif grade >= 0.8:
    print("Rank : B")
elif grade >= 0.7:
    print("Rank : c")
elif grade >= 0.6:
    print("Rank : D")
#elif grade >= 0.5:
#    print("Rank : E")
else:
    print("Rank : F")
