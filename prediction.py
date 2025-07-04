import joblib
import os

dirname = os.path.dirname(__file__)
model = joblib.load(os.path.join(dirname, "model/gboost_model.joblib"))
result_target = joblib.load(os.path.join(dirname, "model/encoder_target.joblib"))

def prediction(data):
    result = model.predict(data.values)
    final_result = result_target.inverse_transform(result)[0]
    print(final_result)
    return final_result