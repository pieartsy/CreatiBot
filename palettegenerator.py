#to open urls
import requests
# to parse requests
import json
#regex
import re
#joins paths for a file
import os.path
#to convert svg to png
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
#to stitch together images
from PIL import Image
#error handler to let me know what's wrong with my code!!
import traceback


def palettegen():
        #grabs a random color palette from colormind.io
        paletteURL = "http://colormind.io/api/"
        data = '{"model": "default"}'

        #returns <Response [200]> from colormind
        paletteResponse = requests.get(paletteURL, data=data)
        #returns json result
        #ex: {'result': [[252, 238, 8], [212, 209, 72], [223, 151, 55], [232, 69, 18], [203, 31, 21]]}
        paletteDict = paletteResponse.json()
        #finagling to turn the result from a response to a dictionary to a list
        #ex: [[[196, 185, 84], [198, 206, 178], [91, 168, 124], [34, 110, 132], [16, 50, 85]]]
        paletteList = list(paletteDict.values())
        print(paletteList)
        #gonna collect the color URLs from thecolorapi.com
        colorURLs = []

        #you need to go deeper into the list elements twice for some reason.
        #I think the list is in a list that's just itself as an element? idk
        #so you need to use two 'for' loops
        for values in paletteList:
                for value in values:
                        #turns [n, n, n] to (n,n,n)
                        value ="(" + re.sub('[\[\]]', '',  str(value)) + ")"
                        value = value.replace(' ', '')
                        print(value)
                        colorURLs.append("https://www.thecolorapi.com/id?rgb=rgb" + value + "&format=svg")
                        print(colorURLs)
        #where to store the files
        filepath = os.getcwd()
        filenames = []

        #for every color in the colorURLs list, grab the info from the URL using requests
        for number in range(5):
                response = requests.get(colorURLs[number])
                #for some reason the last response doesn't work sometimes?? time to find out why
                try:    
                        print(response.status_code)
                except:
                        traceback.print_exc()
                        print("NOPE")
                #if response is good
                if response.status_code == 200:
                        #append a filename to filenames.
                        #Full path will look like C:\\Users\\Maddie\\Pictures\\palettes\\color_1.svg
                        filenames.append(os.path.join(filepath, "color_" + str(number+1) + ".svg"))
                        #Save svg file
                        with open(filenames[number], 'wb+') as f:
                                f.write(response.content)
                        #convert svg file to png.
                        #Full path will look like C:\\Users\\Maddie\\Pictures\\palettes\\color_1.svg.png
                        drawing = svg2rlg(filenames[number])
                        renderPM.drawToFile(drawing, filenames[number] + ".png", fmt="PNG")

        #Time to stitch the palette file together! Makes a blank 500 by 100 px image
        #(because each of the 5 images is 100x100 px)
        palette = Image.new('RGB', (500, 100))
        #Tells us how far away to space the images from each other
        x_offset = 0

        #for every of the 5 colors
        for number in range(5):
                #opens the color file
                color = Image.open(os.path.join(filepath, filenames[number] + ".png"))
                #pastes the color image into the palette image (starting at 0 in the upper left corner)
                palette.paste(color, (x_offset, 0))
                #adds 100 to x_offset (color.size is a tuple containing the width -> 0 and height -> 1)
                x_offset += color.size[0]

        #saves palette as palette.png
        palette.save(os.path.join(filepath, "palette.png"))

palettegen()