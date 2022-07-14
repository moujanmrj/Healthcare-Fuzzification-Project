from fuzzification import *
from inference import *
from defuzzification import *

inference_ = inference.inference()

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        age_fuzz = age_fuzzification()
        age = age_fuzz.calc_fuzzy_age(int(input_dict['age']))
        chestpain_fuzz = chestpain_fuzzification()
        chest_pain = chestpain_fuzz.calc_fuzzy_chestpain(int(input_dict['chest_pain']))
        bloodpressure_fuzz = bloodpressure_fuzzification()
        blood_pressure = bloodpressure_fuzz.calc_fuzzy_bloodpressure(int(input_dict['blood_pressure']))
        cholesterol_fuzz = cholesterol_fuzzification()
        cholesterol = cholesterol_fuzz.calc_fuzzy_cholesterol(int(input_dict['cholestrol']))
        bloodsugar_fuzz = bloodsugar_fuzzification()
        blood_sugar = bloodsugar_fuzz.calc_fuzzy_bloodsugar(int(input_dict['blood_sugar']))
        ECG_fuzz = ECG_fuzzification()
        ecg = ECG_fuzz.calc_fuzzy_ECG(float(input_dict['ecg']))
        heartrate_fuzz = heartrate_fuzzification()
        heart_rate = heartrate_fuzz.calc_fuzzy_heartrate(int(input_dict['heart_rate']))
        exercise_fuzz = exercise_fuzzification()
        exercise = exercise_fuzz.calc_fuzzy_exercise(int(input_dict['exercise']))
        oldpeak_fuzz = oldpeak_fuzzification()
        old_peak = oldpeak_fuzz.calc_fuzzy_oldpeak(float(input_dict['old_peak']))
        thallium_fuzz = thallium_fuzzification()
        thallium = thallium_fuzz.calc_fuzzy_thallium(int(input_dict['thallium_scan']))
        sex_fuzz = sex_fuzzification()
        sex = sex_fuzz.calc_fuzzy_sex(int(input_dict['sex']))

        fuzzy_set = inference_.rules(age, blood_pressure, blood_sugar, cholesterol, heart_rate, ecg, old_peak, exercise, thallium, sex, chest_pain)
        print(fuzzy_set)
        return calculate(fuzzy_set)
