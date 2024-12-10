
---

# Revolutionizing Handwritten Prescription Recognition: A High-Accuracy CNN Model with Explainable AI

An AI-driven application designed to interpret and extract text from medical prescriptions. This project leverages a pre-trained deep learning model and OCR technology to enhance medical data digitization.

## Table of Contents

- [Project Description](#project-description)
- [Folder Structure](#folder-structure)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

This project integrates a **Convolutional Neural Network (CNN)** model with OCR techniques to automate the recognition of handwritten medical prescriptions. 

### Features:
- Text recognition using Tesseract OCR.
- Prediction of prescription details using a trained CNN model.
- User-friendly interface built with Streamlit for easy usage.

---

## Folder Structure

Here is an overview of the project files and their purpose:

```
Medical Scripts/
│
├── app.py                     # Main Streamlit app for UI
├── model_saved.keras          # Pre-trained Keras model for handwritten recognition
├── model-building.ipynb       # Jupyter Notebook for training and building the model
├── ocr_result.txt             # Sample text output from OCR
├── requirements.txt           # List of dependencies for the project
```

---

## Installation Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository
Download the project files from your version control or copy them to your local machine.

```bash
git clone <repository-url>
cd Medical Scripts
```

### 2. Create a Virtual Environment (Optional)

Set up a virtual environment to manage dependencies:

```bash
python -m venv env
```

Activate the environment:
- **Windows**:
  ```bash
  .\env\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

Use the `requirements.txt` file to install all necessary packages:

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Application

Start the Streamlit app by running the following command:

```bash
streamlit run app.py
```

### Steps:

1. **Launch the Web App**:
   The app will open in your default browser.

2. **Upload or Capture an Image**:
   - Upload an image file of a medical prescription.
   - Alternatively, use the camera input to capture an image.

3. **Process the Image**:
   - Perform OCR to extract handwritten text.
   - Use the pre-trained CNN model to predict specific prescription details.

4. **View Results**:
   - Extracted text is displayed in a text area.
   - Predictions from the CNN model are shown below the extracted text.

5. **Save or Download Results**:
   - Download the OCR results as a `.txt` file.

---

## Model Details

### Model Architecture:
- **Input**: Preprocessed prescription images.
- **Layers**:
  - **Convolutional Layers**: Feature extraction from image data.
  - **Pooling Layers**: Downsampling to reduce dimensionality.
  - **Dense Layers**: Fully connected layers for final predictions.
- **Output**: Categorized prediction of prescription details.

### Training Details:
- **Training Notebook**: The model was trained using the `model-building.ipynb` notebook.
- **Dataset**: Handwritten prescription dataset (details omitted for brevity).

---

## Dependencies

### Major Libraries:
- **TensorFlow/Keras**: For deep learning model development.
- **Streamlit**: For building the web application.
- **Pillow**: For image preprocessing.
- **Tesseract OCR**: For optical character recognition.
- **OpenCV**: For additional image processing.

### Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions to improve the project are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your branch and create a pull request.

---
