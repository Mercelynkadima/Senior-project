import streamlit as st
import pickle

# Load the saved model
with open('FakeNewsDetection.pkl', 'rb') as file:
    model = pickle.load(file)

    def main():
     st.title("Fake News Detection")
     st.write("Enter a news article to check if it is real or fake.")

    # Input form
    news_article = st.text_area("News Article", height=200)
    if st.button("Check"):
        # Perform any necessary preprocessing on the news article

        # Use the loaded model to predict the label of the news article
        prediction = model.predict([news_article])

        # Display the prediction result
        st.write(f"Prediction: {prediction[0]}")

if __name__ == "__main__":
    main()

