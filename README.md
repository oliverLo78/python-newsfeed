# python-newsfeed
## Description

Use Python as the basis for a web server. Instead of building it from scratch, we'll refactor the back end of an app that was originally built using Node.js. The app, called Just Tech News, lets users submit links to tech-related articles, comment on other users' articles, and upvote articles for points.

![License Badge](https://img.shields.io/badge/license-MIT-success?style=plastic)

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Contibution](#contribution)
* [Tests](#tests)
* [Questions](#questions)
* [License](#license)

## Installation

Install Python on Windows, if you have an older version installed you need to update Python version 3.8 or greater, so you'll need to uninstall the old one first. In the bottom-left corner of the screen, use the search box to search for "programs" and select "Add or remove programs" from the list. The following image demonstrates what you should see:

![image](https://user-images.githubusercontent.com/109435666/235459474-08145b2f-1840-4713-b6df-1f0be305b853.png)

Next, navigate to the 
![Python download page](https://www.python.org/downloads/) in your browser and select the download button for the latest version, as the following image show

![Screenshot 2023-05-01 Python download](https://user-images.githubusercontent.com/109435666/235461997-6ebc2427-b4d3-4b71-82e9-42f7035af87f.png)

Run the installer after the download finishes. You should see the following image:

![image](https://user-images.githubusercontent.com/109435666/235464310-b8e853ff-c966-40b9-99ef-ddf59bd18af6.png)

Make sure to check "Add Python 3.x to PATH" before selecting "Install Now". Then let the installer run through its steps and close it out.

## Usage

Python, however, doesn't always work with Git Bash. For better results, use the Windows PowerShell command line instead.

To open PowerShell, use the search box in the bottom-left corner of the screen to search for "powershell". The following image demonstrates what you should see:

![image](https://user-images.githubusercontent.com/109435666/235464519-8fa7b951-2977-43dc-a4db-f2bb3146233f.png)

Select "Windows PowerShell" and a new command line window will open. Run the following command in this new window:

```
python --version
```

In VS Code, press Ctrl+Shift+P to open the command prompt. Search for "terminal" in the prompt. The following image demonstrates what you should see:

![Screenshot 2023-05-01 VS terminal](https://user-images.githubusercontent.com/109435666/235465234-52cb4a81-5650-4d37-bacd-ba2fffb2ea04.png)

In the dropdown that appears, select "Terminal: Select Default Shell". This will give you a list of available terminals to choose from, including Windows PowerShell and Git Bash. The following image demonstrates what you should see:

![Screenshot 2023-05-01 Command Prompt](https://user-images.githubusercontent.com/109435666/235465512-d41e83ee-5975-4489-8cf3-e9c5ffe328af.png)

Select "Windows PowerShell". VS Code will now use PowerShell instead of Git Bash whenever you open the integrated terminal.

## Clone the Repo and Create Branches

On your computer, clone the repository using ``` git clone ```

Then use the ``` git checkout -b ``` command to create and switch to the ``` develop ``` branch

so that you're not working directly in the ``` main ``` branch.  Once in the ``` develop ``` branch

run ``` git checkout -b ``` again to create and switch to another branch called ``` feature/app-setup ```

## Create a .gitignore File

For this project, we'll generate many files that we won't need to commit, so the first thing to do on the new feature branch is create a ``` .gitignore ``` file.

Open the ```.gitignore ``` file and add the following lines:

```
venv/
.env

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```
We just added files and directories to the .gitignore file that the official Flask documentation recommends ignoring.

## Set Up the Python Environment

You should already have the latest version of Python installed on your computer. To verify that, run the following command from the command line:

```
python --version
```
That command should print something like ``` Python 3.10.7 ``` to the console

## Install Python Libraries

You'll use several add-on libraries alongside Python. These libraries are comparable to Express.js and Sequelize. But you won't install them globally on your machine, because dependency versions can change from project to project.

## Create a Virtual Environment

Python provides a feature called a virtual environment—a self-contained directory that maintains its own version of Python and its own library dependencies. This way, multiple Python projects can reside on the same machine without interfering with each other.

In the root directory of your ``` python-newsfeed project ```, run the following command:

``` python -m venv venv ```

The ```python -m venv ``` command (or ``` python3 -m venv ```, if your computer requires it) uses Python's built-in ``` venv ``` module to create a new directory. 

In this case, the new directory is also called venv. The venv directory holds all the files that make a virtual environment possible.

In VS Code, you can expand the ``` venv ``` directory to see what it contains, as shown in the following image

![image](https://user-images.githubusercontent.com/109435666/235469899-20455c92-732a-46c8-a4fc-7e1d74ff6a82.png)


