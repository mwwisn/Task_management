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

![image](https://github.com/user-attachments/assets/6a78e35d-0516-4ef5-97e0-f002bbcbb703)

### Uwierzytelnienie (token)

## URL: /api/user/token/

Metoda: POST

Typ danych: application/x-www-form-urlencoded

![image](https://github.com/user-attachments/assets/72b74861-bf5a-433c-9e2a-fdeb93df89de)

pamietaj o wpisaniu tokenu w to miejsce aby oblokowac dostep do sekcji task

![image](https://github.com/user-attachments/assets/c94ae84f-ac8a-4e4f-b3d7-1b6a1479bdf9)

### Operacje na zadaniach

### Tworzenie zadania

## URL: /api/task/tasks/

Metoda: Post

Typ danych" application/json

![image](https://github.com/user-attachments/assets/0e074b56-fa99-4ccf-aea7-7bc19c1297f5)

### Edycja zadania

## URL: /api/task/tasks/{id}/

Metoda: PATCH

Typ danych: application/json

![image](https://github.com/user-attachments/assets/f860803e-0908-4f5b-8bf4-fa17ecb62e4b)


### Wyświetlenie szczegółów zadania

## URL: /api/task/tasks/{id}/

Metoda: GET

![image](https://github.com/user-attachments/assets/0723f669-fb8c-41fd-ab35-f874a00e2f9a)

### Filtrowanie zadań

## URL: /api/task/tasks/

Metoda: GET

Możliwości filtrowania: po id, nazwie, opisie, statusie, przypisanym użytkowniku

![image](https://github.com/user-attachments/assets/e3112059-634e-4a2e-96c6-7812030aad29)

### Historia zmian zadania

## URL: /api/task/tasks/{id}/history/

Metoda: GET

Opis: Pozwala sprawdzić, jak zmieniały się pola zadania w czasie.
![image](https://github.com/user-attachments/assets/12077aaa-c514-40c9-a5c5-14e45b7dc99b)

### Usuwanie zadania
## URL: /api/task/tasks/{id}/

Metoda: DELETE

![image](https://github.com/user-attachments/assets/5915db0e-b20a-4ec6-8759-71f7aac1a4e4)

