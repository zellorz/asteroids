# Asteroids

A classic Asteroids-style arcade game written in Python with Pygame. You pilot a triangular ship in an endless field of asteroids, shoot them to split them into smaller pieces, and try not to collide with any.

Built as a learning project while working through the Asteroids exercise in boot.dev's Python course, then organised and cleaned up by me.

## Features

- Ship with rotation, thrust and a rate-limited shot
- Randomly spawning asteroids of three sizes that split into smaller ones when hit
- Circle-based collision detection
- Game over on collision with an asteroid
- Frame-rate independent movement (delta time, 60 FPS cap)
- Gameplay values (speeds, radii, spawn rate) kept in a single `constants.py`

## Controls

| Key | Action |
| --- | --- |
| `A` / `D` | Rotate left / right |
| `W` / `S` | Move forward / backward |
| `Space` | Shoot |

## Run it

Requires Python 3.10+.

```bash
git clone https://github.com/zellorz/asteroids.git
cd asteroids
python -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

On Linux/macOS, use `python3` instead of `python`.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Game loop, sprite groups, collision checks |
| `circleshape.py` | Base class for circular game objects |
| `player.py` | Ship: movement, rotation, shooting |
| `asteroid.py` | Asteroid behaviour and splitting |
| `asteroidfield.py` | Spawning asteroids at the screen edges |
| `shot.py` | Projectiles |
| `constants.py` | Tunable game settings |

## Ideas for next steps

- Score and lives
- Start and game-over screens
- Sound effects