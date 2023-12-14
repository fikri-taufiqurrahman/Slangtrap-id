from application.controller.autocrop_image import autocrop
from application.controller.cnn import predict_model
from application.controller.autocorrect import autocorrect_text

from flask import jsonify

def predict_controller(user):
    autocrop(user)
    word_cnn = predict_model(user)
    response_data = {"word_cnn": autocorrect_text(word_cnn)}
    return jsonify(response_data)




    