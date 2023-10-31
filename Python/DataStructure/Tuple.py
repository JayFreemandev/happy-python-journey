# t1 = ()
# t2 = (1,)
# t3 = (1,2,3)
# t4 = ('a', 'b', ('c','d'))

# del t1[0]


# before tuple
a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)

# after tuple
c = 10
d = 20
c, d = d, c
print(c, d)


def magu_print(x, y, *rest):
    print(x, y, rest)