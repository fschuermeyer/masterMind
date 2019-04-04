import random
from sty import fg, bg, ef, rs, RgbFg
import sys

class MasterMind:

    color = 8
    holes = 5

    listOfColors = ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige","Bisque","Black","BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGrey","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","Darkorange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkSlateGrey","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DimGrey","DodgerBlue","FireBrick","FloralWhite","ForestGreen","Fuchsia","Gainsboro","GhostWhite","Gold","GoldenRod","Gray","Grey","Green","GreenYellow","HoneyDew","HotPink","IndianRed","Indigo","Ivory","Khaki","Lavender","LavenderBlush","LawnGreen","LemonChiffon","LightBlue","LightCoral","LightCyan","LightGoldenRodYellow","LightGray","LightGrey","LightGreen","LightPink","LightSalmon","LightSeaGreen","LightSkyBlue","LightSlateGray","LightSlateGrey","LightSteelBlue","LightYellow","Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquaMarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin","NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenRod","PaleGreen","PaleTurquoise","PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","SeaShell","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SlateGrey","Snow","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","White","WhiteSmoke","Yellow","YellowGreen"]

    def getRandomColor(self):
        length = len(self.listOfColors) - 1


        possibleColors = []

        for i in range(0,self.color):
            possibleColors.append(self.listOfColors[random.randint(0,length)])

        print("Colors in Game:")

        print(bg.yellow + str(possibleColors) + bg.rs)


        key = []

        for i in range(0,self.holes):
            key.append(possibleColors[random.randint(0,self.color - 1)])

        self.key = key

        print(fg.black + str(self.key) + fg.rs)


        return possibleColors


    def getColors(self,colors):

        white = 0
        black = 0

        if len(colors) != 5:
            return False

        PossibleWhite = []
        PossibleOptions = []


        for i in range(0,5):
            if colors[i] == self.key[i]:
                black += 1
            else:
                PossibleWhite.append(colors[i])
                PossibleOptions.append(self.key[i])

        if black == 5:
            print(bg.red  + "Won" + bg.rs)
            return True


        for color in PossibleOptions:
            if color in PossibleWhite:
                i = 0
                for item in PossibleWhite:
                    if item == color:
                        del PossibleWhite[i]
                        white += 1


                    i += 1

        print()
        print(bg.white + fg.black + "White: " + str(white) + bg.rs + fg.rs)

        print("Black: " + str(black))
        print()




if __name__ == '__main__':

    app = MasterMind()
    colorsPossible = app.getRandomColor()
    b = 0

    while True:
        print(bg.yellow + "Round: " + str(b) + bg.rs)

        ide = []

        for i in range(0,5):
            while True:

                c = input("["+str(i + 1)+"] Color: ")

                if c in colorsPossible:
                    ide.append(c)
                    break;
                else:
                    print(fg.red + "Type a Other Color " + fg.rs + c + " is not a Color")


        help = ''
        for elm in ide:
            help += elm + " "

        print(bg.red + help + bg.rs)

        if app.getColors(ide):
            break;

        b += 1