# Django Blog Project

## Overview
This project is a simple blog application built using Django. It includes features for user authentication, blog post management, and profile management. Users can register, log in, log out, and manage their profiles. Authenticated users can create, view, and manage blog posts.

---

## Features
1. **User Authentication**:
   - User registration with email validation.
   - Login and logout functionality.
   - Profile management for authenticated users.

2. **Blog Management**:
   - Create, view, and manage blog posts.
   - Posts include a title, content, author, and published date.

3. **Profile Management**:
   - View and edit user profiles.
   - Optional fields like bio and profile picture.

4. **Static and Template Integration**:
   - Custom HTML templates for authentication and blog pages.
   - Static files (CSS, JavaScript) for styling and interactivity.

5. **Comment System**:
   - Authenticated users can add comments to blog posts.
   - Comment authors can edit or delete their comments.
   - Comments are displayed under the corresponding blog post.

---

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- Django installed (`pip install django`).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Blackburn0/Alx_DjangoLearnLab.git
   cd django_blog

---

## Comment System

### Features
- Authenticated users can add comments to blog posts.
- Comment authors can edit or delete their comments.
- Comments are displayed under the corresponding blog post.

### How to Use
1. Navigate to a blog post detail page.
2. If logged in, use the comment form to add a comment.
3. Edit or delete your comments using the provided links.

### Permissions
- Only authenticated users can add comments.
- Only the comment author can edit or delete their comments.