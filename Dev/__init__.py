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
# ---------------------------------------------------------------------

# import from multile files that mak-up the addon
# # from . "file name" import "class"
# from . import auto_load
from . import Interface_CudaParticals_Panel
from . import operators_file_export
from . import operators_file_import
from . import operators_mesh_add
from . import operators_node
# "development_ui_classes.py" is "go-by" for "Interface_CudaParticals_Panel.py"
import os
import bpy

bl_info = {
    "name" : "CudaParticals",
    "author" : "Max Oltersdorf",
    "description" : "Enables the use of NIVIDA CUDA for Large realistic Particle Simulations",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Properties", # This is a new tab in the "properties section"
    "warning" : "IN EARLY DEVELOPMENT",
    "category" : "Physics"
    #"wiki_url": "'https://github.com/OltersdorfTechnology/CudaParticals/wiki'",
    #"tracker_url": "https://github.com/OltersdorfTechnology/CudaParticals/issues",
    "support": "Testing",
}

# auto_load.init()

def register():
    #auto_load.register()
    Interface_CudaParticals_Panel.register()
    operators_file_export.register()
    operators_file_import.register()
    operators_mesh_add.register()
    operators_node.register()


def unregister():
    #auto_load.unregister()
    Interface_CudaParticals_Panel.unregister()
    operators_file_export.unregister()
    operators_file_import.unregister()
    operators_mesh_add.unregister()
    operators_node.unregister()

if __name__ == "__main__":
    register()