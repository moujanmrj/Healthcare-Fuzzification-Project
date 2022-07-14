class inference:
    def rules(self, age, blood_pressure, blood_sugar, cholesterol, heart_rate, ecg, old_peak, exercise, thallium, sex, chest_pain):
        file = open('rules.fcl', 'r')
        line = file.readlines()
        file.close()

        output_list_sick1,output_list_sick2,output_list_sick3,output_list_sick4,output_list_healthy = ([] for i in range(5))

        for i in range(len(line)):
            line[i] = line[i].replace('IF', '')
            line[i] = line[i].replace('(', '')
            line[i] = line[i].replace(')', '')
            line[i] = line[i].replace('THEN', '')
            line[i] = line[i].replace(';', '')
            line[i] = line[i].replace('\n', '')
            line[i] = line[i].split()[2:]

        if line[-1] == '':
            del line[-1]

        def add_rule(input, condition):
            if input == 'age':
                return age[condition]
            if input == 'blood_pressure':
                return blood_pressure[condition]
            if input == 'blood_sugar':
                return blood_sugar[condition]
            if input == 'cholestrol':
                return cholesterol[condition]
            if input == 'heart_rate':
                return heart_rate[condition]
            if input == 'ecg':
                return ecg[condition]
            if input == 'old_peak':
                return old_peak[condition]
            if input == 'exercise':
                return exercise[condition]
            if input == 'thallium_scan':
                return thallium[condition]
            if input == 'sex':
                return sex[condition]
            if input == 'chest_pain':
                return chest_pain[condition]

        for i in range(0, 8):
            class_1, condition_1 = line[i][0], line[i][2]
            class_2, condition_2 = line[i][4], line[i][6]
            output =  line[i][9]
            if(output == 'sick_4'):
                output_list_sick4.append(min(add_rule(class_1, condition_1), add_rule(class_2, condition_2)))
            elif(output == 'sick_3'):
                output_list_sick3.append(min(add_rule(class_1, condition_1), add_rule(class_2, condition_2)))
            elif(output == 'sick_2'):
                output_list_sick2.append(min(add_rule(class_1, condition_1), add_rule(class_2, condition_2)))
            elif(output == 'sick_1'):
                output_list_sick1.append(min(add_rule(class_1, condition_1), add_rule(class_2, condition_2)))

        for i in range(8, 10):
            class_1, condition_1 = line[i][0], line[i][2]
            class_1, condition_1 = line[i][4], line[i][6]
            output =  line[i][9]
            output_list_sick1.append(max(add_rule(class_1, condition_1), add_rule(class_2, condition_2)))
        
        for i in range(10, 54):
            class_1, condition_1 = line[i][0], line[i][2]
            output =  line[i][5]
            if(output == 'sick_4'):
                output_list_sick4.append((add_rule(class_1, condition_1)))
            elif(output == 'sick_3'):
                output_list_sick3.append((add_rule(class_1, condition_1)))
            elif(output == 'sick_2'):
                output_list_sick2.append((add_rule(class_1, condition_1)))
            elif(output == 'sick_1'):
                output_list_sick1.append((add_rule(class_1, condition_1)))
            elif(output == 'healthy'):
                output_list_healthy.append((add_rule(class_1, condition_1)))

        return dict(
            output_sick4 = max(output_list_sick4),
            output_sick3 = max(output_list_sick3),
            output_sick2 = max(output_list_sick2),
            output_sick1 = max(output_list_sick1),
            output_healthy = max(output_list_healthy)
        )

