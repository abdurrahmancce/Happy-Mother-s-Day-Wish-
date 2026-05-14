import pyfiglet
import random
import time
import os

# =========================
# COLOR CODES
# =========================
colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m"
}

reset = "\033[0m"

# =========================
# AVAILABLE FONTS
# =========================
fonts = [
    "slant",
    "banner3-D",
    "digital",
    "standard",
    "smscript",
    "big",
    "doom"
]

# =========================
# RANDOM SELECTION
# =========================
selected_font = random.choice(fonts)
selected_color = random.choice(list(colors.keys()))

# =========================
# CLEAR TERMINAL
# =========================
os.system("cls" if os.name == "nt" else "clear")

# =========================
# TITLE
# =========================
title = pyfiglet.figlet_format("Mother's Day", font=selected_font)

# =========================
# DECORATION
# =========================
hearts = "💖 💐 🌸 💕 🌷 💝"

# =========================
# QUOTES
# =========================
quotes = [
    "A mother is your first friend, best friend, forever friend.",
    "Life doesn't come with a manual, it comes with a mother.",
    "Home is wherever Mom is.",
    "Mothers hold their children's hands for a while, but their hearts forever."
]

selected_quote = random.choice(quotes)

# =========================
# PRINT ANIMATION
# =========================
print(colors[selected_color] + hearts + reset)
time.sleep(1)

for line in title.split("\n"):
    print(colors[selected_color] + line + reset)
    time.sleep(0.1)

print(colors["yellow"] + "=" * 70 + reset)

# Typing effect
message = "Happy Mother's Day!"
for char in message:
    print(colors["magenta"] + char + reset, end="", flush=True)
    time.sleep(0.08)

print("\n")

# Quote section
print(colors["cyan"] + f'"{selected_quote}"' + reset)

print(colors["yellow"] + "=" * 70 + reset)

# Footer
print(colors["green"] + "\nMade with ❤️ using Python" + reset)