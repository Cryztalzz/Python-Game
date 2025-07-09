from ursina import *
from ursina.shaders import lit_with_shadows_shader

def spawn_platform_and_stairs(ground):
    platform_height = 10
    platform = Entity(
        model='cube',
        scale=(20, 2, 20),
        position=(35, ground.y + platform_height, 0),
        color=color.brown,
        collider='box',
        shader=lit_with_shadows_shader
    )
    stair_count = 8
    stair_width = 4
    stair_depth = 2
    stair_height = platform_height / stair_count
    for i in range(stair_count):
        Entity(
            model='cube',
            scale=(stair_width, stair_height, stair_depth),
            position=(25 + i*1.5, ground.y + (i+0.5)*stair_height, 0),
            color=color.gray,
            collider='box',
            shader=lit_with_shadows_shader
        )
    return platform 