# 🕹️ Hangman Game (Python Terminal Edition)

This is a Python-based command-line Hangman game. It provides a fun way to guess words using hints. The game supports both limited rounds and an endless mode until you fail.

---

## 📂 File Overview

- `hangman.py` – The complete game script.

---

## 🧠 Game Concept

The classic **Hangman** game is where a player tries to guess a hidden word one letter at a time. For each incorrect guess, the player loses a life. After 6 wrong letter guesses, the game ends for that word.

---

## 🛠️ Features

- 🔢 Two game modes:
  - **Limited Mode**: You choose how many rounds to play.
  - **Unlimited Mode**: Keep playing until you make a wrong full-word guess.
- 💡 Hints for each word.
- ✅ Accepts both letter and full-word guesses.
- 🧮 Score tracking.
- 🧠 Over 90+ curated words with hints across categories.

---

## 🖥️ Requirements

- Python 3.x
- No external libraries needed.

---

## 🚀 How to Run

1. Clone or download the project:

```bash
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
```

2. Run the game:

```bash
python hangman.py
```

---

## 🎮 How to Play

### Step 1: Choose Mode

When you run the game, you will be asked:

```text
1: Limited (Play a specific number of words)
2: Unlimited (Play until you lose)
```

### Step 2: Guessing

- For each word:
  - You'll see the word as blanks (`_ _ _ _`)
  - A **hint** is provided.
  - You have 6 chances to guess incorrectly **letter by letter**.
  - You can also guess the **entire word** at any time.
  - Guessing the word correctly ends the round and gives you 1 point.

---

## 🧪 Example

```text
_ _ _ _ _
Hint: A natural flowing water body

Enter a letter: r
_ _ _ _ r

Enter a letter: e
_ _ _ e r

Enter the word: river
You have guessed the correct word...
```

---

## 📊 Scoring

- +1 point for each correct word guessed.
- Game ends (in unlimited mode) after a failed **word guess**.
- Limited mode ends after your chosen number of rounds.

---

## ⚠️ Edge Cases Handled

- Input validation (only numbers when choosing mode)
- Empty guesses
- Full-word and letter-wise logic separation
- Avoids repeating words by removing used ones from the list

---

## 📌 Possible Improvements

- Add a GUI with `tkinter` or `pygame`
- Leaderboard support
- Difficulty levels (easy/medium/hard word sets)
- Hangman ASCII drawing for visual effect

---

## 👤 Author

- **Pavan Sathvik**
- Project type: Educational / Beginner Python project

---

## 📝 License

This project is open source and free to use.
