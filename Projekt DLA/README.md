# Generowanie fraktali 2D za pomocą symulacji [Diffusion-limited aggregation](https://en.wikipedia.org/wiki/Diffusion-limited_aggregation)

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
git clone https://github.com/wmakoss/python.git
cd python/Projekt\ DLA/
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

## Przykładowe wygenerowane fraktale:
### Przykład 1:<br />
![Przyklad 1](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla1.png?raw=true)
### Przykład 2:<br />
![Przyklad 2](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla2.png?raw=true)
### Przykład 3:<br />
![Przyklad 3](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla3.png?raw=true)
### Przykład 4:<br />
![Przyklad 4](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla4.png?raw=true)
### Przykład 5:<br />
![Przyklad 5](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla5.png?raw=true)
### Przykład 6:<br />
![Przyklad 6](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla6.png?raw=true)
### Przykład 7:<br />
![Przyklad 7](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla7.png?raw=true)
### Przykład 8:<br />
![Przyklad 8](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla8.png?raw=true)
### Przykład 9:<br />
![Przyklad 9](https://github.com/wmakoss/python/blob/main/Projekt%20DLA/dla9.png?raw=true)
