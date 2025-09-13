from colorama import init, Fore, Back, Style
import sys
import os
import time
import random
import textwrap
import json
from datetime import datetime
import threading
import math

# Initialize colorama
init()

# Define color schemes for different levels
LEVEL_COLORS = {
    1: Fore.BLUE,
    2: Fore.CYAN,
    3: Fore.GREEN,
    4: Fore.YELLOW,
    5: Fore.MAGENTA,
    6: Fore.LIGHTRED_EX,
    7: Fore.LIGHTMAGENTA_EX,
    8: Fore.LIGHTCYAN_EX,
    'exam': Fore.RED
}

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL, end="\n"):
    """Print colored text with specified style"""
    print(f"{style}{color}{text}{Style.RESET_ALL}", end=end)

def print_header(title, level=None):
    """Print game header with title"""
    clear_screen()
    color = LEVEL_COLORS.get(level, Fore.CYAN) if level else Fore.CYAN
    
    # Create a decorative header
    print_colored("╔" + "═" * 58 + "╗", color)
    print_colored("║", color, end="")
    print_colored(f"{title:^58}", color, Style.BRIGHT, end="")
    print_colored("║", color)
    print_colored("╚" + "═" * 58 + "╝", color)
    print()

def print_progress(level, score, max_score):
    """Print progress bar and score"""
    progress = (score / max_score) * 100
    bars = int(progress / 5)  # 20 bars for 100%
    
    level_color = LEVEL_COLORS.get(level, Fore.YELLOW)
    
    print_colored(f"Level: {level} ", level_color, Style.BRIGHT, end="")
    print_colored("[" + "█" * bars + "░" * (20 - bars) + "] ", Fore.GREEN, end="")
    print_colored(f"{score}/{max_score}", Fore.MAGENTA, Style.BRIGHT)
    print()

