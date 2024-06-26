# README

![demo](https://github.com/fluffy-moffy/GPT-EmoAnalyser/assets/90229589/e36e0245-b316-4442-9e98-39958c59deac)

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



## Troubleshooting
---------------
- If you encounter issues related to API key permissions or limits, ensure your OpenAI account is active and has the appropriate access levels.
- TextBlob's sentiment analysis can sometimes be unstable. If you observe that there is no change in sentiment temperature, try terminating and restarting the process.
- Using the OpenAI API might incur charges, so please check the current pricing plans on OpenAI's platform and ensure you understand the cost implications before extensive use.
