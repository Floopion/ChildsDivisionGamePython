#A program designed for primary school children to learn division. 10 questions are are asked with time and feedback given. Divisors are to the power of 10.  
import random    #import random module 
import time      #import time module

def main():                                 #Define main function 
    intro()                                 #Run intro function
    again = "Y"                             #Variable 'again' equals 'Y'
    while again[0] == "Y":                  #While loop. 'again equals 'Y'. Only read first character.
        num1 = []                           #Variable 'num1' equals an empty list. 
        num2 = []                           #Variable 'num2' equals an empty list.
        ans = []                            #Variable 'ans' equals an empty list.
        quest = []                          #Variable 'quest' equals an empty list.
        guess = []                          #Variable 'guess' equals an empty list.
        token = []                          #Variable 'guess' equals an empty list.
        listfill(num1,num2,ans)             #run function 'listfill'. Pass in 'num1', 'num2', 'ans'.
        print "+"*77
        print
        Wait = raw_input('\t\t\t    Push enter to begin!')           #Variable 'Wait' equals raw input.
        start = time.time()                                          #Variable start equals current time.
        calc(num1,num2,ans,quest,guess,token)                        #Run function calc. Pass in 'num1', 'num2', 'ans', 'quest', 'guess','token'.
        end = time.time()                                            #Variable end equals current time.
        timer = end - start                                          #Variable Timer equals end time minus start time.
        print
        feedback(num1,num2,ans,quest,guess,token,again,timer)        #Run Function 'feedback'. Pass in 'num1', 'num2', 'ans', 'quest', 'guess', 'again', 'timer','token'. 
        again = raw_input ('\t\t\t    Play again? Y/N? :').upper()   #Variable 'again' equals raw input. Convert string to uppercase.
        print
        

def listfill(num1,num2,ans):                                                        #define function listfill. Recieve variables 'num1', 'num2', 'ans'.
    for i in range (10):                                                            #For loop. Ten cycles.
        num1.append(random.randrange(10000,100001)/(random.choice([100.0,10.0])))   #Append list in num1 with a random integer between 10000 and 100001. Divide by either 100.0 or 10.0 to make a 2 - 3 decimal float.
        num2.append(random.choice([10,100]))                                        #Append list in num2 with 10 or 100 randomly chosen.
        ans.append(num1[i] / num2[i])                                               #Append list in ans with the sum of num1 divided by num2. Position in list selected by the cycle number in the loop [i].



def intro():                                                                        #Define function 'intro' 
    print                                                                           #Print title and program instructions
    print "+"*77
    print
    print '\t\t\t  Division to the powers of 10!'
    print
    print ' You will be shown 10 division equations, each equation has a number missing!'
    print '   Type in the number that you think goes in the blank space and hit enter.'
    print '\t\t       Try to beat your score and your time!'
    print


def calc(num1,num2,ans,quest,guess,token):                              #Define function calc. Recieve 'num1', 'num2', 'ans', 'quest', 'guess'.
    for i in range (10):                                                #For loop. 10 cycles. 
        disp=random.choice([1,2,3])                                     #Variable display equals random choice 1 2 or 3. 
        if disp == 1:                                                   #If statment. if 'display' is equal to '1'.
            quest.append(ans[i])                                        #append list in 'quest' with number in postion [i] in list 'ans'.
            token.append(3)                                             #append list in 'token' with number 3.
            print                                                       #Print Question with answer left blank.
            print '+'*32,'QUESTION ',i+1,'+'*32                         
            print
            print '\t\t\t',num1[i],u' \u00F7 ',num2[i],' = ________'    #Question.
            print
            flag(guess)                                                 #Run function 'flag' pass in 'guess'.
        elif disp == 2:                                                 #ElseIf statment. if 'display' is equal to '2'.
            print                                                       #Print question with second number missing.
            print '+'*32,'QUESTION ',i+1,'+'*32
            print
            quest.append(num2[i])                                       #Append list in 'quest' with number in postion [i] in list 'num2'.
            token.append(2)                                             #Append list in 'token' with number 2.
            print '\t\t\t',num1[i],u' \u00F7 _______ = ',ans[i]         #Question.
            print
            flag(guess)                                                 #Run function 'flag' pass in 'guess'.
        elif disp ==3:                                                  #ElseIf statment. if 'display' is equal to '3'.
            print                                                       #Print question with first number missing.
            print '+'*32,'QUESTION ',i+1,'+'*32
            print
            quest.append(num1[i])                                       #Append list in 'quest' with number in postion [i] in list 'num1'.
            token.append(1)                                             #Append list in 'token' with number 1.
            print u'\t\t\t_______ \u00F7 ',num2[i],' = ',ans[i]         #Question.
            print
            flag(guess)                                                 #Run function 'flag' pass in 'guess'.


