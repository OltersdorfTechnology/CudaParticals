import bpy # import Blender's python interpreter
from mathutils import *
#D = bpy.data
#C = bpy.context

# Define the interface
class Interface_PT_Panel(bpy.types.Panel):
    bl_idname = "MenuName_PT_Panel"
    bl_label = "Panel Name"
    bl_category = "Tab name"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):    
        layout = self.layout

        scene = context.scene

        layout.label(text= "Properties:")

        row = layout.row()
        row.operator("view3d.print_text", text = "Print text", icon='WORLD_DATA')
# end define interface