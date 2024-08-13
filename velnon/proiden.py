from transformers import Scheduler

scheduler = Scheduler(model=model, args=training_args)
scheduler.set_timesteps(custom_timesteps)
