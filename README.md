# 🧠 AI Resume Screening System

An AI-based Resume Screening System that ranks resumes based on their similarity to a given job description using Natural Language Processing (NLP) techniques.

This project uses TF-IDF Vectorization and Cosine Similarity to automatically match resumes with job requirements.

---

## 🚀 Features

- Load resume dataset (CSV file)
- Text preprocessing (lowercase conversion)
- TF-IDF vectorization
- Cosine similarity computation
- Rank resumes based on similarity score
- Display Top 3 matching resumes
- Interactive command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Scikit-learn
- TF-IDF (Term Frequency – Inverse Document Frequency)
- Cosine Similarity

---

## 📂 Project Structure

resume_screening_project/
│
├── resumes.csv
├── src/
│   └── app.py
├── venv/
├── requirements.txt
└── README.md

---

## 📊 Dataset Information

The dataset contains the following columns:

- ID – Unique resume ID
- Resume_str – Resume text content
- Resume_html – Resume in HTML format
- Category – Job category label

This project uses the `Resume_str` column for similarity matching.

---

## ⚙️ Working Process

1. Load resume dataset using Pandas.
2. Convert resume text to lowercase (basic preprocessing).
3. Apply TF-IDF vectorization to convert text into numerical vectors.
4. Accept job description input from the user.
5. Transform job description into TF-IDF vector.
6. Compute cosine similarity between job description and resumes.
7. Rank resumes and display Top 3 matching results.

---

## 🧮 Algorithm Explanation

### 1️⃣ TF-IDF (Term Frequency – Inverse Document Frequency)

TF-IDF converts textual data into numerical feature vectors.

It increases the weight of important words and decreases the weight of common words.

---

### 2️⃣ Cosine Similarity

Cosine Similarity measures similarity between two vectors.

Formula:

cos(θ) = (A · B) / (||A|| ||B||)

Where:
- A = Resume Vector
- B = Job Description Vector
- · = Dot Product
- ||A|| = Magnitude of vector A

If similarity value is close to 1 → High match  
If similarity value is close to 0 → Low match  

---

## ▶️ How to Run the Project

### Step 1: Activate Virtual Environment (Optional)

Windows:
venv\Scripts\activate

---

### Step 2: Install Required Libraries

pip install pandas scikit-learn

---

### Step 3: Run the Application

python src/app.py

---

### Step 4: Enter Job Description

Example:

Enter Job Description:
Looking for a Python developer with machine learning experience

The system will display Top 3 matching resumes with similarity scores.

Type "exit" to stop the program.

---

## 🔥 Sample Output

🔥 Top 3 Matching Candidates

Resume 1 – Score: 0.87  
Resume 2 – Score: 0.81  
Resume 3 – Score: 0.78  

---

## 🎯 Future Enhancements

- Add web interface using Flask or Streamlit
- Add PDF resume upload
- Improve preprocessing (tokenization, stopword removal)
- Deploy as web application
- Add skill extraction module

---

## 📌 Project Domain

Artificial Intelligence  
Machine Learning  
Natural Language Processing  

---

## ⭐ Conclusion

This project demonstrates how Natural Language Processing and Machine Learning techniques can automate resume screening and help recruiters identify suitable candidates efficiently.

The system reduces manual effort and speeds up the recruitment process.