def type_effect(text, color=Fore.WHITE, speed=0.03):
    """Create typing effect for text"""
    for char in text:
        print(f"{color}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(speed)
    print()

def validate_answer(user_input, correct_answers):
    """Validate user input against multiple correct answer formats"""
    user_input = user_input.lower().strip()
    
    # Check if input matches any correct answer
    for answer in correct_answers:
        if user_input == answer.lower():
            return True
            
    # Check if input is a letter that corresponds to a correct answer
    if len(user_input) == 1 and user_input in ['a', 'b', 'c', 'd']:
        index = ord(user_input) - ord('a')
        if index < len(correct_answers):
            return True
            
    return False

def ask_question(question, options, correct_answers, explanation, score):
    """Ask a question and return updated score"""
    print_colored(question, Fore.CYAN, Style.BRIGHT)
    for option in options:
        print_colored(option, Fore.WHITE)
    
    user_answer = input("\n> ").strip()
    
    if validate_answer(user_answer, correct_answers):
        score += 1
        print_colored("✓ Correct! ", Fore.GREEN, Style.BRIGHT)
        print_colored(f"{explanation}\n", Fore.BLUE)
        return score, True
    else:
        print_colored("✗ Incorrect! ", Fore.RED, Style.BRIGHT)
        correct_formatted = f"{correct_answers[0]}" if len(correct_answers) == 1 else f"one of: {', '.join(correct_answers)}"
        print_colored(f"The correct answer is {correct_formatted}. {explanation}\n", Fore.YELLOW)
        return score, False

def ask_exam_question(question, options, correct_answers, question_number, total_questions):
    """Ask an exam question without feedback"""
    print_colored(f"Question {question_number}/{total_questions}:", Fore.MAGENTA, Style.BRIGHT)
    print_colored(question, Fore.CYAN, Style.BRIGHT)
    for option in options:
        print_colored(option, Fore.WHITE)
    
    user_answer = input("\n> ").strip()
    
    # Check if answer is correct
    is_correct = validate_answer(user_answer, correct_answers)
    
    # Clear a few lines to keep the exam clean
    for _ in range(10):
        print("\033[F\033[K", end="")  # Move cursor up and clear line
    
    return is_correct

def level_1(score):
    """Level 1: Basic Grammar"""
    print_header("LEVEL 1: BASIC GRAMMAR", 1)
    print_progress(1, score, 5)
    type_effect("Let's start with some basic grammar questions...", Fore.GREEN)
    
    questions = [
        {
            "question": "The sun ___ in the east.",
            "options": ["a) rise", "b) rises", "c) rising"],
            "correct_answers": ["b", "rises"],
            "explanation": "The sun rises in the east. 'Rises' is the correct present simple tense form for the third person singular."
        },
        {
            "question": "I ___ to school every morning.",
            "options": ["a) goes", "b) going", "c) go"],
            "correct_answers": ["c", "go"],
            "explanation": "I go to school every morning. 'Go' is the correct present simple tense form for the first person."
        },
        {
            "question": "She ___ a beautiful song yesterday.",
            "options": ["a) sings", "b) sang", "c) singing"],
            "correct_answers": ["b", "sang"],
            "explanation": "She sang a beautiful song yesterday. 'Sang' is the correct past tense form of 'sing'."
        },
        {
            "question": "My father ___ coffee every day.",
            "options": ["a) drink", "b) drinks", "c) drinking"],
            "correct_answers": ["b", "drinks"],
            "explanation": "My father drinks coffee every day. 'Drinks' is the correct present simple tense form for the third person singular."
        },
        {
            "question": "We ___ to the park last Sunday.",
            "options": ["a) go", "b) went", "c) goes"],
            "correct_answers": ["b", "went"],
            "explanation": "We went to the park last Sunday. 'Went' is the correct past tense form of 'go'."
        }
    ]
    
    for i, q in enumerate(questions):
        print_colored(f"Question {i+1}:", Fore.MAGENTA, Style.BRIGHT)
        score, correct = ask_question(q["question"], q["options"], q["correct_answers"], q["explanation"], score)
        if not correct and i < len(questions) - 1:
            print_colored("Don't worry! Let's try the next one.", Fore.YELLOW)
    
    return score

def level_2(score):
    """Level 2: Sentence Formation & Vocabulary"""
    print_header("LEVEL 2: SENTENCE FORMATION & VOCABULARY", 2)
    print_progress(2, score, 9)
    type_effect("Great job! Now let's test your sentence formation skills...", Fore.GREEN)
    
    questions = [
        {
            "question": "Arrange the words to make a sentence:\n\"morning / I / coffee / drink / .\"",
            "options": ["a) I drink coffee morning", "b) I drink coffee in the morning", "c) Coffee I drink morning"],
            "correct_answers": ["b", "I drink coffee in the morning"],
            "explanation": "The correct sentence is 'I drink coffee in the morning.' This follows the standard English sentence structure: Subject + Verb + Object + Prepositional Phrase."
        },
        {
            "question": "One word is spelled incorrectly. Spot it.",
            "options": ["freind, school, book"],
            "correct_answers": ["freind", "a"],
            "explanation": "'Freind' is misspelled. The correct spelling is 'friend' (i before e except after c)."
        },
        {
            "question": "Give the opposite word.\ntall → ?",
            "options": ["Enter the opposite word:"],
            "correct_answers": ["short"],
            "explanation": "The opposite of 'tall' is 'short'. Other opposites could be 'small' or 'low' depending on context."
        },
        {
            "question": "Find the synonym for the given word.\nHappy →",
            "options": ["a) sad", "b) glad", "c) angry"],
            "correct_answers": ["b", "glad"],
            "explanation": "A synonym for 'happy' is 'glad'. Other synonyms include 'joyful', 'cheerful', and 'content'."
        }
    ]
    
    for i, q in enumerate(questions):
        print_colored(f"Question {i+1}:", Fore.MAGENTA, Style.BRIGHT)
        score, correct = ask_question(q["question"], q["options"], q["correct_answers"], q["explanation"], score)
        if not correct and i < len(questions) - 1:
            print_colored("Don't worry! Let's try the next one.", Fore.YELLOW)
    
    return score

def level_3(score):
    """Level 3: Advanced Grammar & Vocabulary"""
    print_header("LEVEL 3: ADVANCED GRAMMAR & VOCABULARY", 3)
    print_progress(3, score, 19)
    type_effect("Impressive! Now let's challenge you with advanced grammar...", Fore.GREEN)
    
    questions = [
        {
            "question": "Choose the correct sentence:",
            "options": ["a) She don't like apples.", "b) She doesn't likes apples.", "c) She doesn't like apples."],
            "correct_answers": ["c", "she doesn't like apples"],
            "explanation": "The correct sentence is 'She doesn't like apples.' 'Doesn't' is used with third person singular and should be followed by the base form of the verb."
        },
        {
            "question": "Which sentence is in the past perfect tense?",
            "options": ["a) I am eating dinner.", "b) I had eaten dinner before she arrived.", "c) I will eat dinner."],
            "correct_answers": ["b", "i had eaten dinner before she arrived"],
            "explanation": "The past perfect tense is 'had + past participle'. It's used to describe an action that was completed before another action in the past."
        },
        {
            "question": "Identify the correct conditional sentence:",
            "options": ["a) If I will see him, I will tell him.", "b) If I see him, I will tell him.", "c) If I saw him, I will tell him."],
            "correct_answers": ["b", "if i see him, i will tell him"],
            "explanation": "The correct first conditional sentence is 'If I see him, I will tell him.' The structure is 'If + present simple, will + base verb'."
        },
        {
            "question": "Choose the correct word to complete the sentence:\nThe movie was ___ than I expected.",
            "options": ["a) good", "b) better", "c) best"],
            "correct_answers": ["b", "better"],
            "explanation": "The correct word is 'better'. When comparing two things, we use the comparative form. Good → Better → Best."
        },
        {
            "question": "Which word is a synonym for 'happy'?",
            "options": ["a) sad", "b) joyful", "c) angry"],
            "correct_answers": ["b", "joyful"],
            "explanation": "A synonym for 'happy' is 'joyful'. Synonyms are words with similar meanings."
        },
        {
            "question": "Identify the sentence with correct punctuation:",
            "options": ["a) She said, 'Hello.'", "b) She said 'Hello'.", "c) She said 'Hello.'"],
            "correct_answers": ["a", "she said, 'hello.'"],
            "explanation": "The correct punctuation is: She said, 'Hello.' Direct speech should be separated with a comma before the quotation."
        },
        {
            "question": "Fill in the blank with the correct adjective form:\nShe has a ___ voice.",
            "options": ["a) beauty", "b) beautify", "c) beautiful"],
            "correct_answers": ["c", "beautiful"],
            "explanation": "The correct adjective form is 'beautiful'. Adjectives describe nouns, and 'voice' is a noun that needs description."
        },
        {
            "question": "Choose the correct adverb:\nHe ran ___ to catch the bus.",
            "options": ["a) quick", "b) quickly", "c) quickness"],
            "correct_answers": ["b", "quickly"],
            "explanation": "The correct adverb is 'quickly'. Adverbs describe verbs, and 'ran' is a verb that needs description of how the action was performed."
        },
        {
            "question": "What is the abstract noun for 'know'?",
            "options": ["a) knowing", "b) knowledge", "c) known"],
            "correct_answers": ["b", "knowledge"],
            "explanation": "The abstract noun for 'know' is 'knowledge'. Abstract nouns represent ideas, qualities, or states rather than concrete objects."
        },
        {
            "question": "Identify the correct passive voice sentence:",
            "options": ["a) The cake was eaten by the children.", "b) The children ate the cake.", "c) The children have eaten the cake."],
            "correct_answers": ["a", "the cake was eaten by the children"],
            "explanation": "The correct passive voice sentence is 'The cake was eaten by the children.' In passive voice, the subject receives the action."
        }
    ]
    
    for i, q in enumerate(questions):
        print_colored(f"Question {i+1}:", Fore.MAGENTA, Style.BRIGHT)
        score, correct = ask_question(q["question"], q["options"], q["correct_answers"], q["explanation"], score)
        if not correct and i < len(questions) - 1:
            print_colored("Don't worry! Let's try the next one.", Fore.YELLOW)
    
    return score

def level_4(score):
    """Level 4: Expert English Mastery"""
    print_header("LEVEL 4: EXPERT ENGLISH MASTERY", 4)
    print_progress(4, score, 29)
    type_effect("Wow! You've reached the expert level. Prepare for a challenge...", Fore.GREEN)
    
    questions = [
        {
            "question": "Which sentence contains a dangling modifier?",
            "options": ["a) Running quickly, the finish line was crossed.", "b) While eating dinner, the phone rang.", "c) After studying all night, the exam was easy."],
            "correct_answers": ["a", "running quickly, the finish line was crossed"],
            "explanation": "The sentence with a dangling modifier is 'Running quickly, the finish line was crossed.' The modifier 'running quickly' doesn't logically modify any word in the sentence."
        },
        {
            "question": "Identify the sentence with correct subject-verb agreement:",
            "options": ["a) Neither of the books are interesting.", "b) Each of the students has completed the assignment.", "c) The team are playing well today."],
            "correct_answers": ["b", "each of the students has completed the assignment"],
            "explanation": "The correct sentence is 'Each of the students has completed the assignment.' 'Each' is singular and requires a singular verb."
        },
        {
            "question": "Which word is misspelled?",
            "options": ["a) accommodate", "b) embarrass", "c) existance"],
            "correct_answers": ["c", "existance"],
            "explanation": "The misspelled word is 'existance'. The correct spelling is 'existence'."
        },
        {
            "question": "Choose the correct sentence:",
            "options": ["a) I should of gone to the store.", "b) I should have gone to the store.", "c) I should have went to the store."],
            "correct_answers": ["b", "i should have gone to the store"],
            "explanation": "The correct sentence is 'I should have gone to the store.' 'Should have' is followed by the past participle 'gone', not 'of' or 'went'."
        },
        {
            "question": "Identify the sentence that uses 'whom' correctly:",
            "options": ["a) Whom is coming to the party?", "b) To whom should I address this letter?", "c) Whom did you give the book to?"],
            "correct_answers": ["b", "to whom should i address this letter"],
            "explanation": "The correct usage is 'To whom should I address this letter?' 'Whom' is used as the object of a verb or preposition."
        },
        {
            "question": "Which sentence is grammatically correct?",
            "options": ["a) Me and him went to the store.", "b) He and I went to the store.", "c) Him and me went to the store."],
            "correct_answers": ["b", "he and i went to the store"],
            "explanation": "The correct sentence is 'He and I went to the store.' When subjects of a sentence, use subjective pronouns (I, he, she, etc.)."
        },
        {
            "question": "Choose the correct word pair:",
            "options": ["a) affect/effect", "b) compliment/complement", "c) principle/principal"],
            "correct_answers": ["a", "affect/effect"],
            "explanation": "All pairs are correct, but 'affect/effect' is the most commonly confused. 'Affect' is usually a verb (to influence), and 'effect' is usually a noun (a result)."
        },
        {
            "question": "Identify the sentence with the correct use of the subjunctive mood:",
            "options": ["a) If I was you, I would study more.", "b) I wish I was taller.", "c) If I were you, I would study more."],
            "correct_answers": ["c", "if i were you, i would study more"],
            "explanation": "The correct subjunctive form is 'If I were you, I would study more.' The subjunctive uses 'were' for all subjects in hypothetical situations."
        },
        {
            "question": "Which sentence demonstrates correct parallel structure?",
            "options": ["a) She likes cooking, jogging, and to read.", "b) She likes cooking, jogging, and reading.", "c) She likes to cook, jogging, and reading."],
            "correct_answers": ["b", "she likes cooking, jogging, and reading"],
            "explanation": "The sentence with correct parallel structure is 'She likes cooking, jogging, and reading.' All items in the list are gerunds (-ing forms)."
        },
        {
            "question": "Choose the correctly punctuated sentence:",
            "options": ["a) The man, who is my uncle, is waiting outside.", "b) The man who is my uncle is waiting outside.", "c) The man, who is my uncle is waiting outside."],
            "correct_answers": ["a", "the man, who is my uncle, is waiting outside"],
            "explanation": "The correctly punctuated sentence is 'The man, who is my uncle, is waiting outside.' The clause 'who is my uncle' is non-restrictive and needs commas."
        }
    ]
    
    for i, q in enumerate(questions):
        print_colored(f"Question {i+1}:", Fore.MAGENTA, Style.BRIGHT)
        score, correct = ask_question(q["question"], q["options"], q["correct_answers"], q["explanation"], score)
        if not correct and i < len(questions) - 1:
            print_colored("This is tough stuff! Let's try the next one.", Fore.YELLOW)
    
    return score

def level_5(score):
    """Level 5: Master English Linguistics"""
    print_header("LEVEL 5: MASTER ENGLISH LINGUISTICS", 5)
    print_progress(5, score, 39)
    type_effect("Incredible! You've reached the highest level of English mastery...", Fore.GREEN)
    
    questions = [
        {
            "question": "Identify the sentence with correct use of the past subjunctive:",
            "options": ["a) I wish I was there yesterday.", "b) I wish I had been there yesterday.", "c) I wish I would be there yesterday."],
            "correct_answers": ["b", "i wish i had been there yesterday"],
            "explanation": "The correct past subjunctive form is 'I wish I had been there yesterday.' The past subjunctive uses 'had + past participle' for wishes about the past."
        },
        {
            "question": "Which sentence correctly uses a gerund phrase as the subject?",
            "options": ["a) To swim in the ocean is my favorite activity.", "b) Swimming in the ocean is my favorite activity.", "c) Swim in the ocean is my favorite activity."],
            "correct_answers": ["b", "swimming in the ocean is my favorite activity"],
            "explanation": "The correct sentence is 'Swimming in the ocean is my favorite activity.' A gerund (verb + -ing) can function as a noun and serve as the subject of a sentence."
        },
        {
            "question": "Identify the sentence with correct use of 'whom' in a relative clause:",
            "options": ["a) The person whom we met yesterday is a famous author.", "b) The person who we met yesterday is a famous author.", "c) The person which we met yest                                if lvl2q1 in ans:
                                    print(f'\033[34m{lvl2_user_score}1\033[0m')
                                    lvl2q2 = input('One word is spelled incorrectly. Spot it.\nfreind, school, book\n').lower()
                                    if lvl2q2 in ans:
                                        print(f'\033[34m{lvl2_user_score}2\033[0m')
                                        lvl2q3 = input('Give the opposite word.\ntall → ?\n').lower()
                                        if lvl2q3 in ans:
                                            print(f'\033[34m{lvl2_user_score}3\033[0m')
                                            lvl2q4 = input('Find the synonym for the given word.\nHappy → (a) sad (b) glad (c) angry\n ').lower()
                                        elif lvl2q3 not in ans:
                                            print(f'Oops! The correct answer is\033[1;32mshort\033[0m')
                                        else:
                                            print(Invalid)
                                    elif lvl2q2 not in ans:
                                        print(f'Oops! The correct answer is\033[1;32mfreind\033[0m')
                                    else:
                                        print(Invalid)
                                elif lvl2q1 not in ans:
                                    print(f'Oops! The correct answer is\033[1;32mI drink coffee in the morning\033[0m')
                                else:
                                    print(Invalid)
                            elif level2 == 'MAYBE LATER':
                                print('Aight! Maybe next time!')
                            else:
                                print(Invalid)
                        elif question5 not in ans:
                            print(f'Oops! The correct answer is b) \033[1;32went\033[0m')
                        else:
                            print(Invalid)
                    elif question4 not in ans:
                        print(f'Oops! The correct answer is b) \033[1;32drinks\033[0m')
                    else:
                        print(Invalid)
                elif question3 not in ans:
                    print(f'Oops! The correct answer is b) \033[1;32sang\033[0m')
                else:
                    print(Invalid)
            elif question2 not in ans:
                print(f'Oops! The correct answer is c) \033[1;32mgo\033[0m')
            else:
                print(Invalid)
        elif question1 not in ans:
            print('Oops! The correct answer is b) \033[1;32mrises\033[0m ')
        else:
            print(Invalid)
    elif ready_check == 'NO':
        print(f'Okay! Come Back When You Are Ready!!')
    else:
        print(Invalid)
elif wanna_play == 'NO':
    print('Okay Next Time!')
else:
    print(Invalid)

input("Press Enter to exit...")
