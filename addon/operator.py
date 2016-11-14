import bpy
from bpy.types import Operator
from bgl import glEnable, GL_BLEND, glColor4f, glLineWidth, glBegin, GL_LINES, glVertex3f, glEnd, glDisable
from mathutils import Vector

class selection_bounds(Operator):
  bl_idname = 'view3d.selection_bounds'
  bl_label = 'Selection Bounds'
  bl_description = 'Display bound indicators around objects.'
  bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}


  def modal(self, context, event):

    if context.area:

      context.area.tag_redraw()

    return {'PASS_THROUGH'}


  def invoke(self, context, event):

    bpy.types.SpaceView3D.draw_handler_add(self.draw_bounds, (self, context), 'WINDOW', 'POST_VIEW')

    context.window_manager.modal_handler_add(self)

    return {'RUNNING_MODAL'}


  @staticmethod
  def draw_bounds(self, context):

    if context.object:

      try: option = context.scene.selection_bounds
      except: return
      length = option.length*0.5

      glEnable(GL_BLEND)
      glLineWidth(option.width)

      if option.mode == 'ACTIVE':

        if context.object.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE'}:

          color = option.color if not option.use_object_color else context.object.color
          glColor4f(color[0], color[1], color[2], color[3])

          matrix = context.object.matrix_world
          bounds = context.object.bound_box

          draw_corner(length, matrix, bounds)

      elif option.mode == 'SELECTED':

        for object in context.selected_objects:

          if object.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'LATTICE'}:

            color = option.color if not option.use_object_color else object.color
            glColor4f(color[0], color[1], color[2], color[3])

            matrix = object.matrix_world
            bounds = object.bound_box

            draw_corner(length, matrix, bounds)

      else: return

      glColor4f(0.0, 0.0, 0.0, 1.0)
      glLineWidth(1)
      glDisable(GL_BLEND)

    else:

      return


def draw_corner(length, matrix, bounds):

  for index in range(0, 8):

    pointer_x = index + 4 if index < 4 else index - 4

    pointer_y = 3 - index if index < 4 else 10 - (index - 1)

    pointer_z = index + 1 if index % 2 == 0 else index - 1

    draw_lines(length, matrix, bounds[index], bounds[pointer_x], bounds[pointer_y], bounds[pointer_z])


def draw_lines(length, matrix, origin, x, y, z):

  x = (origin[0] - (origin[0] - x[0])*length, x[1], x[2])
  y = (y[0], origin[1] - (origin[1] - y[1])*length, y[2])
  z = (z[0], z[1], origin[2] - (origin[2] - z[2])*length)

  origin = matrix * Vector(origin)
  x = matrix * Vector(x)
  y = matrix * Vector(y)
  z = matrix * Vector(z)

  glBegin(GL_LINES)

  glVertex3f(origin[0], origin[1], origin[2])
  glVertex3f(x[0], x[1], x[2])
  glVertex3f(origin[0], origin[1], origin[2])
  glVertex3f(y[0], y[1], y[2])
  glVertex3f(origin[0], origin[1], origin[2])
  glVertex3f(z[0], z[1], z[2])

  glEnd()
