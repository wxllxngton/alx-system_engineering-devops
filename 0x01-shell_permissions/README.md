List all commands in a few
#!/bin/bash

su betty - change user to betty
whoami - print the effective username of the currrnt user
groups $(whoami) - prints all the groups the current user is part of.
chown - used to change the owner of a file
chmod u+x - adds execute permission to the owner of the file
chmod g+x - adds execute permission to the group owner of the file
chmod o+r - adds read permission to other users
