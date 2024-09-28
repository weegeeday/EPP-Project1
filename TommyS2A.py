import math

res_x, res_y = 640, 480
half_x, half_y = res_x/2, res_y/2
fov_x, fov_y = 75, 60
def pixelToAngle(pixel, half, fov):
    return round(math.degrees(math.atan( ( (pixel-half) * math.tan(math.radians(fov/2)) ) / half)))