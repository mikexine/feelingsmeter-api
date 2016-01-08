from subprocess import check_output
from config import paths
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
    def __get_command__(file_path):
        command = '{mallet} classify-file --input {input} --encoding utf-8 --output - --classifier {classifier}' \
        .format(mallet=paths['mallet'], input=file_path, classifier=paths['classifier'])
        return command

    @staticmethod
    def __parse__(output_texts, to_json=False):
        # Regex to find all numbers with 16 decimals
        regex = r'\d+\.\d{1,16}'
        compiled_regex = re.compile(regex)
        # If caller has requested to_json, put the data into a list of dicts, othwerwise just a list of lists
        if to_json:
            keys = ('angry', 'animated', 'empowered', 'fearful', 'joy')
            for each_line in output_texts.split('\n'):
                temp_dict = dict()
                for key, val in zip(keys, compiled_regex.findall(each_line)):
                    temp_dict[key] = val
                yield temp_dict
        else:
            for each_line in output_texts.split('\n'):
                yield [float(n) for n in compiled_regex.findall(each_line)]
        
    @staticmethod
    def single_classification(texts, to_json=False):
        file_path = Classification.__write__(texts)
        cmd = Classification.__get_command__(file_path)
        print cmd        
        # Call the classifier with the saved file
        stdout = check_output(cmd.split())
        print stdout
        # Remove the file again
        os.remove(file_path)
        
        # Return the received data from the mallet classifier
        parsed_data = list(Classification.__parse__(stdout, to_json=to_json))
        # Slice the last one away (The last dict is empty)
        # TODO: Check if this happens prior to calling Mallet
        # This has a relatively large cost when calls are small
        return parsed_data[:-1]
