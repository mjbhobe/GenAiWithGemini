# GenAiWithGemini

Generative AI examples with Google Gemini LLM

**Setup:**
* Create a new folder to hold all the code examples (for example `~/code/google_gemini`). We'll refer to this folder as `CODE_HOME` henceforth. Anywhere you see `$CODE_HOME`, expand it to the folder you created to hold all the code.
* Change directory to `$CODE_HOME` (i.e. `cd $CODE_HOME`)
* Create a local python environment in the `$CODE_HOME` folder `conda -p ./myenv python=3.11 -y`<br/>
  (NOTE: I have named the local environment `myenv` , you can use whatever name you like. Recommended python versions is >= 3.9 - I have used 3.11. I am using `conda` here to create the environment, you can use your favourite Python environment management module, such as `poetry` for example)
* Activate the local environment `conda activate ./myenv` - check your command line prompt to confirm that local environment has been activated.
* Install _at least_ the following modules:
  `pip install langchain google-generativeai langchain-google-genai ipykernel dotenv`
  Alternatively, you can create a `requirements.txt` file and add these modules to that file. Then install
  as follows ($> is the command line prompt):
  `$> pip install -r requirements.txt`
* Get Google API key
    * Navigate to the [Google AI for Developers](https://ai.google.dev/gemini-api?gad_source=1&gclid=CjwKCAjwp4m0BhBAEiwAsdc4aCOlLcAIsM7yx_1xe1_tWd5rDdFG6i5IkUWEswPu6BrGL3edmCawJhoCGf8QAvD_BwE)
    * Click on the large 'Get API in Google AI Studio button`
    * Click the **Create API Key** button to create a new API key (**WARING: Immediately** copy the key to clipboard & paste into some local text editor - once generated you cannot copy again!)
    * In `$CODE_HOME`, create a `.env` file and add the following line to the `.env` file.<br/>`GOOGLE_API_KEY=<<the value of key you just copied to clipboard>>`
  * You are all set!