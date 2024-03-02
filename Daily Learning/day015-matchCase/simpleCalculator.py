"""Match case using arithmetic symbol."""

a = int(input("Enter first number :\t"))
b = int(input("Enter the second number : \t"))
print("What operation you want to perform ? (+ , - , * , / )\t")
operation = input("Enter your operation:")

match operation:
    case "+":
        print("Sum is :", a + b)
    case "-":
        print("Difference is:", a - b)
    case "*":
        print("Multiplication is :", a * b)
    case "/":
        print("The division is :", a / b)
    case _:
        print("Invalid operation symbol.")
