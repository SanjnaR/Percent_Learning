from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

WORDLIST_FILENAME = "civil_war.txt"

def load_words():
    """
    Returns a string words in specified textfile.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    full_text = " "
    # full_text: text of all strings
    for line in inFile:
        full_text += line.lower()

    print(len(full_text), "words loaded")

    return full_text



def entities_text(text):
    """ Detects entities """
    """ Param: text string of text """
    """ Returns salient words and entity types """

    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    entities = client.analyze_entities(document).entities

    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
    ent_list = []

    for entity in entities:
        ent_list.append((entity.name, entity_type[entity.type]))

    return ent_list


print(entities_text(load_words()))

