# File List utility for VSCode

This is a powershell command-line utility that gets all files in the file tree starting from the current working directory, and constructs a command to easily open it in VScode.

## Requirements

VScode, Powershell, Python 3.12

## Setup

The scripts folder has the actual code. The test folder is a playground to test it out.

1. Save the .py file in a permanent location
2. Add the powershell function in your profile
3. Modify the powershell function in your profile:
   1. Save the absolute path to the python file in the mentioned variable

## Usage

The output is organized by filetype.

If you call file-list from the command line, it lists all files that it finds in all subfolders recursively.

The powershell command accepts two argument types: ```-include``` (```-i```) and ```-exclude``` (```-e```).

You can provide a list of patterns (string-type) that will be matched like a regex to the absolute file paths, allowing you to include or exclude files from the search.

You can use both at the same time, providing multiple comma-separated patterns to each to include or exclude those patterns from the search.

## Example commands

Open a powershell terminal in the ```test\``` folder and run these commands:

```
file-list -i blah
file-list -e .md
file-list -i md,py
file-list -i txt -e hello
```
