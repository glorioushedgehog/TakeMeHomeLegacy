# Take Me Home Legacy
Django app ready to be attached to legacy Take Me Home databases

Supports searches with facial recognition.

Also supports the demographic search used by the legacy software.
## Support
If you encounter any issues with the software or would like to request a feature, email takemehomesoftware@outlook.com
## Installation Instructions
### Install Python

Download Python 3.6

https://www.python.org/downloads/release/python-368/

When installing python, be sure to add it to path. Also, ensure that pip gets installed.
### Create virtualenv
First, install virtualenv

pip install virtualenv

In the project root folder, run

virtualenv venv

To create the virtual environment. This will put python and other dependencies in the venv folder.

Then, activate the virtual environment:

source venv/bin/activate
If not using Windows. On Windows, do 
venv\Scripts\activate

The virtual environment can be deactivated by running

deactivate

For the rest of this guide, it will be assumed that the virtual environment is activated.
### Install dependencies
In the project root folder, run

pip install -r requirements.txt

to install all the app's dependencies. This might take a while.
### Migrate

Add dropdown options to models.py

note that old software would replace BR with B

### Generate Embeddings

### Serve