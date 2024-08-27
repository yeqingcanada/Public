print('############################### 3- Ternary Operator ########################################################')
age = 22
if age >= 18:
    message = 'Eligible'
else:
    message = 'Not eligible'

message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)

print('############################### 11- Iterables ########################################################')
print(type(range(5)))
for x in range(5):
    print(x)

for x in "python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)
