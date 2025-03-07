"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import json
from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="Zohar/distilgpt2-finetuned-restaurant-reviews")

def handler(event, context):
    response = {
        "statusCode": 200,
        "body": nlp(event['text'])[0]
    }
    return response