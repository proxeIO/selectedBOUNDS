
'''
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# addon info
bl_info = {
  'name': 'Selection Bounds',
  'author': 'Trentin Frederick (proxe)',
  'version': (0, 2),
  'blender': (2, 69, 0),
  'location': '3D View \N{Rightwards Arrow} Properties Shelf \N{Rightwards Arrow} Display',
  'description': 'Display bound indicators around objects.',
  # 'wiki_url': '',
  # 'tracker_url': '',
  'warning': 'Requires Restart',
  'category': '3D View'
}

# imports
import bpy
from bpy.app.handlers import persistent
from bpy.utils import register_module, unregister_module
from bpy.props import PointerProperty

from .addon import interface, operator, properties


@persistent
def load_handler(self):
  bpy.ops.view3d.selection_bounds('INVOKE_DEFAULT')

bpy.app.handlers.load_post.append(load_handler)

def register():

  register_module(__name__)

  bpy.types.Scene.selection_bounds = PointerProperty(
    type = properties.selection_bounds,
    name = 'Selection Bounds',
    description = 'Storage location for selection bounds settings.'
  )

  bpy.types.VIEW3D_PT_view3d_display.append(interface.draw)

def unregister():

  unregister_module(__name__)

  bpy.types.VIEW3D_PT_view3d_display.remove(interface.draw)

  del bpy.types.Scene.selection_bounds
