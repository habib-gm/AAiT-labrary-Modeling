import sys, pygame 
from pygame.locals import * 
from pygame.constants import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
from camera.camera import Camera 
from loader.objloader import * 
import numpy as np 
from OpenGL.GL.shaders import * 
import os 
from PIL import * 
 
pygame.init() 
cam = Camera() 
 
obj = OBJ("mesh/of3.obj") 
# obj.generate() 
 
clock = pygame.time.Clock() 
glMatrixMode(GL_PROJECTION) 
glLoadIdentity() 
width, height = (800,600) 
gluPerspective(90.0, width/float(height), 1, 100.0) 
glEnable(GL_DEPTH_TEST) 
glMatrixMode(GL_MODELVIEW) 
 
glClearColor(1,1,1,1)
while 1: 
    clock.tick(30) 
    for e in pygame.event.get(): 
        if e.type == QUIT: 
            sys.exit() 
        cam.takeAc(e) 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
 
    glTranslate(cam.transX/10., cam.transY/10.,cam.transY/10. - cam.zpos) 
    glRotate(cam.rotx, 1, 0, 0) 
    glRotate(cam.roty, 0, 1, 0) 
    glScale(cam.sx, cam.sy, cam.sz) 
    obj.render() 
 
    pygame.display.flip()