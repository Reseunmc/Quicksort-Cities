__author__ = 'Re'
from cs1lib import *


WINDOW_HEIGHT=320
WINDOW_WIDTH=720
PIXEL_CONVERSION=2
WINDOW_CENTERH=WINDOW_HEIGHT/2
WINDOW_CENTERW=WINDOW_WIDTH/2

#function to draw the cities
def draw_cities():
    img=load_image("world.png")
    draw_image(img,0,0)

#opens the file for reading
    file_name="cities_population.txt"
    in_file =open(file_name,"r" )

#c is the counter to determine when 50 dots have been drawn
    c=0

#for loop to strip and split the line into a list. Appends the objects to the empty list and indexes for the
#object parameters after the line is stripped and split
    for line in in_file:

#strips and splits the sentence into a list with comma breaks
        sentence= line.strip()
        stripped_sentence= sentence.split(",")

#iterate c and converts the latitude and longitude to the image given
        c+=1
        latitude=float(stripped_sentence[2])
        new_latitude=(latitude*PIXEL_CONVERSION)+WINDOW_CENTERH
        longitude=float(stripped_sentence[3])
        new_longitude=(longitude*PIXEL_CONVERSION)+WINDOW_CENTERW

#sets the fill color to red and draws the circle at the longitude and latitude points
        enable_smoothing()
        set_fill_color(1,0,0)
        draw_circle(new_longitude,new_latitude,4)
        request_redraw()
        sleep(.2)

#if the c is greater than 50 then the program will stop and the file will be closed
        if c>50:
            break
    in_file.close()

#True flipped the top and bottom
start_graphics(draw_cities,"World",WINDOW_WIDTH,WINDOW_HEIGHT,True)
