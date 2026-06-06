# 🚨 Offline Crisis Response Chatbot

An AI-powered chatbot that works completely offline — no internet needed after setup. Built for crisis situations like natural disasters, medical emergencies, and network outages.

## 💡 Features

- 100% offline after setup — works during network outages
- First Aid guidance (bleeding, burns, CPR, fractures)
- Natural Disaster help (earthquake, flood, fire, cyclone)
- Health emergencies (fever, heart attack, heatstroke)
- Mental Health support (anxiety, depression, grief)
- Emotional support (loneliness, self-esteem, motivation)
- Semantic search using Sentence Transformers
- Interfaces — Streamlit

## 🛠️ Tech Stack

- Python 3.14
- Sentence Transformers (all-MiniLM-L6-v2)
- Streamlit

## 🚀 Setup

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run Streamlit version:
   streamlit run streamlit_app.py

pre-encoded tag descriptions using cosine similarity.
The closest matching tag's response is returned.
Zero internet needed after initial model download.
