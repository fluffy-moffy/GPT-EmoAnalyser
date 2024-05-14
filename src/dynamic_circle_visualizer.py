import math
import pygame
import pygame.gfxdraw

class DynamicCircle:
    def __init__(self, screen, center_x, center_y, radius):
        # Initialize values
        self._screen = screen
        self._center_x = center_x
        self._center_y = center_y
        self._radius = radius

    # Helpers
    @staticmethod # Fpr handling arguments
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    def draw(self, data, start_time):
        # Control effect with time based sigmoid function
        current_time = pygame.time.get_ticks()
        time_elapsed = (current_time - start_time) / 1000.0
        t = max(0, min(1, time_elapsed))  # time between 0 and 1
        # I add some value for more smooth effect
        smooth_step = self.sigmoid(10 * (t - 0.5))
        total = data['positive'] + data['negative']

        # Rotation speed between 0.25(1/4) per/sec to 0.05(1/20) per/sec
        rotate_speed = (0.25 * data['positive'] / total + 0.05 * data['negative'] / total) * smooth_step
        angle_offset = current_time / 1000 * 360 * rotate_speed

        # calculate position in every radian
        for angle in range(360):
            rad = math.radians(angle + angle_offset)
            wave_effect = 10 * math.sin(math.radians(angle * 6)) # Number of vertices = 6
            r = self._radius + wave_effect
            x = self._center_x + r * math.cos(rad)
            y = self._center_y + r * math.sin(rad)

            color_ratio = angle / 360
            red = 255 * (1 - color_ratio) + 255 * color_ratio * (data['positive'] / total) * smooth_step
            blue = 255 * color_ratio + 255 * (1 - color_ratio) * (data['negative'] / total) * smooth_step
            color = (int(red), 30, int(blue))

            # antialiasing
            pygame.gfxdraw.filled_circle(self._screen, int(x), int(y), 2, color)
            pygame.gfxdraw.aacircle(self._screen, int(x), int(y), 2, color)

    # Getter and Setter methods
    def get_center_x(self):
        return self._center_x

    def set_center_x(self, value):
        self._center_x = value

    def get_center_y(self):
        return self._center_y

    def set_center_y(self, value):
        self._center_y = value

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value
