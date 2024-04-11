"""PII Scan"""
from urllib.parse import urlparse, parse_qs
import re
import spacy
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.predefined_recognizers import (ItDriverLicenseRecognizer,
                                                      ItVatCodeRecognizer,
                                                      ItFiscalCodeRecognizer,
                                                      ItIdentityCardRecognizer,
                                                      ItPassportRecognizer,
                                                      EsNifRecognizer,
                                                      PlPeselRecognizer)
from presidio_anonymizer import AnonymizerEngine

# make sure en_core_web_lg is loaded correctly
# this can also be achieved with
# python -m spacy download en_core_web_lg
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Create an analyzer object
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
# Add some language specific recognizers as english instead of default language
registry.add_recognizer(ItDriverLicenseRecognizer(supported_language='en'))
registry.add_recognizer(ItVatCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItFiscalCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItIdentityCardRecognizer(supported_language='en'))
registry.add_recognizer(ItPassportRecognizer(supported_language='en'))
registry.add_recognizer(EsNifRecognizer(supported_language='en'))
registry.add_recognizer(PlPeselRecognizer(supported_language='en'))
analyzer = AnalyzerEngine(registry=registry)
anonymizer = AnonymizerEngine()


def show_aggie_pride():
    """Show Aggie Pride"""
    return "Aggie Pride - Worldwide"


def anonymize_text(text: str, entity_list: list) -> str:
    """
    Anonymize the text using the entity list
    :param text: the text to be anonymized
    :param entity_list: the list of entities to be anonymized
           https://microsoft.github.io/presidio/supported_entities/
    """
    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                               entities=entity_list,
                               language='en')

    # Analyzer results are passed to the AnonymizerEngine for anonymization
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    return anonymized_text.text


def anonymize_file(file_path: str):
    """
    Anonymize the text using the entity list
    :param file_path: the path to the file to be anonymized
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(anonymize_text(line, []))


if __name__ == '__main__':
    anonymize_file('case_notes.txt')


def check_url(url):
    """Method for the URL"""
    #Creating function to determine if pii is in URL
    private_info = r'password|passwd|pwd|secret|token|api_key'

    qurey_url = urlparse(url)
    url_parameters = parse_qs(qurey_url.query)

    for _, values in url_parameters.items():
        if any(re.search(private_info, value, re.IGNORECASE) for value in values):
            return True
    return False