def flag (guess):                                       #Define Function 'flag'. Recieve variable 'guess'.
    flag = 'n'                                          #Variable 'flag' equals 'n'.
    while flag =='n':                                   #While loop. While flag equals 'n'.
        check = (raw_input('Your Answer: '))            #Varible is equal to raw input.
        if check.isalpha()== False:                     #Check that the input is not alphanumeric.
            check=float(check)                          #Convert input to a float.
            guess.append(check)                         #Append the list in 'guess' with 'check'.
            flag='y'                                    #Variable 'flag' is equal to 'y'.
        else:                                           #Else statment.
            print 'Please enter a valid number'         #Print error message.
            

def feedback(num1,num2,ans,quest,guess,token,again,timer):              #Define function feedback. Recieve variables, 'num1', 'num2', 'ans', 'quest', 'guess', 'again', 'timer'.  
    print'+'*34,' Result ','+'*34                                       #Title.
    print       
    good=0                                                              #Variable 'good' equals 0
    for k in range (10):                                                #For loop. 10 Cycles.
        if quest [k] == guess [k] and token[k] == 1:                    #If position [k] in list quest matches position [k] in list guess and position [k] in list token equals 1.
            good += 1                                                   #Add 1 to the variable 'good'.
            print k+1,u'. _______ \u00f7 ',num2[k],' = ', ans[k]        #Print Question.
            print 'Your answer = ',guess[k],u'\t\t\t\u2713'             #Print students answer with a tick.
            print
        elif quest [k] == guess [k] and token[k] == 2:                  #If position [k] in list quest matches position [k] in list guess and position [k] in list token equals 2.
            good += 1                                                   #Add 1 to the variable 'good'.
            print k+1,'. ',num1[k],u' \u00f7 _______ = ', ans[k]        #Print Question.
            print 'Your answer = ',guess[k],u'\t\t\t\u2713'             #Print students answer with a tick.
            print
        elif quest [k] == guess [k] and token[k] == 3:                  #If position [k] in list quest matches position [k] in list guess and position [k] in list token equals 3.
            good += 1                                                   #Add 1 to the variable 'good'.
            print k+1,'. ',num1[k],u' \u00f7 ',num2[k],' = _______'     #Print Question.
            print 'Your answer = ',guess[k],u'\t\t\t\u2713'             #Print students answer with a tick.
            print
        elif quest [k] != guess [k] and token[k] == 1:                  #If position [k] in list quest does not match position [k] in list guess and position [k] in list token equals 1.
            print k+1,u'. _______ \u00f7 ',num2[k],' = ', ans[k]        #Print Question.
            print 'Your answer = ',guess[k],u'\t\t\tX'                  #Print students answer with a cross.
            print 'The correct answer = ',quest[k]                      #Print correct answer.
            print
        elif quest [k] != guess [k] and token[k] == 2:                  #If position [k] in list quest does not match position [k] in list guess and position [k] in list token equals 2.
            print k+1,'. ',num1[k],u' \u00f7 _______ = ', ans[k]        #Print Question.
            print 'Your answer = ',guess[k],u'\t\t\tX'                  #Print students answer with a cross.
            print 'The correct answer = ',quest[k]                      #Print correct answer.
            print
        elif quest [k] != guess [k] and token[k] == 3:                  #If position [k] in list quest does not match position [k] in list guess and position [k] in list token equals 3.
            print k+1,'. ',num1[k],u' \u00f7 ',num2[k],' = _______'     #Print Question.
            print 'Your answer = ',guess[k],u'\t\t\tX'                  #Print students answer with a cross.
            print 'The correct answer = ',quest[k]                      #Print correct answer.
            print
    print '+'*77
    print

    if quest == guess:                                                                                                                          #If statment, quest equals guess.
        print 'Well done! you got all of the questions right in %5.2f seconds! Your practice paid off! Try again to get a faster time!'%(timer) #Print well done message and display time it took.
        print
    else:                                                                                                                                       #Else Statment.
        print 'Good try! You scored %1d / 10 in %6.2f seconds! Keep practicing to get all'%(good,timer)                                         #Print try again statment. Display total questions correct and time it took.
        print 'the questions right!'
        print



main()      #Run function 'main'.
