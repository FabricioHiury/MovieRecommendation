# 🎬 Movie Recommendation System

A Django-based movie recommendation system that utilizes collaborative filtering techniques to suggest movies to users based on their preferences.

## 📁 Project Structure

```
MovieRecommendation/
├── MovieRecomendation/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── recommendations/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Recomendation-Service.ipynb
└── README.md
```

## 🚀 Features

- **User-Based Collaborative Filtering**: Recommends movies based on user similarity.
- **Django Framework**: Utilizes Django for rapid development and clean design.
- **Dockerized Setup**: Easily deployable using Docker and Docker Compose.
- **Jupyter Notebook**: Includes a notebook for exploratory data analysis and model prototyping.

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Docker & Docker Compose (optional for containerized setup)

### Steps

1. **Clone the repository**:

```bash
git clone https://github.com/FabricioHiury/MovieRecommendation.git
cd MovieRecommendation
```

2. **Create a virtual environment and activate it**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Apply migrations**:

```bash
python manage.py migrate
```

5. **Run the development server**:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

## 🐳 Docker Deployment

1. **Build and run the containers**:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8000/`.

## 📊 Jupyter Notebook

The `Recomendation-Service.ipynb` notebook provides an exploratory analysis and demonstrates the collaborative filtering approach used in the recommendation system.
