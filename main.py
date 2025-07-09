from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import time
import random
from enemy import Enemy, spawn_enemies, update_enemies
from obstacle import spawn_obstacles
from platform_utils import spawn_platform_and_stairs
from ui import show_start_menu, show_finish_screen
from shooting import shoot
import os
import sys

app = Ursina()

ground = Entity(model='plane', scale=(100, 1, 100), color=color.lime, texture='white_cube', texture_scale=(100, 100), collider='box', shader=lit_with_shadows_shader, y=10)

sky = Sky(texture=load_texture('resources/environments/sky.exr'), scale=150, y=ground.y, color=color.white)

player = FirstPersonController()
player.position = (0, ground.y + 5, -40)
player.speed = 10
player.walk_speed = 3
player.crouch_speed = 2
player.default_camera_y = player.camera_pivot.y
player.crouch_camera_y = player.default_camera_y * 0.5
player.stand_height = 2
player.crouch_height = 1
player.stand_camera_y = 1
player.recoil_offset = 0
player.base_camera_rot_x = 0

gun = Entity(
    model='cube',
    parent=camera.ui,
    scale=(0.1, 0.3, 0.5),
    position=(0.3, -0.25),
    rotation=(-10, 20, -10),
    color=color.dark_gray,
    texture='white_cube',
    shader=lit_with_shadows_shader
)

pause_menu = Entity(parent=camera.ui, enabled=False)
Entity(parent=pause_menu, model='quad', scale=99, color=color.black66)

Button(parent=pause_menu, text='Keluar', color=color.azure.tint(-.2), y=-0.1, scale_y=0.1, on_click=application.quit)

wall_thickness = 2
wall_height = 20
map_size = 100

Entity(model='cube', scale=(map_size, wall_height, wall_thickness), position=(0, wall_height/2 + ground.y, map_size/2), collider='box', color=color.gray, shader=lit_with_shadows_shader)
Entity(model='cube', scale=(map_size, wall_height, wall_thickness), position=(0, wall_height/2 + ground.y, -map_size/2), collider='box', color=color.gray, shader=lit_with_shadows_shader)
Entity(model='cube', scale=(wall_thickness, wall_height, map_size), position=(-map_size/2, wall_height/2 + ground.y, 0), collider='box', color=color.gray, shader=lit_with_shadows_shader)
Entity(model='cube', scale=(wall_thickness, wall_height, map_size), position=(map_size/2, wall_height/2 + ground.y, 0), collider='box', color=color.gray, shader=lit_with_shadows_shader)

num_obstacles = 8
num_enemies = 6

obstacle_colors = [color.azure, color.violet, color.yellow, color.lime, color.orange, color.cyan, color.magenta, color.brown]

obstacle_boxes = spawn_obstacles(num_obstacles, map_size, ground, obstacle_colors)

enemy_list = spawn_enemies(num_enemies, map_size, ground.y)

platform = spawn_platform_and_stairs(ground)

fire_rate = 0.2
last_shot_time = 0

enemy_mode = None

finish_screen = None

def pilih_mode(mode, start_menu):
    global enemy_mode
    enemy_mode = mode
    start_menu.enabled = False
    mouse.locked = True
    application.paused = False
    gun.enabled = True

def input(key):
    if key == 'escape':
        pause_menu.enabled = not pause_menu.enabled
        application.paused = pause_menu.enabled
        gun.enabled = not gun.enabled
        mouse.locked = not pause_menu.enabled
    if key == 'mouse move':
        player.base_camera_rot_x = camera.rotation_x - player.recoil_offset

def try_again():
    global enemy_list, finish_screen, start_menu, obstacle_boxes, platform, enemy_mode
    for e in enemy_list:
        destroy(e)
    enemy_list = spawn_enemies(num_enemies, map_size, ground.y)
    for box in obstacle_boxes:
        pass
    destroy(platform)
    platform = spawn_platform_and_stairs(ground)

    if finish_screen:
        destroy(finish_screen)
        finish_screen = None

    enemy_mode = None
    start_menu.enabled = True
    mouse.locked = False
    application.paused = True
    gun.enabled = False

def update():
    global last_shot_time, finish_screen
    if held_keys['control']:
        player.speed = player.crouch_speed
        player.camera_pivot.y = player.crouch_camera_y
    elif held_keys['shift']:
        player.speed = player.walk_speed
        player.camera_pivot.y = player.default_camera_y
    else:
        player.speed = 10
        player.camera_pivot.y = player.default_camera_y

    if (finish_screen is None or not finish_screen.enabled) and all(not e.alive for e in enemy_list):
        finish_screen = show_finish_screen(try_again_callback=try_again)
        application.paused = True
        mouse.locked = False
        gun.enabled = False

        player.recoil_offset *= 0.85
    else:
        player.recoil_offset = 0
    camera.rotation_x = player.base_camera_rot_x + player.recoil_offset

    update_enemies(enemy_list, enemy_mode, map_size)

    if held_keys['left mouse'] and not application.paused:
        if time.time() - last_shot_time > fire_rate:
            shoot(player, camera, gun, enemy_list, application, held_keys)
            last_shot_time = time.time()

start_menu = show_start_menu(pilih_mode)

app.run() 