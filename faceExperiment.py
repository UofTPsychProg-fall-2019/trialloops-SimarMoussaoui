#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging
from psychopy.hardware import keyboard
from psychopy import core

event.globalKeys.add(key='q',func=core.quit)

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()


instructions = visual.TextStim(win, text = 'Thank you for participating in this experiment.Today, you will be deciding which of the faces presented are most trustworthy. In order to make your decision, you need to press l or r on your keyboard to indicate the left or right face is most trustworthy. When you are ready, please press the letter s to start the task.',pos = (0,0), color = 'black', height = 0.05) #note default color is white, which you can't see on a white screen!

instructions.draw()

win.flip()

keys = event.waitKeys(keyList = ('s'))

core.wait(1)

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things


# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
stimLeft = [r'rateFace\facesR\1.jpg', r'rateFace\facesR\2.jpg', r'rateFace\facesR\3.jpg', r'rateFace\facesR\4.jpg', r'rateFace\facesR\5.jpg', r'rateFace\facesR\6.jpg', r'rateFace\facesR\7.jpg', r'rateFace\facesR\8.jpg']
stimRight = [r'rateFace\facesR\8.jpg', r'rateFace\facesR\7.jpg', r'rateFace\facesR\6.jpg', r'rateFace\facesR\5.jpg', r'rateFace\facesR\4.jpg', r'rateFace\facesR\3.jpg', r'rateFace\facesR\2.jpg', r'rateFace\facesR\1.jpg']

# make your loop

trial = 0


#kb = keyboard.Keyboard()


#keys = kb.getKeys(['l', 'r'])
#for key in keys:
#    print(key.name)

#ListofKeys = getKeys(keyList=('l','r'), modifiers=False, timeStamped=False)

while trial <7:
    for t in range(8) :
        faceLeft = visual.ImageStim(win, image = stimLeft[t], pos = (-0.5,0))
    
        # include your trial code in your loop but replace anything that should 
        # change on each trial with a variable that uses your iterater
        # e.g. thisStimName = stim[t]
        #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
        # if you're recording responses, be sure to store your responses in a list
        # or DataFrame which also uses your iterater!
        faceRight = visual.ImageStim(win, image = stimRight[t], pos = (0.5,0))
    
        trial += 1
    
        myText = visual.TextStim(win, text = 'Which face is most TRUSTWORTHY?',pos = (0,0.2), color = 'black', height = 0.04) #note default color is white, which you can't see on a white screen!
        responseText = visual.TextStim(win, text = 'l = Left, r = Right.',pos = (0,-0.2), color = 'black', height = 0.03)
        # Step 2 draw stimuli
        faceLeft.draw()
        faceRight.draw()
        myText.draw()
        responseText.draw()
    
        # Step 3 flip window to show stim
        win.flip()

        # Step 4 wait for a response
        keys = event.waitKeys(keyList = ('l', 'r'))
        
        # saveAsExcel(fileName, sheetName='rawData', stimOut=None, dataOut=('n', 'all_mean', 'all_std', 'all_raw'), matrixOnly=False, appendFile=True, fileCollisionMethod='rename')
        
        
    break

conclusion = visual.TextStim(win, text = 'Thank you for participating in this experiment! Please call the experimenter for the next steps.',pos = (0,0), color = 'black', height = 0.07) #note default color is white, which you can't see on a white screen!

conclusion.draw()

win.flip()

keys = event.waitKeys(keyList = ('s'))

core.wait(1)

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
