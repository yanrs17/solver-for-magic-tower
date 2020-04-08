# import pygame
# from pygame.locals import * 
# from pygame.sprite import Sprite

# WINDOW_TITLE = "Magic Tower"

# class Tile(Sprite):
#     """single map tile.
#     Derives from Sprite().
    
#     this gives us a Surface() and a Rect() to store a loaded image.
#     """
#     def __init__(self, color):
#         """create surface"""
#         Sprite.__init__(self)
#         # get main screen, save for later
#         self.screen = pygame.display.get_surface()
        
#         # create empty surface, and color it        
#         self.color = pygame.Color(color) # convert the string to a pygame.Color()
#         self.image = pygame.Surface([64, 64])   # width, height
#         self.image.fill(self.color)
        
#         # save Rect() of loaded image
#             # Rect()s do tons of things, and have lots of helpers. 
#             # see details at: http://www.pygame.org/docs/ref/rect.html#pygame.Rect
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (100, 100)        
        
#         #or you could do
#             # self.rect.center = (100,100)
        
#     def draw(self):
#         """draw to screen"""
#         self.screen.blit(self.image, self.rect)
        
        
        
# class GameMain(object):
#     """game Main entry point. handles intialization of game and graphics, as well as game loop"""    
#     done = False
#     color_bg = Color('seagreen') # or also: Color(50,50,50) , or: Color('#fefefe')
    
#     def __init__(self, width=800, height=600):
#         """Initialize PyGame window.
        
#         variables:
#             width, height = screen width, height
#             screen = main video surface, to draw on
            
#             fps_max     = framerate limit to the max fps
#             limit_fps   = boolean toggles capping FPS, to share cpu, or let it run free.
#             now         = current time in Milliseconds. ( 1000ms = 1second)
#             color_bg    = backround color, accepts many formats. see: pygame.Color() for details
#         """
#         pygame.init()

#         # save w, h, and screen
#         self.width, self.height = width, height
#         self.screen = pygame.display.set_mode(( self.width, self.height ))
#         pygame.display.set_caption( WINDOW_TITLE )        

#         # fps clock, limits max fps
#         self.clock = pygame.time.Clock()
#         self.limit_fps = True
#         self.fps_max = 40        

#         # tile class,
#         #   later replace with a Map() class
#         self.tile = Tile('darkgrey')

#     def main_loop(self):
#         """Game() main loop.
#         Normally goes like this:
        
#             1. player input
#             2. move stuff
#             3. draw stuff
#         """
#         while not self.done:
#             # get input
            
#             self.handle_events()
#             # move stuff            
#             self.update()
            
#             # draw stuff
#             self.draw()
            
#             # cap FPS if: limit_fps == True
#             if self.limit_fps: self.clock.tick( self.fps_max )
#             else: self.clock.tick()
    
#     def draw(self):
#         """draw screen"""
#         # clear screen."
#         self.screen.fill( self.color_bg )
        
#         # draw code
#         self.tile.draw()
        
#         # update / flip screen.
#         pygame.display.flip()
        
#     def update(self):
#         """move guys.
#         Currently it only stores the current time in MS"""
#         self.now = pygame.time.get_ticks()        

#     def handle_events(self):
#         """handle events: keyboard, mouse, etc."""
#         events = pygame.event.get()
#         kmods = pygame.key.get_mods()
        
#         for event in events:
#             if event.type == pygame.QUIT: self.done = True
#             # event: keydown
#             elif event.type == KEYDOWN:
#                 if event.key == K_ESCAPE: self.done = True
                
#                 # other events , uncomment to use
                
#                 # boilerplate : keydown
                
#                 elif event.key == K_DOWNARROW:
#                     print('move down')
#                 elif event.key == K_UPARROW:
#                     stuff()
                    
                

#             # other events , uncomment to use
            
#             elif event.type == MOUSEMOTION:
#                 x,y = event.pos                
#                 print(x,y)
                
#             elif event.type == MOUSEBUTTONUP:                
#                 x,y = event.pos
#                 button = event.button
#                 print(x, y, button)
                
#             elif event.type == MOUSEBUTTONDOWN:
#                 x,y = event.pos
#                 button = event.button                                

#                 # state based on key
#                 if button == 1:
#                     # if LMB + ctrl + shift
#                     if kmods & KMOD_LCTRL and kmods & KMOD_LSHIFT:
#                         print("ctrl + shift + LMB ")
                

# if __name__ == "__main__":             
#     game = GameMain()
#     game.main_loop()    
