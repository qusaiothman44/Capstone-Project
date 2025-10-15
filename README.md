# Capstone-Project

# StayStory – Real Traveler Experience Platform

## Project Overview
**StayStory** is a Django-based web application that allows travelers to share and explore genuine experiences from their stays at hotels, hostels, or Airbnb accommodations.  
Users can post reviews, rate places, and upload real photos from their visits, helping others make more informed travel decisions.  

The purpose of StayStory is to create a trustworthy and community-driven space where backpackers and travelers can tell their stories, highlight honest experiences, and discover new places based on authentic reviews rather than marketing.

---

## Core Features
- **User Authentication:** Sign up, log in, and log out using Django’s built-in authentication system.  
- **CRUD for Reviews:** Users can create, edit, and delete their own reviews.  
- **Ratings & Averages:** Each place displays an average rating based on all user reviews.  
- **Photo Uploads:** Option to include real photos of the stay.  
- **Dynamic Pages:** Places and reviews rendered dynamically with Django templates.  
- **Responsive Design:** Clean, consistent, mobile-friendly layout using custom CSS (no frameworks).  

---

## Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS  ,JS
- **Database:** PostgreSQL  
- **Authentication:** Django’s built-in system  

---

## Goal
To develop a complete, responsive full-stack Django web application that demonstrates proficiency in Django models, views, templates, URL routing, and authentication — while solving a real-world problem for travelers seeking trustworthy accommodation reviews.

---





## ERD Diagram



```mermaid
erDiagram
    USER ||--o{ REVIEW : writes
    REVIEW ||--o{ REVIEWIMAGE : contains
    PLACE ||--o{ REVIEW : has
    USER ||--o{ COMMENT : writes
    REVIEW ||--o{ COMMENT : receives

    USER {
        int id PK
        string username
        string email
    }

    PLACE {
        int id PK
        string name
    }

    REVIEW {
        int id PK
        string title
        text description
        int rating
        datetime date_created
        int user_id FK
        int place_id FK
    }

    REVIEWIMAGE {
        int id PK
        string image
        int review_id FK
    }

    COMMENT {
        int id PK
        text content
        datetime date_created
        int user_id FK
        int review_id FK
    }



```````



## User Stories

### Authentication & Permissions
- **As a visitor (not logged in):** I want to view all places and their reviews, so that I can browse content without an account.
- **As a visitor:** I want to see a prompt to log in or sign up when trying to add or edit a review, so that I know I need an account to contribute.
- **As a registered user:** I want to log in securely, so that I can access my account and manage my reviews.
- **As a registered user:** I want to log out easily, so that my account stays protected.

---

### Places & Reviews
- **As a logged-in user:** I want to add a new review for any place, including a rating, comment, price, and photo, so that I can share my experience.
- **As a logged-in user:** I want to edit or delete **only my own reviews**, so that I can manage my content without affecting others.
- **As any user (visitor or logged-in):** I want to see the average rating and total number of reviews for each place, so that I can compare options easily.

---

### Search & Navigation
- **As a user:** I want to search for a place by name or city, so that I can quickly find locations I’m interested in.
- **As a user:** I want clear navigation links, so that I can move easily between pages (Home, Place Detail, Login/Sign Up).

---

### Photos & Visuals
- **As a reviewer:** I want to upload photos of my stay, so that others can see what the place actually looks like.
- **As a visitor:** I want to see user-uploaded photos on the place’s page, so that I can make informed decisions.

---
### Comments

**As a logged-in user:** I want to comment on other users' reviews, so that I can share feedback or ask questions.

**As a review owner:** I want to see comments on my review, so that I can engage with others.

**As any user:** I want to view all comments under a review, sorted by newest first, so that I can follow the discussion easily.

**As a logged-in user:** I want to delete my own comments, so I can manage what I’ve said.

---
%% --- INSTALLATION & SETUP GUIDE ---
flowchart TD
    A[📁 Clone Repository] --> B[💻 Install Dependencies (Pipenv)]
    B --> C[🐘 Setup PostgreSQL Database]
    C --> D[⚙️ Apply Migrations]
    D --> E[🌱 (Optional) Load Demo Data]
    E --> F[🚀 Run Development Server]

    subgraph Steps
    A1["git clone https://github.com/yourusername/StayStory.git"]
    A2["cd StayStory"]
    B1["pipenv install"]
    B2["pipenv shell"]
    C1["CREATE DATABASE staystory_db;"]
    D1["python manage.py makemigrations"]
    D2["python manage.py migrate"]
    E1["python manage.py shell"]
    E2["from staystory_db.load_data import load_data()"]
    E3["load_data()"]
    F1["python manage.py runserver"]
    end

    click A href "https://github.com/yourusername/StayStory" "Open Repository"
