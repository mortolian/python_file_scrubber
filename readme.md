# File Scrubber

This is a simple tool that will scrub a path from the files matching the criteria
you have specified. This is helpful to remove system files like .DS_Store and Thumbs.db from NAS
servers and folder structures which are authorative in nature.

# How to use it

Below is the document on how to use the tool. You can also get the help by typing
--help.

```
USAGE: scrub.py [path] [match string] [arguments[]]

ARGUMENTS:
    --dry-run       This will cause no action to be taken and only output to the
                    the screen.
    --no-git        This will ignore all files and folders in .git folders
    --directory     This will scrub entire directories and not files
    --help          Displays this help text
```

# Possible Improvements

* Unit Tests
* Consider makeing the code a bit more eligant
* Consider adding a statistics report at the END
* Complete the .git igore feature

# Contribute

You are welcome to fork and contribute to this project.

# Technology
* Python 2.7
* OS: Any OS with Python installed
* GIT

# Some files which are popular to scrub

```
*.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon

# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk
```
