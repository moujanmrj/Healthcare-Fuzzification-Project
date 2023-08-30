# Healthcare-Fuzzification-Project
# Medical Diagnosis Expert System

Welcome to the Medical Diagnosis Expert System! This project aims to provide accurate and reliable medical diagnosis predictions based on a combination of fuzzy logic and expert rules. The system takes into account various health metrics provided by the user and employs a well-defined set of rules to make informed medical condition predictions.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Fuzzy Logic and Inference](#fuzzy-logic-and-inference)
- [Web Interface](#web-interface)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Introduction
The Medical Diagnosis Expert System is designed to assist medical professionals and individuals in making preliminary medical condition predictions. By leveraging fuzzy logic and expert-defined rules, the system provides an additional layer of analysis to help users understand potential health conditions based on their provided health metrics.

## Features
- **Fuzzy Logic-Based Diagnosis:** The core of the system's functionality is based on fuzzy logic, a mathematical approach that handles uncertainty and imprecision in data. Fuzzy logic allows for nuanced decision-making by mapping input data to linguistic variables using membership functions.

- **Fuzzification of Input Data:** The system includes a robust fuzzification process that converts crisp input data (such as age, blood pressure, cholesterol levels, etc.) into fuzzy linguistic values. These fuzzy values enable the system to work with imprecise data and make more accurate predictions.

- **Expert-Defined Rules:** The project incorporates a set of expert-defined rules that relate different health metrics to potential medical conditions. These rules capture the collective wisdom of medical professionals and are used by the system to infer possible diagnoses based on the fuzzified input data.

- **Web Interface for User Interaction:** To make the system accessible to a wide range of users, a user-friendly web interface has been developed. Users can easily input their health metrics through the interface and receive diagnosis predictions in response.

- **Defuzzification for Result Generation:** After applying fuzzy inference based on the input data and expert rules, the system employs defuzzification to translate the fuzzy output into a crisp diagnosis prediction.

## Getting Started

### Prerequisites
- Python 3.x
- Flask (Install using `pip install Flask`)

### Installation
1. **Clone the Repository:** Start by cloning the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/medical-diagnosis-expert.git
   cd medical-diagnosis-expert
   ```

2. **Install Dependencies:** Install the required Python packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Application:** Launch the application by executing the following command.
   ```bash
   python app.py
   ```

2. **Access the Web Interface:** Open a web browser and navigate to `http://127.0.0.1:8448` to access the user-friendly web interface.

3. **Provide Health Metrics:** Input the patient's health metrics, such as age, blood pressure, cholesterol levels, and more, using the provided form.

4. **Get Diagnosis Prediction:** Click the "Get Diagnosis" button to initiate the diagnosis prediction process. The system will apply fuzzy inference and display the predicted medical condition based on the provided data.

## Fuzzy Logic and Inference
The Medical Diagnosis Expert System relies on fuzzy logic to manage uncertainty and imprecision in health metric data. The system includes fuzzification classes for various health metrics, such as age, blood pressure, blood sugar, and more. Additionally, expert-defined rules govern how different health metrics contribute to potential medical conditions. The inference process combines fuzzified input data and expert rules to generate diagnosis predictions.

## Web Interface
The user-friendly web interface simplifies the interaction with the Medical Diagnosis Expert System. Users can effortlessly input their health metrics, submit the form, and receive a diagnosis prediction. The result page showcases the predicted medical condition and provides insights into the potential health status of the patient.



