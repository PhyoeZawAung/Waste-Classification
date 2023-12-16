import tensorflow as tf
import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import io
from pathlib import Path


@st.cache_resource(show_spinner="Model is loading...")
def load_model():
    """
        Load the model
    """
    model = tf.keras.models.load_model('garbage-classification.h5')
    return model

def predict(image_data, model):
        size = (400,400)    
        img = tf.image.resize(image_data, size)
        pred_prob = model.predict(tf.expand_dims(img, axis=0), verbose=0) 
        return pred_prob

def main():
    st.title("Classify page")   
    class_names = ['battery', 'biological', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']
    model = load_model()
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
            
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image")
        with st.spinner("Classifying...."):
            prediction = predict(image, model)
            pred_class = class_names[prediction.argmax()]
            st.write(pred_class,prediction[0][prediction.argmax()] * 100)
    else:
        st.info("Please upload an image to classify")
if __name__ == "__main__":
    main()