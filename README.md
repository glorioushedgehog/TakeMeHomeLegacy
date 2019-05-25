# Take Me Home Legacy
Django app ready to be attached to legacy Take Me Home databases. Supports both search with facial recognition and demographic search used by the legacy software. This app is designed to not interfere with the legacy software, so you may at any time revert to using the old app.
## Support
If you encounter any issues with the software or would like to request a feature, either open an issue on this repo or email takemehomesoftware@outlook.com
## Installation Instructions
### 1. Install Python
Download [Python 3.6](https://www.python.org/downloads/release/python-368/)

When installing python, be sure to add it to your path environment variable. Also, ensure that pip gets installed.
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
if not using Windows. On Windows, do
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
### 4. Connect to Database
In a text editor, open [`TakeMeHomeDjango/settings.py`](/TakeMeHomeDjango/settings.py). Go to the definition of the `DATABASES` dictionary and enter the connection information for the Take He Home database.

Now, start the server by running
```
python manage.py runserver
```
You should see something like
```
Starting development server at http://127.0.0.1:8000/
```
in the output. Open http://127.0.0.1:8000/ (or whatever url Django indicates) in your browser and you should see the new Take Me Home GUI. If you try running a search, you should see a long stack trace. That's because the app requires two tables in the database that are not part of the legacy app.

To add the tables, run the following SQL in your database.
```
BEGIN TRANSACTION
--
-- Create model InferenceTask
--
CREATE TABLE [Inference_Task] (
	[id] int IDENTITY (1, 1) NOT NULL PRIMARY KEY, 
	[state] nvarchar(22) NOT NULL, 
	[Embedding] nvarchar(max) NULL, 
	[Date Created] datetime2 NULL
);
--
-- Create model ImageData
--
CREATE TABLE [Image_Data] (
	[person_id] varchar(22) NOT NULL PRIMARY KEY, 
	[PictureURL] nvarchar(100) NOT NULL, 
	[Embedding] nvarchar(max) NULL
);
ALTER TABLE [Image_Data] ADD CONSTRAINT [Image_Data_person_id_b3701060_fk_TAKEMEHOME_PrimaryKey] FOREIGN KEY ([person_id]) REFERENCES [TAKEMEHOME] ([PrimaryKey]);
COMMIT;
```
If you're familiar with Django, you're probably wondering why we're using SQL instead of Django's migration system. The explanation is [here](https://github.com/glorioushedgehog/TakeMeHomeLegacy/issues/37#issue-448330438).

After adding the `ImageData` and `InferenceTask` tables, you can `runserver` again and try to perform a search with the Take Me Home webapp. This time, it should work!

If you perform a search, you'll notice that no images appear for the people in the database. To fix this, follow the directions to [generate the embeddings](#5-generate-embeddings) for the images.
### 5. Generate Embeddings
This step will accomplish two things: it will make images appear in search results, and it will make those images searchable with facial recognition.

While the server is running, open http://127.0.0.1:8000/manage_facial_recognition in your browser, replacing the base URL with whatever URL Django gives when you run `runserver`. You should see a page describing the state of the images in the database. Click the button at the bottom to start an "FR preparation" thread. This thread will do three things:
1. Save all images in the Person table to disk outside the database. You should see the `tmh/static/images` folder fill up with the images. This is done because Django has a hard policy against storing files in binary fields, which is exactly what the legacy software does with images in the TAKEMEHOME table.
2. Detect faces in all images in the Person table. Using a neural network, the thread will find the location of faces in each picture. If it cannot find a face in some picture, it will say so in stdout.
3. Analyze faces in all images in the Person table. For all images that have detectable faces, the thread will use another neural network to analyze the faces and get "embedding" vectors, which encode the person's identity. These embeddings will then be stored in the `ImageData` table.

After the "FR preparation" process is complete, you can reload http://127.0.0.1:8000/manage_facial_recognition to see the new facial recognition coverage stats. If there are still some people without pictures ready to be viewed in the GUI, it is probably because there are entries in the TAKEMEHOME table don't have pictures. If there are people that have pictures but the pictures are not ready to be searched with facial recognition, it is probably because the neural network could not find a face in the image for the person. The output that the "FR preparation" task printed to the console will tell you if either of these two things happened for each person. It will give you the primary keys for the TAKEMEHOME table so that you can find the entries that may need images added or just new images with clearly visible faces.

Now, you can reload http://127.0.0.1:8000/ and try running a facial recognition search or a demographic search. Both should work.

At this point, you're good to go! The server is ready for use.

Below are instructions on changing some settings and adding new entries to the database.
### 6. Dropdown Options
The legacy app stores some settings data in the `Cfg_Lookup` table. Specifically, the table dictates what values the following fields can take on:
1. Eye Color
2. Hair Color
3. Organization
4. Race
5. Record Type
6. Emergency Contact Relationship
7. Sex
8. Home State

For example, the default race options are:

- ('A', 'ASIAN')
- ('B', 'AFRICAN AMERICAN')
- ('BR', 'BI-RACIAL')
- ('H', 'HISPANIC')
- ('O', 'OTHER')
- ('P', 'PACIFIC ISLANDER')
- ('W', 'WHITE NON-HISPANIC')

Where the first entry in each tuple is what gets stored in the column and the second entry is the human-readable version.

Note: the legacy has a bug related to the 'race' field. It uses 'BR' to represent 'BI-RACIAL', but the 'race' field is only one character, so 'BR' gets trimmed to 'B', which represents 'AFRICAN AMERICAN'. This app fixes the problem by using 'R' to represent 'BI-RACIAL'. This works for new entries made in the Django app, but there might still be entries in your database that have incorrect 'race' fields due to this bug.

If open [`tmh/models.py`](/tmh/models.py), at the top of the `Person` class you will see the definitions of the "dropdown options" for each field. If your department might have changed these options or the data in the `DEFAULT_CHOICES` dictionary, then you should take the following steps:
1. Run the server
2. In your browser, go to http://127.0.0.1:8000/dropdown_options. Making the request to this URL will tell the Django server to read in your `Cfg_Lookup` table and print out the corresponding Python code, just like you saw in [`tmh/models.py`](/tmh/models.py). If you prefer the version that is prints to the console, then you can copy and paste it into [`tmh/models.py`](/tmh/models.py) (before doing this, keep in mind the bug mentioned above).
3. That's it! You don't even need to restart the server. The new dropdown options should show up in the demographic search form after you refresh the page.
### 7. Add People to Database
The easiest way to add people to the database is to open the legacy app, create the new entry, then run the "FR preparation" task as described in [step 5](#5-generate-embeddings). If you are adding more than one person, then you can input all the data through the legacy app, then run the FR preparation task just once at the end.