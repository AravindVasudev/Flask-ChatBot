from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
import os
import shutil

# Path to save the model
SAVE_PATH = './models/trained/'

# Load the training data
training_data = load_data('./data/training.json')
print('training data loaded...')

# Load and train the model
print('training initiated...')
trainer = Trainer(RasaNLUConfig('./config.json'))
trainer.train(training_data)

# Save the model
model_directory = trainer.persist('./models/')
if os.path.exists(SAVE_PATH): # removed old model if exists
    shutil.rmtree(SAVE_PATH)
    print('{} is removed to save the new model.'.format(SAVE_PATH))

os.rename(model_directory, SAVE_PATH) # rename new model to SAVE_PATH

print('done. model saved @ {}'.format(SAVE_PATH))
