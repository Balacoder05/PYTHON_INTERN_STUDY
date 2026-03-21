import random

while True:
    print("Rolling dice...")
    print(random.randint(1, 6))

    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        break