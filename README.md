# 📚 Content-Based Book Recommendation System

The system analyzes book metadata and recommends books based on content similarity, without relying on user ratings or history.

---

## 🚀 Features

- Recommends books based on **title + tags**
- Uses Goodreads dataset (**books, tags, book_tags**)
- Interactive user input system (**CLI-based**)
- Shows top matching books before recommending
- Returns **top 5 highly rated similar books**

---

## 🛠️ Tech Stack

- Python  
- Pandas – Data handling & preprocessing  
- Scikit-learn – Machine learning tools  
- CountVectorizer – Text vectorization  
- Cosine Similarity – Similarity calculation  

---

## ⚙️ How It Works

### 1. Data Processing
- Load datasets (`books.csv`, `book_tags.csv`, `tags.csv`)
- Merge tag IDs with tag names
- Combine all tags for each book into a single string

### 2. Feature Engineering
- Create a combined feature:
- - Handle missing values

### 3. Vectorization
- Convert text into numerical form using **CountVectorizer**

### 4. Similarity Calculation
- Compute similarity between books using **cosine similarity**

### 5. Recommendation System
- Takes user input (book name)
- Finds closest matching titles
- Recommends top similar books sorted by rating

---

## 📜 Dataset

Dataset sourced from Goodreads (Kaggle).

---

## ▶️ How to Run

### 1. Install Dependencies
```bash
pip install pandas scikit-learn
2. Run the Program
python recom.py
💻 Example
Input
Find books similar to: jane eyre
Output
Matching books:

1. Jane Eyre

Using: Jane Eyre

Top 5 Similar Books:

Wuthering Heights ⭐ 3.9  
Pride and Prejudice ⭐ 4.3  
Great Expectations ⭐ 3.8  
The Tenant of Wildfell Hall ⭐ 4.1  
Rebecca ⭐ 4.2  

🧠 Key Concepts Used
Content-Based Filtering
Text Vectorization
Cosine Similarity
Data Merging & Aggregation

🔮 Future Improvements
Improve matching (user selects exact book instead of auto-pick)
Use TF-IDF instead of CountVectorizer
Build a web interface (Streamlit/Flask)
Add filtering by genre, rating, or author
