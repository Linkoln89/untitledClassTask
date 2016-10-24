test_text = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


#wrong solution
symbol = 'abcdefghijklmnopqrstuvwxyz'
for key in symbol:
    print (key, test_text.count(key))

#import string
#string.ascii_letters


# best solution
tracker = {}
for char in L:
    if char not in tracker:
        tracker[char] = L.count(char)
print(tracker)

# another solution
tracker = {}
for char in L[::2]:
    if char in tracker:
            continue
        tracker[char] = L.count(char)


print(tracker.keys())
print (set.L())




# sets
L = set('qwertrtrtet')
L2 = set('qweewrewrwerwe')

print(L)
print(L2)

print (L2 - L)

print (L2 | L)


#bool
a = 0
if not a:
    print('Got nothing')

# "exit code"
for _ in a:
    print(_)
    if _ == 'r':
        break
    else:
        print('not broken')












