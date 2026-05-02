from random import choice
fortunes = (                                                           
    "Your next bug will teach you more than your last success.",
    "Clean code today saves you from chaos tomorrow.",
    "A small fix now prevents a big headache later.",
    "Every error message is a clue, not a failure.",
    "Consistency will take you further than motivation.",
    "The code you write today will shape your skills tomorrow.",
    "Debugging is where real learning happens.",
    "Your persistence will turn confusion into clarity."
)
fortune_teller = choice(fortunes) # I used choice it will randomly select a fortune from the tuple.
print(fortune_teller)