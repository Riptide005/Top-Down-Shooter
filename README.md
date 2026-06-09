# 2D Top-Down Arena Shooter

A arcade style Top Down Shooter inspired by games like Vampire Survivors and Swarm game mode in League of Legends.

## 🚀 Features

* **Responsive 2D Movement:** Smooth character tracking across axes with normalized diagonal velocity vectors to prevent speed exploitation.
* **Vector-Based Aiming & Rotation:** Dynamic player and projectile rotation tracking using trigonometric angular calculations (`math.atan2`).
* **Dual-Weapon Kit:**
    * **Primary Fire (Bullets):** Straight-line projectiles initialized with precise floating-point trajectories based on the player's last-known facing vector.
    * **Secondary Fire (Explosion Blast):** A dynamic, frame-scaled Area of Effect (AoE) attack with custom pixel-perfect circular distance collision handling.
* **Modular Architecture:** Fully decoupled modules for entity logic (`player.py`, `enemy.py`, `weapons.py`) managed by a central runtime game loop.

## 🎮 Controls

* **Move:** `W` `A` `S` `D` (or Arrow Keys)
* **Shoot Bullets:** `Spacebar` (200ms cooldown)
* **Explosion Blast:** `E` (5-second cooldown tracked via CPU millisecond ticks)

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.12+
* **Libraries:** Pygame, NumPy
* **Version Control:** Managed natively via Git on Ubuntu/Linux terminal

## 💻 Installation & How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/Riptide005/Top-Down-Shooter](https://github.com/Riptide005/Top-Down-Shooter.git)

## 🎨 Credits & Attributions

Special thanks to the creators who provided the visual assets for this project:

* **Player & Enemy Sprites:** Designed by [The Pixel Oasis](https://thepixeloasis.itch.io).
* **Explosion & Bullet Sprites:** Particle sheets created by [BDragon1727](https://bdragon1727.itch.io).
* **Game Concept Inspiration:** Developed as a part of learning experience for OOP guided by Gemini.