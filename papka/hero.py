# напиши свій код тут


key_swich_camera = 'c'
key_swich_mod = 'z'
key_forward = 'w'
key_back = 's'
key_left = 'a'
key_right = 'd'
key_up = 'e'
key_down = 'q'

key_turn_left = 'n'
key_turn_right = 'm'

class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModer('smile')
        self.hero.setColor(1,0.5,0)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBird()
        self.accept_events()

    def cameraBird(self):
        base.disableMouse()
        base.camera.setH(100)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True

    def camerUP(self):
        pos = self.hero.gotPos()
        base.mouseInterfaeNode.setPos(-pos[0],-pos[1],-pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp:
        else:
            self.cameraBird()

    def turn_left(self):
        self.hero.setH(self.hero.getH()+5% 360)

    def turn_right(self):
        self.hero.setH(self.hero.getH()-5% 360)

    def look_at(self,angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dx
        return  x_to, y_to,z_from

    def just_move(self,angle):
        pos =self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        id self.mode:
            self.just_move(angle)

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)


    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)


    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)


    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True
    def try_move(self,angle):
        pos = self.look_at(angle)
        if self.landd.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1],pos[2] +1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)


    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addblock(pos)
        else:
            self.land.buildBlock(pos)


    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addblock(pos)
        else:
            self.land.buildBlockFrom(pos)

        def accept_events(self):
            base.accept(key_turn_left, self.turn_left)
            base.accept(key_turn_left + '-reparet', self.turn_left)
            base.accept(right(), self.turn_left)
            base.accept(key_turn_right + '-reparet', self.turn_right)

            base.accept(key_forward, self.forward)
            base.accept(key_forward + '-reparet', self.forward)
            base.accept(key_back, self.back)
            base.accept(key_back + '-reparet', self.back)
            base.accept(key_left, self.left)
            base.accept(key_left + '-reparet', self.left)
            base.accept(key_right, self.right)
            base.accept(key_right + '-reparet', self.right)

            base.accept(key_swich_camera, self.changeview)
            base.accept(key_swich_mod, self.changeview)

            base.accept(key_up, self.up)
            base.accept(key_up + '-repeat', self.up)
            base.accept(key_down, self.down)
            base.accept(key_down + '-repeat', self.down)

            base.accept(key_build, self.build)
            base.accept(key_destroy, self.destroy)