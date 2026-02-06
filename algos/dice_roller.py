import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
  1: ("┌─────────┐",
      "│         │",
      "│    ●    │",
      "│         │",
      "└─────────┘"),  
  2: ("┌─────────┐",
      "│ ●       │",
      "│         │",
      "│       ● │",
      "└─────────┘"),
  3: ("┌─────────┐",
      "│ ●       │",
      "│    ●    │",
      "│       ● │",
      "└─────────┘"),
  4: ("┌─────────┐",
      "│ ●     ● │",
      "│         │",
      "│ ●     ● │",
      "└─────────┘"),
  5: ("┌─────────┐",
      "│ ●     ● │",
      "│    ●    │",
      "│ ●     ● │",
      "└─────────┘"),
  6: ("┌─────────┐",
      "│ ●     ● │",
      "│ ●     ● │",
      "│ ●     ● │",
      "└─────────┘"),
}


dice = []
total = 0

num_of_dice = int(input('주사위를 몇 번 던질건가요?'))

# range(start, stop, step)
# randint(start, stop): start에서 stop미만의 랜덤 숫자 반환
for dic in range(num_of_dice):
    dice.append(random.randint(1, 6))

print(dice)

# for dic in range(num_of_dice):
#     for line in dice_art.get(dice[dic]):
#         print(line)  

for line  in range(5):
    for dic in dice:
        print(dice_art.get(dic)[line], end=" ")  # end=""는 줄바꿈을 하지 않음
    print()

for dic in dice:
    total += dic

print(f"주사위 값의 총합은: {total}")
