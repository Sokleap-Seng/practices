# Get the number entered from keyboard and store it into a variable userMessage
# If the userMessage is lower than 0, display "Negative Number!"
# Else display "Positive Number"
user_input = int(input("Enter your number:"))
user_message =''
if user_input < 0:
    user_message="Negative Number!"
else:
     user_message="Positive Number"
print(user_message) 