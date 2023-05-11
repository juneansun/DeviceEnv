from collections import deque
import gym
import numpy as np
import random
#from sklearn.metrics import r2_score

from abc import *

class Processor():
    def __init__(self):
        self.running_tasks = 0;
        self.utilization_rate = 0;
        self.makespan_time = 0;

    def run(self, task, profile):
        model_id = task.id
        start_time = task.start_time

        end_time = start_time + self.profile[model_id][running_tasks]

        return end_time

class CPU(Processor):

    def __init__(self):
        super().__init__()
        self.profile = ( # Tuple is faster?
                ''' MoblieNet '''
                ( 85168,	86290,  	99093,    0xffffff,	0xffffff,	99999,  99999 ),
                ''' InceptionNet '''
                ( 564661,  	587842,  	661378,   680000,  	720000, 	760000 ),
                ''' YamNet '''
                ( 17089,    17839,    	18132,    18723,   	19230,      20003,	0xffffff ),
                ''' MoveNET - DSP is totally unavailable '''
                ( 139362,   140168,   	145170,   0xffffff, 720000,     760000, 0xffffff,	0xffffff ), // CPU
                ''' BERT '''
                ( 2332900,  2361000,  	2420000,  0xffffff, 720000,     760000, 0xffffff,   0xffffff ), // CPU
                )

        def run(self, task):
            return super.run(task, self.profile);

### TODO implement GPU, DSP, NPU like CPU

# for compaciton trace version
class SmartPhone(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, config):
        super().init()
        self.running_tasks = 0
        self.

    def __callable__(self):
        return self

    def step(self, action):
        reward = running_tasks
        done = True
        info = {}
        return np.array(self.state, dtype=np.float32), reward, done, info
    pass

def reset(self):
    pass

def render(self, mode='human'):
    pass

def close(self):
    pass

