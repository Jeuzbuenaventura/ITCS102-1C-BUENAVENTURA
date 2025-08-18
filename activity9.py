a = 12
b = 13
c = 14
d = 15

print(( a > b ) and ( c < d ))
print(( a > b ) or ( c < d ))
print(not( a < b ) and ( c < d ))
print(not( a < b ) or ( c < d ))

result = ((a < b) and not (c > d) or ((b == a + d and (a != d)) or (c < a)))
print(result)