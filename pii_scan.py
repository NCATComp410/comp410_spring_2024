"""PII Scan"""
import spacy
from presidio_analyzer import AnalyzerEngine
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
analyzer = AnalyzerEngine()
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


if __name__ == '__main__':
    print(show_aggie_pride())
    print(anonymize_text('my name is John Doe', ['PERSON']))
