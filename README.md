# Batch Job

This application allows you to submit multiple audio or video files to the [AssemblyAI API](https://www.assemblyai.com/) for transcription and enrichment.

## To Run

* Delete any information in the `urls.txt` file.
* Add your audio or video files to the `uploads` folder
* Update `post_json` variable on line 12 of `app.py` to include the parameters you would like to include in your requests
* Run the `upload.py` file (this will upload your local files to AAI and write the file names and URLs to the `urls.txt` file)
* Run the `batch.py` file (this wil submit up to 10 files at a time to AAI for transcription and save the completed JSON responses in the `json` folder and the transcription text in the `text` folder)
