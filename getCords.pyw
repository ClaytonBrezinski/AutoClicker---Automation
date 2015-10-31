##
##All coordinates assume a screen resolution of 1280x1024, and Chrome 
##maximized with the Bookmarks Toolbar disabled.
##
# For the image grab function
import ImageGrab, os, time
# For the mousing around function
import win32api, win32con

#---Globals---
# top left corner of the screen
xCo = 78
yCo = 0
# to bottom right corner of the screen
xDif = 919
yDif = 1078
#-------------
def getCords():
    x,y = win32api.GetCursorPos()
    x = x - xCo
    y = y - yCo
    print x,y

#### - Main - ####                         
def main():
    getCords()             
if __name__ == '__main__':
    main()
