spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

#These statements are similar; both if and while check the value of spam, and if it’s less than 5, they print a message. 
#But when you run these 2 code snippets, something very different happens for each one. 
#For the if statement, the output is simply "Hello, world." 
#But for the while statement, it’s "Hello, world." repeated five times! 
## The loop stops after five prints because the integer in spam increases by 1 at the end of each loop iteration, 
## which means that the loop will execute five times before spam < 5 is False.

