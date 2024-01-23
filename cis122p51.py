'''
Title: CIS 122 Spring 2022 Project 5-1 - Mars rover starter code
Author(s): Steven Sanchez-Jimenez, Wyatt Humphries 
Credit: CIS 122 Resources, Office Hours
Description: Mars Rover Starter Code
'''
from turtle import*
import random
def mars_explore_setup():
    '''
    set up printed and graphical output
    called from: mars_explore_main
    >>> mars_explore_setup()
    '''
    # print title line for printed output
    print('xpos', '\t', # label for print output
    'ypos', '\t', # note special char \t
    'water', '\t', # which acts like the
    'temp') # tab key
    # set up graphical output
    reset()
    title('Mars Rover')
    speed('fastest')
    display_color = 'blue'
    pencolor(display_color)
    dot(10, display_color) # mark the rover's starting position
    return

def mars_explore_main():
    '''main function for mars_explore'''
    # set up printed and graphical environment
    mars_explore_setup()
    #explore Mars
    mars_explore(20)
    return

def mars_explore(stops):
    for i in range(stops):
        collect_data()

def collect_data():
    x = rover_loc()
    y = rover_loc()
    stamp()
    setpos(x, y)
    w = water_content()
    t = temperature()
    print(x , '\t', y, '\t', w,'\t', t)
    
def rover_loc():
    '''
    return random number for rover location
    >>> rover_loc()
    125 [for example]
    '''
    return random.randint(-275, 275)


def water_content():
    '''
    return random number for water content
    >>>water_content()
    150 [for example]
    '''
    return random.randint(1, 290)


def temperature():
    '''
    return random number for temperature
    >>>temperature()
    -50 [temperature]
    '''
    return random.randint(-178, 1)

mars_explore_main()
    
