import pygame as pig
import typing
import colorsys
import math


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.jump = False
        self.bash_power = 3
        self.bash_cooldown = 0
        self.aiming = False
        self.arrow_pos = pig.mouse.get_pos()
        self.arrow_end_pos = pig.mouse.get_pos()
        self.speed =2
        self.digging = False
        self.gravityi = True
        self.gravity = .2
        self.velocity_x = 0
        self.velocity_y = 0
        self.trail = []
        self.inverse = False
        self.rainbow = True
        self.platform = False
        self.click = (0,0)


    def is_colliding(self, collider) -> typing.Tuple[str, bool]:
        if (self.x < collider.x + collider.width and
                self.x + self.width > collider.x):
            return ('x_axis_collision',True)
        if (self.y < collider.y + collider.height and
                self.y + self.height > collider.y):
            return ('y_axis_collision',True)

    def bash(self, collider, screen):
        if self.bash_power > 0 and self.bash_cooldown == 0:
            self.bash_power -= 1
            self.bash_cooldown = 60  # Cooldown for 60 frames (1 second)
            self.fire(collider, screen)

    def dig(self, collider, colliders:list):
        # Perform dig ability actions here
        # ...

        # Remove the collider from the list
        colliders.remove(collider)

    def draw(self, screen):
        pig.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

        if self.aiming:
            pig.draw.line(screen, (0, 255, 0), self.arrow_pos, self.arrow_end_pos, 2)

    def fire(self, collider, screen):
        dir_vector = (self.arrow_end_pos[0] - self.arrow_pos[0],
                      self.arrow_end_pos[1] - self.arrow_pos[1])
        magnitude = math.sqrt(dir_vector[0] ** 2 + dir_vector[1] ** 2)
        if magnitude != 0:
            normalized_vector = (dir_vector[0] / magnitude, dir_vector[1] / magnitude)
            speed = 10
            dx = normalized_vector[0] * speed
            dy = normalized_vector[1] * speed

            #

    def start_digging(self):
        self.digging = True

    def stop_digging(self):
        self.digging = False

    def move(self, screen_height):
        for event in pig.event.get():
            if event.type == pig.QUIT:
                quit()
            elif event.type == pig.KEYDOWN:
                if event.key == pig.K_UP or event.key == pig.K_SPACE and self.y == screen_height - 20:
                    self.velocity_y -= 3
                    self.jump = True
                    #print("jump")
                elif event.key == pig.K_LEFT or event.key == pig.K_a:
                    self.velocity_x =- self.speed
                elif event.key == pig.K_RIGHT or event.key == pig.K_d:
                    self.velocity_x = self.speed
            if pig.mouse.get_pressed()[0]:
                self.click=pig.mouse.get_pos()
                #print(self.click)
        

    def update(self, screen_height: int, screen_width: int, colliders:list) -> None:
       selfbounds = pig.Rect(self.x, self.y, self.width, self.width)
    
       # Check for collisions with colliders
       self.gravityi = True  # Assume gravity is applied unless a collision is detected
       
       for collider in colliders:
           iscolliding = selfbounds.colliderect(collider)
           if iscolliding:
               self.gravityi = False
               # Adjust the player's position to be on top of the block
               self.y = collider.y - self.height  # Place player on top of the block
               self.platform = True
               #print('COLLISION')
               if self.jump and self.platform:
                   self.y -= 5
                   self.jump = False
                   self.platform = False
              # else:
               self.velocity_y = 1

               
               

       if self.gravityi:
           self.velocity_y += self.gravity
      
   
       self.x += self.velocity_x
       if self.gravityi:
          self.y += self.velocity_y
   
       if self.y > screen_height - 20:
           self.y = screen_height - 20
           self.velocity_y = 0
       if self.x <= 0:
           self.velocity_x = 1
       if self.x >= screen_width:
           self.velocity_x = -1
   
       if self.velocity_x > 0:
           self.velocity_x -= 0.1
       if self.velocity_x < 0:
           self.velocity_x += 0.1
   
       self.trail.append((self.x, self.y))  # Add current position to trail
   
       if len(self.trail) > 20:  # Limit the trail length to 10
           self.trail.pop(0)  # Remove the oldest position
       
               #if iscolliding[1]:
               #    if self.digging:
               #        self.dig(collider)  # Perform dig ability on collision
               #    if iscolliding[0] == 'y_axis_collision':
               #        gravity = 0
               #    #    self.bash(collider, screen)  # Perform bash ability on collision
               

       # Update arrow position if aiming
       if self.aiming:
           self.arrow_end_pos = pig.mouse.get_pos()

    def delete_tile(self, terrain):
        # Check if the provided coordinates are within the bounds of the terrain
        #if 0 <= self.click[1] < len(terrain) and 0 <= self.click[0] < len(terrain[self.click[1]]):
            # Set the value at the specified position to 8 (sky block/empty tile)
        try:
            terrain[self.click[1]//10][self.click[0]//10] = 8
        except:
            print("tile does not exist")
        #else:
         #   print("Invalid coordinates")

    def draw_trail(self, screen: pig.Surface) -> None:
        trail_s_num: int = 1
        trail_l_num: int = len(self.trail)
        add_tsize: int = 1
    
        if self.inverse:
            for position in self.trail:
                pig.draw.circle(
                    screen, (255, 255, 255), position, (trail_l_num - trail_s_num)
                )
                trail_s_num += 1
        else:
            if self.rainbow:
                hue_step = 360 / len(self.trail)
                hue = 0
                for position in self.trail:
                    rgb = colorsys.hsv_to_rgb(hue / 360, 1, 1)
                    r, g, b = [int(c * 255) for c in rgb]
                    pig.draw.circle(
                        screen, (r, g, b), position, (trail_s_num + add_tsize)
                    )
                    add_tsize += 0.5
                    hue += hue_step
            else:
                r: int = 255
                g: int = 255
                b: int = 255
                for position in self.trail:
                    pig.draw.circle(
                        screen, (r, g, b), position, (trail_s_num + add_tsize)
                    )
                    add_tsize += 0.5
    
    def clear_trail(self) -> None:
        self.trail = []  # Clear the trail
    