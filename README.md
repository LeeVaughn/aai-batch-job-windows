# Batch Job

This application allows you to submit multiple audio or video files to the [AssemblyAI API](https://www.assemblyai.com/) for transcription and enrichment.

Note: The code in this application is specific to Windows. If you are working on a Mac please see this [repository](https://github.com/LeeVaughn/aa-batch-job-mac).

## Setting Up the Application
* Create a `config.py` file in the root directory of the project
  * Create an `auth_key` variable in the `config.py` file and set the value to a string containing your AssemblyAI API key.
* Create an `endpoint` variable in the `config.py` file and set the value to this string: `'https://api.assemblyai.com/v2'`

## Running the Application
* Add your audio or video files to the `uploads` folder
* Update the `post_json` variable on line 12 of `app.py` to comment in any parameters you would like to include in your requests
* Run the `batch.py` file, which will do the following:
  * Clear any previous info from the `urls.txt` file
  * Upload your local files and save the file names and upload URLs to the `urls.txt` file
  * Empty the `json` and `text` directories
  * Iterate over the `urls.txt` file to submit 15 files at a time to the AAI API
  * Save the full JSON response and transcript text for each file when completed to the `json` and `text` directories respectively

**Note:** Each time you run the `batch.py` file it will remove any files from the `json` and `text` directories. If you would rather not do that you can comment out lines 29 and 30 in the `batch.py` file.
