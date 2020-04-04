import os
import bpy
from bpy.types import (
    Operator,
    Panel,
    PropertyGroup,
)
from bpy.props import (
    BoolProperty,
    EnumProperty,
)
bl_info = {
    "name" : "CudaParticals",
    "author" : "Max Oltersdorf",
    "description" : "Enables the use of NIVIDA CUDA for Large realistic Particle Simulations",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 2),
    "location" : "Properties", # This is a new tab in the "properties section"
    "warning" : "IN EARLY DEVELOPMENT",
    "category" : "SYSTEM",
    #"wiki_url": "'https://github.com/OltersdorfTechnology/CudaParticals/wiki'",
    #"tracker_url": "https://github.com/OltersdorfTechnology/CudaParticals/issues",
    "support" : "Dev",
}
# Define the interface
class CudaParticlePanel(bpy.types.Panel):
    bl_idname = "CudaParticle_Panel"
    bl_label = "CudaParticle"
    bl_category = "SYSTEM"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
   # bl_context = "CudaParticle"

    def draw(self, context):    
        layout = self.layout

        #scene = context.scene

        layout.label(text= "CudaParticals Properties:")

        #row = layout.row()
        #row.operator("view3d.print_text", text = "Print text", icon='WORLD_DATA')
        #global custom_icons
        self.layout.label(text="CudaParticle"),
        #custom_icons = None
        #custom_icons["PARTICLE_POINT"].icon_id
# end define interface
# global variable to store icons in
classes = (
    CudaParticlePanel,
)
def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)