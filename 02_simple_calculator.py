def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    raise ValueError("Operator must be +, -, * or /.")


if __name__ == "__main__":
    first = float(input("First number: "))
    op = input("Operator (+, -, *, /): ").strip()
    second = float(input("Second number: "))
    print("Result:", calculate(first, op, second))
