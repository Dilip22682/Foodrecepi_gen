🍳 AI Recipe Generator – Django + Groq (LLaMA 3)

An AI-powered Recipe Generator built using Django that creates unique and creative recipes based on user-provided ingredients.
The application integrates with the Groq API (LLaMA 3 model) to generate intelligent, step-by-step cooking instructions in real time.

🚀 Project Overview

This project allows users to enter ingredients and receive a fully generated recipe that includes:

🍽️ Dish Name

📝 Step-by-step Cooking Instructions

📋 Organized Ingredient Usage

🤖 AI-generated creative combinations

Additionally, the system includes validation logic in the prompt to ensure that if non-food items are entered, the AI responds with:

"Not possible"

instead of generating irrelevant content.

🧠 How It Works

User enters ingredients (comma-separated).

Django view processes the request.

Ingredients are sent to Groq’s OpenAI-compatible endpoint.

The LLaMA 3 (llama3-8b-8192) model generates:

A unique recipe name

Detailed step-by-step instructions

The generated recipe is rendered dynamically on the frontend.

🛠️ Tech Stack

Backend Framework: Django

AI Model: LLaMA 3 via Groq API

API Communication: Python requests

Template Rendering: Django Templates

Security: API key stored securely in settings.py

✨ Key Features

✅ Real-time AI recipe generation

✅ Prompt engineering with food-validation logic

✅ Clean Django architecture (views + utils separation)

✅ API error handling

✅ Secure Bearer token authentication

✅ Dynamic content rendering

📂 Project Architecture

views.py → Handles HTTP request & response

utils.py → Manages Groq AI API integration

templates/ → Displays generated recipe

settings.py → Secure API key configuration

🎯 Learning Outcomes

Through this project, I gained practical experience in:

Integrating LLM APIs with Django

Designing structured AI prompts

Handling external API responses

Implementing secure configuration management

Building real-world AI-powered web applications

🔮 Future Enhancements

Save generated recipes to database

Add user authentication

Recipe rating & favorites system

Nutrition information analysis

Convert to Django REST API version

Docker deployment
