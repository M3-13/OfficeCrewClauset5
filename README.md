# Clauset5 – Glamouröser Kleiderschrank-Manager

Ein glamouröser Kleiderschrank-Manager mit Web-GUI im Hollywood-Stil. Benutzer registrieren sich, legen Kleidungsstücke mit Bildern und Kategorien an, durchstöbern ihre Garderobe und kombinieren im Outfit-Creator Einzelteile zu gespeicherten Outfits – alles in einer eleganten Red-Carpet-Optik.

## Tech-Stack

- **Backend**: Python mit FastAPI
- **Datenbank**: SQLite mit SQLAlchemy + Alembic
- **Auth**: JWT (python-jose) + bcrypt
- **File Storage**: Lokales Dateisystem (uploads/)
- **Frontend**: React mit Vite, TypeScript
- **Styling**: Tailwind CSS mit Hollywood-Glamour-Farbpalette
- **Testing**: pytest (Backend), vitest (Frontend)

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Der Vite-Dev-Server startet auf http://localhost:5173 und leitet `/api`-Anfragen an das Backend auf http://localhost:8000 weiter.

## Umgebungsvariablen

| Variable | Beschreibung | Erforderlich |
|---|---|---|
| `JWT_SECRET` | Secret-Key für JWT-Tokens | Ja (kein Default!) |

## API-Endpunkte

### Health

| Methode | Pfad | Beschreibung |
|---|---|---|
| GET | `/api/health` | Health-Check → `{"status": "ok"}` |

### Auth (`/api/auth`)

| Methode | Pfad | Beschreibung |
|---|---|---|
| POST | `/api/auth/register` | Registrierung |
| POST | `/api/auth/login` | Login |
| POST | `/api/auth/logout` | Logout |
| POST | `/api/auth/refresh` | Token-Refresh |

### Kleidungsstücke (`/api/items`)

| Methode | Pfad | Beschreibung |
|---|---|---|
| GET | `/api/items/` | Alle Kleidungsstücke |
| POST | `/api/items/` | Neues Kleidungsstück |
| GET | `/api/items/{id}` | Einzelnes Kleidungsstück |
| PUT | `/api/items/{id}` | Kleidungsstück bearbeiten |
| DELETE | `/api/items/{id}` | Kleidungsstück löschen |

### Outfits (`/api/outfits`)

| Methode | Pfad | Beschreibung |
|---|---|---|
| GET | `/api/outfits/` | Alle Outfits |
| POST | `/api/outfits/` | Neues Outfit |
| GET | `/api/outfits/{id}` | Einzelnes Outfit |
| PUT | `/api/outfits/{id}` | Outfit bearbeiten |
| DELETE | `/api/outfits/{id}` | Outfit löschen |

## Features

- Benutzerregistrierung und -login mit JWT-Authentifizierung
- Kleidungsstücke mit Bildern und Kategorien (Tops, Bottoms, Outerwear, Shoes, Accessories, Dresses)
- Garderoben-Ansicht mit Filter und Suche
- Outfit-Creator zum Kombinieren von Kleidungsstücken
- Outfit-Übersicht mit Bearbeiten und Löschen
- Hollywood-Glamour-Design mit Gold-Akzenten und Burgunderrot
