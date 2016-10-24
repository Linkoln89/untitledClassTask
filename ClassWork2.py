# Classwork 2

def function(x='OOPS', y=2):
    print(x)

    function('HEY!')
    function()


# comprehension lists

L = [1,2,3,0]

t = (i*2 for i in L if i)
l = [i*2 for i in L if i>2]
d = {i: i*2 for i in L if i}

print(t)
print(l)
print(d)

#generator
def gimme():
    L = [1, 3, 55, 8]
    for _ in L:
        return _
print (gimme())


def gimme():
    return xrange(100000)
response = gimme()
print(response)
print('Done')

#
def server_responce():
    return 'Not ready :505'

def gimme():
    i =0
    while True:
        #i < 5
        yield i
        i += 1

response = gimme()
print(response)
print('Done')

#a=next(generator)
for _ in response
    print(_)
