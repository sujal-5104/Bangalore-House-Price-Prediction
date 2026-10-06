# 🏠 Bangalore House Price Prediction

A Machine Learning based web application that predicts house prices in Bangalore based on important property features such as location, BHK, total square feet, number of bathrooms, and balconies.

## 🚀 Project Overview

The Bangalore House Price Prediction project uses Machine Learning to estimate the approximate price of a residential property.

The project provides a simple and user-friendly web interface where users can enter property details and get an estimated house price in Lakhs.

## ✨ Features

* 🏠 Bangalore house price prediction
* 📍 Location selection
* 🛏️ BHK input
* 📐 Total area in square feet
* 🚿 Bathroom selection
* 🌿 Balcony selection
* 🤖 Machine Learning prediction
* 🌐 Flask web application
* 📱 Responsive Bootstrap interface

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* HTML
* CSS
* Bootstrap
* Machine Learning

## 📂 Project Structure

```text
Bangalore-House-Price-Prediction/
│
├── main.py
├── Cleaned_data.csv
├── RidegModel.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Bangalore-House-Price-Prediction.git
```

Open the project folder:

```bash
cd Bangalore-House-Price-Prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python main.py
```

Open your browser and visit:

```text
http://127.0.0.1:5001
```

## 🧠 How It Works

1. The user selects a Bangalore location.
2. The user enters the number of BHK.
3. The user enters the total area in square feet.
4. The user enters the number of bathrooms.
5. The user enters the number of balconies.
6. The Flask application sends the data to the trained Machine Learning model.
7. The model predicts the estimated house price.
8. The predicted price is displayed on the webpage.

## 📊 Input Features

| Feature    | Description                 |
| ---------- | --------------------------- |
| Location   | Bangalore property location |
| BHK        | Number of bedrooms          |
| Total Sqft | Total property area         |
| Bath       | Number of bathrooms         |
| Balcony    | Number of balconies         |

## 🎯 Purpose

This project demonstrates how Machine Learning can be integrated with a Flask web application to create a practical real-world house price prediction system.

## 👨‍💻 Author

**Pranay Padhiyar**

B.Tech Computer Science Engineering
Machine Learning Project
