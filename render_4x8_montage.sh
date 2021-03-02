#! /bin/bash
#
# automate rendering and combining renders into 8x4 montage frames
#
# takes parameter for the blender file name and skull iteration

BLEND=$1
ITTERATION=$2

SOURCE="$BLEND$ITTERATION.blend"
echo "Attempting to render $SOURCE"
mkdir -p "/tmp/skulls/"
blender --background "$SOURCE" --python matcap_camera_setup.py

montage "/tmp/skulls/right_eye_down__*.png" -tile 8x1 -geometry +0+0 "/tmp/skulls/line_${ITTERATION}_right_eye_down__montage.png"
montage "/tmp/skulls/front__*.png" -tile 8x1 -geometry +0+0 "/tmp/skulls/line_${ITTERATION}_front__montage.png"
montage "/tmp/skulls/left_eye_up__*.png" -tile 8x1 -geometry +0+0 "/tmp/skulls/line_${ITTERATION}_left_eye_up__montage.png"
montage "/tmp/skulls/rear_up__*.png" -tile 8x1 -geometry +0+0 "/tmp/skulls/line_${ITTERATION}_rear_up__montage.png"

montage "/tmp/skulls/line_${ITTERATION}_right_eye_down__montage.png" "/tmp/skulls/line_${ITTERATION}_front__montage.png" "/tmp/skulls/line_${ITTERATION}_left_eye_up__montage.png" "/tmp/skulls/line_${ITTERATION}_rear_up__montage.png" -tile 1x4 -geometry +0+0 "/tmp/skulls/montage_${ITTERATION}.png"
