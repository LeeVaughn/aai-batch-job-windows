#!/usr/bin/env python
import os


def delete_files(folder):
    dir = folder

    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


delete_files('./json')
delete_files('./text')
