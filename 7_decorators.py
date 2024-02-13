def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(5)
def greet(name):
    print(f"Hello, {name}!")


# Calling the decorated function
if __name__ == '__main__':
    greet("Adrian")
