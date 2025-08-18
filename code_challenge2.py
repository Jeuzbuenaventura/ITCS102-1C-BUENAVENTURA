amount = eval(input("Enter amount to deposit : "))

print("Here is a breakdown of your deposited amount using the PH denominations : ")

onethousand = amount // 1000
one_thousand = amount % 1000

fivehundred = amount // 500
five_hundred = amount % 500

twohundred = amount // 200
two_hundred = amount % 200

onehundred = amount // 100
one_hundred = amount % 100

fifty = amount // 50
fifiy_pesos = amount % 50

twenty = amount // 20
twenty_pesos = amount % 20

ten = amount // 10
ten_pesos = amount % 10

one = amount // 1
one_pesos = amount % 1

print( onethousand," - 1000" )
print( one_thousand )
print( fivehundred," - 500" )
print( five_hundred )
print( twohundred," - 200" )
print( two_hundred )
print( onehundred," - 100" )
print( one_hundred )
print( fifty," - 50" )
print( fifty_pesos )
print( twenty," - 20" )
print( twenty_pesos )
print( ten," - 10" )
print( ten_pesos )
print( one," - 1" )
print( one_pesos )
