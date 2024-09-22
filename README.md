# LangChain Demo with Google API

## Overview
This project demonstrates how to integrate LangChain with Google's Gemini Pro model using Streamlit for a simple and interactive web-based interface. The application allows users to input queries, which are processed by a Google Generative AI (Gemini) through LangChain's framework. Responses are generated by the AI model and displayed to the user in real-time.

## Features
- **LangChain Integration**: Utilizes LangChain for prompt creation and output processing.
- **Google Generative AI**: Leverages the `ChatGoogleGenerativeAI` model (Gemini Pro) for high-quality responses.
- **Streamlit Interface**: Provides a simple and user-friendly UI where users can input queries and receive responses.
- **Dynamic Querying**: Users can type any question, and the app uses Google's LLM to generate helpful answers.
- **Environmental Configuration**: API keys for both Google and Langsmith are securely loaded via environment variables using `dotenv`.