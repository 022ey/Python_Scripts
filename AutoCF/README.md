# AutoCF
An automatic test case parser that grabs test cases from Codeforces, feeds it to CppFastOlympicCoding and opens Sublime Text for you.
[Video Tutorial](https://youtu.be/W5nxjhGT5Pc)

# How to Setup:
- Install the required dependencies
- Clone the github repo
- Place the main.py file in your desired folder
- Open the Codeforces problem page on Google Chrome (Support for other sites and browsers will be added later)
- Open Command Prompt in the folder containing main.py (Ctrl-L -> cmd -> Enter)
- execute the python file.
- Now it will create a new folder containing your test case file and your cpp file and open Sublime Text for you.

# Dependencies
- install Python3
- pip install bs4
- pip install lxml
- pip install pywinauto
- pip install requests

# Other Requirements
- This script assumes that Sublime Text 3 command line interface is intalled at C:\Program Files\Sublime Text 3\subl.exe If Sublime Text 3 is installed at other location, modify the script at line 52.
