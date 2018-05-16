#!/usr/bin/env python

import os
import random
import logging

import boto3

logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def find_random_s3_image():
    client = boto3.client('s3')
    # Return one random key in the bucket
    key = random.choice(client.list_objects_v2(
        Bucket='gimmeatroll.com',
        MaxKeys=1000
    )['Contents'])['Key']
    return "https://s3.{}.amazonaws.com/gimmeatroll.com/{}".format(
            os.environ['AWS_DEFAULT_REGION'],
            key)

def handler(event, context):
    logger.debug(event)

    logo = find_random_s3_image()
    html = "<html><meta property='og:image' content='{}'/><img src='{}'></html>".format(logo, logo)
    return html

if __name__== "__main__":
    event = {}
    context = {}
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    print(handler(event, context))

