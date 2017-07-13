from flask import Flask, request, jsonify
from classification import Classification
from word_category_counter import score_text


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
    use_new_classifier = request.args.get('new_cls')
    
    if classifiers_to_use:
        classifiers_to_use = classifiers_to_use.split(',')
    elif use_new_classifier:
        use_new_classifier = (use_new_classifier.lower() == 'true')
    
    post_payload = request.get_json(force=True)
    cl = Classification()
    data = post_payload['data']
    predictions = list(cl.single_classification(tuple(data), to_json=True))

    for text, preds in zip(data, predictions):
        preds['text'] = text
        preds["affective processes"] = score_text(text).get("Affective Processes")
        # preds["ANGER"] = preds.pop("ANGRY")
        # preds["SADNESS"] = preds.pop("SAD")
        # preds["EXCITEMENT"] = preds.pop("ANIMATED")
        # preds["JOYFUL"] = preds.pop("JOY")
    print(predictions)
    
    response = {'count':len(predictions),
                'data':predictions}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=8081, threaded=True)

