import bpy

from bpy.types import PropertyGroup
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty, IntProperty, FloatProperty

from .config import defaults as default

class selection_bounds(PropertyGroup):

  running = BoolProperty(
    name = 'Running',
    description = 'Used internally.',
    default = False
  )

  mode = EnumProperty(
    name = 'Display Mode',
    description = 'What objects to display bounds around.',
    items = [
      ('NONE', 'None', 'Disable selection bounds.'),
      ('SELECTED', 'Selected Objects', 'The selected objects.'),
      ('ACTIVE', 'Active Object', 'The active object.'),
    ],
    default = default['mode']
  )

  color = FloatVectorProperty(
    name = 'Color',
    description = 'Color of the bounds.',
    subtype = 'COLOR',
    size = 4,
    min = 0.0,
    max = 1.0,
    default = default['color']
  )

  use_object_color = BoolProperty(
    name = 'Use Object Color',
    description = 'Use the object\'s color.',
    default = default['use_object_color']
  )

  width = IntProperty(
    name = 'Width',
    description = 'Width of the lines in pixels.',
    min = 1,
    max = 10,
    default = default['width']
  )

  length = FloatProperty(
    name = 'Length',
    description = 'Length of the lines as they extend from the cornders.',
    min = 0.1,
    max = 1.0,
    default = default['length']
  )
