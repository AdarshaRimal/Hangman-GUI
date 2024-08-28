import random
import tkinter as tk
from tkinter import messagebox
import hangman_stages
import hangman_word


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.chosen_word = random.choice(hangman_word.word_list)
        self.lives = 6
        self.game_over = False
        self.display = ["_" for _ in self.chosen_word]

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=400, height=100)
        self.canvas.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.label_word = tk.Label(self.root, text=" ".join(self.display), font=('Helvetica', 18))
        self.label_word.grid(row=1, column=0, columnspan=3, pady=10)

        self.entry_guess = tk.Entry(self.root, font=('Helvetica', 16), width=5)
        self.entry_guess.grid(row=2, column=1, pady=10)

        self.btn_guess = tk.Button(self.root, text="Guess", command=self.make_guess, font=('Helvetica', 14))
        self.btn_guess.grid(row=3, column=0, pady=10)

        self.btn_reset = tk.Button(self.root, text="Reset", command=self.reset_game, font=('Helvetica', 14))
        self.btn_reset.grid(row=3, column=2, pady=10)

        self.label_lives = tk.Label(self.root, text=f"Lives: {self.lives}", font=('Helvetica', 14))
        self.label_lives.grid(row=4, column=0, columnspan=3, pady=10)

        self.label_stage = tk.Label(self.root, text=hangman_stages.stages[self.lives], font=('Courier', 12))
        self.label_stage.grid(row=5, column=0, columnspan=3, pady=10)

    def make_guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)

        if guess in self.display:
            messagebox.showinfo("Hangman", f"You've already guessed {guess}")
            return

        if guess in self.chosen_word:
            for position in range(len(self.chosen_word)):
                if self.chosen_word[position] == guess:
                    self.display[position] = guess
            self.label_word.config(text=" ".join(self.display))
        else:
            self.lives -= 1
            self.label_lives.config(text=f"Lives: {self.lives}")
            self.label_stage.config(text=hangman_stages.stages[self.lives])
            messagebox.showinfo("Hangman", f"Incorrect guess. The letter {guess} is not in the word.")

        if "_" not in self.display:
            self.game_over = True
            messagebox.showinfo("Hangman", "You win!")
            self.reset_game()

        if self.lives == 0:
            self.game_over = True
            messagebox.showinfo("Hangman", f"You lose! The word was: {self.chosen_word}")
            self.reset_game()

    def reset_game(self):
        self.chosen_word = random.choice(hangman_word.word_list)
        self.lives = 6
        self.game_over = False
        self.display = ["_" for _ in self.chosen_word]
        self.label_word.config(text=" ".join(self.display))
        self.label_lives.config(text=f"Lives: {self.lives}")
        self.label_stage.config(text=hangman_stages.stages[self.lives])


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
