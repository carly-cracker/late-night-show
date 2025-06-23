# Late Show API — Flask Code Challenge

A RESTful API built using Flask for managing guests, episodes, and appearances on a fictional Late Night TV show.

---

## Folder Structure

```
late-show-api/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   └── appearance.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── auth_controller.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   └── appearance_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md
```

---

## Setup Instructions

### 1. Install Dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary python-dotenv flask-bcrypt
pipenv shell
```

### 2. PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE late_show_db;
```

### 3. Environment Configuration

Create a `.env` file and add:

```
DATABASE_URI=postgresql://....
JWT_SECRET_KEY=your_jwt_secret
```

Or configure `server/config.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
```

---

## Run the App

### 1. Initialize and Migrate Database

```bash
export FLASK_APP=server.app:create_app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 2. Seed the Database

```bash
python -m server.seed
```

### 3. Start the Server

```bash
export FLASK_RUN_PORT=5555
flask run
```

The API will run at: `http://localhost:5555/`

---

## Authentication Flow

### 🔸 Register a User
**POST** `/register`

```json
{
  "username": "admin",
  "password": "admin123"
}
```

### 🔸 Login to Get Token
**POST** `/login`

```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response:**
```json
{
  "access_token": "your.jwt.token"
}
```

### 🔸 Use Token in Protected Routes

In Thunder Client or Postman, add this header:

```
Authorization: Bearer <your_token_here>
```

---

## API Routes

| Route | Method | Auth? | Description |
|-------|--------|-------|-------------|
| `/register` | POST | Register a user |
| `/login` | POST | Log in + get JWT |
| `/episodes` | GET |List all episodes |
| `/episodes/<id>` | GET | Get episode + appearances |
| `/episodes/<id>` | DELETE | Delete an episode |
| `/guests` | GET | List guests |
| `/appearances` | POST | Create a guest appearance |

---

## Testing the API

1. Open **Thunder Client** or **Postman**
2. Import the file:  
   `challenge-4-lateshow.postman_collection.json`
3. Use the `/login` endpoint to get your token
4. Add `Authorization: Bearer <token>` in headers for protected routes

---

## Tech Stack

- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL
- Python Dotenv
- Flask-Bcrypt
