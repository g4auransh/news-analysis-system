from transformers import pipeline

# Load pipelines (cached locally on first run)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment = pipeline("sentiment-analysis")
ner = pipeline("ner", aggregation_strategy="simple")

def process_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    sent = sentiment(text)[0]
    entities = ner(text)
    return summary, sent, entities