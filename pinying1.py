import pyglet as gl
import MyInput as MI

window=gl.window.Window()
window.height=100

batch=gl.graphics.Batch()
Inp1=MI.Input(batch=batch,text="INPUT",x=0,y=window.height/2)

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_motion(x,y,dx,dy):
    Inp1.mouseMove(x,y)

@window.event
def on_mouse_press(x, y, button,modifiers):
    Inp1.mousePress(x,y,button,modifiers)

@window.event
def on_key_press(symbol,modifiers):
    Inp1.KeyInput(symbol,modifiers)
gl.app.run()
