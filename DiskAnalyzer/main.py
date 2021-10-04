#!/usr/bin/python3
import sys
import os
import pandas as pd


def get_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size
        except Exception as e:
            print(f"Exception : {e}")
            total += 0
    return total


if __name__ == '__main__':
    print("Copy and Paste your directory path")
    path = input()
    dir = sys.argv[1] if len(sys.argv) > 1 else path
    size = []
    paths = []
    for entry in os.scandir(dir):
        if (entry.is_dir(follow_symlinks=False)):
            total = get_size(entry.path) / (1024 * 1024)
            # print(entry.path,total)
            paths.append(entry.path)
            size.append(total)
    size_dict = {'Directory': paths, 'Size(Mb)': size}
    df = pd.DataFrame(size_dict)
    df.to_csv("DiskReport.csv",index_label="S.No")
    os.startfile("DiskReport.csv")