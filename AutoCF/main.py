from logging import error
from bs4 import BeautifulSoup
from pywinauto import Application
import requests
import sys
import os
import json
import shutil

def main():

    # Get url of current window using pywinauto
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*")
    dlg = app.top_window()
    url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
    if url.find('https://') == -1:
        url = 'https://' + url
    if url.find('https://codeforces.com') == -1 and url.find('https://codechef.com') == -1:
        print('Please open a problem page and try again')
        exit()
    else:
        try:
            html_text = requests.get(url).text
        except error as e:
            print(e)
            exit()

    #########################################################
    # generate file name of test case file
    file_name = url[-1:].lower() + '.cpp__tests'

    # if you want to have a fixed filename everytime, comment above line and uncomment the below 4 lines.

    # if len(sys.argv) == 2:
    #     file_name = sys.argv[1] + '__tests'
    # else:
    #     file_name = 'solution.cpp__tests'

    #########################################################
    # create folder, solution file, and open sublime
    new_dir = file_name[:file_name.find('.')]
    
    if new_dir in os.listdir():
        shutil.rmtree(new_dir)
    try:
        os.mkdir(new_dir)
    except error as e:
        print(e)
    os.chdir(new_dir)
    # new_file = open(file_name[:file_name.find('_')], 'w')
    os.system('"C:\Program Files\Sublime Text 3\subl.exe" {}'.format(file_name[:file_name.find('_')]))

    #########################################################
    # parse the testcases

    soup = BeautifulSoup(html_text, 'lxml')
    sample_tests = soup.select('pre')
    tests = []

    for i in range(0, len(sample_tests)):

        if i%2 == 0:# this is an input
            sample_test_input = {"test" : "{}".format(str(sample_tests[i])[5:-6].replace('<br/>', '\n').lstrip("\n"))}
            tests.append(sample_test_input)

        else:# this is output
            lst = ["{}".format(str(sample_tests[i])[5:-6].replace('<br/>', '\n').strip("\n"))]
            tests[-1].update({"correct_answers" : lst})

    writeFile = open(file_name, 'w')
    writeFile.write(json.dumps(tests))
    
if __name__ == '__main__':
    main()