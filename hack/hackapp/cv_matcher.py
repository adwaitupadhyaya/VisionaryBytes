import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pdf_text = ""
        for page in pdf.pages:
            pdf_text += page.extract_text()
    return pdf_text

# Function to calculate TF-IDF scores and matching score
def calculate_matching_score(vacancy_text, cv_text):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([vacancy_text, cv_text])
    matching_score = ((tfidf_matrix[0] * tfidf_matrix[1].T).A)[0, 0]
    return matching_score

def comparer(cv_path, vacancy_pdf_path):
    # Path of the pdf to be compared
    # Extract text from the PDFs
    vacancy_text = extract_text_from_pdf(vacancy_pdf_path)
    cv_text = extract_text_from_pdf(cv_path)

    # Preprocess the text (convert to lowercase for better matching)
    vacancy_text = vacancy_text.lower()
    cv_text = cv_text.lower()

    # Calculate the matching score
    matching_score = calculate_matching_score(vacancy_text, cv_text)
    return matching_score
    # Setting the threshold for considering a CV as a potential match


    # Checking if the CV is a potential match
    

