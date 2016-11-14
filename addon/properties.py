import bpy
from bpy.types import PropertyGroup
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty, IntProperty, FloatProperty

class selection_bounds(PropertyGroup):

  mode = EnumProperty(
    name = 'Display Mode',
    description = 'What objects to display bounds around.',
    items = [
      ('ACTIVE', 'Active', 'The active object.'),
      ('SELECTED', 'Selected', 'The selected objects.')
    ],
    default = 'ACTIVE'
  )

  color = FloatVectorProperty(
    name = 'Color',
    description = 'Color of the bounds.',
    subtype = 'COLOR',
    size = 4,
    min = 0.0,
    max = 1.0,
    default = (1.0, 1.0, 1.0, 0.5)
  )

  use_object_color = BoolProperty(
    name = 'Use Object Color',
    description = 'Use the object\'s color.',
    default = False
  )

  width = IntProperty(
    name = 'Width',
    description = 'Width of the lines in pixels.',
    min = 1,
    max = 10,
    default = 2
  )

  length = FloatProperty(
    name = 'Length',
    description = 'Length of the lines as they extend from the cornders.',
    min = 0.1,
    max = 1.0,
    default = 0.5
  )
