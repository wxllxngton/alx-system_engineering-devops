List all commands in a few
#!/bin/bash

su betty - change user to betty
whoami - print the effective username of the currrnt user
groups $(whoami) - prints all the groups the current user is part of.
chown - used to change the owner of a file
((chmod u+x,g+x,o+r hello)) - an example of multiple permissions
chmod u+x - adds execute permission to the owner of the file
chmod g+x - adds execute permission to the group owner of the file
chmod o+r - adds read permission to other users
mode=$(stat -c %a olleh) - The stat command is used to get the mode of the file olleh. The %a option is used to print the mode in octal notation. The mode is then stored in the mode variable.
chmod "$mode" hello - command is used to set the mode of the file hello to the same mode as the file olleh, using the value stored in the mode variable.
