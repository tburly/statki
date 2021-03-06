#!/usr/bin/env python3

"""

    Uruchamianie gry.

"""

import tkinter as tk

from statki.gui.interfejs import Interfejs


def main():
    """Uruchom grę."""
    okno_glowne = tk.Tk()
    okno_glowne.title("Statki")
    Interfejs(
        rodzic=okno_glowne,
        kolumny=15,
        rzedy=15
    )  # dopuszczalny rozmiar planszy: 8-26 kolumn x 8-30 rzędów
    okno_glowne.resizable(False, False)
    okno_glowne.mainloop()


if __name__ == "__main__":
    main()
