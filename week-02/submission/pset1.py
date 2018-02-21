

#A LISTS
# poem used as stings is by rupi kaur, in honor of black history month
string1 = 'it is a blessing'
print (string1)
string2 = 'to be the color of earth'
print (string2)
string3 = 'do you know how often'
print (string3)
string4 = 'flowers confuse me for home'
print (string4)

#CREAT LIST
LIST =[string1, string2, string3, string4]
print (LIST)
print (LIST[3])
print (LIST[1:3])
string5 = 'last'
LIST2 =[string1, string2, string3, string4, string5]
print (LIST2)
print (len(LIST2))
string5 ='new'
LIST2 = LIST2 =[string1, string2, string3, string4, string5]
print (LIST2)


# B STRING
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
print (sentence_words)
# code source -https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
" ".join(['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them'])
print (" ".join(['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']))
print (" ".join(reversed(['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them'])))

sentence_words.sort()
print (sentence_words)

sorted(['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them'])
"""
The difference between the .sort() method and the sorted() method is that because we are copying the content of the list
into the sorted() function and not calling up the list itself, it will not change the content of sentence_words, while
the other one does/
"""

 # C Random Function
from random import randint
# this returns random integer: 100 <= number <= 1000
num = randint(100, 1000)
print (num)

assert(100 <= num <= 1000)
assert(0 <= num <= 1000)
#come back to this

print (num)

# D String Formatting Function

number = 5
booktitle = "beauty is a wound"
booktitle = booktitle.title()

def bestseller(n, book):

    message = "The number {} bestseller today is: {}" .format (n, book)
    return message

print (bestseller(number,booktitle))


# E PASSWORD VALIDATION FUNCTION???
# code source - stackflow- username -srinivasu u and Rafał Rawicki
# link -https://stackoverflow.com/questions/41117733/validation-a-password-python?rq=1
def password_check(password):

    SpecialSym=['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    return_val=True
    if len(password) < 8:
        print('the length of password should be at least 8 char long')
        return_val=False
    if len(password) > 14:
        print('the length of password should be not be greater than 14')
        return_val=False
    if sum(map(str.isdigit, password)) < 2:
        print('the password should have at least two numeral')
        return_val=False
    if not any(char.isupper() for char in password):
        print('the password should have at least one uppercase letter')
        return_val=False
    if not any(char.islower() for char in password):
        print('the password should have at least one lowercase letter')
        return_val=False
    if not any(char in SpecialSym for char in password):
        print('the password should have at least one of the symbols $@#')
        return_val=False
    if return_val:
        print('Congratulations')
    return return_val

password = input('enter the password : ')
print(password_check(password))



# F EXPONENTIAL FUNCTION
# code borrowd from DoEdu IT Educations available at:https://www.youtube.com/watch?v=DR5pxqzKIwY

a = 5
b = 4
exp = 1
for i in range (1,(b + 1)):
    exp = exp * a
print("The result is:", exp)

# in case input is not fixed / to turn it into a function
a = int(input("ENTER NUMBER: "))
b = int(input("ENTER EXPONENT: "))
exp = 1
for i in range (1,(b + 1)):
    exp = exp * a
print("The result is: ", exp)



# EXTRA CREDIT MIN AND MAX
#code borrowed from Martijn Pieters available at https://stackoverflow.com/questions/30313149/minimum-in-python-without-using-min-function-python-2-7
def min(x):
    minimum = x[-5]
    for i in x[-5:]:
        if i < minimum:
            minimum = i
            return minimum
A = [2,4,0,7,-1,19,3]
print(min(A))



def max(x):
    maximum = x[0]
    for i in x:
        if maximum > i:
            maximum = i
            return maximum

A = [2,4,0,7,-1,19,3]
print(max(A))
