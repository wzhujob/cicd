#!/bin/bash
set -xe

# Copy war file from S3 bucket to tomcat webapp folder
#aws s3 cp s3://codestack8-webappdeploymentbucket-qfkvzbvpi1kz/SpringBootHelloWorldExampleApplication.war /usr/local/tomcat9/webapps/SpringBootHelloWorldExampleApplication.war
aws s3 cp s3://codedeploy1whiteboatbucket/httpserver.py /usr/local/pythonserver/httpserver.py

# Ensure the ownership permissions are correct.
chown -R pythonapp:pythonapp /usr/local/pythonserver