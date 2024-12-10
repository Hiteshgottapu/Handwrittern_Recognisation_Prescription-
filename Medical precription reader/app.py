import streamlit as st
from PIL import Image, UnidentifiedImageError
import pytesseract
import io

# Set the Tesseract path (make sure this path points to where Tesseract is installed on your machine)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if necessary

# Set the Streamlit page configuration
st.set_page_config(page_title="Revolutionizing Handwritten Prescription Recognition: A High-Accuracy CNN Model with Explainable AI", layout="wide")

# Define Color Variables for better UI consistency
PRIMARY_COLOR = '#4CAF50'  # Green
SECONDARY_COLOR = '#2196F3'  # Blue
ALERT_COLOR = '#F44336'  # Red
BACKGROUND_COLOR = '#f0f8ff'  # Soft light blue background
TEXT_COLOR = '#333'  # Dark text for readability
ACCENT_COLOR = '#00bcd4'  # Teal accent color

# Inject custom CSS for modern UI & UX improvements
st.markdown(f"""
    <style>
        /* General Body Styling */
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, {BACKGROUND_COLOR}, #e1f5fe);
            color: {TEXT_COLOR};
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            box-sizing: border-box;
        }}

        /* Main Container Styling */
        .main-container {{
            background-color: #fff;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            padding: 40px;
            width: 90%;
            max-width: 1200px;
            text-align: center;
            margin-top: 40px;
            transition: all 0.3s ease;
            overflow: hidden;
        }}
        
        .main-container:hover {{
            transform: scale(1.02);
        }}

        /* Header */
        .header {{
            font-size: 48px;
            font-weight: 700;
            background: linear-gradient(135deg, {ACCENT_COLOR}, {PRIMARY_COLOR});
            -webkit-background-clip: text;
            color: transparent;
            margin-bottom: 25px;
            text-transform: uppercase;
        }}

        /* Subheader Styling */
        .subheader {{
            color: {TEXT_COLOR};
            font-size: 18px;
            margin-top: 0;
            font-weight: 300;
            line-height: 1.5;
        }}

        /* File Uploader Styling */
        .stFileUploader {{
            background-color: #fff;
            padding: 30px;
            border: 3px dashed {PRIMARY_COLOR};
            border-radius: 15px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            display: inline-block;
            width: 100%;
        }}

        .stFileUploader:hover {{
            background-color: #f0f8ff;
            transform: scale(1.05);
        }}

        /* Button Styling */
        .stButton button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border: none;
            padding: 15px 35px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        .stButton button:hover {{
            background-color: #45a049;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        }}

        .stButton button:active {{
            transform: scale(0.98);
        }}

        /* Camera Button Styling */
        .stCameraInput {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border: none;
            padding: 15px 35px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
            width: 100%;
            display: block;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        .stCameraInput:hover {{
            background-color: #45a049;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        }}

        .stCameraInput:active {{
            transform: scale(0.98);
        }}

        /* Text Area Styling */
        .stTextArea textarea {{
            background-color: #f9f9f9;
            border: 2px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
            width: 100%;
            height: 250px;
            resize: vertical;
            transition: border-color 0.3s ease;
            box-sizing: border-box;
        }}

        .stTextArea textarea:focus {{
            border-color: {PRIMARY_COLOR};
            outline: none;
        }}

        /* Download Button Styling */
        .stDownloadButton button {{
            background-color: {SECONDARY_COLOR};
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s ease;
        }}

        .stDownloadButton button:hover {{
            background-color: #1e88e5;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}

        .stDownloadButton button:active {{
            transform: scale(0.98);
        }}

        /* Spinner Styling */
        .stSpinner div {{
            border-top: 4px solid {PRIMARY_COLOR};
            animation: rotate 1s linear infinite;
        }}

        @keyframes rotate {{
            0% {{
                transform: rotate(0deg);
            }}
            100% {{
                transform: rotate(360deg);
            }}
        }}

        /* Layout Adjustments */
        .stContainer {{
            display: flex;
            justify-content: space-between;
            gap: 30px;
            flex-wrap: wrap;
        }}

        .stContainer > div {{
            flex: 1;
            min-width: 300px;
            box-sizing: border-box;
        }}

        /* Image Container */
        .image-container {{
            margin-top: 20px;
            padding: 20px;
            border: 3px solid {PRIMARY_COLOR};
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            width: 70%;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }}

        .image-container img {{
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }}

        /* Clear Image Button */
        .stButton.clear {{
            background-color: {ALERT_COLOR};
            margin-top: 20px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}
        
        .stButton.clear:hover {{
            background-color: #f44336;
            transform: scale(1.05);
        }}

        .stButton.clear:active {{
            transform: scale(0.98);
        }}

    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="header">Revolutionizing Handwritten Prescription Recognition: A High-Accuracy CNN Model with Explainable AI</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    # Header and Description
    st.markdown('<p class="subheader">Capture or upload an image to extract text using Tesseract OCR.</p>', unsafe_allow_html=True)

    # Sidebar for preprocessing options
    st.sidebar.header("Preprocessing Options")
    grayscale = st.sidebar.checkbox("Convert to Grayscale before OCR", value=False)
    contrast = st.sidebar.slider("Adjust Contrast", 1.0, 2.0, 1.0)

    # Initialize session state for uploaded file if it doesn't exist
    if 'uploaded_file' not in st.session_state:
        st.session_state['uploaded_file'] = None

    # Initialize session state to track the camera visibility
    if 'camera_on' not in st.session_state:
        st.session_state['camera_on'] = False

    # Camera Control
    camera_on_button = st.button("Turn on Camera")
    if camera_on_button:
        st.session_state['camera_on'] = True

    if st.button("Turn off Camera"):
        st.session_state['camera_on'] = False

    # Layout for camera and uploaded image
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)

    # Camera input section
    captured_image = None
    if st.session_state['camera_on']:
        captured_image = st.camera_input("Capture Image")
        if captured_image:
            st.image(captured_image, caption="Captured Image", use_column_width=True)

    # Image Upload Section
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    if uploaded_file:
        # Read the uploaded file into a byte stream
        img_bytes = uploaded_file.read()

        # Open the image using PIL
        image = Image.open(io.BytesIO(img_bytes))

        # Display the uploaded image
        st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # OCR Processing Button
    if st.button("Start OCR"):
        if uploaded_file or captured_image:
            with st.spinner("Extracting text... Please wait."):

                try:
                    # Choose the image to process (either uploaded or captured)
                    if uploaded_file:
                        image = Image.open(io.BytesIO(img_bytes))
                    elif captured_image:
                        image = Image.open(io.BytesIO(captured_image))

                    # Preprocessing (convert to grayscale if needed)
                    if grayscale:
                        image = image.convert("L")

                    # Perform OCR
                    ocr_result = pytesseract.image_to_string(image)

                    if not ocr_result.strip():
                        st.warning("No text detected. Try a different image or adjust preprocessing.")
                    else:
                        st.subheader("Extracted Text:")
                        st.text_area("OCR Output", ocr_result, height=300, max_chars=3000)

                        # Download Button for OCR result
                        st.download_button(label="Download OCR Result", data=ocr_result, file_name="ocr_result.txt", mime="text/plain")
                except UnidentifiedImageError:
                    st.error("The uploaded file is not a valid image. Please upload a valid image file (jpg, jpeg, png).")
                except pytesseract.TesseractError:
                    st.error("An error occurred while processing the image with Tesseract. Please check the image quality.")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")
        else:
            st.info("Please upload or capture an image to extract text.")

    # Clear Image Button
    if st.button("Clear Image"):
        st.session_state['uploaded_file'] = None
        st.session_state['camera_on'] = False
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
