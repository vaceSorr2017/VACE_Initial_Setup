import boto3
import os
import time

access_key = "AKIAIDKSYHBVCWRKNG4A"
access_secret = "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"
region ="us-east-1"
queue_url = "https://sqs.us-east-1.amazonaws.com/414209115789/Echo"

def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)

    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message

client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

while(1):
    try:
        message = pop_message(client, queue_url)
        #print(message)
        if "first" in message:
            print('First Scan')
            os.system('nmap -sV google.com')
        elif "second" in message:
            print('Second Scan')
            os.system('nmap -sV espn.com')
        elif "third" in message:
            print('Third Scan')
            os.system('nmap -sV 50.253.25.241')
        elif "fourth" in message:
            print('Fourth Scan')
            os.system('nmap -sV 50.253.25.244')
    except:
        pass

