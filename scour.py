#!/usr/bin env python
# -*- coding: utf-8 -*-
#
#   scour (until you find)
#   python script
#
#   this takes a type of object to search for as string argument
#   ('text' or 'file') and respectively the keyword or filename
#
#   if the path to search in is not specified, it defaults
#   to the current working directory
#
#   TODO: 
#   - simplify this clunky, ugly code and make it more efficient
#
##################################################################

import argparse
import os
import sys

new_file_name = []
current_path = os.getcwd()
full_current_path = os.path.abspath(current_path)
default_dir = current_path
ignore_this = ['.html', '.mp4', '.mp3', '.png', '.jpeg', '.jpg']


def load_file(filepath):
    try:
        with open(filepath, encoding='cp437') as file:
            return file.readlines()
    except Exception as e:
        print("Failed to open {}: {}".format(filepath, e))


def search_file_contents(content, query):
    try:
        # split contents into lines
        lines = content.splitlines()
        # find all lines that contain the query
        return [line for line in lines if query in line.lower()]
    except Exception as e:
        print("Failed to readlines: {}".format(e))



def Scour(path, keyword, flag):
    print("MODE: {}".format(flag))
    print("searching for '{}' in {}..\n".format(keyword, path))
    lower_keyword = keyword.lower()
    
    os.chdir(path)
    xfiles = os.listdir()

    for folder, dirs, files in os.walk(path):
        #print("+--- Now in folder: " + folder)
        for file in files:
            fullpath = os.path.join(folder, file)
            if flag.lower() == "file":
                if file.lower() in keyword.lower():

                    print("found: {}".format(fullpath))
            
            #extension = file.split('.')[1]
            extension = os.path.splitext(file)[1]
            if extension.lower() not in ignore_this:
                
                abs_path = os.path.abspath(file)
                if flag.lower() == "text":
                    try:
                        data = load_file(fullpath)
                        for i in range(len(data)):
                            if lower_keyword in data[i]:
                                print(f'line {i+1} in {fullpath}')
                            else:
                                pass

                    except UnicodeDecodeError as e:
                        print(fullpath)
                        print(e)


if __name__ == '__main__':   

    parser = argparse.ArgumentParser(description='search for keyword or keyfile')
    parser.add_argument('type', help="a type, either 'text' or 'file'")
    parser.add_argument('-k', '--keyword', type=str, help="keyword necessary to search for")
    parser.add_argument('-p', '--path', type=str, help="path will default to current directory if none given")
    parser.add_argument('-f', '--file', type=str, help="file necessary to search for")

    args = parser.parse_args()

    options = ['file', 'text']
    if args.type not in options:
        print("type must be either 'text' or 'file'")
        exit()

    if not args.path:
        path = default_dir
    else:
        path = args.path


    if args.type == "text":
        if not args.keyword:
            print("please specify -k/--keyword to search for")
            exit()

        keyword = args.keyword
        Scour(path, keyword, flag="text")

    elif args.type == 'file':
        if not args.file:
            print("please specify -f/--file to search for")
            exit()

        keyword = args.file
        Scour(path, keyword, flag="file")
