import requests
from bs4 import BeautifulSoup
import random

def fetch_questions():
    url = "https://www.today.com/life/relationships/questions-to-ask-a-girl-rcna131397"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    } 

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, "html.parser")

        questions = []
        for item in soup.find_all(["ul", "ol"]): 
            for li in item.find_all("li"): 
                question_text = li.get_text(strip=True)
                if question_text.endswith("?"):
                    questions.append(question_text)
        
        return questions

    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
        return None

def ask_random_questions(questions, num_questions=5):
    if questions:
        random_questions = random.sample(questions, num_questions)
        print("Questions for your date:")
        for i, question in enumerate(random_questions, 1):
            print(f"{i}. {question}")
    else:
        print("No questions available.")

questions = fetch_questions()

ask_random_questions(questions, num_questions=100)
