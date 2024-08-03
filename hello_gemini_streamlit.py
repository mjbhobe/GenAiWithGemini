""" hello_gemini.py: Hello Google Gemini
This is a streamlit based Q&A application that works with Google Gemini

@author: Manish Bhobe
My experiments with Python, Data Science, Deep Learning & Generative AI.
Code is made available as-is & for learning purposes only, please use at your own risk!!
"""

import pathlib
import textwrap
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st

import google.generativeai as genai

# the following modules are useful only if you run code in Notebooks
from IPython.display import display
from IPython.display import Markdown

# load env variables from .env file
_ = load_dotenv(find_dotenv())  # read local .env file
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# create instance of the text model
model = genai.GenerativeModel("gemini-pro")


def to_markdown(text):
    """function to convert response from model to correct format"""
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


def get_gemini_response(
    prompt_text: str,
    llm=model,
    temperature=None,
    top_p=None,
    top_k=None,
):
    """return response form LLM given prompt_text"""
    try:
        gen_config = {"temperature": temperature, "top_k": top_k, "top_p": top_p}
        response = llm.generate_content(prompt_text, generation_config=gen_config)
        return response.text
    except ValueError as err:
        print(f"get_gemini_response() Error: {err}")
        print(f"{response.prompt_feedback}")


def main():
    # setup Streamlit UI
    st.set_page_config(page_title="Ask Gemini: Q&A Demo with Google Gemini")
    st.header("Q&A with Google Gemini")

    prompt_text = st.text_area("Your Question? ", key="prompt_text")
    submit = st.button("Go!")

    if submit:
        # the submit button is clicked
        response = get_gemini_response(prompt_text, temperature=0.0)
        st.write(response)


if __name__ == "__main__":
    main()
