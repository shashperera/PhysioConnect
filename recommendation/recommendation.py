from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Example exercises from your RDS (replace with your fetched data)
all_exercises = [
    {"id": 1, "name": "Hamstring Stretch", "description": "Stretch your hamstrings by reaching for your toes while sitting."},
    {"id": 2, "name": "Quad Stretch", "description": "Stand and pull your ankle to stretch your quadriceps."},
    {"id": 3, "name": "Calf Stretch", "description": "Lean against a wall to stretch your calf muscles."},
    {"id": 4, "name": "Glute Bridge", "description": "Lie on your back and lift your hips to strengthen glutes."},
    {"id": 5, "name": "Lunge", "description": "Step forward and lower your hips to stretch and strengthen legs."}
]

# Simulated user history (IDs of exercises they liked or did recently)
user_liked_ids = [1, 3]

# Get descriptions of user's liked exercises and all exercises
user_descriptions = [ex['description'] for ex in all_exercises if ex['id'] in user_liked_ids]
all_descriptions = [ex['description'] for ex in all_exercises]

# Use TF-IDF Vectorizer to compute similarity
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_descriptions)
user_profile = vectorizer.transform([' '.join(user_descriptions)])

# Calculate cosine similarity between user profile and all exercises
similarities = cosine_similarity(user_profile, tfidf_matrix).flatten()

# Recommend exercises not already liked, sorted by similarity
recommendations = sorted(
    ((i, sim) for i, sim in enumerate(similarities) if all_exercises[i]['id'] not in user_liked_ids),
    key=lambda x: x[1],
    reverse=True
)

print("Recommended exercises for you:")
for idx, sim in recommendations[:3]:  # Top 3 recommendations
    ex = all_exercises[idx]
    print(f"{ex['name']} (Similarity: {sim:.2f}) - {ex['description']}")