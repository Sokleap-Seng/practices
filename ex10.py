# Enter a string word in the console.
# Enter the number n in the console.
# If word equal to "good" and the number between 7 and 15,it will be print "It's good"
# If word equal to "bad" and the number lower than 7 or greater than 15, it will be print "It's bad"
text = input("please input your text: ")
if len(text)>7 and len(text)<15:
    print("It's good")
else:
    print("It's bad")