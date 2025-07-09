from ursina import *
from ursina.shaders import lit_with_shadows_shader
import random

class Enemy(Entity):
    def __init__(self, position=(0,0,0), color=color.red, ground_y=10):
        tinggi = 2.5
        fixed_pos = (position[0], ground_y + tinggi/2, position[2])
        super().__init__(
            model='sphere',
            color=color,
            scale=(1,tinggi,1),
            position=fixed_pos,
            collider='box',
            shader=lit_with_shadows_shader
        )
        self.alive = True
        print(f"Enemy spawned at {fixed_pos} with color {color}")

    def kill(self):
        self.alive = False
        destroy(self)

def spawn_enemies(num_enemies, map_size, ground_y):
    enemy_list = []
    for _ in range(num_enemies):
        pos_x = random.uniform(-map_size/2 + 5, map_size/2 - 5)
        pos_z = random.uniform(-map_size/2 + 5, map_size/2 - 5)
        enemy = Enemy(position=(pos_x, 0, pos_z), color=color.red, ground_y=ground_y)
        enemy.strafe_center = pos_x
        enemy.strafe_range = random.uniform(8, 20)
        enemy.strafe_dir = random.choice([-1, 1])
        enemy_list.append(enemy)
    return enemy_list

def update_enemies(enemy_list, enemy_mode, map_size):
    if enemy_mode == 'strafing':
        for enemy in enemy_list:
            if enemy.alive:
                speed = 6
                enemy.x += enemy.strafe_dir * speed * time.dt
                min_x = enemy.strafe_center - enemy.strafe_range/2
                max_x = enemy.strafe_center + enemy.strafe_range/2
                if enemy.x <= min_x or enemy.x >= max_x:
                    enemy.strafe_dir *= -1
                enemy.x = max(min_x, min(max_x, enemy.x)) 