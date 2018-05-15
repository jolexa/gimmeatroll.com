#!/usr/bin/env python

import os
import logging

import boto3

logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def handler(event, context):
    logger.debug(event)

    logo = "https://media0.giphy.com/media/8oh42nM14t50Q/giphy.gif"

    html = "<html><meta property='og:image' content='{}'/><img src='{}'></html>".format(logo, logo)

    return html

if __name__== "__main__":
    event = {}
    context = {}
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
    print(handler(event, context))

