Weight = float(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')

if unit.lower() == 'l':
    converted_weight = round(Weight * 0.453592, 1)
    print(f'Your weight in kilograms is {converted_weight}')
elif unit.lower() == 'k':
    converted_weight = round(Weight * 2.20462, 1)
    print(f'Your weight in pounds is {converted_weight}')
else:
    print('Invalid unit. Please enter either (L)bs or (K)g.')