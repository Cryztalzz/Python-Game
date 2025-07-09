from ursina import *
import random
from ursina.shaders import lit_with_shadows_shader

def spawn_obstacles(num_obstacles, map_size, ground, obstacle_colors):
    obstacle_boxes = []
    def is_overlap(box1, box2):
        return not (
            box1['max_x'] < box2['min_x'] or box1['min_x'] > box2['max_x'] or
            box1['max_z'] < box2['min_z'] or box1['min_z'] > box2['max_z']
        )
    for _ in range(num_obstacles):
        for attempt in range(30):
            size_x = random.uniform(3, 12)
            size_y = random.uniform(4, 12)
            size_z = random.uniform(2, 8)
            pos_x = random.uniform(-map_size/2 + 10, map_size/2 - 10)
            pos_z = random.uniform(-map_size/2 + 10, map_size/2 - 10)
            pos_y = ground.y + size_y/2
            new_box = {
                'min_x': pos_x - size_x/2,
                'max_x': pos_x + size_x/2,
                'min_z': pos_z - size_z/2,
                'max_z': pos_z + size_z/2
            }
            if all(not is_overlap(new_box, box) for box in obstacle_boxes):
                Entity(
                    model='cube',
                    scale=(size_x, size_y, size_z),
                    position=(pos_x, pos_y, pos_z),
                    color=random.choice(obstacle_colors),
                    collider='box',
                    shader=lit_with_shadows_shader
                )
                obstacle_boxes.append(new_box)
                break
    return obstacle_boxes 