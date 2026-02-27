import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLP model
nlp = spacy.load("en_core_web_sm")

RESUME_COLUMN = "Resume_str"

# Load dataset
data = pd.read_csv("resumes.csv").head(300)

print("\nDataset Columns:")
print(data.columns)

# Check column existence
if RESUME_COLUMN not in data.columns:
    print(f"\n❌ Column '{RESUME_COLUMN}' not found in dataset!")
    print("Please change RESUME_COLUMN value.")
    exit()

# Text preprocessing
def preprocess(text):
    doc = nlp(str(text).lower())

    tokens = [
        token.lemma_
        for token in doc
        if token.is_alpha and not token.is_stop
    ]

    return " ".join(tokens)

# Clean resume text
data["clean_text"] = data[RESUME_COLUMN].apply(preprocess)

# Vectorization
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(data["clean_text"])

print("\n✅ Resume Screening System Ready")

# User prediction loop
while True:

    job_desc = input("\nEnter Job Description (or type exit): ")

    if job_desc.lower() == "exit":
        break

    clean_job = preprocess(job_desc)

    query_vector = vectorizer.transform([clean_job])

    similarity = cosine_similarity(query_vector, matrix)[0]

    data["score"] = similarity

    # Top 3 candidates
    top3 = data.sort_values("score", ascending=False).head(3)

    print("\n🔥 Top 3 Matching Candidates\n")

    print(top3[[RESUME_COLUMN, "score"]])