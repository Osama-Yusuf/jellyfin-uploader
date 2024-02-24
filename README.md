# jellyfin-uploader
A simple, easy-to-use and self-hosted jellyfin media uploader straight to your jellyfin volume folders.
Upload media from anywhere on your device or from other devices on your network or you can expose it and upload media from anywhere in the world (Not recommended, unless you know what you're doing).

## ⭐ Features

- Upload videos straight to jellyfin volume
- Selecting which folder inside the jellyfin volume do you want to save (movies, series, courses, etc)
- Uploading progres bar

## 🔧 How to Install

Requirements:
- [Docker](https://docs.docker.com/engine/install/) 
- [Docker Compose](https://docs.docker.com/compose/install/) (Optional)

### Basic
- To run the jellyfin uploader on top of docker just clone the repo and deploy it with docker-compose as follows:
    ```bash
        git clone https://github.com/Osama-Yusuf/jellyfin-uploader.git
        cd jellyfin-uploader
        docker-compose up -d --build
    ```
jellyfin-uploader is now running on http://localhost:5005