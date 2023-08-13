
import os
import streamlit as st
import requests
import time
import requests
import uuid
import json


st.set_page_config(layout="wide", page_title="NLP Application")

# os.system("/home/appuser/venv/bin/python -m spacy download en_core_web_sm")
st.title("NLP Application")

# write a short description of the app
st.info("This app is a NLP application that can generate sentences from a given sentence without losing the meaning of the original sentence.")


VI_MODEL_API_URL = "https://api-inference.huggingface.co/models/vandung/t5paraphase-finetuned"
EN_MODEL_API_URL_1 = "https://api-inference.huggingface.co/models/ihgn/similar-questions"
EN_MODEL_API_URL_2 = "https://api-inference.huggingface.co/models/ihgn/gpt3-paraphrase"

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model_name_vi = "vandung/t5paraphase-finetuned"
model_vi = AutoModelForSeq2SeqLM.from_pretrained(model_name_vi)
tokenizer_vi = AutoTokenizer.from_pretrained(model_name_vi)

def text2text(sentence, max_new_tokens, API_URL):
    input_ids = tokenizer_vi.encode(sentence, return_tensors="pt")
    outputs = model_vi.generate(input_ids, max_length=max_new_tokens, do_sample=True, num_return_sequences=5, temperature=1.0)
    return [tokenizer_vi.decode(output_id, skip_special_tokens=True) for output_id in outputs]

st.sidebar.title("Select language")
language = st.sidebar.radio(
    "Language", ["English - T5", "English - GPT3", "Vietnamese"])

if language == "English - T5":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        maxnewtokens = len(en_sentence) + 5
        answer = text2text(en_sentence, maxnewtokens, API_URL=EN_MODEL_API_URL_1)
        for i in range(len(answer)):
            st.success(answer[i]["generated_text"])
elif language == "English - GPT3":
    en_sentence = st.text_input("Enter your sentence:")
    if st.button("Generate"):
        maxnewtokens = len(en_sentence) + 5
        answer = text2text(en_sentence, maxnewtokens, API_URL=EN_MODEL_API_URL_2)
        for i in range(len(answer)):
            st.success(answer[i]["generated_text"])
else:
    vi_sentence = st.text_input("Enter your vi sentence:")
    if st.button("Generate"):
        maxnewtokens = len(vi_sentence) + 5
        answer = text2text(vi_sentence, maxnewtokens, API_URL=VI_MODEL_API_URL)
        for i in range(len(answer)):
            st.success(answer[i]["generated_text"])

st.sidebar.title("About")
st.sidebar.info(
    "This app is created by Van Dung and Sang Sinh. Advised by Mr. Le Anh Cuong.")

# add a link to the source code
st.sidebar.title("Source code and Reference")
st.sidebar.info("https://github.com/vandung3101/uni-project-webapp")

# add a link to the model on hugingface
st.sidebar.title("Model cards")
st.sidebar.info("https://huggingface.co/ihgn/similar-questions")
st.sidebar.info("https://huggingface.co/ihgn/gpt3-paraphrase")
st.sidebar.info("https://huggingface.co/vandung/t5paraphase-finetuned")

# add Contact info
st.sidebar.title("Contact")
st.sidebar.info("Email:  51900046@student.tdtu.edu.vn")

# display the images in /images folder
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.write("")
with col2:
    st.image("images/6.png")
    st.image("images/4.png")
    st.image("images/5.png")
    st.image("images/1.png")
    st.image("images/2.gif")
    st.image("images/3.png")
with col3:
    st.write("")
