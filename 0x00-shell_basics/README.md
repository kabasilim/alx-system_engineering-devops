# 0x00-shell_basics

## Description and script
1. current_working_directory: prints the absolute path name of the current working directory.
2. listit: Display the contents list of your current directory.
3. bring_me_home:Write a script that changes the working directory to the user’s home directory.
4. listfiles: Display current directory contents in a long format.
5. listmorefiles: Display current directory contents, including hidden files (starting with .). Use the long format.
6. listfilesdigitonly: Display current directory contents.
* Long format
* with user and group IDs displayed numerically
* And hidden files (starting with .)
7. firstdirectory: Create a script that creates a directory named my_first_directory in the /tmp/ directory.
8. Move the file betty from /tmp/ to /tmp/my_first_directory.
9. Delete the file betty.
* The file betty is in /tmp/my_first_directory
10. Delete the directory my_first_directory that is in the /tmp directory.
11. Write a script that changes the working directory to the previous one.
12. Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
13. Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
14. Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
15. Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
* You can consider that all HTML files have the extension .html
16. Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
* You can assume that the directory /tmp/u will exist when we will run your script
