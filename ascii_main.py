from PIL import Image,ImageFont,ImageDraw
import numpy as np
import random
import os

def asciify_function(img,flag,f_name):
    
    font=ImageFont.load_default()
    letter_width=font.getsize('x')[0]
    letter_height=font.getsize('x')[1]

    WCF=letter_height/letter_width
    if flag==1:
        SCF=0.15 #Scaling factor adjustment adjusts how big the output is going to be 
    elif flag==2: 
        SCF=0.08

    width_BY_Letter=round(img.size[0]*SCF*WCF)
    height_BY_Letter=round(img.size[1]*SCF)
    S=(width_BY_Letter,height_BY_Letter)
    img=img.resize(S)
    img=np.sum(np.asarray(img),axis=2)
    img-=img.min()
    img=(1.0-img/img.max())
    GCF=1.5
    img=img**GCF
    # The array of ascii symbols from white to black
    #chars = np.asarray(list(' .,:irs?@9B&#'))
    colors=['* " ` . ,  ~ ` . myster_e : ; % ','* " ` . ,  ~ ` . MYSTER_E : ; % ','* " ` . ,  ~ ` . MyStEr-E : ; % ']
    i=random.randrange(0,len(colors))

    chars = np.asarray(list(colors[i]))

    
    # Map grayscale values to the symbol's index in the array
    img = (img*(chars.size-1)).astype(int)
    # Generate the ascii art symbols 
    lines = ("\n".join(
        ("".join(r) for r in chars[img]) )).split("\n")

    # Create an image object, set its width and height, 
    #  background color
    bgcolor='black'
    newImg_width= letter_width *width_BY_Letter
    newImg_height = letter_height * height_BY_Letter
    newImg = Image.new("RGBA", (
        newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)

    # pick color for each line by a gradient spectrum
    nbins = len(lines)


    # Print symbols to image
    leftpadding=0
    y = 0

    for line in lines:

        draw.text((leftpadding, y), 
            line, 'green', font=font)
        y += letter_height
    if flag==1:
        newImg = newImg.convert('RGB')
        newImg.save(os.getcwd()+'\\Results\\'+f_name)
    elif flag==2:
        newImg = newImg.convert('RGB')
        return newImg

#asciify_function('test.jpg',1)