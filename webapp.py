import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize(text):
    return summarizer(text)[0]['summary_text']

gr.Interface(fn=summarize, inputs="textbox", outputs="textbox").launch()
