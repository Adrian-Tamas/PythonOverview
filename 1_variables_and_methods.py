number_of_users = 3
message = f"Sent message to {number_of_users} users"


def print_message(message: str) -> None:
    print(message)


def increment(value: int) -> int:
    return value + 3


print_message(message=message)
print(f"Number of users equals: {number_of_users}")

a = increment(number_of_users)

print(f"new number of users: {a}")

number_of_users = "four"

print(f"new value for the variable: {number_of_users}")

# hints not static types
b = increment(4.0)

print(f"value of b: {b}")

