import math

res_x, res_y = 640, 480
half_x, half_y = res_x/2, res_y/2
fov_x, fov_y = 75, 60
def pixelToAngle(pixel_x, pixel_y):
    try:
        if pixel_x > 0 and pixel_x <= res_x and pixel_y > 0 and pixel_y <= res_y:
                calc_x = math.degrees(math.atan( ( (pixel_x-half_x) * math.tan(math.radians(fov_x/2)) ) / half_x)) + fov_x/2
                calc_y = math.degrees(math.atan( ( (pixel_y-half_y) * math.tan(math.radians(fov_y/2)) ) / half_y)) + fov_y/2
                return fov_x - round(calc_x), round(calc_y)
        else:
            print("ERROR: Values are not within the bounds of the screen's resolution!")
            return
    except TypeError:
            print("ERROR: Input values are not numbers!")
            return