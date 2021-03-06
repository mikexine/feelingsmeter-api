from sklearn.externals import joblib
# from sklearn.feature_extraction import text
import warnings
warnings.filterwarnings("ignore")

six_way = 'prediction_models/six_way.pkl'
six_way_labels = ('sw_anger', 'sw_excitement', 'sw_empowered',
                  'sw_fearful', 'sw_joy', 'sw_sadness')

pos_neg = 'prediction_models/pos_neg.pkl'
pos_neg_labels = ('pn_negative', 'pn_positive')

arousal = 'prediction_models/arousal.pkl'
arousal_labels = ('ac_aroused', 'ac_calm')

twentyseven_way = 'prediction_models/twentyseven_way.pkl'
twentyseven_way_labels = ('27_accomplished', '27_amused', '27_angry',
                          '27_annoyed', '27_awesome', '27_bad', '27_confident',
                          '27_confused', '27_depressed', '27_determined',
                          '27_disappointed', '27_disgusted', '27_down',
                          '27_excited', '27_fantastic', '27_great', '27_happy',
                          '27_heartbroken', '27_hopeful', '27_pissed',
                          '27_proud', '27_pumped', '27_sad', '27_scared',
                          '27_super', '27_wonderful', '27_worried')

six_way_model = joblib.load(six_way)
pos_neg_model = joblib.load(pos_neg)
arousal_model = joblib.load(arousal)
twentyseven_way_model = joblib.load(twentyseven_way)
print("Joblib models loaded")

models = [
    {
        "model": six_way_model,
        "labels": six_way_labels
    },
    {
        "model": pos_neg_model,
        "labels": pos_neg_labels
    },
    {
        "model": arousal_model,
        "labels": arousal_labels
    },
    {
        "model": twentyseven_way_model,
        "labels": twentyseven_way_labels
    }
]


input_dir = 'temp/'
