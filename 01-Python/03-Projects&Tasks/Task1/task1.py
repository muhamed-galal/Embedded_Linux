import pyautogui
import webbrowser
import time

post1='This is first post using python script'
post2='Second'
post3='Third'
posts=[post1,post2,post3]
link = 'https://www.facebook.com/mohamed.galal.313924'

webbrowser.open_new(link)

time.sleep(5)
for i in posts:
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite("What's on your mind?")
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.typewrite(i)
    pyautogui.click(900,800)
    time.sleep(5)


'''

#while True:
    #print(pyautogui.position())    #check the mouce click position

webbrowser.register('chrome', 
                    None,
                    webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                   )               
#webbrowser.get('chrome').open_new(link)
 
                   '''