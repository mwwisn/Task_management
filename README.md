# Task_Management

Aplikacja do zarządzania zadaniami oparta na Django i Django REST Framework.

## Opis

**Task_Management** to aplikacja serwerowa umożliwiająca tworzenie i zarządzanie zadaniami — w tym przypisywanie użytkowników, aktualizację statusów oraz śledzenie historii zmian.

Projekt wykorzystuje:

- Django 5
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- Gunicorn (serwer produkcyjny)

---

## Technologie

- **Backend**: Django, Django REST Framework  
- **Baza danych**: PostgreSQL  
- **Środowisko uruchomieniowe**: Docker, Docker Compose  
- **Serwer aplikacji**: Gunicorn  

---

## Wymagania

- Docker
- Docker Compose

---

## Instalacja i uruchomienie

### 1. Zbuduj kontenery i uruchom aplikację

```bash
docker-compose build
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose up
```

### Aplikacja będzie dostępna pod adresem:

http://127.0.0.1:8000/

### Testowanie
## aby uruchomic testy
```bash
docker-compose run --rm app sh -c "python manage.py test"
```


### Przykładowe użycie API

### Rejestracja użytkownika

## URL: /api/user/create/

Metoda: POST

Typ danych: multipart/form-data

### Uwierzytelnienie (token)

## URL: /api/user/token/

Metoda: POST

Typ danych: application/x-www-form-urlencoded

### Operacje na zadaniach

### Edycja zadania

## URL: /api/task/tasks/{id}/

Metoda: PATCH

Typ danych: application/json


### Wyświetlenie szczegółów zadania

## URL: /api/task/tasks/{id}/

Metoda: GET

### Filtrowanie zadań

## URL: /api/task/tasks/

Metoda: GET

Możliwości filtrowania: po id, nazwie, opisie, statusie, przypisanym użytkowniku

### Historia zmian zadania

## URL: /api/task/tasks/{id}/history/

Metoda: GET

Opis: Pozwala sprawdzić, jak zmieniały się pola zadania w czasie.

### Usuwanie zadania
## URL: /api/task/tasks/{id}/

Metoda: DELETE
