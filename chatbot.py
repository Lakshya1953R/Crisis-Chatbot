import json
import random
from sentence_transformers import SentenceTransformer, util

with open("knowledge_base.json", "r",encoding="utf-8") as file:
    data = json.load(file)

print("⏳ Loading AI model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ Model loaded!")

tag_list         = []
description_list = []
response_list    = []

for intent in data["intents"]:
    if intent["tag"] == "default":
        continue
    tag_list.append(intent["tag"])
    description_list.append(intent["description"])
    response_list.append(intent["responses"])

print("⏳ Building meaning vectors...")
description_vectors = model.encode(
    description_list,
    convert_to_tensor=True
)
print("✅ Ready! Chatbot is live.")

def get_response(user_input):

    user_vector = model.encode(
        user_input,
        convert_to_tensor=True
    )

    scores = util.cos_sim(user_vector, description_vectors)[0]
    best_index = scores.argmax().item()
    best_score = scores[best_index].item()

    print(f"🔍 Matched: {tag_list[best_index]} (score: {round(best_score, 2)})")
    if best_score < 0.25:
        for intent in data["intents"]:
            if intent["tag"] == "default":
                return random.choice(intent["responses"])

    return random.choice(response_list[best_index])