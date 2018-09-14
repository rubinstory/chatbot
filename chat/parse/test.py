from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

try:
    # we can now start Firefox and it will run inside the virtual display
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    print (browser.title) #this should print "Google"

finally:
    #tidy-up
    browser.quit()
    display.stop() # ignore any output from this.
