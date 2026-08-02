import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="MNIST Digit Recognition", page_icon="🔢")

st.title("🔢 MNIST Digit Recognition")
st.write("Upload an image of a handwritten digit (0–9).")

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mnist_cnn.keras")

model = load_model()

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    # Display uploaded image
    image = Image.open(uploaded_file).convert("L")
    st.image(image, caption="Uploaded Image", width=200)

    # Preprocess image
    image = image.resize((28, 28))

    img_array = np.array(image)

    # Invert colors if background is white
    if img_array.mean() > 127:
        img_array = 255 - img_array

    img_array = img_array.astype("float32") / 255.0

    img_array = img_array.reshape(1, 28, 28, 1)

    # Prediction
    prediction = model.predict(img_array)

    predicted_digit = np.argmax(prediction)
    confidence = np.max(prediction)

    st.success(f"Predicted Digit: **{predicted_digit}**")
    st.write(f"Confidence: **{confidence*100:.2f}%**")

    # Probability chart
    st.subheader("Prediction Probabilities")

    fig, ax = plt.subplots(figsize=(7,4))
    ax.bar(range(10), prediction[0])
    ax.set_xlabel("Digit")
    ax.set_ylabel("Probability")
    ax.set_xticks(range(10))
    st.pyplot(fig)
