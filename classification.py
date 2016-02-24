from subprocess import check_output
from config import paths, output_columns
import os
import re

class Classification:


    @staticmethod
    def __write__(texts):
        # Create file path
        abs_path = os.getcwd() + '/'
        file_path = ''.join([abs_path, paths['input_dir'], str(hash(texts))])
        # Open stream
        f = open(file_path,'w')
        # Write data to file
        texts_len = len(texts) - 1 # Compute length prior to execution

        for i, each_line in enumerate(texts):
            f.write(each_line)
            # Only apply newline if it's not the last line
            if i != texts_len:
                f.write('\n')
        # Close stream and return the file path
        f.close()
        return file_path

    @staticmethod
    def __get_command__(file_path, classifier_name):

        if classifier_name is None:
            raise ValueError()

        command = '{mallet} classify-file --input {input} --encoding utf-8 --output - --classifier {classifier}' \
        .format(mallet=paths['mallet'], input=file_path, classifier=paths[classifier_name])
        return command

    @staticmethod
    def __parse__(output_texts, classifier_name, to_json=False):
        # Regex to find all numbers with 16 decimals
        regex = r'\d+\.\d{1,16}'
        compiled_regex = re.compile(regex)
        # If caller has requested to_json, put the data into a list of dicts, othwerwise just a list of lists
        if to_json:
            keys = output_columns[classifier_name]
            for each_line in output_texts.decode('utf-8').split('\n'):
                temp_dict = dict()
                for key, val in zip(keys, compiled_regex.findall(each_line)):
                    temp_dict[key] = val
                yield temp_dict
        else:
            for each_line in output_texts.decode('utf-8').split('\n'):
                yield [float(n) for n in compiled_regex.findall(each_line)]
        
    @staticmethod
    def single_classification(texts, to_json=False, classifiers_to_include=None):
        file_path = Classification.__write__(texts)
        parsed_data = []
  
        if not classifiers_to_include:
            classifiers = ['pos_neg_classifier', '6_way_classifier', 'aroused_calm_classifier', '27_way_classifier']
        else:
            classifiers = classifiers_to_include

        for classifier in classifiers:
            cmd = Classification.__get_command__(file_path, classifier)        
            # Call the classifier with the saved file
            stdout = check_output(cmd.split())

            # Return the received data from the mallet classifier
            
            data = list(Classification.__parse__(stdout, classifier, to_json=to_json))[:-1]
            if not parsed_data:
                parsed_data = data
            else:
                for parsed, each in zip(parsed_data, data):
                    parsed.update(each)
            # Slice the last one away (The last dict is empty)
            # TODO: Check if this happens prior to calling Mallet
            # This has a relatively large cost when calls are small

        # Remove the file again
        os.remove(file_path)
        return parsed_data
