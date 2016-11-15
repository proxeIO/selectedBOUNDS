import bpy
from bpy.types import AddonPreferences


class preferences(AddonPreferences):

  bl_idname = __name__.partition('.')[0]

  def draw(self, context):

    layout = self.layout

    column = layout.column()
    column.enabled = not context.scene.selection_bounds.running
    column.scale_y = 2

    text = 'Enable' if not context.scene.selection_bounds.running else 'Running'
    column.operator('view3d.selection_bounds', text=text)
