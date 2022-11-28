#import json
"""tranlation module"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(english_text):
    """Translate ENglish text to French text"""
    if english_text is None or len(english_text) == 0:
        return None
    #write the code here
    french_text=english_text
    # Invoke a method
    authenticator=IAMAuthenticator(apikey)
    language_translator=LanguageTranslatorV3(
        version='2022-11-15',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')
    language_translator.set_disable_ssl_verification(False)
    #languages=language_translator.list_identifiable_languages().get_result()
    # print("languages -- ")
    # print(json.dumps(languages, indent=2))
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    print(french_text)
    return french_text

def frenchToEnglish(french_text):
    """Translate French text to English text"""
    if french_text is None or len(french_text) == 0:
        return None
    #write the code here
     #write the code here
    english_text = french_text
    # Invoke a method
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2022-11-15',
        authenticator=authenticator
    )
    language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com')
    language_translator.set_disable_ssl_verification(False)
   # languages = language_translator.list_identifiable_languages().get_result()
    # print("languages -- ")
    # print(json.dumps(languages, indent=2))
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    print(english_text)

    return english_text
