# import re
from ipaddress import ip_address
import sys
import time
# import string
import requests

# import json

base_endpoint = "https://api.assemblyai.com/v2"
headers = {'authorization': "your API key here"}


# Start the transcription process
def start_transcript(audio_url):
    # word_boost = ['schwach']
    post_json = {
        "audio_url": audio_url,
        # "language_code": "de",
        # "punctuate": False,
        # "format_text": False,
        # "word_boost": word_boost,
        # "dual_channel": True,
        # "entity_detection": True,
        # "auto_highlights": True,
        # "iab_categories": True,
        # "content_safety": True,
        # "sentiment_analysis": True,
        # "auto_chapters": True,
        # "speaker_labels": True,
        # "disfluencies": True,
        # "filter_profanity": True,
        "redact_pii": True,
        "redact_pii_sub": "entity_name",
        "redact_pii_policies": [
            "medical_process", "medical_condition", "blood_type", "drug", "injury", "number_sequence", "email_address", "date_of_birth", "phone_number", "us_social_security_number", "credit_card_number", "credit_card_expiration", "credit_card_cvv", "date", "nationality", "event", "language", "location", "money_amount", "person_name", "person_age", "organization", "political_affiliation", "occupation", "religion", "drivers_license", "banking_information"
        ]
    }

    r = requests.post(base_endpoint + "/transcript", headers=headers, json=post_json)

    if 'error' in r.json():
        print(r.json())
        
    return r.json()


# Get the completed transcription
def get_transcript(id):
    r = requests.get(base_endpoint + "/transcript/" + id, headers=headers)
    return r.json()


# Wait for the status of the transcription to be completed
def wait_for_result(id):
    print("polling for result...")
    response = get_transcript(id)
    while response['status'] not in ['completed', 'error']:
        time.sleep(3)
        response = get_transcript(response['id'])
        print(response['status'])
    return response


def main(audio_url):
    response = start_transcript(audio_url)
    print("transcript id: %s" % response['id'])
    response = wait_for_result(response['id'])

    # if response['status'] == "error":
    #     raise Exception(response['error'])

    return response
 

if __name__ == "__main__":
    audio_url = sys.argv[1]
    print(audio_url)
    main(audio_url)