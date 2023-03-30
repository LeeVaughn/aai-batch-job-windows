import json
import os
from concurrent.futures import ThreadPoolExecutor
from app import main

lines = []


def run_file(audio_url, file_name):
    data = main(audio_url)
    text_filename = file_name + '.txt'
    json_filename = file_name + '.json'
    
    text_file = open('./text/' + text_filename, 'x', encoding='utf8')
    json_file = open('./json/' + json_filename, 'x', encoding='utf8')

    text_file.write(data['text'])
    text_file.close()
    json_file.write(json.dumps(data, ensure_ascii=False, indent=2))
    json_file.close()


# uploads files to get back an upload URL
print('Uploading files...')
os.system('./upload.py')

# deletes any files in the json or text directories
print('Emptying folders...')
os.system('./empty_folders.py')

f = open('urls.txt', 'r')

# loop over each line in text file and append them to dictionary
for x in f:
    lines.append(x)

with ThreadPoolExecutor(10) as executor:
    for line in lines:
        # splits file names and urls
        split_line = line.split(',')
        split_url = split_line[1].split('\n')
        executor.submit(run_file, split_url[0], split_line[0])
