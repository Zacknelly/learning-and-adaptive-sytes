# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ldrSO8v-5UpfDPfudyi8Viuzsdq0VkRf
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install googletrans
# %pip install deep_translator

from deep_translator import GoogleTranslator

def translate_text(text, src_lang, dest_lang):
    try:
        translator = GoogleTranslator(source=src_lang, target=dest_lang)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {e}"

# Test cases
test_sentences = [
    ("He was heartbroken", "en", "sw"),
    ("Ninakula chakula", "sw", "en"),
    ("School is important for learners.", "en", "sw"),
    ("Nimesafiri siku nzima.", "sw", "en"),
]

# Running tests
for sentence, src, dest in test_sentences:
    translated_text = translate_text(sentence, src, dest)
    print(f"Original ({src}): {sentence}")
    print(f"Translated ({dest}): {translated_text}\n")

