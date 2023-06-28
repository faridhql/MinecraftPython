from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
        )
        
class Test_button(Button):
            def __init__(self):
                super().__init__(
                    model = 'cube',
                    texture = 'brick',
                    color = color.blue
                )
        

def update():
    if held_keys['a']:
     test_square.x -= 4 * time.dt
app = Ursina()

test_square = Entity(model = 'cube', color =color.red,scale = (1,3), position = (5,1))
sans_texture = load_texture('assets/owi.jpg')
sans = Entity(model = 'quad', texture = sans_texture )


test_cube = Test_button()

app.run()