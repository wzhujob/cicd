#!/bin/bash
#set -x Prints out command arguments during execution.
#set -e Instructs a shell to exit if a command fails, i.e., if it outputs a non-zero exit status.
set -xe

# Start Tomcat, the application server.
#service tomcat start
#start the python3 server
#python3 /usr/local/pythonserver/httpserver.py
sudo -u pythonapp python3 /usr/local/pythonserver/httpserver.py
