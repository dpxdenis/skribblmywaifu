from pynput import mouse
import subprocess

canvas = []
positionSet = False
listener = 0
print('Welcome to SkribbleMyWaifu! Your weeb SkribblIO Drawing bot!')
print('Select your ScribbleIO PlayArea by leftclicking upleft and downright!')
print('What pic u want? Name it waifu.jpg!')

def on_click(x,y,button,pressed):
    if pressed:
        if len(canvas) < 2:
            canvas.append([x,y])
            print('Saved {0} Position: X: {1} Y: {2}'.format(len(canvas),x,y))
            global positionSet
            if len(canvas) == 2 and positionSet == False:
                positionSet = True
                listener.stop()
                if canvas[0][0] < 0:
                    print('Lol u would use me an ur second monitor? nice. U cant do this now.')
                    exit()
                print('Ready to haxxor Skribbl! IN 5 SECONDS! Dont worry senpai i close myself and running in the 9 ehm... background :)')
                print('Pro Tip! You can stop me with CONTROL+ALT+ESC (STRG+ALT+ESC)')
                subprocess.Popen('skribblmywaifu.py {0} {1} {2} {3}'.format(canvas[0][0],canvas[0][1],canvas[1][0],canvas[1][1]), shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
                #Other Methods
                #subprocess.Popen('skribblmywaifu.py {0} {1} {2} {3}'.format(canvas[0][0],canvas[0][1],canvas[1][0],canvas[1][1]), shell=True)
                #subprocess.Popen('powershell.exe py dev5.py {0} {1} {2} {3}'.format(canvas[0][0],canvas[0][1],canvas[1][0],canvas[1][1]))
                exit()

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()
