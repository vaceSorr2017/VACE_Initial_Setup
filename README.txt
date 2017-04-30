Required items:
Amazon Alexa
Amazon account
Computer with Linux OS

Setting up:
Step 1: Setup and connect Alexa to local Wifi
Step 2: Go to https://console.aws.amazon.com/sqs
    2a: In upper right hand corner ensure region is set to US East N. Virginia 
    2b: Click "Create New Queue", name it and keep default settings
    2c: Take note of new queue url, you'll need it later
Step 3: Go to iam website, https://console.aws.amazon.com/iam
    3a: Click user tab -> click add users
    3b: Click "Security Credentials" tab and select "Create Access K"ey
    3c: Download csv file
    3d: Take note of api access key and access secret, you'll need these later
Step 4: Open command line and install boto3 (sudo pip3 install boto3)**Ensure pip is installed**
Step 5: Go to https://console.aws.amazon.com/lambda and ensure region in top right corner is set to US East N. Virginia
    5a: Click "Create A Lambda Function"
    5b: In the drop down menu select runtime python2.7 and select blank project
    5c: Configure the trigger -> First grey box select -> Click Next
    5d: Enter function name and description then create custom role under the role dropdown called "lambda_basic_execution" with default rights
    5e: Select Python2.7 from runtime drop down and when it opens remove the default code
    5f: Copy and paste the code in enter_this_into_lambda.py located in the github repo here
    5g: Enter YOUR Access key, access secret, region(ex.) "us-east-1" ), and queue url.
    5h: Click Next and "Create Function"
Step 6: Copy check_queue.py into your working directory
    6a: Enter YOUR Access key, access secret, region(ex.) "us-east-1" ), and queue url. 
    6b: The "message" will be your intent name
Step 7: For testing create a skill as depicted in skill_info.png and Screenshot from 2017-04-30 19-03-01.png
    7a: Enter your Lambda ARN URL into the corrct field in the configuration tab.
    7b: To initiate the skill say "Alexa ... Ask vace[vase] First Scan" Where "vace[vase]" is the skill name, "First" is replaced by any other intent name, and "Scan" is replaced by anything written in the samples for the intent name.


Future use:
1.) Enable a skill to take in an undefined string and process it
2.) Change the check_queue.py to run in the crontab to constantly check instead of running as an infinite loop
