# sentiment_analysis.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Dataset (sadə nümunə - sən sonradan IMDb, Twitter və s. əlavə edə bilərsən)
data = {
    "text": [
        "I love this movie, it was fantastic!",
        "This film is terrible, I hate it.",
        "Amazing acting, really enjoyed it.",
        "Worst plot ever, boring movie.",
        "What a great experience, loved it!",
        "Not worth watching, waste of time."
    ],
    "label": ["positive", "negative", "positive", "negative", "positive", "negative"]
}

df = pd.DataFrame(data)

# Train-test bölmə
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# Text → sayğac (bag-of-words)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Proqnoz
y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
