from db_connection import get_db_connection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Connect to your RDS SQL Server database using the separate connection file
conn = get_db_connection()
cursor = conn.cursor()

# 2. Fetch all exercises
cursor.execute("SELECT id, name, description FROM exercises")
all_exercises = [
    {"id": row.id, "name": row.name, "description": row.description or ""}
    for row in cursor.fetchall()
]

# 3. Simulate user history (fetch from your user tracking table or hardcode for now)
user_liked_ids = [1, 3]  # Replace with actual logic for your app

# 4. Prepare descriptions
user_descriptions = [ex['description'] for ex in all_exercises if ex['id'] in user_liked_ids]
all_descriptions = [ex['description'] for ex in all_exercises]

# 5. Content-based recommendation logic
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_descriptions)
user_profile = vectorizer.transform([' '.join(user_descriptions) if user_descriptions else ""])

similarities = cosine_similarity(user_profile, tfidf_matrix).flatten()

# 6. Recommend exercises not already liked, sorted by similarity
recommendations = sorted(
    ((i, sim) for i, sim in enumerate(similarities) if all_exercises[i]['id'] not in user_liked_ids),
    key=lambda x: x[1],
    reverse=True
)

print("Recommended exercises for you:")
for idx, sim in recommendations[:3]:
    ex = all_exercises[idx]
    print(f"{ex['name']} (Similarity: {sim:.2f}) - {ex['description']}")

# 7. Clean up
conn.close()