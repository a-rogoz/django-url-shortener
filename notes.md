# Wytyczne dotyczące aplikacji

## Opis aplikacji
- Stwórz projekt "API w DRF do skracania URLi" - coś w rodzaju URL Shortener, Branded Short Links & Analytics | TinyURL tylko samo API.

## Wymagania
- Funkcjonalność ma być ekstremalnie minimalistyczna, nie chodzi o dodawanie super features
- Testy jednostkowe
- E2E

## Opis implementacji

### Projekt powinien umożliwiać:
- 👉 stworzenie skróconego urla, czyli np. wkładamy
`http://example.com/very-very/long/url/even-longer` w zamian dostajemy krótki url wygenerowany przez API, np `http://localhost:8000/shrt/%5C%60
- 👉 rozwinięcie skróconego urla do oryginalnego, czyli odwrotność poprzedniej operacji.

## Inne
- 🌱 Jak coś nie jest zrozumiałe to improwizuj i krótko opisz co było niejasne i jaka decyzja została podjęta.

- 🔗 Rozwiązanie prześlij jako link do repozytorium na GitHubie.

## Pytania i decyzje
- Czy zwracamy oryginalny URL do warstwy front-endowej i tam przekierowujemy użytkownika, czy od razu przekierowujemy? -> Przekierowujemy użytkownika po stronie back-endu.
- Walidujemy https? -> Tak
