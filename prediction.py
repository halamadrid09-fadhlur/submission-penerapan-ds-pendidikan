import joblib

model = joblib.load("./model/model.joblib")
label_encoder = joblib.load("./model/label_encoder.joblib")


def predict(data):
    """
    Predict the label for the input data using the pre-trained model.
    """
    # Make prediction
    prediction = model.predict(data)

    # Decode the prediction back to original labels
    decoded_prediction = label_encoder.inverse_transform(prediction)[0]

    return decoded_prediction
