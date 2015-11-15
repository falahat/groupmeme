
## Introduction

This is a simple wrapper for the Groupme API along with some IPython examples. 
As of now, you can just fetch a list of your groups and access the message / like history for that group into a pandas Dataframe

## Setup

### PythonPath
You need to have this directory in your `PYTHONPATH`. Learn more about this [here](http://stackoverflow.com/questions/11960602/how-to-add-something-to-pythonpath).

If this project is at `/home/you/code/groupmeme`, add `/home/you/code/` to your `PYTHONPATH`. You can do this by opening `~/.bash_profile` and adding this line:
`export PYTHONPATH=$PYTHONPATH:/home/you/code/`.

### Dependencies
I suggest using [conda](https://www.continuum.io/downloads) and [pip](http://pip.readthedocs.org/en/stable/installing/) to install these. Conda will also automatically download most of them for you.

* ipython
* pandas
* numpy
* matplotlib
* requests

### Authentication Token
To use this, you need a Groupme authentication token. You can get one [here](https://dev.groupme.com/)

Save your authentication token in the groupmeme root directory (same folder as `api.py` and `group.py`). Just paste the token and save your file as `auth.key`.
Be careful not to add this key to your git history or to paste it in any other files!

## Running IPython Examples
While in the app's root directory, run `ipython notebook examples/`. This will open up an IPython notebook in your web browser. If one doesn't automatically open, just navigate to `localhost:8888`.
