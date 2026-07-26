# Movie Recommender System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Machine%20Learning-Recommendation-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker">
</p>

<p align="center">
An intelligent Movie Recommendation System built using Machine Learning, Streamlit, Docker, and the TMDB API.
</p>

---

## About the Project

Finding the perfect movie to watch can be difficult with thousands of available options. This project helps users discover movies similar to their favorites using a **Content-Based Recommendation System**.

The recommendation engine analyzes movie metadata and calculates similarity scores to suggest the five most relevant movies. Movie posters are fetched dynamically from **The Movie Database (TMDB) API**, providing an engaging and interactive user experience.

---

## Features

- Content-Based Movie Recommendation
- Search from thousands of movies
- Machine Learning recommendation engine
- Cosine Similarity based recommendations
- Live movie posters using TMDB API
- Interactive Streamlit UI
- Docker Support
- Deployment Ready

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| NLP | CountVectorizer |
| Similarity | Cosine Similarity |
| Web Framework | Streamlit |
| API | TMDB API |
| Deployment | Docker |
| Version Control | Git & GitHub |

---

## Project Structure

```text
Movie-Recommender/
│
├── app.py
├── similarity.pkl
├── movie_dict.pkl
├── requirements.txt
├── Dockerfile
```

---

## How It Works

1. Load the movie dataset.
2. Load the pre-computed similarity matrix.
3. User selects a movie.
4. Find similar movies using cosine similarity.
5. Fetch posters through the TMDB API.
6. Display recommendations on the Streamlit web app.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/ankit70808/Movie-Recommender.git
```

```bash
cd Movie-Recommender
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## Run with Docker

Pull the image

```bash
docker pull ankit70808/movie-recommender .
```

Run the container

```bash
docker run -p 8501:8501 ankit70808/movie-recommender
```

Visit

```
http://localhost:8501
```

---

## Machine Learning Workflow

```
Movie Dataset
      │
      ▼
Feature Engineering
      │
      ▼
CountVectorizer
      │
      ▼
Feature Vectors
      │
      ▼
Cosine Similarity Matrix
      │
      ▼
Top 5 Similar Movies
      │
      ▼
TMDB API
      │
      ▼
Movie Posters
```

---

## Future Enhancements

- User Login
- Collaborative Filtering
- Hybrid Recommendation System
- Personalized Recommendations
- Movie Trailers
- IMDb Ratings
- Watchlist
- Genre Filtering
- Cloud Deployment

---

## What I Learned

- Building Recommendation Systems
- Feature Engineering
- Natural Language Processing
- Cosine Similarity
- Streamlit Development
- REST API Integration
- Docker Containerization
- End-to-End ML Deployment
- Git & GitHub Workflow

---

## Contributing

Contributions are always welcome.

```bash
git checkout -b feature-name
git commit -m "Added new feature"
git push origin feature-name
```

Then create a Pull Request.

---

## Author

**Ankit Kumar**

- GitHub: https://github.com/ankit70808
- LinkedIn: https://www.linkedin.com/in/ankit-kumar-9553a0372


---

<p align="center">
Made using Python, Machine Learning, Streamlit & Docker
</p>
