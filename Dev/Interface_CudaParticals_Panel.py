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
)
# Define the interface
class CudaParticlePanel(bpy.types.Panel):
    bl_idname = "CudaParticle_Panel"
    bl_label = "CudaParticle"
    bl_category = "SYSTEM"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'UI'
   # bl_context = "CudaParticle"

    def draw(self, context):    
        #layout = self.layout

        #scene = context.scene

        #layout.label(text= "Properties:")

        #row = layout.row()
        #row.operator("view3d.print_text", text = "Print text", icon='WORLD_DATA')
        global custom_icons
        self.layout.label(text="CudaParticle",
# end define interface

icon_value=custom_icons["custom_icon"].icon_id)
# global variable to store icons in
custom_icons = None

classes = (
    CudaParticlePanel,
)


def register():
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    script_path = bpy.context.space_data.text.filepath
    icons_dir = os.path.join(os.path.dirname(script_path), "Icons")
    custom_icons.load("Tool_Icon", os.path.join(icons_dir, "Tool_Icon.png"), 'IMAGE')
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    global custom_icons
    bpy.utils.previews.remove(custom_icons)
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
