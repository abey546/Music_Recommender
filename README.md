# Music Recommendation System

![Project Banner](https://via.placeholder.com/800x300?text=Music+Recommendation+System)

## Overview

The Music Recommendation System is a web application designed to provide users with personalized music recommendations based on their preferences. By integrating with the Spotify API, the application fetches and displays song recommendations, allowing users to discover new music tailored to their tastes.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Architecture Diagram](#architecture-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication**: Secure login and registration system using Flask-Login.
- **Personalized Recommendations**: Fetches music recommendations from the Spotify API based on user preferences.
- **Responsive Design**: Compatible with mobile devices for a seamless user experience.

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (using SQLAlchemy for ORM)
- **Authentication**: Flask-Login
- **API Integration**: Spotipy (Spotify API)
- **Deployment**: Heroku (using Gunicorn as the WSGI server)
- **Version Control**: Git/GitHub

## Architecture Diagram

![Architecture Diagram](https://via.placeholder.com/800x300?text=Architecture+Diagram)

## Installation

To get a local copy up and running, follow these steps:

1. **Clone the repository**:
    ```bash
    git https://github.com/abey546/Music_recommender.git
    cd Music_recommender
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    flask shell
    from website import create_app, db
    app = create_app()
    db.create_all(app=app)
    exit()
    ```

5. **Run the application**:
    ```bash
    flask run
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Register for a new account or log in with existing credentials.
3. Enter a song title to receive personalized music recommendations.
4. View the recommendations, including song titles, artists, and cover images.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Your Name**: [LinkedIn](https://www.linkedin.com/in/abey-abdi) | [GitHub](https://github.com/abey546)
- **Project Repository**: [GitHub](https://github.com/abey546/Music_recommender.git)
- **Deployed Project**: [Heroku](http://yourproject.herokuapp.com/)

---

Thank you for checking out the Music Recommendation System! We hope it helps you discover your next favorite song.


