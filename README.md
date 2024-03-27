# GenAiWithGemini

Generative AI examples with Google Gemini LLM

**Setup:**
* Create a new folder to hold all the code examples
* Create a local python environment in this folder `conda -p ./myenv python=3.11 -y`
  (NOTE: python version >= 3.9 - I am using `conda` here, you can use your favourite env management module)
* Activate the local environment `conda activate ./myenv` - check your command line prompt to confirm that local environment has been activated.
* Install _at least_ the following modules:
  `pip install langchain google-generativeai langchain-google-genai ipykernel dotenv`
  Alternatively, you can create a `requirements.txt` file and add these modules to that file. Then install
  as follows ($> is the command line prompt):
  `$> pip install -r requirements.txt`
* Get Google API key
    * Navigate to the Google AI for Developers website
    * Click on the large 'Get API in Google AI Studio button`
    * ..... TODO: complete this