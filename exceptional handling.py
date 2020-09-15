age = input('enter your age:')
try:
    a = int(age)
except:
    a = -1
if a>0:
    print('good job !')
else:
    print('not a number..')         
