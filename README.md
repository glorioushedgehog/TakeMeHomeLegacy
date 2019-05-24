# Take Me Home Legacy
Django app ready to be attached to legacy Take Me Home databases

Supports searches with facial recognition.

Also supports the demographic search used by the legacy software.
## Support
If you encounter any issues with the software or would like to request a feature, email takemehomesoftware@outlook.com
## Installation Instructions
### 1. Install Python

Download [Python 3.6](https://www.python.org/downloads/release/python-368/)

When installing python, be sure to add it to path environment variable. Also, ensure that pip gets installed.
### 2. Create virtualenv
First, install virtualenv
```
pip install virtualenv
```
In the project root folder, run
```
virtualenv venv
```
To create the virtual environment. This will put python and other dependencies in the venv folder.

Then, activate the virtual environment:
```
source venv/bin/activate
```
If not using Windows. On Windows, do
```
venv\Scripts\activate
```
which should work in the command prompt but won't work in Git Bash.

The virtual environment can be deactivated by running
```
deactivate
```
For the rest of this guide, it will be assumed that the virtual environment is activated.
### 3. Install dependencies
In the project root folder, run
```
pip install -r requirements.txt
```
to install all the app's dependencies. This might take a while.
### 4. Migrate
In a text editor, open [`TakeMeHomeDjango/settings.py`](/TakeMeHomeDjango/settings.py)
Go to the definition of
```
DATABASES
```
and input the connection information for the Take He Home database.

The Django app is setup for the default database tables and settings from the original Take He Home software. If you know that your department has never changed the tables or the choices for fields like home state, organization, hair color etc., then you can skip to [generating the embeddings](#5-generate-embeddings)

Add dropdown options to models.py

note that old software would replace BR with B

### 5. Generate Embeddings

### 6. Serve