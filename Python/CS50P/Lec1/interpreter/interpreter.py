def main():
    exp = input("Expression: ")
    x, y, z = exp.split(" ")
    x = float(x)
    z = float(z)
    match y:
        case "+":
            print(add(x,z))
        case "*":
            print(mul(x,z))
        case "/":
            print(div(x,z))
        case "-":
            print(sub(x,z))


def add(x,z):
    return round(float(x + z), 1)
def mul(x,z):
    return round(float(x * z) , 1)
def div(x,z):
    return round(float(x / z) , 1)
def sub(x,z):
    return round(float(x - z), 1)




main()
