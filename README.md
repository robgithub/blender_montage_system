Blender montage system

takes 4 camera positions and 8 matcap selections and creates 32 image files

usage
render_animation.sh folder_of_blend_itterations blender_itterations_prefix

This will call render_4x8_montage.sh which will load each .blend file and execute
matcap_camera_setup.py

requires imagemagick and ffmpeg

alternatively, you can load all the resulting "frame" images as an image sequence into Blender VSE and use a speed control strip

A video detailing how to create these scripts
https://youtu.be/Td1rZIw37JU

These scripts were used in the creation of the Skull presentation video
https://www.youtube.com/embed/5OysJCpzK-I
and discussed on https://www.jumpstation.co.uk/flog/Feb2021.html#p210220212340

You can get the Human Skull mesh for free from https://www.blendswap.com/blend/27441
