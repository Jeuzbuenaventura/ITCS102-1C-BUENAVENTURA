amount = eval(input("Enter amount to deposit : "))

print("Here is the breakdown of your deposit : ")

a = amount // 1000
amount = amount % 1000

b = amount // 500
amount = amount % 500

c = amount // 200
amount = amount % 200

d = amount // 100
amount = amount % 100

e = amount // 50
amount = amount % 50

f = amount // 20
amount = amount % 20

g = amount // 10
amount = amount % 10

h = amount // 1
amount = amount % 1

print("1000\t-" , a)
print("500\t-" , b)
print("200\t-" , c)
print("100\t-" , d)
print("50\t-" , e)
print("20\t-" , f)
print("10\t-" , g)
print("1\t-" , h)
