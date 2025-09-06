print("GRADE CALCULATOR")
score_input = int(input("Enter a test score (or done ) :"))
max_score = 100
score = int(score_input)
if score_input > 100 or score_input < 0:
  print("Invalid score")
else:
    if score >= 75 and score <= 100:
       print("You got an A")
    elif score >= 60 and score < 75:
       print("You got a B")
    elif score >= 50 and score < 60:
       print("You got a C")
    elif score >= 40 and score < 50:
       print("You got a D")
    else:
       print("You got an F")