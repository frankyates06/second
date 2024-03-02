def fancy_hello():
    greeting = "Hello, World!"
    border = "*" * (len(greeting) + 4)
    print(f"{border}\n* {greeting} *\n{border}")

fancy_hello()
