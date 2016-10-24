# Homework2 - check in class




#for key in sorted(letters):
#    print(str(key) + '=' + str (letters[key]))

#    print('{}={}'.format(key, counter[key]))
#    print('{K}={C}'.format(K=key, C=counter[key]))
#    print('{0}={1}{0}'.format(key, counter[key]))

#    print('%s=%f' % (key, counter[key]))

def fine_print(to_print):
    for _ in to_print:
        print(str(_) + '=' + str(to_print[key]))

letters = {}
for litera in L:
        counter = letters.get(litera,0)
        counter +=1
        letters[litera] = counter

fine_print(letters)
fine_print(letters(sort))
fine_print(sorted(letters,key=lambda x: x.islower()))

# idael
counter = {}
storage_list = []

for char in L:
    if char in counter:
        continue
        counter[char] = L.count(char)

#for _ in counter:
    #storage_list.append((_, counter[]))
    storage_tuple = ((_, counter[_]) for _ in counter)

def sorting_algorythm(x):
    return x[1]

print(sorted(storage_tuple, key=sorting_algorythm, reverse=True))
print(sorted(storage_tuple, key=lambda x: x[1], reverse=True))

print(filter(lambda x: x>2), storage_tuple)