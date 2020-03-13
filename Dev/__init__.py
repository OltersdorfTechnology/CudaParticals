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

bl_info = {
    "name" : "CudaParticals",
    "author" : "Max Oltersdorf",
    "description" : "Enables the use of NIVIDA CUDA for Large realistic Particle Simulations",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "TBD", # This is a new Editor? custom node system
    "warning" : "IN EARLY DEVELOPMENT",
    "category" : "Physics"
    "wiki_url": "https://github.com/OltersdorfTechnology/CudaParticals/wiki",
    "tracker_url": "https://github.com/OltersdorfTechnology/CudaParticals/issues",
    "support": "DEVELOPMEMT",
}

# import from multile files that mak-up the addon
# # from . "file name" import "class"
from . import auto_load
from . Interface_CudaParticals_Panel import Interface_PT_Panel
# "development_ui_classes.py" is "go-by" for "Interface_CudaParticals_Panel.py"

auto_load.init()

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()
