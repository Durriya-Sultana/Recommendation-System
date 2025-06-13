import streamlit as st
import random

# === Data with Tags ===
movies = [
    {"title": "Inception", "tags": ["dream", "sci-fi", "mind", "thriller"]},
    {"title": "Interstellar", "tags": ["space", "time", "sci-fi", "drama"]},
    {"title": "The Dark Knight", "tags": ["superhero", "action", "dc", "crime"]},
    {"title": "Titanic", "tags": ["romance", "history", "tragedy"]},
    {"title": "The Matrix", "tags": ["ai", "future", "sci-fi", "simulation"]},
    {"title": "Avatar", "tags": ["fantasy", "alien", "adventure", "sci-fi"]},
    {"title": "La La Land", "tags": ["romance", "music", "drama"]},
    {"title": "The Shawshank Redemption", "tags": ["prison", "hope", "drama"]},
    {"title": "Gravity", "tags": ["space", "thriller", "survival"]},
    {"title": "Guardians of the Galaxy", "tags": ["space", "superhero", "action", "comedy"]}
]

kdramas = [
    {"title": "Crash Landing on You", "tags": ["romance", "military", "comedy", "drama"]},
    {"title": "Goblin", "tags": ["fantasy", "immortal", "romance", "tragic"]},
    {"title": "Vincenzo", "tags": ["mafia", "action", "law", "revenge"]},
    {"title": "Itaewon Class", "tags": ["drama", "business", "revenge", "friendship"]},
    {"title": "Extraordinary Attorney Woo", "tags": ["law", "autism", "inspiration", "drama"]},
    {"title": "Descendants of the Sun", "tags": ["romance", "military", "action", "drama"]},
    {"title": "Start-Up", "tags": ["tech", "startup", "romance", "youth"]},
    {"title": "True Beauty", "tags": ["romance", "school", "comedy", "self-esteem", "drama"]},
    {"title": "My Love from the Star", "tags": ["fantasy", "alien", "romance", "mystery"]},
    {"title": "Twenty-Five Twenty-One", "tags": ["nostalgia", "sports", "romance", "coming of age"]}
]

books = [
    {"title": "Harry Potter", "tags": ["fantasy", "magic", "school", "adventure"]},
    {"title": "The Hobbit", "tags": ["fantasy", "adventure", "dragons", "journey"]},
    {"title": "1984", "tags": ["dystopia", "future", "politics", "control"]},
    {"title": "The Alchemist", "tags": ["philosophy", "inspiration", "dream", "journey"]},
    {"title": "Pride and Prejudice", "tags": ["romance", "classic", "society", "family"]},
    {"title": "The Martian", "tags": ["space", "survival", "science", "humor"]},
    {"title": "To Kill a Mockingbird", "tags": ["justice", "racism", "classic", "law"]},
    {"title": "The Great Gatsby", "tags": ["wealth", "love", "tragedy", "classic"]},
    {"title": "Mistborn", "tags": ["fantasy", "magic", "rebellion", "epic"]},
    {"title": "Dune", "tags": ["space", "politics", "fantasy", "epic"]}
]

# === Recommendation Function ===
def recommend(query, data):
    query_tags = query.lower().split()
    return [item for item in data if any(tag in query_tags for tag in item["tags"])]

# === Streamlit UI ===
st.title("🎯 Recommendation System")

category = st.selectbox("Choose a category:", ["Movies", "K-Dramas", "Books"])
query = st.text_input("Enter your preference (e.g. space, fantasy, romance):", "")

# === Get the data for selected category ===
if category == "Movies":
    data = movies
elif category == "K-Dramas":
    data = kdramas
else:
    data = books

# === Get Recommendations Live ===
results = recommend(query, data) if query else []

# === Save results to session_state for Surprise Me button ===
st.session_state["results"] = results

# === Show Recommendations ===
st.markdown("### 📌 Recommendations")
if results:
    for item in results:
        st.write("•", item["title"])
else:
    st.write("🔍 Enter a keyword to see matching items.")

# === Surprise Me ===
if st.button("🎲 Surprise Me"):
    if st.session_state["results"]:
        pick = random.choice(st.session_state["results"])
        st.info(f"🎉 Random Pick: {pick['title']}")
    else:
        st.warning("No items to surprise you with. Please enter a keyword.")
