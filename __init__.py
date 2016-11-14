
'''
Selection Box Addon
Copyright (C) 2016 Trentin Frederick (proxe)

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
  'version': (0, 0),
  'blender': (2, 69, 0),
  'location': '3D View \N{Rightwards Arrow} Properties Shelf \N{Rightwards Arrow} Display',
  'description': 'Display bounds of each selected object.',
  # 'wiki_url': '',
  # 'tracker_url': '',
  'category': '3D View'
}

# imports
import bpy
from bpy.utils import register_module, unregister_module
from bpy.props import PointerProperty

from .addon import interface, operator, properties
