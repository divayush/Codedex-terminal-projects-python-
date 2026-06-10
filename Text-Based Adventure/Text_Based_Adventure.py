print("Adventure Game")

name = input("Enter your name: ")

print(f"\nWelcome {name}")

choice = input("""
You are an adventurer and currently on dragon hunting.

While walking through the forest...

you found a baby dragon alone.

What do you want to do?

1. Kill him
2. Rescue him and take him with you

Choose: """)

# -----------------
# KILL ROUTE
# -----------------

if choice == "1":

    print("""
You attacked the baby dragon.

The forest became silent.

Nothing happened.

Then...

A roar shook the entire mountain.

Mother dragon found you.
""")

    choice2 = input("""
What do you do?

1. Run away
2. Fight

Choose: """)

    if choice2 == "2":

        print("""
You took out your weapon.

Mother dragon looked at you.

You attacked.

One hit.

That was all.

Years later...

People still tell stories
about a hunter
who challenged a dragon.

ENDING UNLOCKED:
The Fallen Hunter

GAME OVER
""")

    elif choice2 == "1":

        hide = input("""
You started running.

Mother dragon saw you.

Where do you hide?

1. Under water
2. Inside cave

Choose: """)

        if hide == "1":

            print("""
You hid underwater.

You waited.

And waited.

Eventually...

your breath disappeared.

You drowned.

Mother dragon never touched you.

ENDING UNLOCKED:
Silent Lake

GAME OVER
""")

        elif hide == "2":

            cave = input("""
You entered the cave.

1. Go outside
2. Go deeper

Choose: """)

            if cave == "1":

                print("""
You walked outside.

Mother dragon was waiting.

Fire covered everything.

Nothing remained.

ENDING UNLOCKED:
Burned by Fate

GAME OVER
""")

            elif cave == "2":

                bear = input("""
While moving deeper...

A wild bear appeared.

1. Run away
2. Fight

Choose: """)

                if bear == "1":

                    print("""
You tried escaping.

Too slow.

The bear caught you.

ENDING UNLOCKED:
Lost in Darkness

GAME OVER
""")

                elif bear == "2":

                    print("""
You fought.

You nearly lost.

But somehow...

you defeated the bear.

Inside the cave
you found treasure.

Gold.
Weapons.
Ancient maps.

Years later—

you became rich.

But people still remembered—

you once killed a dragon.

ENDING UNLOCKED:
Lone Survivor

RESULT:
Treasure Found

YOU WIN
""")

# -----------------
# SAVE ROUTE
# -----------------

elif choice == "2":

    print("""
You picked up the baby dragon.

At first it was scared.

But after some time—

it stopped shaking.

It followed you.

You gave it food.

You continued walking.

Hours passed.

Suddenly—

a huge shadow covered the sky.

Mother dragon landed.

She looked directly at you.
""")

    dragon = input("""
What do you do?

1. Return baby dragon
2. Keep baby dragon

Choose: """)

    if dragon == "2":

        print("""
You stepped back.

Baby dragon looked confused.

Mother dragon became angry.

She roared.

You realized—

some things do not belong to us.

Fire covered the forest.

ENDING UNLOCKED:
Selfish Choice

GAME OVER
""")

    elif dragon == "1":

        print("""
You slowly stepped forward.

The baby dragon looked at you.

Then happily ran to its mother.

You prepared yourself.

You thought she would attack.

But...

she lowered her head.

She understood.

You saved her child.

The baby dragon returned to you
and sat beside your feet.

Mother dragon watched quietly.

Then—

an arrow landed beside you.

Another.

Another.

Dragon hunters.

Their leader shouted:

"Kill them all!"

Mother dragon roared.

But she was injured.

The hunters surrounded all of you.
""")

        battle = input("""
What do you do?

1. Run away
2. Stay and help

Choose: """)

        if battle == "1":

            print("""
You escaped.

You survived.

Years later—

you returned.

Nothing remained.

No dragons.

No life.

Only silence.

You realized—

surviving is not always winning.

ENDING UNLOCKED:
Coward's Regret

GAME OVER
""")

        elif battle == "2":

            print("""
You held your weapon.

Your hands shook.

The hunters laughed.

Battle started.

You fought.

Mother dragon protected you.

You protected the baby dragon.

More hunters arrived.

You became tired.

You fell.

Then—

the baby dragon stood forward.

Small flames appeared.

Then stronger.

Then—

a huge fire burst.

Everyone stopped.

Mother dragon stood up.

She roared.

Together—

you fought.

Hours passed.

The hunters finally retreated.

Rain started.

Everything became quiet.

Mother dragon walked toward you.

She lowered her head.

Then turned around.

She wanted you to follow.
""")

            input("\nPress Enter to continue...")

            print("""
You walked.

One day.

Two days.

Three days.

Across mountains.

Across snow.

Across rivers.

Until—

the clouds opened.

A hidden valley appeared.

Thousands of dragons.

Flying.

Sleeping.

Living peacefully.

No human had ever entered.

Mother dragon looked at you.

Then—

she knelt.

All dragons followed.

You understood.

They accepted you.

Years passed.

The baby dragon grew.

Every morning—

it waited outside your home.

Every evening—

you flew together.

Stories spread across kingdoms.

People searched for the valley.

Nobody found it.

Because dragons only opened their gates—

to people who protected others.

You never became
the greatest hunter.

You became something greater.

Family.
""")

            input("\nPress Enter to continue...")

            print("""
ENDING UNLOCKED:
Guardian of Dragons

RESULT:
Dragon Trust Earned
Hidden Kingdom Found
Companion Obtained
Legend Created

TRUE ENDING

YOU WIN
""")

else:
    print("Wrong input. Type 1 or 2")