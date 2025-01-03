import random

def display_question(question, options):
    print(question)
    random.shuffle(options)
    print(f"Options are:\n{options}")

def get_user_input():
    return input("Enter the correct answer:").lower()

def main():
    questions = [
        "What is the capital city of Nepal?",
        "What is the currency of Nepal?",
        "What is the highest mountain in the world?",
        "What is the national animal of Nepal?"
    ]

    options = [
        ["a.Pokhara", "b.Dolpa", "c.Kathmandu", "d.Rolpa"],
        ["a.Rupees", "b.Dollar", "c.Pound", "d.Euro"],
        ["a.Mt.Kanchanjunga", "b.Dhaulagiri", "c.Sagarmatha", "d.Mt.Monaslu"],
        ["a.Dog", "b.Cat", "c.Cow", "d.Rabbit"]
    ]

    correct_answers = ["Kathmandu", "Rupees", "Sagarmatha", "Cow"]
    additional_amounts = [1000, 10000, 20000, 300000]

    # Shuffle questions
    question_order = list(range(len(questions)))
    random.shuffle(question_order)

    count = 0

    for i in question_order:
        question = questions[i]
        option = options[i]
        correct_answer = correct_answers[i]
        additional_amount = additional_amounts[i]

        print(f"Questions for {additional_amount}")
        display_question(question, option)

        user_answer = get_user_input()

        if user_answer == correct_answer.lower():
            count += additional_amount
            print(f"The answer is correct, and your amount earned is {count} rs.")
        else:
            print("Wrong answer! Game Over.")
            break

if __name__ == "__main__":
    main()