""" hello_gemini.py: Hello Google Gemini
This module introduces Google Gemini API and tests whether everything is 
setup correctly to use the gemini-pro text LLM

@author: Manish Bhobe
My experiments with Python, Data Science, Deep Learning & Generative AI.
Code is made available as-is & for learning purposes only, please use at your own risk!!
"""

import pathlib
import textwrap
import os
from dotenv import load_dotenv, find_dotenv

import google.generativeai as genai

# the following modules are useful only if you run code in Notebooks
# from IPython.display import display
# from IPython.display import Markdown

# load env variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


def to_markdown(text):
    """function to convert response from model to correct format"""
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


def main():
    # create instance of the text LLM
    llm = genai.GenerativeModel("gemini-pro")
    prompt_text = """I am writing a blog about Generative AI.\n
        Can you give me a comparison of Chat GPT 4 and Google Gemini?
        Please return response asa JSON object.
    """
    # ask Gemini
    try:
        response = llm.generate_content(prompt_text)
        print(response.text)
    except ValueError as err:
        print(f"Error: {err}")
        print(f"{response.prompt_feedback}")


if __name__ == "__main__":
    main()
