'''
You can't store a function in a shelf but you can store strings, so store the functions as a string 
then use exec() or eval() to use them from the shelve To change a function to a string use inpect.getsource() 
However , you cannot use inspect.getsource when directly running the interpreter
'''
#when storing a function:

#functions
sq=lambda x:x*x
def sum(n,n2):
    return n+n2

#---------------
import shelve
from inspect import getsource
with shelve.open('path to shelf') as mem:
    sf=getsource(sum)
    mem['sum function']='def {}'+sf[sf.index('('):]
    mem['lambda function']=getsource(sq)
#getsource() does not work if you are not running a file

#when putting the function into your program:

import shelve
with shelve.open('path to shelf') as mem:
    previous_lambda=eval(mem['lambda function'])
    exec(mem['sum function'].format('prev_f'))#prev_f being the name of the function


#now you can use your functions
print(previous_lambda(4))
print(prev_f(2,3))
#in case you need to know whether a function is a lambda or a normal function (because both of them are stored differently):

if func.__name__=="<lambda>":
    print('func is lambda')
elif callable(func):
    print('func is an ordinary function')
else:
    print('func is not a functio
