import math

res_x, res_y = 640, 480
half_x, half_y = res_x/2, res_y/2
fov_x, fov_y = 75, 60
def pixelToAngle(pixel_x, pixel_y):
    calc_x = round(math.degrees(math.atan( ( (pixel_x-half_x) * math.tan(math.radians(fov_x/2)) ) / half_x)))
    calc_y = round(math.degrees(math.atan( ( (pixel_y-half_y) * math.tan(math.radians(fov_y/2)) ) / half_y)))
    return calc_x, calc_y