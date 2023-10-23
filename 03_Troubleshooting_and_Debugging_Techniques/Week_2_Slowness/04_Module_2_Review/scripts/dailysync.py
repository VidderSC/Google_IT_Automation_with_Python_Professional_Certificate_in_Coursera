#!/usr/bin/env python3

# import subprocess
# 
# src = "/data/prod/"
# dest = "/data/prod_backup/"
# 
# subprocess.call(["rsync", "-arq", src, dest])

import os
import subprocess
from multiprocessing import Pool

src = "data/prod"
dest = "data/prod_backup"

paths = []

# Use os.walk to get all directories under the source directory
for dirpath, dirnames, _ in os.walk(src):
    paths.append(dirnames)

# Keep just the first group of directories
paths = paths[0]


def rsync_copy(path):
    rsync_command = ["rsync", "-zavh", path, dest]
    subprocess.run(rsync_command)


if __name__ == "__main__":
    num_processes = os.cpu_count()
    dir_paths = []

    # Update the paths to Absolute paths
    cwd = os.getcwd()

    src = os.path.join(cwd, src)
    dest = os.path.join(cwd, dest)

    for path in paths:
        dir_paths.append(os.path.join(src, path))

    # Create the multiprocessing pool and call map.
    pool = Pool(num_processes)
    pool.map(rsync_copy, dir_paths)
    pool.close

