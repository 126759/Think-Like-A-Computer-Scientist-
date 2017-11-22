ss = "Hello, World"
tt = ss.upper()

print (tt)

fruit = 'apple'
m = fruit[1]
print(m)

m = fruit[0]
print (m)

list(enumerate(fruit))
[(0, 'a'), (1, 'p'), (2, 'p'), (3, 'l'), (4, 'e')]

sz = len(fruit)
last = fruit[sz - 1]

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

for c in fruit:
    print(c)
