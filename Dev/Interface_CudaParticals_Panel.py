# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Documentation for this software can be found here:
# https://github.com/OltersdorfTechnology/CudaParticals

import bpy # import Blender's python interpreter
from mathutils import *
#D = bpy.data
#C = bpy.context
from bpy.types import (
    Operator,
    Panel,
    PropertyGroup,
)
from bpy.props import (
    BoolProperty,
    EnumProperty,
    Pointe

# Define the interface
class Interface_PT_Panel(bpy.types.Panel):
    bl_idname = "MenuName_PT_Panel"
    bl_label = "Panel Name"
    bl_category = "Tab name"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"

    def draw(self, context):    
        layout = self.layout

        scene = context.scene

        layout.label(text= "Properties:")

        row = layout.row()
        row.operator("view3d.print_text", text = "Print text", icon='WORLD_DATA')
# end define interface

classes = (
    Interface_PT_Panel,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
