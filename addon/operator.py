import bpy
from bpy.types import Operator
from bgl import glEnable, GL_BLEND, glColor4f, glLineWidth, glBegin, GL_LINES, glVertex3f, glEnd, glDisable
from mathutils import Vector

class selection_bounds(Operator):
  bl_idname = 'view3d.selection_bounds'
  bl_label = 'Selection Bounds'
  bl_description = 'Display bounds of each select object.'
  bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}


  
