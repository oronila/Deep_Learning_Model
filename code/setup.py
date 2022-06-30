import gym
from stable_baselines3 import PPO
import os
from custom_env import CustomEnv


models_dir = "models/PPO"
logdir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = CustomEnv()
env.reset()

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)
model_path = f"{models_dir}/600000.zip"
model = PPO.load(model_path, env=env)


TIMESTEPS = 25000
iters = 0
while True:
    iters += 1
    
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
    model.save(f"{models_dir}/{TIMESTEPS*iters}")