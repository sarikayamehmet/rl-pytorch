"""
Written by Matteo Dunnhofer - 2018

Configuration class
"""
import math
import torch
from torch.autograd import Variable


class Configuration(object):
    """
    Class defining all the hyper parameters of:
        - net architecture
        - training
        - test
        - dataset path
        ...
    """
    PROJECT_NAME = 'REINFORCE'

    ENV = 'CartPole-v0'
    DATA_PATH = ''
    EXPERIMENTS_PATH = '../experiments'

    # training hyperparameters
    OBSERVATION_SIZE = [80, 80]

    SEED = 123
    LEARNING_RATE = 1e-2
    DECAY_LR = False
    DECAY_LR_STEPS = [500]
    OPTIM = 'adam'
    MOMENTUM = 0.95
    MAX_EPISODES = 200
    GAMMA = 0.99
    STD_REWARDS = True
    CLIP_REWARDS = False
    

    ENTROPY_BETA = 1e-2
    
    ROLLOUT_STEPS = 10
    NUM_ACTIONS = 2
    
    USE_GPU = True
    GPU_IDS = [0] #[0, 1, 2]


    DISPLAY_STEP = 100
    SAVE_STEP = 100

    def __init__(self):
        super(Configuration, self).__init__()

    def __str__(self):
        cfg2str = "Configuration parameters\n"
        cfg2str += "PROJECT_NAME = " + str(self.PROJECT_NAME) + '\n'
        cfg2str += "SEED = " + str(self.SEED) + '\n'
        cfg2str += "LEARNING_RATE = " + str(self.LEARNING_RATE) + '\n'
        cfg2str += "DECAY_LR = " + str(self.DECAY_LR) + '\n'
        cfg2str += "DECAY_LR_STEPS = " + str(self.DECAY_LR_STEPS) + '\n'
        cfg2str += "OPTIM = " + str(self.OPTIM) + '\n'
        cfg2str += "MOMENTUM = " + str(self.MOMENTUM) + '\n'
        cfg2str += "MAX_EPISODES = " + str(self.MAX_EPISODES) + '\n'
        cfg2str += "NUM_ACTIONS = " + str(self.NUM_ACTIONS) + '\n'
        cfg2str += "GAMMA = " + str(self.GAMMA) + '\n'
        cfg2str += "ROLLOUT_STEPS = " + str(self.ROLLOUT_STEPS) + '\n'
        cfg2str += "ENTROPY_BETA = " + str(self.ENTROPY_BETA) + '\n'
        cfg2str += "STD_REWARDS = " + str(self.STD_REWARDS) + '\n'
        cfg2str += "CLIP_REWARDS = " + str(self.CLIP_REWARDS) + '\n'
        cfg2str += "DISPLAY_STEP = " + str(self.DISPLAY_STEP) + '\n'
        cfg2str += "SAVE_STEP = " + str(self.SAVE_STEP) + '\n'
        cfg2str += "DATA_PATH = " + str(self.DATA_PATH) + '\n'
        cfg2str += "EXPERIMENTS_PATH = " + str(self.EXPERIMENTS_PATH) + '\n'
        cfg2str += "USE_GPU = " + str(self.USE_GPU) + '\n'
        cfg2str += "GPU_IDS = " + str(self.GPU_IDS) + '\n'

        return cfg2str
