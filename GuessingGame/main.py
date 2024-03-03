class Question:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

questions: list[Question] = [
    Question("What is 1 + 1?", "2"),
    Question("The capital of New Zealand?", "Wellington"),
]

def main() -> None:
    score = 0
    for question in questions:
        answer = input(f"{question.question} ")
        if answer.strip().lower() == question.answer.lower():
            score += 1
    print(f"You got {score}/{len(questions)} questions correct!")
    print()
    print("Correct Answers:")
    for question in questions:
        print(f"{question.question} {question.answer}")

if __name__ == "__main__":
    main()
