# Mumbai House Price Prediction


## Overview

This project is an end-to-end machine learning application for predicting house prices in Mumbai, India. It takes user inputs such as location, number of bedrooms, and square feet area as features and predicts the price of the house. The machine learning models used for prediction include Multiple Linear Regression, Lasso Regression, and Ridge Regression. The Lasso Regression model has been selected as the final model and is saved as a pickle file.

The project also includes a Flask backend to provide a user-friendly interface for inputting data and viewing the predictions.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.

~~~
git clone https://github.com/ojshav/Mumbai_house_price_predictor
.git
cd Mumbai_house_price_predictor
~~~
## Install the required dependencies.


pip install -r requirements.txt

## Run the Flask application.
~~~
python app.py
~~~

## Access the application in your web browser at http://localhost:5000.


## Project Structure
~~~
Mumbai_house_price_predictor/
├── app.py
├── models/
│   ├── lasso_model.pkl
│   ├── ...
├── static/
├── templates/
├── README.md
├── requirements.txt
~~~
## Dependencies
Flask
NumPy
Pandas
Scikit-Learn
Pickle (for model serialization)
You can install all the dependencies using the requirements.txt file as mentioned in the "Getting Started" section.

## Usage
Once the Flask application is running, you can access it through your web browser. Provide the required input features such as location, number of bedrooms, and square feet area, and the application will use the Lasso Regression model to predict the house price.

## Contributing
Contributions to this project are welcome. Feel free to open issues and pull requests to suggest improvements or report bugs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to copy and paste this into your GitHub repository's README file, making
