# Exercise Recommendation System: How It Works

This document explains the logic behind the recommendation system implemented in your physiotherapy app.

---

## 1. What Does the System Do?

- It suggests new exercises to a user based on the exercises they have recently performed or liked.
- The recommendations are **personalized** and aim to be similar to the user's preferences.

---

## 2. How Does It Work?

### **Step-by-Step Process**

1. **User History**
    - The system keeps track of exercises a user has recently performed or liked (e.g., IDs `[1, 3]`).

2. **Exercise Database**
    - All available exercises are listed, each with an `id`, `name`, and `description`.

3. **Text Representation (TF-IDF)**
    - Each exercise description is converted into a numerical vector using **TF-IDF Vectorization**:
        - **TF-IDF** stands for **Term Frequency-Inverse Document Frequency**.
        - It measures the importance of each word in the description relative to all other descriptions.

4. **User Profile Vector**
    - The system concatenates the descriptions of exercises the user likes and vectorizes them, forming a "user profile vector."

5. **Similarity Calculation (Cosine Similarity)**
    - The system calculates the **cosine similarity** between the user profile vector and each exercise's vector.
    - **Cosine similarity** measures how similar two vectors are (1 = very similar, 0 = not similar).

6. **Filtering and Sorting**
    - Exercises the user already liked are **excluded**.
    - The remaining exercises are **sorted** from most similar to least similar, based on the similarity score.

7. **Recommendation Output**
    - The top N most similar exercises are presented as recommendations, along with a similarity score and their descriptions.

---

## 3. Example Output

```
Recommended exercises for you:
Quad Stretch (Similarity: 0.24) - Stand and pull your ankle to stretch your quadriceps.
Glute Bridge (Similarity: 0.15) - Lie on your back and lift your hips to strengthen glutes.
Lunge (Similarity: 0.15) - Step forward and lower your hips to stretch and strengthen legs.
```

- **Interpretation:**  
  The system found "Quad Stretch" to be most similar to the user's previous choices, based on the language in the descriptions.

---

## 4. Why Is This Useful?

- **Personalization:**  
  Users receive exercise suggestions that match their interests or rehab needs.
- **Scalability:**  
  As the database grows, the system can recommend from hundreds of exercises without manual curation.
- **User Engagement:**  
  Suggesting relevant exercises can keep users motivated and engaged.

---

## 5. Technical Summary

- **Algorithm:** Content-based filtering (using TF-IDF + cosine similarity).
- **Libraries Used:** `scikit-learn` for TF-IDF and similarity computation.
- **Input:** User's liked/performed exercise IDs.
- **Output:** Ranked list of recommended exercises.

---

*For questions or improvements, refer to the source code or contact the development team.*