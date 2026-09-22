import sys
from random import choice
from pyfiglet import Figlet

def main():

    if len(sys.argv) == 1:
        ## random font, f = random.choice(fontlist)
        s = input("Input: ")
        figlet = Figlet()
        f = choice(figlet.getFonts())
        figlet.setFont(font=f)
        print("Output: ",figlet.renderText(s) , sep ="\n")
    elif len(sys.argv) == 3:
        ## specific font
        figlet = Figlet()
        if sys.argv[1] == "-f" and sys.argv[2] in figlet.getFonts():
            s = input("Input: ")
            f = sys.argv[2]
            figlet.setFont(font=f)
            print("Output: ",figlet.renderText(s) , sep ="\n")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")



#figlet = Figlet()
# figlet.setFont(font = "slant")
# print(figlet.renderText("S"))
main()
