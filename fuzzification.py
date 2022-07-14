class age_fuzzification:
    def __init__(self):
        pass

    def age_young(self, x):
        if 0 <= x < 29:
            return 1
        elif 29 <= x <= 38:
            return (38 - x)/9
        else:
            return 0

    def age_mild(self, x):
        if 33 <= x <= 38:
            return (x - 33)/5
        elif 38 < x <= 45:
            return (45 - x)/7
        else:
            return 0

    def age_old(self, x):
        if 40 <= x <= 48:
            return (x - 40)/8
        elif 48 < x <= 58:
            return (58 - x)/10
        else:
            return 0

    def age_veryold(self, x):
        if 0 <= x < 52:
            return 0
        elif 52 <= x <= 60:
            return (x - 52)/8
        else:
            return 1
    
    def calc_fuzzy_age(self, age):
        return dict(
            young = self.age_young(age),
            mild = self.age_mild(age),
            old = self.age_old(age),
            very_old = self.age_veryold(age)
        )

class bloodpressure_fuzzification:
    def __init__(self):
        pass

    def bloodpressure_low(self, x):
        if 0 <= x < 111:
            return 1
        elif 111 <= x <= 134:
            return (134 - x)/23
        else:
            return 0

    def bloodpressure_medium(self, x):
        if 127 <= x <= 139:
            return (x - 127)/12
        elif 139 < x <= 153:
            return (153 - x)/14
        else:
            return 0

    def bloodpressure_high(self, x):
        if 142 <= x <= 157:
            return (x - 142)/16
        elif 157 < x <= 172:
            return (172 - x)/15
        else:
            return 0

    def bloodpressure_veryhigh(self, x):
        if 0 <= x <= 154:
            return 0
        elif 154 < x <= 171:
            return (x - 154)/17
        else:
            return 1
    
    def calc_fuzzy_bloodpressure(self, blood_pressure):
        return dict(
            low = self.bloodpressure_low(blood_pressure),
            medium = self.bloodpressure_medium(blood_pressure),
            high = self.bloodpressure_high(blood_pressure),
            very_high = self.bloodpressure_veryhigh(blood_pressure)
        )

class bloodsugar_fuzzification:
    def __init__(self):
        pass

    def bloodsugar_pos(self, x):
        if 120 < x:
            return 1
        elif 105 <= x <= 120:
            return (x - 105)/15
        else:
            return 0
    
    def calc_fuzzy_bloodsugar(self, blood_sugar):
        return dict(
           true = self.bloodsugar_pos(blood_sugar),
           false = 1 - self.bloodsugar_pos(blood_sugar)
        )   

class cholesterol_fuzzification:
    def __init__(self):
        pass

    def cholesterol_low(self, x):
        if 0 <= x < 151:
            return 1
        elif 151 <= x <= 197:
            return (197 - x)/46
        else:
            return 0

    def cholesterol_medium(self, x):
        if 188 <= x <= 215:
            return (x - 188)/27
        elif 215 < x <= 250:
            return (250 - x)/35
        else:
            return 0

    def cholesterol_high(self, x):
        if 217 <= x <= 263:
            return(x - 217)/46
        elif 263 < x <= 307:
            return (307 - x)/44
        else:
            return 0

    def cholesterol_veryhigh(self, x):
        if 0 <= x < 281:
            return 0
        elif 281 <= x <= 347:
            return (x - 281)/93
        else:
            return 1
    
    def calc_fuzzy_cholesterol(self, cholesterol):
        return dict(
            low = self.cholesterol_low(cholesterol),
            medium = self.cholesterol_medium(cholesterol),
            high = self.cholesterol_high(cholesterol),
            very_high = self.cholesterol_veryhigh(cholesterol)
        ) 

class heartrate_fuzzification:
    def __init__(self):
        pass

    def heartrate_low(self, x):
        if 0 <= x < 100:
            return 1
        elif 100 <= x <= 141:
            return (141 - x)/41
        else :
            return 0

    def heartrate_medium(self, x):
        if 111 <= x <= 152:
            return (x - 111)/41
        elif 152 < x <= 194:
            return (194 - x)/42
        else:
            return 0

    def heartrate_high(self, x):
        if 0 <= x < 152:
            return 0
        elif 152 <= x <= 210:
            return (x - 152)/58
        else:
            return 1

    def calc_fuzzy_heartrate(self, heart_rate):
        return dict(
            low = self.heartrate_low(heart_rate),
            medium = self.heartrate_medium(heart_rate),
            high = self.heartrate_high(heart_rate)
        )        

