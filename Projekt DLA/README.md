# Generowanie fraktali w 2D za pomocą symulacji [Diffusion-limited aggregation](https://en.wikipedia.org/wiki/Diffusion-limited_aggregation)

### Autor: Wojciech Makosiej
---

## Specyfikacja techniczna:

### Program został przetestowany w środowisku:
- Windows 10
- Python 3.8.10
- pip 21.1.1

### Wymagane biblioteki:
- [pygame](https://pypi.org/project/pygame/) 2.1.2
- [pypng](https://pypi.org/project/pypng/) 0.20220715.0

### Jak uruchomić program:
```
pip install -r requirements.txt
python dla.py
```

## Działanie programu:

1. Program wczytuje od użytkownika poniższe wartości:
    - **WINDOW WIDTH** - Szerokość okna i generowanego obrazu png
    - **WINDOW HEIGHT** - Wysokość okna i generowanego obrazu png
    - **POINT SIZE** - Wysokość i szerokość punktów w symulacji
    - **AMOUNT** - Ilość punktów w symulacji
    #### Gdy powyższe wartości nie zostaną wczytane, będą miały wartości domyślne podane poniżej:
    - **WINDOW WIDTH:** 700
    - **WINDOW HEIGHT:** 700
    - **POINT SIZE:** 3
    - **AMOUNT:** 4000 
2. Następnie Przeprowadza symulację wyświetlając na żywo stan symulacji w oknie pygame.
   W trakcie symulacji naciśnięcie na okno spowoduje schowanie/pokazanie zielonych punktów.
3. Po skończeniu symulacji rezultat zostaje zapisany do pliku "dla.png".

## Symulacja przebiega w następujący sposób:

Program losowo rozmieszcza punkty w oknie (Zielone) i jeden punkt na środku okna (czerwony). Następnie wykonuje iteracje aż do momenu gdy każdy zielony punkt zamieni się na czerwony. Każda iteracja polega na losowym ruchu każdego zielonego punktu i sprawdzeniu czy ma kontakt z czerwonym punktem. Jeżeli tak kolor punktu zostaje zmieniony na czerwony.