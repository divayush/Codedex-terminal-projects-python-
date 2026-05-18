print("🤑 Who Wants to Be a Millionaire") #lol
print("So in this, you have 10 questions related to Python\n;> For every step, the points get doubled and the difficulty increases.")
print("Lets start!")
player_score = 0
questions = [                                                                         # So i created list with sub dictnories 

    {
        "question": "What keyword is used to create a function in Python?",           #print(questions[0]["question"])
        "options": {
            "a": "func",
            "b": "define",
            "c": "def",
            "d": "function"
        },
        "answer": "c",
        "value": 1000
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "a": "//",
            "b": "#",
            "c": "/*",
            "d": "<!--"
        },
        "answer": "b",
        "value": 2000
    },

    {
        "question": "What data type is returned by input() in Python?",
        "options": {
            "a": "int",
            "b": "float",
            "c": "string",
            "d": "bool"
        },
        "answer": "c",
        "value": 5000
    },

    {
        "question": "Which loop is mainly used when the number of iterations is known?",
        "options": {
            "a": "while",
            "b": "repeat",
            "c": "loop",
            "d": "for"
        },
        "answer": "d",
        "value": 10000
    },

    {
        "question": "Which data type stores key-value pairs in Python?",
        "options": {
            "a": "list",
            "b": "tuple",
            "c": "dictionary",
            "d": "set"
        },
        "answer": "c",
        "value": 20000
    },

    {
        "question": "What will len([1, 2, 3, 4]) return?",
        "options": {
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "Error"
        },
        "answer": "b",
        "value": 50000
    },

    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": {
            "a": "catch",
            "b": "final",
            "c": "try",
            "d": "error"
        },
        "answer": "c",
        "value": 100000
    },

    {
        "question": "What does append() do in a list?",
        "options": {
            "a": "Removes an item",
            "b": "Sorts the list",
            "c": "Adds an item to the end",
            "d": "Replaces the list"
        },
        "answer": "c",
        "value": 250000
    },

    {
        "question": "Which file mode is used to append data to a file?",
        "options": {
            "a": "r",
            "b": "w",
            "c": "x",
            "d": "a"
        },
        "answer": "d",
        "value": 500000
    },

    {
        "question": "What is the output type of {x for x in range(3)} ?",
        "options": {
            "a": "list",
            "b": "tuple",
            "c": "set",
            "d": "dictionary"
        },
        "answer": "c",
        "value": 1000000
    }

]

for q in questions:

    print(q["question"])

    for key, value in q["options"].items():
        print(f"{key}) {value}")

    while True:

        ask = input("Answer: ").lower()

        if ask not in ["a", "b", "c", "d"]:
            print("Error! Enter only a, b, c or d.")
            continue

        break

    if ask == q["answer"]:
        player_score += q["value"]

        print(
            f"Congratulations! You won ${q['value']}. "
            f"Your total prize money is now ${player_score}."
        )

    else:
        print("Wrong answer! You lost all your money.")
        break

# I know this one is a little hard but don’t give up ;>