class ECG_fuzzification:
    def __init__(self):
        pass

    def ECG_normal(self, x):
        if -0.5 <= x < 0:
            return 1
        elif 0 <= x <= 0.4:
            return (0.4 - x)/0.4
        else:
            return 0

    def ECG_abnormal(self, x):
        if 0.2 <= x <= 1:
            return (x - 0.2)/0.8
        elif 1 < x <= 1.8:
            return (1.8 - x)/0.8
        else:
            return 0

    def ECG_hypertrophy(self, x):
        if -0.5 <= x < 1.4:
            return 0
        elif 1.4 <= x <= 1.9:
            return (x - 1.4)/0.5
        else:
            return 1

    def calc_fuzzy_ECG(self,ECG):
        return dict(
            normal = self.ECG_normal(ECG),
            abnormal = self.ECG_abnormal(ECG),
            hypertrophy = self.ECG_hypertrophy(ECG)
        )

class oldpeak_fuzzification:
    def __init__(self):
        pass

    def oldpeak_low(self, x):
        if 0 <= x < 1:
            return 1
        elif 1 <= x <= 2:
            return (2 - x)
        else:
            return 0

    def oldpeak_risk(self, x):
        if 1.5 <= x <= 2.8:
            return (x - 1.5)/1.3
        elif 2.8 < x <= 4.2:
            return (4.2 - x)/1.4
        else:
            return 0

    def oldpeak_terrible(self, x):
        if 0 < x < 2.5:
            return 0
        elif 2.5 <= x <= 4:
            return (x - 2.5)/1.5
        else:
            return 1

    def calc_fuzzy_oldpeak(self, old_peak):
        return dict(
            low = self.oldpeak_low(old_peak),
            risk = self.oldpeak_risk(old_peak),
            terrible = self.oldpeak_terrible(old_peak)
        )   

class exercise_fuzzification:
    def __init__(self):
        pass

    def true(self, x):
        if x == 1:
            return 1
        else: 
            return 0

    def false(self, x):
        if x == 0:
            return 1
        else: 
            return 0

    def calc_fuzzy_exercise(self, num):
        return dict(
            true = self.true(num),
            false = self.false(num)
        )

class thallium_fuzzification:
    def __init__(self):
        pass

    def normal(self, x):
        if x == 3:
            return 1
        else: 
            return 0

    def medium(self, x):
        if x == 6:
            return 1
        else: 
            return 0

    def high(self, x):
        if x == 7:
            return 1
        else: 
            return 0

    def calc_fuzzy_thallium(self,num):
        return dict(
           normal = self.normal(num),
           medium = self.medium(num),
           high = self.high(num)
        ) 

class sex_fuzzification:
    def __init__(self):
        pass

    def male_sex(self, x):
        if x == 0:
            return 1
        else: 
            return 0

    def female_sex(self, x):
        if x == 1:
            return 1
        else: 
            return 0

    def calc_fuzzy_sex(self, num):
        return dict(
            male = self.male_sex(num),
            female = self.female_sex(num)
        )       

class chestpain_fuzzification:
    def __init__(self):
        pass

    def typical_angina(self, x):
        if x == 1:
            return 1
        else:
            return  0
    def atypical_angina(self, x):
        if x == 2:
            return 1
        else:
            return  0
    def non_anginal_pain(self, x):
        if x == 3:
            return 1
        else:
            return  0
    def asymptomatic(self, x):
        if x == 4:
            return 1
        else:
            return  0

    def calc_fuzzy_chestpain(self, num):
        return dict(
            typical_anginal = self.typical_angina(num),
            atypical_anginal = self.atypical_angina(num),
            non_aginal_pain = self.non_anginal_pain(num),
            asymptomatic = self.asymptomatic(num)
        )     

class output:
    def __init__(self, inf):
        self.inf = inf

    def output_healthy(self, x):
        alpha = self.inf['output_healthy']
        if alpha == 0:
            return 0
        elif 0 <= x < 0.25:
            return alpha
        elif 0.25 <= x <= 1:
            return min(alpha, (1 - x)/0.75)
        else:
            return 0

    def output_sick1(self, x):
        alpha = self.inf['output_sick1']
        if alpha == 0:
            return 0
        elif 0 <= x <= 1:
            return min(alpha, x) 
        elif 1 < x <= 2:
            return min(alpha, (2 - x))
        else:
            return 0

    def output_sick2(self, x):
        alpha = self.inf['output_sick2']
        if alpha == 0:
            return 0
        elif 1 <= x <= 2:
            return min(alpha, (x - 1))
        elif 2 < x <= 3:
            return min(alpha, (3 - x))
        else:
            return 0

    def output_sick3(self, x):
        alpha = self.inf['output_sick3']
        if alpha == 0:
            return 0
        elif 2 <= x <= 3:
            return min(alpha, (x - 2))
        elif 3 < x <= 4:
            return min(alpha, (3 - x))
        else:
            return 0

    def output_sick4(self, x):
        alpha = self.inf['output_sick4']
        if alpha == 0:
            return 0
        elif 0 <= x < 3:
            return 0
        elif 3 <= x <= 3.75:
            return min(alpha, (x - 3)/0.75)
        else:
            return alpha     

    def output(self, x):
        return max(self.output_healthy(x), self.output_sick1(x), self.output_sick2(x), self.output_sick3(x), self.output_sick4(x))