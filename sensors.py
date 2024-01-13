import pygame
import math
import numpy as np


def uncertainty_add(distance, angle, sigma):
    mean = np.array([distance, angle])
    covariance = np.diag(sigma ** 2)
    distance, angle = np.random.multivariate_normal(mean, covariance)
    distance = max(distance, 0)
    angle = max(angle, 0)
    return [distance, angle]


class LaserSensor:

    def __init__(self, Range, map, uncertainty):
        self.Range = Range
        self.speed = 4
        self.sigma = np.array([uncertainty[0], uncertainty[1]])
        self.position = (0, 0)
        self.map = map
        self.W, self.H = pygame.display.get_surface().get_size()
        self.sensedObstacles = []

    def distance(self, obstaclePosition):
        px = (obstaclePosition[0] - self.position[0]) ** 2
        py = (obstaclePosition[1] - self.position[1]) ** 2
        return math.sqrt(px + py)
    
    def sense_obstacles(self):
        data = []
        x1, y1 = self.position
        for angle in np.linspace(0, 2 * math.pi):
            x2 = x1 + self.Range * math.cos(angle)
            y2 = y1 - self.Range * math.sin(angle)
            for i in range(0, 20):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.W and 0 < y < self.H:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (255, 0, 0):
                        distance = self.distance((x, y))
                        output = uncertainty_add(distance, angle, self.sigma)
                        #output = [distance, angle]
                        output.append((255,0,0))
                        output.append(self.position)
                        # Store the measurements
                        data.append(output)

            for i in range(20, 40):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.W and 0 < y < self.H:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (255, 155, 0):
                        distance = self.distance((x, y))
                        output = uncertainty_add(distance, angle, self.sigma)
                        #output = [distance, angle]
                        output.append((255,155,0))
                        output.append(self.position)
                        # Store the measurements
                        data.append(output)

            for i in range(40, 60):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.W and 0 < y < self.H:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (200, 200, 25):
                        distance = self.distance((x, y))
                        output = uncertainty_add(distance, angle, self.sigma)
                        #output = [distance, angle]
                        output.append((200,200,25))
                        output.append(self.position)
                        # Store the measurements
                        data.append(output)

            for i in range(60, 80):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.W and 0 < y < self.H:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (0, 255, 0):
                        distance = self.distance((x, y))
                        output = uncertainty_add(distance, angle, self.sigma)
                        #output = [distance, angle]
                        output.append((0,255,0))
                        output.append(self.position)
                        # Store the measurements
                        data.append(output)
            for i in range(80, 100):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.W and 0 < y < self.H:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (0, 0, 255):
                        distance = self.distance((x, y))
                        output = uncertainty_add(distance, angle, self.sigma)
                        #output = [distance, angle]
                        output.append((0,0,255))
                        output.append(self.position)
                        # Store the measurements
                        data.append(output)
                        break
        return data
        # if len(data)>0:
        #     return data
        # else:
        #     return False