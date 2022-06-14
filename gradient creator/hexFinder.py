colours = [
    0xFF0018, # red
    0xFFA52C, # orange
    0xFFFF41, # yellow
    0x008018, # green
    0x0000F9, # blue
    0x86007D, # purple
]

coloursDict = {
    "red": [0xFF, 0x00, 0x18],
    "orange": [0xFF, 0xA5, 0x2C],
    "yellow": [0xFF, 0xFF, 0x41],
    "green": [0x00, 0x80, 0x18],
    "blue": [0x00, 0x00, 0xF9],
    "purple": [0x86, 0x00, 0x7D],
}

colourStr = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
]

loopCounter = 0
devision = 50
for x, colour in enumerate(colourStr):
    for i in range(0, devision):
        thestr = ""
        for rgb in range(0,3):
            try:
                differnce = coloursDict[colourStr[x+1]][rgb] - coloursDict[colourStr[x]][rgb]
            except:
                differnce = coloursDict[colourStr[0]][rgb] - coloursDict[colourStr[x]][rgb]
            differnceStep = differnce / devision
            
            if rgb == 0:
                thestr += f"{hex(round(coloursDict[colour][rgb] + (differnceStep * i)))}"
                thestr = thestr.replace("0x", "")
                if len(thestr) == 1:
                    thestr += "0"
                
            elif rgb == 1:
                thestr += f"{hex(round(coloursDict[colour][rgb] + (differnceStep * i)))}"
                thestr = thestr.replace("0x", "")
                if len(thestr) == 3:
                    thestr += "0"
                
            elif rgb == 2:
                thestr += f"{hex(round(coloursDict[colour][rgb] + (differnceStep * i)))}"
                thestr = thestr.replace("0x", "")
                if len(thestr) == 3:
                    thestr += "0"

        print(f"0x{thestr}")
        loopCounter += 1
        #print(f"{thestr}")
            

print(f"{loopCounter}")
