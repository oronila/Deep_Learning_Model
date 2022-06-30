import gym
from gym import spaces
import pygame
import math
import numpy as np
import random

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""

    def __init__(self):
        super(CustomEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        
        self.action_space = spaces.Discrete(4)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=-1000, high=1000,
                                            shape=(6,), dtype=np.int64)
                                            

    def step(self, action):
        vel = 5
        
        moves = 200

        
        if(action == 0): # W
            self.y += vel
        if(action == 1): # S
            self.y -= vel
        if(action == 2): # A
            self.x -= vel
        if(action == 3): # D
            self.x += vel
        
        self.movenum+=1
        
        number = math.sqrt(math.pow(self.startgoalx-self.startx,2)+math.pow(self.startgoaly-self.starty,2))/100.0
        #reward code
        self.reward = (math.sqrt(math.pow(self.startgoalx-self.startx,2)+math.pow(self.startgoaly-self.starty,2))-math.sqrt(math.pow(self.startgoalx-self.x,2)+math.pow(self.startgoaly-self.y,2)))/number

        if(self.movenum>=moves or self.x >= 500 or self.y >= 500 or self.y <= 0 or self.x <= 0):
            self.done = True
            self.reward = -1000
        
        if(self.x<=self.startgoalx+7 and self.x>=self.startgoalx-7 and self.y>=self.startgoaly-7 and self.y<=self.startgoaly+7):
            self.done = True
            self.reward = 5000 #- (self.movenum*1000)
        #print(self.reward)
        info = {}
        

        #observation code
        botx = self.x
        boty = self.y
        gx = self.goalx
        gy = self.goaly
        delta_goalx = self.goalx - botx
        delta_goaly = self.goaly - botx

        

        self.observation = [botx, boty, gx, gy, delta_goalx, delta_goaly]
        self.observation = np.array(self.observation)

        return self.observation, self.reward, self.done, info
    def reset(self):
        pygame.init()
        self.window = pygame.display.set_mode((500,500))
        pygame.display.set_caption("A literal moving block")
        self.done = False
        self.score = 0
        self.startx = random.randint(10, 490)
        self.starty = random.randint(10, 490)
        self.startgoalx = random.randint(10, 490)
        self.startgoaly = random.randint(10, 490)
        while(abs(self.startx-self.startgoalx)>=20 and abs(self.starty-self.startgoaly)>=20):
            self.startgoalx = random.randint(10, 490)
            self.startgoaly = random.randint(10, 490)
        self.x = self.startx
        self.y = self.starty # random()*self.y
        self.goalx = self.startgoalx
        self.goaly = self.startgoaly
        self.width = 10
        self.height = 10
        self.movenum = 0
        # botx, boty, gx, gy, delta_goalx, delta_goaly
        botx = self.x
        boty = self.y
        gx = self.goalx
        gy = self.goaly
        delta_goalx = self.goalx - botx
        delta_goaly = self.goaly - botx

        self.observation = list([botx, boty, gx, gy, delta_goalx, delta_goaly])
        self.observation = np.array(self.observation)

        return self.observation  # reward, done, info can't be included

    def render(self):#, mode='human'):
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        self.window.fill((0,0,0))

        pygame.draw.circle(self.window, (0,255,0), (self.startgoalx,self.startgoaly), 10, 20)
        
        pygame.draw.rect(self.window, (255,0,0), (self.x, self.y, self.width, self.height))

        pygame.display.update() 

    def close(self):
        pygame.quit()

