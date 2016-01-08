from flask import Flask, request, jsonify
from classification import Classification

app = Flask(__name__)

@app.route('/', methods=['POST'])
def classify():
    """

    Takes post data structured like this:
    {
      "data":["I like them apples", "I prefer green apples"]
    }
    """
    post_payload = request.get_json(force=True)
    cl = Classification()
    data = post_payload['data']
    predictions = list(cl.single_classification(tuple(data), to_json=True))    
    
    for text, preds in zip(data, predictions):
        preds['text'] = text
    
    response = {'count':len(predictions),
                'data':predictions}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

