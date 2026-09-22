def main():
    while True:
        try:
            fraction = input("Fraction: ") # x/y
            x,y = fraction.split("/")
            if x.isnumeric() and y.isnumeric():
                x = int(x)
                y = int(y)
                if x <= y:
                    get_percent(x,y)
                    break
        except ValueError:
            pass

def get_percent( x , y ):
    try:
        z = (x/y)*100
    except ZeroDivisionError:
        pass
    else:
        if z <= 1:
            print("E")
            return
        elif z >= 99:
            print("F")
            return
        print(f"{round(z)}%")

main()
