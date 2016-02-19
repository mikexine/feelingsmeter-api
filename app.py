from flask import Flask, request, jsonify
from classification import Classification

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    """

    Takes post data structured like this:
    {
      "data":["I like them apples", "I prefer green apples"]
    }
    """
    classifiers_to_use = request.args.get('classifiers')
    if classifiers_to_use:
        classifiers_to_use = classifiers_to_use.split(',')

    post_payload = request.get_json(force=True)
    cl = Classification()
    data = post_payload['data']
    predictions = list(cl.single_classification(tuple(data), to_json=True, classifiers_to_include=classifiers_to_use))
    
    for text, preds in zip(data, predictions):
        preds['text'] = text
    
    response = {'count':len(predictions),
                'data':predictions}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

