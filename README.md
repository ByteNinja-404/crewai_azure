# AI Crew using Azure OpenAI Endpoint

## Overview

This project demonstrates the use of **CrewAI** and **Azure OpenAI** services to create an AI-powered agent framework that performs tasks autonomously. By leveraging **CrewAI**, agents are managed and assigned tasks that utilize the power of **Azure's GPT models** to process information, execute actions, and generate responses. This specific example uses CrewAI to create a **Senior Researcher** agent tasked with identifying emerging trends in AI.

---

## Features

- **Azure OpenAI Integration**: Seamlessly interact with Azure's GPT models through the provided API credentials.
- **CrewAI Framework**: Manage AI agents and assign tasks using the CrewAI library, which coordinates actions.
- **Modular Setup**: Environment variables (`.env` file) allow for easy configuration of your system and credentials.
- **Development Tools**: Includes integrated tools for linting, testing, and formatting code.

---

## Prerequisites

Ensure you have the following tools and services available to run this project:

- **Python 3.10 or 3.11**: Ensure Python 3.10.x or 3.11.x is installed. This project does not support Python 3.12.x yet.
- **Poetry**: Poetry is used for dependency management and virtual environment handling.
- **Azure OpenAI API**: You need an active Azure OpenAI API subscription and the necessary API keys.

---

## Setup Instructions

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/yourusername/crewai-azure.git
cd crewai-azure

