from ursina import *
def show_start_menu(pilih_mode_callback):
    start_menu = Entity(parent=camera.ui, enabled=True)
    Text(parent=start_menu, text='Pilih Mode Musuh', origin=(0,0), scale=1.5, y=0.15, color=color.white)
    Button(parent=start_menu, text='Musuh Diam', color=color.azure, y=0, scale_y=0.1, on_click=lambda: pilih_mode_callback('static', start_menu))
    Button(parent=start_menu, text='Musuh Strafing', color=color.orange, y=-0.15, scale_y=0.1, on_click=lambda: pilih_mode_callback('strafing', start_menu))
    mouse.locked = False
    application.paused = True
    return start_menu

def show_finish_screen(try_again_callback=None):
    finish_screen = Entity(parent=camera.ui, enabled=True)
    Text(parent=finish_screen, text='GAME FINISH!', origin=(0,0), scale=2, y=0.1, color=color.yellow)
    Button(parent=finish_screen, text='Keluar', color=color.azure.tint(-.2), y=-0.1, scale_y=0.1, on_click=application.quit)
    if try_again_callback:
        Button(parent=finish_screen, text='Try Again', color=color.lime, y=0.05, scale_y=0.1, on_click=try_again_callback)
    mouse.locked = False
    application.paused = True
    return finish_screen 