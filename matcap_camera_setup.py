# Blender montage script
# applies scene settings and then each defined camera setting and each matcap selection
# renders each configuration creating 32 image files
import bpy

def set_scene():
    bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
    bpy.context.scene.world.color = (0, 0, 0)
    bpy.context.scene.render.resolution_x = 1080
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.resolution_percentage = 25

def set_camera(setup):
    bpy.data.objects['Camera'].location[0] = setup['location'][0]
    bpy.data.objects['Camera'].location[1] = setup['location'][1]
    bpy.data.objects['Camera'].location[2] = setup['location'][2]
    bpy.data.objects['Camera'].rotation_euler[0] = setup['rotation'][0]
    bpy.data.objects['Camera'].rotation_euler[1] = setup['rotation'][1]
    bpy.data.objects['Camera'].rotation_euler[2] = setup['rotation'][2]
    bpy.data.objects['Camera'].data.sensor_width = setup['sensor']   # default 36

def set_matcap(exr_name):
    bpy.context.scene.display.shading.light = 'MATCAP'
    bpy.context.scene.display.shading.studio_light = "{}.exr".format(exr_name)

def do_render(destination_path, filename):
    bpy.context.scene.render.filepath = "{0}{1}".format(destination_path, filename)
    bpy.ops.render.render(write_still = True)

def main():
    cam_setups = [ 
                {'camera_name':'right_eye_down', 'location': [-7.24919, -6.81488, 3.98134], 'rotation': [1.10932, 0, -0.827971], 'sensor': 19 } ,
                {'camera_name':'front', 'location': [0, -11.08, -0.854227], 'rotation': [1.5708, 0, 0], 'sensor': 22 },
                {'camera_name':'left_eye_up', 'location': [6.40053, -8.27252, -3.57425], 'rotation': [1.83712, 0.00174524, 0.695701], 'sensor': 22 },
                {'camera_name':'rear_up', 'location': [-6.86748, 5.43022, -6.71921], 'rotation': [2.15199, 0.00174571, -2.26718], 'sensor': 20 }
                 ]
    mat_caps = ['basic_2', 'jade', 'metal_carpaint', 'ceramic_lightbulb', 'check_normal+y', 'check_rim_dark', 'resin', 'toon']
    destination_path = '/tmp/skulls/'
    set_scene()
    for cam in cam_setups:
        set_camera(cam)
        for mat in mat_caps:
            set_matcap(mat)
            do_render(destination_path, "{0}__{1}".format(cam['camera_name'], mat))

if __name__ == '__main__':
    main()

