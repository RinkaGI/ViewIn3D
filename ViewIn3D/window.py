import pygame as pg
import moderngl as gl
import sys

class Visualizer:
    def __init__(self, title: str = "ViewIn3D Visualizer", width: int = 800, height: int = 600):
        self.title, self.width, self.height = title, width, height

        pg.init()

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode((self.width, self.height), flags= pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption(self.title)

        self.ctx = gl.create_context()
        self.clock = pg.time.Clock()

    def checkEvents(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit(0)

    def render(self):
        self.ctx.clear(color=(0.0, 0.0, 0.0))
        pg.display.flip()

    def run(self):
        while True:
            self.checkEvents()
            self.render()
            self.clock.tick(120)

if __name__ == '__main__':
    Visualizer().run()