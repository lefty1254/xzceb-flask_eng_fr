"""Module to translate text from english to french and french to english """
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-16',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """function that takes english text, translates and returns to french"""
    if english_text is None:
        return "Can't have null input"
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
        ).get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """function that takes french text, translates and returns to english"""
    if french_text is None:
        return "Can't have null input"
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
        ).get_result()['translations'][0]['translation']
    return english_text
