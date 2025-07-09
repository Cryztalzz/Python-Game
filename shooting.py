from ursina import *
from ursina.shaders import lit_with_shadows_shader

def shoot(player, camera, gun, enemy_list, application, held_keys):
    gun.position = (0.3, -0.2)
    invoke(setattr, gun, 'position', (0.3, -0.25), delay=0.1)

    hit_info = raycast(camera.world_position, camera.forward, distance=100, ignore=[player])
    target_pos = None
    hit_enemy = None
    if hit_info.hit:
        target_pos = hit_info.world_point
        for enemy in enemy_list:
            if hit_info.entity == enemy and enemy.alive:
                hit_enemy = enemy
                break
    else:
        target_pos = camera.world_position + camera.forward * 100

    bullet = Entity(
        model='sphere',
        color=color.yellow,
        scale=0.1,
        position=camera.world_position,
        rotation=camera.world_rotation,
        shader=lit_with_shadows_shader
    )

    bullet.animate_position(
        target_pos,
        duration=0.15,
        curve=curve.linear
    )

    def on_bullet_hit():
        destroy(bullet)
        if hit_enemy:
            hit_enemy.kill()
    invoke(on_bullet_hit, delay=0.15) 