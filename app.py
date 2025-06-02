import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize(text):
    return summarizer(text)[0]['summary_text']

demo = gr.Interface(fn=summarize, inputs="textbox", outputs="textbox")
demo.launch()
