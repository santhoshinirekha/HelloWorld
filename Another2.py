numbers = [5, 2, 5, 2, 2]
for shape in numbers:
    print(numbers)








for x in range(5):
    for y in range(4):
        print(f' ({x}, {y})')




















prices = [10,  20, 30]

total = 0
for prices in [10, 20, 30, 40, 50]:
    total =+ prices
print(f"total: {total}")
























secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('You Failed!')








guess_count = 1
while guess_count <= 5:
    print('*' * guess_count)
    guess_count = guess_count + 1
print("Done")












weight = int(input('weight: '))
print(type(weight))
weight_lbs_kgs = input('(lbs) or (kgs): ')
print(type(weight_lbs_kgs))
if weight_lbs_kgs == "lbs":
    print(f"You are ({weight * 0.5}) kilograms")
else:
    print(f"You are ({weight * 2.2}) pounds")