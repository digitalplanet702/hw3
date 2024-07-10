number: int = int(input("Give me a number?"));


if number % 3 == 0 and number % 5 == 0:
    print(f"Fizz Buzz");
elif number % 3 == 0:
    print(f"Buzz");
elif number % 5 == 0:
    print(f"Fizz");