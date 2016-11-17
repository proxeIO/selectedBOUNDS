import bpy

from bpy.types import PropertyGroup
from bpy.props import BoolProperty, EnumProperty, FloatVectorProperty, IntProperty

from .config import defaults as default

class selected_bounds(PropertyGroup):

  running = BoolProperty(
    name = 'Running',
    description = 'Used internally.',
    default = False
  )

  mode = EnumProperty(
    name = 'Display Mode',
    description = 'What objects to display bounds around.',
    items = [
      ('NONE', 'None', 'Disable selected bounds.'),
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
    description = 'Width of the lines.',
    min = 1,
    max = 20,
    subtype = 'PIXEL',
    default = default['width']
  )

  length = IntProperty(
    name = 'Length',
    description = 'Length of the lines as they extend from the corners.',
    min = 10,
    max = 100,
    subtype = 'PERCENTAGE',
    default = default['length']
  )
