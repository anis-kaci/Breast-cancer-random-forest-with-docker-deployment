from flask import Flask , request , jsonify 
import joblib


def flask_app():

    #create the flask app
    app = Flask(__name__)


    @app.route('/')
    def homePage():
        return 'Welcome to the breast cancer prediction app'
    
    #load our model 
    model = joblib.load("model.pkl")


    #define the flask root to /predict endpoint
    #and that the app only listens to POST requests 
    @app.route('/predict', methods=['POST'])
    #define our predict functin 
    def predict():
        #get client request data 
        data = request.get_json()
        #extract the features from JSON data 
        features = data["features"]


        #perform predictions using the loaded model 
        prediction = model.predict([features])
        #calculate the proba of the prediction
        proba = model.predict_proba([features])

        print(str(prediction) + ' pb ' + str(proba))
        #return the response(the results of the prediction) to the client as JSON
        return jsonify({"prediction": int(prediction[0]), "probability": float(proba[0][1])})

    
    return app 

#if script is run directly then starts the flask app on port 5000 
#host = 0.0.0.0 to make it accessible externally  
if __name__ == '__main__':
    app = flask_app()
    app.run(host='0.0.0.0', port = 5000)

