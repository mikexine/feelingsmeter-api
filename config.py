paths = {
'mallet_bin': 'mallet/bin/',
'mallet': 'mallet/bin/mallet',
#'5_way_classifier': 'prediction_models/5feelings_angry_animated_empowered_fearful_joy.classifier.trial0',
'6_way_classifier': 'prediction_models/6feelings_angry_animated_empowered_fearful_joy_sad.classifier.trial0',
'input_dir':'temp/',
'aroused_calm_classifier': 'prediction_models/aroused_calm_complete.classifier.trial0',
'pos_neg_classifier': 'prediction_models/pos_neg_balanced_trigram_maxent.classifier.trial0',
'27_way_classifier': 'prediction_models/28feelings_classes_v3.classifier.trial0'
}

output_columns = {
#'5_way_classifier': ('angry', 'animated', 'empowered', 'fearful', 'joy'),
'6_way_classifier': ('ANGER', 'EXCITEMENT', 'EMPOWERED', 'FEARFUL', 'JOY', 'SADNESS'),
'aroused_calm_classifier': ('aroused_excited_angry_pissed', 'calm_tired_relaxed_sleepy'),
'pos_neg_classifier': ('neg_sad_disgusted_disappointed', 'pos_happy_great_wonderful'),
'27_way_classifier': ('accomplished', 'amused', 'angry', 'annoyed', 'awesome', 'bad', 'confident', 'confused', 'depressed', 'determined', 'disappointed', 'disgusted', 'down', 'excited', 'fantastic', 'great', 'happy', 'heartbroken', 'hopeful', 'pissed', 'proud', 'pumped', 'sad', 'scared', 'super', 'wonderful', 'worried')
}

column_prefix = {
'6_way_classifier': '6_way_',
'27_way_classifier': '27_way_'
}
