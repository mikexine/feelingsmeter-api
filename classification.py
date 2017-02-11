from config import models, input_dir
import os
from nltk.tokenize import RegexpTokenizer


class Classification:

    @staticmethod
    def __write__(texts):
        # Create file path
        abs_path = os.getcwd() + '/'
        file_path = ''.join([abs_path, input_dir, str(hash(texts))])
        # Open stream
        f = open(file_path, 'w')
        # Write data to file
        texts_len = len(texts) - 1  # Compute length prior to execution

        tokenizer = RegexpTokenizer(r'\w+')

        for i, each_line in enumerate(texts):
            tokenized_line = ' '.join(tokenizer.tokenize(each_line.lower()))
            f.write(tokenized_line.encode('utf-8'))
            # Only apply newline if it's not the last line
            if i != texts_len:
                f.write('\n')
        # Close stream and return the file path
        f.close()
        return file_path

    @staticmethod
    def single_classification(texts, to_json=True):
        file_path = Classification.__write__(texts)
        parsed_data = []

        for m in models:
            data = list(Classification.__scikit__(m["model"], m["labels"],
                                                  texts, to_json=to_json))
            if not parsed_data:
                parsed_data = data
            else:
                for parsed, each in zip(parsed_data, data):
                    parsed.update(each)

        os.remove(file_path)
        return parsed_data

    @staticmethod
    def __scikit__(model, labels, texts, to_json=False):
        predicted = model.predict_proba(texts)

        if to_json:
            for probas in predicted:
                probability_dict = dict()
                for proba, label in zip(probas, labels):
                    probability_dict[label] = proba
                yield probability_dict
        else:
            yield ValueError('not implemented')
