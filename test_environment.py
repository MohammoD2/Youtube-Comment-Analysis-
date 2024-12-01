import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
import mlflow

# Define the preprocessing function
def preprocess_comment(comment):
    """Apply preprocessing transformations to a comment."""
    try:
        # Convert to lowercase
        comment = comment.lower()

        # Remove trailing and leading whitespaces
        comment = comment.strip()

        # Remove newline characters
        comment = re.sub(r'\n', ' ', comment)

        # Remove non-alphanumeric characters, except punctuation
        comment = re.sub(r'[^A-Za-z0-9\s!?.,]', '', comment)

        # Remove stopwords but retain important ones for sentiment analysis
        stop_words = set(stopwords.words('english')) - {'not', 'but', 'however', 'no', 'yet'}
        comment = ' '.join([word for word in comment.split() if word not in stop_words])

        # Lemmatize the words
        lemmatizer = WordNetLemmatizer()
        comment = ' '.join([lemmatizer.lemmatize(word) for word in comment.split()])

        return comment
    except Exception as e:
        print(f"Error in preprocessing comment: {e}")
        return comment

# Load the model and vectorizer
def load_model_and_vectorizer(model_name, model_version, vectorizer_path):
    try:
        # Load model from MLflow
        model_uri = f"models:/{model_name}/{model_version}"
        print(f"Loading model from URI: {model_uri}")
        model = mlflow.pyfunc.load_model(model_uri)

        # Load vectorizer from local storage
        vectorizer = joblib.load(vectorizer_path)
        print("Vectorizer successfully loaded.")

        return model, vectorizer
    except Exception as e:
        print(f"Failed to load model and vectorizer: {e}")
        raise

# Debugging function to test vectorizer and model compatibility
def debug_vectorizer_and_model(model, vectorizer, comments):
    try:
        # Step 1: Preprocess comments
        preprocessed_comments = [preprocess_comment(comment) for comment in comments]
        print("Preprocessed Comments:")
        print(preprocessed_comments)

        # Step 2: Transform comments using the vectorizer
        print("\nTesting Vectorizer Transformation...")
        transformed_comments = vectorizer.transform(preprocessed_comments)
        print("Shape of Transformed Comments:", transformed_comments.shape)

        # Step 3: Test the vectorizer with a sample input
        test_data = vectorizer.transform(["This is a test comment"])
        print("\nShape of Test Data:", test_data.shape)

        # Step 4: Make a prediction with the test data
        print("\nTesting Model Prediction...")
        prediction = model.predict(test_data)
        print("Prediction for Test Data:", prediction)

        # Step 5: Make predictions for all transformed comments
        print("\nPredictions for Input Comments:")
        predictions = model.predict(transformed_comments)
        print(predictions)

    except Exception as e:
        print(f"Error during debugging: {e}")

# Main execution
if __name__ == "__main__":
    # Example comments to debug
    debug_comments = ["This video is amazing!", "I didn't like it."]

    # Specify model and vectorizer paths
    model_name = "yt_chrome_plugin_model"
    model_version = "5"
    vectorizer_path = "./tfidf_vectorizer.pkl"  # Adjust the path to where your vectorizer file is stored

    try:
        # Load the model and vectorizer
        model, vectorizer = load_model_and_vectorizer(model_name, model_version, vectorizer_path)

        # Run debugging tests
        debug_vectorizer_and_model(model, vectorizer, debug_comments)
    except Exception as main_error:
        print(f"Error in main execution: {main_error}")
