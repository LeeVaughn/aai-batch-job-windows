#!/usr/bin/env python
from config import auth_key, endpoint
import os
import requests
from concurrent.futures import ThreadPoolExecutor


file_dir = './uploads'
uploaded_files = os.listdir(file_dir)


def upload_file(filename):
    print(f"{filename} uploading...")

    def read_file(filename, chunk_size=5242880):
        with open('./uploads/' + filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
    

    headers = {'authorization': auth_key}
    response = requests.post(endpoint + '/upload', headers=headers, data=read_file(filename))

    response = response.json()

    print(f"{filename} complete: {response['upload_url']}")

    # write file names and URLs to a text file
    f = open('urls.txt', 'a')
    f.write(filename + ',' + response['upload_url'] + '\n')
    f.close()


# clears any previous info from the urls.txt file
clear_file = open('urls.txt', 'w')
clear_file.close()


with ThreadPoolExecutor(15) as executor:
    for x in range(0, len(uploaded_files)):
        executor.submit(upload_file, uploaded_files[x])
