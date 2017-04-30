import boto3

access_key = "AKIAIDKSYHBVCWRKNG4A"
access_secret = "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"
region ="us-east-1"
queue_url = "https://sqs.us-east-1.amazonaws.com/414209115789/Echo"

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def post_message(client, message_body, url):
    response = client.send_message(QueueUrl = url, MessageBody= message_body)
    
def lambda_handler(event, context):
    client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
    intent_name = event['request']['intent']['name']
    if intent_name == "First":
        post_message(client, 'first', queue_url)
        message = "Scanning Google"
    elif intent_name == "Second":
        post_message(client, 'second', queue_url)
        message = "Scanning ESPN"
    elif intent_name == "Third":
        post_message(client, 'third', queue_url)
        message = "Scanning War Room Gateway"
    elif intent_name == "Fourth":
        post_message(client, 'fourth', queue_url)
        message = "Scanning Research Server"
    else:
        message = "Unknown"
        
    speechlet = build_speechlet_response("Computer Status", message, "", "true")
    return build_response({}, speechlet)
