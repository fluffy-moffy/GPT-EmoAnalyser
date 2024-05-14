# README

This guide provides instructions on how to set up and run the GPT-EmoAnalyser application, which interfaces with OpenAI's GPT models and utilizes sentiment analysis from TextBlob.


## Installation Instructions
-----------------
1. **Clone the repository or download the source code:**
   ```bash
   git clone https://github.com/fluffy-moffy/GPT-EmoAnalyser.git
   ```
   ```bash
   cd GPT-EmoAnalyser
   ```


2. Install required Python libraries:
   ```bash 
   pip install -r requirements.txt
   ```
   if you want, install it within the virtual environment.


3. Obtain an API key from OpenAI:
- Visit [https://platform.openai.com/api-keys](https://platform.openai.com/docs/quickstart)
- Follow the instructions to get the OPENAI_API Key and set it up.


## Running the Application
-----------------
To run the application, execute the following command in the terminal:
```bash
cd src
```
```bash
python driver.py
```

## Additional Setup
----------------
- TextBlob Library:
  After installing the required libraries, run the following command to download the necessary corpora for TextBlob:
python -m textblob.download_corpora

Note: TextBlob's sentiment analysis can sometimes be unstable. If you observe that there is no change in sentiment temperature, try terminating and restarting the process.

## Troubleshooting
---------------
- If you encounter issues related to API key permissions or limits, ensure your OpenAI account is active and has the appropriate access levels.
- Using the OpenAI API might incur charges, so please check the current pricing plans on OpenAI's platform and ensure you understand the cost implications before extensive use.

If you need further assistance, contact support@openai.com
