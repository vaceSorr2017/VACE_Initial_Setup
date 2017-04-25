gmail account:
usna2017vace@gmail.com
password: vace2017

github:
vaceSorr2017
password: vace2017

amazon account:
account:
password:

Watcha Need:
Amazon Alexa
Amazon account
Computer with Linux OS

Setting up:
Step 1: Setup and connect Alexa to local Wifi
Step 2: go to https://console.aws.amazon.com/sqs
    2a: in upper right hand corner ensure region is set to US East N. Virginia 
    2b: click "Create New Queue", name it and keep default settings
    2c: take note of new queue url, you'll need it later
Step 3: go to iam website, https://console.aws.amazon.com/iam
    3a: click user tab -> click add users
    3b: click "Security Credentials" tab and select "Create Access K"ey
    3c: download csv file
    3d: take note of api access key and access secret, you'll need these later
Step 4: Open command line and install boto3 (sudo pip3 install boto3)**Ensure pip is installed**
Step 5: go to https://console.aws.amazon.com/lambda and ensure region in top right corner is set to US East N. Virginia
    5a: Click "Create A Lambda Function"
    5b: In the drop down menu select runtime python2.7 and select blank project
    5c: Configure the trigger -> First grey box select -> Click Next
    5d: Enter function name and description then create custom role under the role dropdown called "lambda_basic_execution" with default rights
    5e: Select Python2.7 from runtime drop down
    5f: Copy and paste the code "********" located in the github repo here
    5g: Enter your Access key, access secret, region(ex.) "us-east-1" ), and queue url.
    5h: Click Next and "Create Function"
