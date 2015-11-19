# To Get Started

## Set Up the Environment
source setup.py

That does a lot of pip and venv stuff to get your Python environment ready for running Flask.

## Add Models

Add models to models.py

## Add Models to Config

Edit config.py and add your model there. Choose if it is dynamic or static.

## Recreate the Database (if needed)

python recreate.py

This creates the tables. 

Note: this script needs to be fixed to acknowledge the new config structure under the "models" key.

## Run Flask

python api.py

We don't have a username integrated into this yet (from an authentication perspective). That would be

USER=jadudm python api.py

