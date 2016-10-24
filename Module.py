#import ClassWork1

#print('Imported!')


#useful_function()
def useful_function():
    pass

if __name__ == '__main__':
    print(globals())

#
age = 10
a = ''
if age < 20:
    a='Hi!'
elif age > 30:
     a= 'Hello!'
else:
    a = 'Get off!'
print(a)

#
def useful_func (useful_string):
    print (useful_string * 20)

useful_func('asdasdadas')

#
def useful_func (useful_string):
    seen = L.count(useful_string)
    return seen, 10

a,b= useful_func('a')

print(useful_func('a'))