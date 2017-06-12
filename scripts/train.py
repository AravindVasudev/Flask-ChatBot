from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

# Load the training data
training_data = load_data('./data/training.json')
print('training data loaded...')

# Load and train the model
print('training initiated...')
trainer = Trainer(RasaNLUConfig('./config.json'))
trainer.train(training_data)

# Save the model
model_directory = trainer.persist('./models/')
print('done. model saved @ {}'.format(model_directory))
