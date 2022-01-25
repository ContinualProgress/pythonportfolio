# yahooapi
---
## Description
This is a CLI implementation of the yahoofinanceapi API.  The site for the api in question is located at https://www.yahoofinanceapi.com.  In order to use this tool, you'll need an api key, which can be gained by siging up for a free account.\
\
The output of the script is returned in a JSON format. 

## Libraries Used
---
* click
* requests
* json
* pprint

## Setup Instructions

1. Create a virtual environment.\
`python3 -m venv <path-to-virtual-environment>`

**NOTE:**  If you don't have the appropriate module (venv) installed, you can do so with the following:
`python3 -m pip install venv`

2. Activate the new virtual environment.\
`source <path-to-virtual-environment>/bin/activate>`

3. Once the virtual environment has been activated, add the packages listed in REQUIREMENTS.txt.\
`pip install -U pip`\
`pip install -r REQUIREMENTS.txt`

4. Remove the placeholder from api-key.txt, replace the line with an API key.

5. Within the virtual environment, the command can be invoked with the following...\
`python3 yahooapi.py`
