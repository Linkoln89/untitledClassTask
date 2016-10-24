    def gimme():
        i = 1
        while True:
            i += 1
            yield i

a = gimme()

name = 'Andrei'

d = {letter: next(a) for letter in name}
print(d)