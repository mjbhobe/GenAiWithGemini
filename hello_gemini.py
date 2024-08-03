""" hello_gemini.py: Hello Google Gemini
This module introduces Google Gemini API and tests whether everything is 
setup correctly to use the Google Gemini LLM

@author: Manish Bhobe
My experiments with Python, Data Science, Deep Learning & Generative AI.
Code is made available as-is & for learning purposes only, please use at your own risk!!
"""

import os
from dotenv import load_dotenv, find_dotenv

import google.generativeai as genai

# load env variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# create an instance of Gemini LLM
# alternatively, use "gemini-pro" instead of "gemini-1.5-flash"
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What is Google Gemini?")
print(response.text)
