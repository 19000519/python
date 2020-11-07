#Author : Phenyo
#Purpose : validate length of a string

weight = float(input('Weight : '))
unit = input('(L)bs or (K)g : ')

if unit.upper() == "L" :
    converted = weight * 0.453
    print(f'you are {converted} kilograms')

elif unit.upper() == "K":
    converted = weight / 0.453
    print(f'you are {converted} pounds')
45
