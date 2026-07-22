def greet(name="World"):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    assert greet() == "Hello, World!"
    assert greet("Mihir") == "Hello, Mihir!"
    print(greet())
