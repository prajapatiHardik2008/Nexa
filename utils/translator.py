from deep_translator import GoogleTranslator


def Translator(text):
    translated = GoogleTranslator(
        source="auto",
        target="en"
    ).translate(text)
    return translated



print(Translator("or bhai kya haal hai sab kuch thik hai na ?"))

