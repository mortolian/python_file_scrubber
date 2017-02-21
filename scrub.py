#!/usr/bin/python
# This is a simple script that will run through a directory
# and scrub files from your filesystem.
#
# Maintainer    : Mortolio <hello@mortolio.com>
# Version       : 1.0
#
# TODO:
# - Have to enable the ignore .git directories for both files and directories ::: http://stackoverflow.com/questions/120656/directory-listing-in-python
#

import os
import shutil
import fnmatch
import sys
from stat import *

#
# Define script colours
#
class bcolors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

#
# This will perform the delete based on folder or file delete
#
def delete_src(resource,scrubtype,dryrun):
    if dryrun == False:
        if scrubtype == 'd':
            shutil.rmtree(resource)
        else:
            os.remove(resource)

    print bcolors.FAIL + "   - DELETE " + get_scrub_type() + " :: " + resource + bcolors.ENDC
    return

#
# This will scrub folders if so chosen
#
def scrub_folders(path,match,scrubtype,dryrun):
    for root, subFolders, files in os.walk(path):
        for folder in subFolders:
            if fnmatch.fnmatch(folder, match):
                resource = os.path.join(root, folder)
                delete_src(resource,scrubtype,dryrun)
    return

#
# This will scrub files if so chosen
#
def scrub_files(path,match,scrubtype,dryrun):
    for root, subFolders, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, match):
                resource = os.path.join(root, file)
                delete_src(resource,scrubtype,dryrun)
    return

#
# This will return the SCRUB type text for various print to CLI features
#
def get_scrub_type():
    if scrubtype == 'd':
        return "DIRECTORY"
    else:
        return "FILE(S)"

#
# This will print the header for the CLI
#
def print_header():
    print bcolors.WARNING
    print " SCRUBBING " + get_scrub_type() + " " + bcolors.BOLD + match + bcolors.ENDC + bcolors.WARNING +" IN " + path
    print bcolors.ENDC
    return

#
# This will print the footer for the CLI
#
def print_footer():
    print bcolors.OKGREEN
    print " COMPLETED THE WORK - Removed all matches for " + match
    print bcolors.ENDC
    return

def print_help():
    print bcolors.OKGREEN
    print '''
        PYTHON SCRUBBING TOOL
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        USAGE: scrub.py [path] [match string] [arguments[]]
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        ARGUMENTS:
            --dry-run       This will cause no action to be taken and only output to the
                            the screen.
            --no-git        This will ignore all files and folders in .git folders
            --directory     This will scrub entire directories and not files
            --help          Displays this help text
    '''
    print bcolors.ENDC
    exit(0)


# Get a list of the files you want removed
path            = '' #this is the path which will be checked '.' is default
match           = '' #this is the string to match, can be wildcarded
dryrun          = False #this will only print to terminal what it will do
scrubtype       = 'f' #this is the type of remove to do [f = file, d = dir]
ignore_git      = False #this will ignore git folders if set to true

# If no arguments, print the help bit
try:
    # Set the path
    if os.path.isdir(sys.argv[1]) == False:
        print "OOOPS! Invalid path given"
        exit(0)
    else:
        path = sys.argv[1]

    # Set the match
    match = sys.argv[2]

    # Process the various arguments from the CLI
    for argument in sys.argv:
        if argument == '--no-git':
            ignore_git = True
        if argument == '--directory':
            scrubtype = 'd'
        if argument == '--dry-run':
            dryrun = True
        if argument == '--help':
            print_help()
except:
    print_help()

# Print the header
print_header()

# Try and complete the scrubbing
try:
    if scrubtype == 'd':
        scrub_folders(path,match,scrubtype,dryrun)
    else:
        scrub_files(path,match,scrubtype,dryrun)
except Exception, e:
    print "     ERROR: Could not complete the entire process. :: " + str(e)
    print ""
    exit(0)

# Print the footer
print_footer()
