a = [x/10 for x in range(11)]
print(a)

b = {(x, x**2, x**3) for x in range(-10, 11)}
print(b)

napisy = {'jeden','dwa','trzy'}
c = {x:len(x) for x in napisy}
print(c)