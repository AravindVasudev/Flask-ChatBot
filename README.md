# Flask-ChatBot
A chat bot microservice app that can be trained on different datasets.

## Dependencies
  * python 3.x
    * Rasa NLU
    * MITIE
    * scikit-learn
    * Flask
    * Flask-cors
  * virtualenv
  * gunicorn
  * nginx
  * Rasa NLU Trainer

## Installation
  1. Install python 3.6 or above
  2. Create a virtual environment to install dependencies
    ```
      $ virtualenv venv
    ```
  3. Enter the virtual environment
    ```
      $ source venv/bin/activate
    ```
  4. Install dependencies
    ```
      $ pip install -r requirements.txt
    ```

## Training
  1. Use Rasa NLU Trainer to generate `training.json`.
  2. Place it at `./data/training.json`
  3. run `./chatai.sh train`
  4. Create `./data/answers.json`.
  5. Use intents in the training data as key and value as answers.

## Serving
  * Run `./chatBot start`
