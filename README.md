# Pancreas Tower Defense

A tower defense where you protect the pancreas from waves of sugary desserts (puddings, caramel...). Made by **Pudim Games** during the Gamerama game jam, November 2013.

## History

- **2 Nov 2013**: first sketch (`pudim3-2`).
- **4 Nov 2013**: towers, enemies and art (`pudim13`).
- **5-6 Nov 2013**: final jam builds (`pudim15`, `pudim16`) and the py2exe build script (`pygame2exe.py`).

## Team

Pudim Games - Fernando Luiz Neme Chibli ([@fershibli](https://github.com/fershibli)) and colleagues from the Digital Games course at Fatec.

## Play in the browser

**[https://fershibli.github.io/pancreas-tower-defense/](https://fershibli.github.io/pancreas-tower-defense/)**

The web version runs the game with pygbag (CPython + pygame-ce compiled to WebAssembly); `web/main.py` is the original loop made async so the browser gets a frame after each `display.update()`. It is rebuilt and published by `.github/workflows/pages.yml` on every push to `main`.

## Releases

Builds are made by GitHub Actions (`.github/workflows/release.yml`) for macOS, Windows and Linux (Python 3.12 + pygame). Push a tag such as `v1.0` (or run the workflow by hand) and the zipped builds are attached to a GitHub release.

To play from source: `python3 pancreas_defense.py`.
