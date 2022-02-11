
# Text Summarizer 

This project is about developing a text summarizer using Hugging Face.


## Screenshot

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Text-Summarizer---Hugging-Face/blob/main/images/Screenshot.png?raw=true)



## API

To get the API 
- Go to https://huggingface.co/settings/token 
- Choose Access Tokens
- New Token 

Now replace xxxxxxx with your token 

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Text-Summarizer---Hugging-Face/blob/main/images/Screenshot%20api.png)

You can also use a different model 
- Go to https://huggingface.co/models?pipeline_tag=summarization&sort=downloads
- Select a model
- Click on deploy (right side of the page)
- Select Accelerated Inference, copy the API_URL and replace it.


## Run Locally

Clone the project

```
  git clone https://github.com/xx-CRAZINESS-xx/Text-Summarizer---Hugging-Face.git
```

Go to the project directory

```
  cd Text-Summarizer---Hugging-Face
```

Install dependencies

```
  pip install -r requirements.txt
```

Start the server

```
  python app.py
```

