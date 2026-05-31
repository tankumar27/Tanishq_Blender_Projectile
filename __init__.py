
bl_info = {
    "name": "Tanishq-Projectile",
    "author": "Tanishq Kumar",
    "version": (2, 1),
    "blender": (3, 0, 0),
    "location": "3D View Sidebar > Physics tab",
    "description": "Rigid body instancer",
    "tracker_url": "https://github.com/tankumar27/Tanishq_Blender_Projectile",
    "category": "Physics"
}

import bpy
from bpy.app.handlers import persistent

from . import props
from . import ui
from . import ops
from . import utils


# Functions to run on file load
@persistent
def file_load_callback(scene):
    props.subscribe_to_rna_props()

    # Toggle trajectory drawing if enabled in this .blend
    utils.toggle_trajectory_drawing()

def register():
    props.register()
    ui.register()
    ops.register()

    # Add a callback for file load
    bpy.app.handlers.load_post.append(file_load_callback)

    props.subscribe_to_rna_props()

def unregister():
    props.unregister()
    ui.unregister()
    ops.unregister()

    # Remove file load handler
    bpy.app.handlers.load_post.remove(file_load_callback)

    props.unsubscribe_to_rna_props()

    # Remove the draw handler
    ui.PHYSICS_OT_projectle_draw.remove_handler()
