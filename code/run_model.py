import gym
from stable_baselines3 import PPO
from custom_env import CustomEnv

models_dir = "models/PPO"

env = CustomEnv() # continuous: LunarLanderContinuous-v2
env.reset()

model_path = f"{models_dir}/600000.zip"
model = PPO.load(model_path, env=env)

episodes = 10

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
        print(rewards)