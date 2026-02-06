from hangman_words import words
import random

# words = ('banana', 'apple', 'cherry', 'orange')
hangman_art = {
                0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\"),}

# print(hangman_art[0])

# for line in hangman_art[6]:
#     print(line)

def display_man(wrong_guesses):
    print('************************')
    for line in hangman_art[wrong_guesses]:
        print(line)
    print('************************')

def display_hint(hint):
    print(' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))

def main():
    answer = random.choice(words)  # words 튜플에서 랜덤한 하나의 단어를 선택
    # print(answer)

    hint = ["_"] * len(answer)
    # print(hint)

    wrong_guesses = 0
    guessed_letters = set()
    is_running =True

    print(answer)

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("문자를 입력해 주세요: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("영문 알파벳 한 글자만 입력해 주세요.")
            continue

        if guess in guessed_letters:
            print(f"{guess}는 이미 입력한 문자입니다.")

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            print("오답입니다. 다시 생각하세요.")
            wrong_guesses += 1

        if "_" not in hint:  # hint에 _가 없으면 True
            display_man(wrong_guesses)
            display_answer(answer)
            print("정답입니다!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("게임 오버! 틀렸어요!")
            is_running = False

if __name__ == '__main__':
    main()
