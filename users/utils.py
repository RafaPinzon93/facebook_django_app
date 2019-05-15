import base64
import json


def base64_url_decode(input):
    input = input.encode(u'ascii')
    input += '=' * (4 - (len(input) % 4))
    return base64.urlsafe_b64decode(input)


def parse_facebook_signed_request(input):

    encoded_sig, encoded_payload = input.split('.', 1)
    payload = json.loads(base64_url_decode(encoded_payload))

    if payload['algorithm'] != 'HMAC-SHA256':
        raise Exception('Invalid request. (Unsupported algorithm.)')

    return payload
