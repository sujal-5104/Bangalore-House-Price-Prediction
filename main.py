import os
import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, request


# =========================================================
# FLASK APP
# =========================================================

app = Flask(__name__)


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================================================
# FILE PATHS
# =========================================================

DATA_FILE = os.path.join(BASE_DIR, "Cleaned_data.csv")
MODEL_FILE = os.path.join(BASE_DIR, "RidegModel.pkl")


# =========================================================
# LOAD DATA
# =========================================================

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(
        "Cleaned_data.csv not found. "
        "Please put Cleaned_data.csv in the same folder as main.py."
    )

data = pd.read_csv(DATA_FILE)


# =========================================================
# CHECK LOCATION COLUMN
# =========================================================

if "location" not in data.columns:
    raise ValueError(
        "The column 'location' was not found in Cleaned_data.csv."
    )


# =========================================================
# GET LOCATIONS
# =========================================================

locations = sorted(
    data["location"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(
        "RidegModel.pkl not found. "
        "Please put RidegModel.pkl in the same folder as main.py."
    )

with open(MODEL_FILE, "rb") as file:
    model = pickle.load(file)

print("========================================")
print("RidegModel.pkl loaded successfully!")
print(f"Locations loaded: {len(locations)}")
print("========================================")


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/", methods=["GET"])
def home():

    return render_template(
        "index.html",
        location=locations,
        prediction_text=None
    )


# =========================================================
# PREDICT HOUSE PRICE
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # -------------------------------------------------
        # GET FORM VALUES
        # -------------------------------------------------

        location = request.form.get(
            "location",
            ""
        ).strip()

        bhk = float(
            request.form.get(
                "bhk",
                0
            )
        )

        total_sqft = float(
            request.form.get(
                "total_sqft",
                0
            )
        )

        bath = float(
            request.form.get(
                "bath",
                0
            )
        )

        balcony = float(
            request.form.get(
                "balcony",
                0
            )
        )


        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        if not location:
            raise ValueError(
                "Please select a location."
            )

        if bhk <= 0:
            raise ValueError(
                "BHK must be greater than 0."
            )

        if total_sqft <= 0:
            raise ValueError(
                "Total area must be greater than 0."
            )

        if bath <= 0:
            raise ValueError(
                "Bathroom must be greater than 0."
            )

        if balcony < 0:
            raise ValueError(
                "Balcony cannot be negative."
            )


        # -------------------------------------------------
        # CREATE INPUT DATAFRAME
        # -------------------------------------------------

        input_data = pd.DataFrame({
            "location": [location],
            "total_sqft": [total_sqft],
            "bath": [bath],
            "balcony": [balcony],
            "bhk": [bhk]
        })


        print("\nInput data:")
        print(input_data)


        # -------------------------------------------------
        # MAKE PREDICTION
        # -------------------------------------------------

        prediction = model.predict(input_data)


        # -------------------------------------------------
        # CONVERT PREDICTION TO NUMBER
        # -------------------------------------------------

        predicted_price = float(
            np.asarray(prediction).ravel()[0]
        )


        # -------------------------------------------------
        # FORMAT RESULT
        # -------------------------------------------------

        prediction_text = (
            f"🏠 Estimated House Price: "
            f"₹ {predicted_price:.2f} Lakhs"
        )


        print(f"Prediction: {predicted_price:.2f} Lakhs")


        # -------------------------------------------------
        # SHOW RESULT
        # -------------------------------------------------

        return render_template(
            "index.html",
            location=locations,
            prediction_text=prediction_text
        )


    except ValueError as e:

        error_message = (
            f"Prediction Error: {str(e)}"
        )

        return render_template(
            "index.html",
            location=locations,
            prediction_text=error_message
        )


    except Exception as e:

        error_message = (
            f"Prediction Error: {str(e)}"
        )

        print(error_message)

        return render_template(
            "index.html",
            location=locations,
            prediction_text=error_message
        )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    print("\n========================================")
    print("Bangalore House Price Prediction")
    print("========================================")
    print("Server starting...")
    print("Open: http://127.0.0.1:5001")
    print("========================================\n")

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5001
    )