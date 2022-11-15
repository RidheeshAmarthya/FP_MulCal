import PySimpleGUI as sg
import json
from datetime import datetime

with open('cutoffs.txt', 'r') as fh:
    cutoffs = json.load(fh)

def score_cal(atr=None, sub_atr=None, data=None):

    if atr == 'Durable':
        data_l = []
        life = 0
        warr = 0
        for num_str in data.split():
            # num_int = int(num_str)
            # data_l.append(num_int)
            #     if i[0] == 'L':
            #         life = i[1]
            #     elif i[0] == 'W':
            #         warr = i[i]
            LW = num_str.split(":")[0:1]
            LW_D = num_str.split(":")[1:2]
            for i in range(len(LW)):
                if LW[i] == 'L':
                    life = int(LW_D[i])
                elif LW[i] == 'W':
                    warr = int(LW_D[i])
        print(life, warr)
    elif atr == 'Fire resistance': pass
    else: data = float(data)
    score = -1

    # Helper functions
    def range_4(data, cut):
        cut = float(cut)
        if data > cut * (1.25):
            return 0
        elif data <= cut * (1.25) and data > cut * (1):
            return 0.5
        elif data <= cut * (1) and data > cut * (0.5):
            return 1
        elif data <= cut * (0.50) and data > cut * (0.25):
            return 1.5
        elif data <= cut * (0.25):
            return 2
        else:
            return -1
    def durable_cal(l_score, warranty):
        if life >= l_score and warr < warranty:
            return 1
        elif life >= l_score and warr >= warranty:
            return 2
        elif warr >= warranty:
            return 1
        elif life >= 25 and life < l_score or warr >= 10 and warr < warranty:
            return 0.5
        else:
            return 0

    # Happy with these
    if atr == 'Low embodied energy':
        if sub_atr == 'Overall':
            cut = cutoffs["Low embodied energy"]["Overall"]
            score = range_4(data, cut)
        elif sub_atr == 'Cladding':
            cut = cutoffs["Low embodied energy"]["Cladding"]
            score = range_4(data, cut)
        elif sub_atr == 'Flooring':
            cut = cutoffs["Low embodied energy"]["Flooring"]
            score = range_4(data, cut)
        elif sub_atr == 'Insulation MJ/m2':
            cut = cutoffs["Low embodied energy"]["Insulation MJ/m2"]
            score = range_4(data, cut)
        elif sub_atr == 'Insulation MJ/m3':
            cut = cutoffs["Low embodied energy"]["Insulation MJ/m3"]
            score = range_4(data, cut)
        elif sub_atr == 'Interior Finishes':
            cut = cutoffs["Low embodied energy"]["Interior Finishes"]
            score = range_4(data, cut)
        elif sub_atr == 'Roofing':
            cut = cutoffs["Low embodied energy"]["Roofing"]
            score = range_4(data, cut)
        elif sub_atr == 'Structure':
            cut = cutoffs["Low embodied energy"]["Structure"]
            score = range_4(data, cut)
        else:
            score = -1
    elif atr == 'Low embodied Carbon':
        if sub_atr == 'Overall':
            cut = cutoffs["Low embodied carbon"]["Overall"]
            score = range_4(data, cut)
        elif sub_atr == 'Cladding':
            cut = cutoffs["Low embodied carbon"]["Cladding"]
            score = range_4(data, cut)
        elif sub_atr == 'Flooring':
            cut = cutoffs["Low embodied carbon"]["Flooring"]
            score = range_4(data, cut)
        elif sub_atr == 'Insulation kgCO2eq/m2':
            cut = cutoffs["Low embodied carbon"]["Insulation kgCO2eq/m2"]
            score = range_4(data, cut)
        elif sub_atr == 'Insulation kgCO2eq/m3':
            cut = cutoffs["Low embodied carbon"]["Insulation kgCO2eq/m3"]
            score = range_4(data, cut)
        elif sub_atr == 'Interior Finishes':
            cut = cutoffs["Low embodied carbon"]["Interior Finishes"]
            score = range_4(data, cut)
        elif sub_atr == 'Roofing':
            cut = cutoffs["Low embodied carbon"]["Roofing"]
            score = range_4(data, cut)
        elif sub_atr == 'Structure':
            cut = cutoffs["Low embodied carbon"]["Structure"]
            score = range_4(data, cut)
        else:
            score = -1

    # No 1.5 score
    # Needs Testing...
    elif atr == 'Durable':
        if sub_atr == 'Overall':
            u_score = int(cutoffs["Durable"]["Overall"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Overall"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Overall"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Structure':
            u_score = int(cutoffs["Durable"]["Structure"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Structure"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Structure"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Walls':
            u_score = int(cutoffs["Durable"]["Walls"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Walls"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Walls"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Flooring finishes':
            u_score = int(cutoffs["Durable"]["Flooring finishes"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Flooring finishes"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Flooring finishes"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Paint/Plaster':
            u_score = int(cutoffs["Durable"]["Paint/Plaster"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Paint/Plaster"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Paint/Plaster"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Insulation':
            u_score = int(cutoffs["Durable"]["Insulation"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Insulation"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Insulation"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Boards':
            u_score = int(cutoffs["Durable"]["Boards"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Boards"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Boards"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Roofs':
            u_score = int(cutoffs["Durable"]["Roofs"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Roofs"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Roofs"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Ceilings':
            u_score = int(cutoffs["Durable"]["Ceilings"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Ceilings"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Ceilings"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0
        elif sub_atr == 'Window & Door':
            u_score = int(cutoffs["Durable"]["Window & Door"]["Max Life"])
            l_score = int(cutoffs["Durable"]["Window & Door"]["Min Life"])
            warranty = int(cutoffs["Durable"]["Window & Door"]["Warranty"])
            score = durable_cal(l_score, warranty)
            # if data_l[0] >= u_score and data_l[1] >= warranty:
            #     score = 2
            # elif data_l[0] >= u_score and data_l[0] < l_score and data_l[1] >= warranty:
            #     score = 1
            # elif data_l[0] >= l_score and data_l[0] < u_score and data_l[1] >= warranty:
            #     score = 0.5
            # else:
            #     score = 0

    # Happy with this
    elif atr == 'Recycled content':
        if data < float(cutoffs["Recycled content"]["Overall"]["Range1"]):
            score = 0
        elif data >= float(cutoffs["Recycled content"]["Overall"]["Range1"]) and data < float(cutoffs["Recycled content"]["Overall"]["Range2"]):
            score = 0.5
        elif data >= float(cutoffs["Recycled content"]["Overall"]["Range2"]) and data < float(cutoffs["Recycled content"]["Overall"]["Range3"]):
            score = 1
        elif data >= float(cutoffs["Recycled content"]["Overall"]["Range3"]) and data < float(cutoffs["Recycled content"]["Overall"]["Range4"]):
            score = 1.5
        elif data >= float(cutoffs["Recycled content"]["Overall"]["Range4"]):
            score = 2
        else:
            score = -1

    elif atr == 'Thermal Barrier':
        if sub_atr == 'Floor Finish and others':
            if data > float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range1"]):
                score = 0
            elif data <= float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range1"]) and data > float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range2"]):
                score = 0.5
            elif data <= float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range2"]) and data > float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range3"]):
                score = 1
            elif data <= float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range3"]) and data > float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range4"]):
                score = 1.5
            elif data <= float(cutoffs["Thermal Barrier"]["Floor Finish and others"]["Range4"]):
                score = 2
            else:
                score = -1
        elif sub_atr ==  'insulation':
            if data > float(cutoffs["Thermal Barrier"]["insulation"]["Range1"]):
                score = 0
            elif data <= float(cutoffs["Thermal Barrier"]["insulation"]["Range1"]) and data > float(cutoffs["Thermal Barrier"]["insulation"]["Range2"]):
                score = 0.5
            elif data <= float(cutoffs["Thermal Barrier"]["insulation"]["Range2"]) and data > float(cutoffs["Thermal Barrier"]["insulation"]["Range3"]):
                score = 1
            elif data <= float(cutoffs["Thermal Barrier"]["insulation"]["Range3"]) and data > float(cutoffs["Thermal Barrier"]["insulation"]["Range4"]):
                score = 1.5
            elif data <= float(cutoffs["Thermal Barrier"]["insulation"]["Range4"]):
                score = 2
            else:
                score = -1
        elif sub_atr == 'U value for windows':
            if data > float(cutoffs["Thermal Barrier"]["U value for windows"]["Range1"]):
                score = 0
            elif data <= float(cutoffs["Thermal Barrier"]["U value for windows"]["Range1"]) and data > float(cutoffs["Thermal Barrier"]["U value for windows"]["Range2"]):
                score = 0.5
            elif data <= float(cutoffs["Thermal Barrier"]["U value for windows"]["Range2"]) and data > float(cutoffs["Thermal Barrier"]["U value for windows"]["Range3"]):
                score = 1
            elif data <= float(cutoffs["Thermal Barrier"]["U value for windows"]["Range3"]) and data > float(cutoffs["Thermal Barrier"]["U value for windows"]["Range4"]):
                score = 1.5
            elif data <= float(cutoffs["Thermal Barrier"]["U value for windows"]["Range4"]):
                score = 2
            else:
                score = -1

    # No 0.5 Score
    elif atr == 'Acoustic Regulator':
        if sub_atr == 'db Reduction wall/floor unit':
            if data < float(cutoffs["Acoustic Regulator"]["db Reduction wall/floor unit"]["Range1"]):
                score = 0
            elif data >= float(cutoffs["Acoustic Regulator"]["db Reduction wall/floor unit"]["Range1"]) and data < float(cutoffs["Acoustic Regulator"]["db Reduction wall/floor unit"]["Range2"]):
                score = 1
            elif data >= float(cutoffs["Acoustic Regulator"]["db Reduction wall/floor unit"]["Range2"]) and data < float(cutoffs["Acoustic Regulator"]["db Reduction wall/floor unit"]["Range3"]):
                score = 1.5
            elif data >= float(cutoffs["Acoustic Regulator"]["db Reduction wall/floor unit"]["Range3"]):
                score = 2
            else:
                score = -1
        elif sub_atr == 'db Reduction insulation, Windows and doors':
            if data < float(cutoffs["Acoustic Regulator"]["db Reduction insulation, Windows and doors"]["Range1"]):
                score = 0
            elif data >= float(
                    cutoffs["Acoustic Regulator"]["db Reduction insulation, Windows and doors"]["Range1"]) and data < float(
                    cutoffs["Acoustic Regulator"]["db Reduction insulation, Windows and doors"]["Range2"]):
                score = 1
            elif data >= float(
                    cutoffs["Acoustic Regulator"]["db Reduction insulation, Windows and doors"]["Range2"]) and data < float(
                    cutoffs["Acoustic Regulator"]["db Reduction insulation, Windows and doors"]["Range3"]):
                score = 1.5
            elif data >= float(cutoffs["Acoustic Regulator"]["db Reduction insulation, Windows and doors"]["Range3"]):
                score = 2
            else:
                score = -1
        elif sub_atr == 'Impact absorption':
            if data < float(cutoffs["Acoustic Regulator"]["Impact absorption"]["Range1"]):
                score = 0
            elif data >= float(
                    cutoffs["Acoustic Regulator"]["Impact absorption"]["Range1"]) and data < float(
                    cutoffs["Acoustic Regulator"]["Impact absorption"]["Range2"]):
                score = 1
            elif data >= float(
                    cutoffs["Acoustic Regulator"]["Impact absorption"]["Range2"]) and data < float(
                    cutoffs["Acoustic Regulator"]["Impact absorption"]["Range3"]):
                score = 1.5
            elif data >= float(cutoffs["Acoustic Regulator"]["Impact absorption"]["Range3"]):
                score = 2
            else:
                score = -1
        elif sub_atr == 'Noise Reduction Coefficient':
            if data < float(cutoffs["Acoustic Regulator"]["Noise Reduction Coefficient"]["Range1"]):
                score = 0
            elif data >= float(
                    cutoffs["Acoustic Regulator"]["Noise Reduction Coefficient"]["Range1"]) and data < float(
                    cutoffs["Acoustic Regulator"]["Noise Reduction Coefficient"]["Range2"]):
                score = 1
            elif data >= float(
                    cutoffs["Acoustic Regulator"]["Noise Reduction Coefficient"]["Range2"]) and data < float(
                    cutoffs["Acoustic Regulator"]["Noise Reduction Coefficient"]["Range3"]):
                score = 1.5
            elif data >= float(cutoffs["Acoustic Regulator"]["Noise Reduction Coefficient"]["Range3"]):
                score = 2
            else:
                score = -1
        else:
            score = -1

    # Happy with this
    elif atr == 'Fire resistance':
        if sub_atr ==  'No Certification':
            score = 0
        elif sub_atr == 'Euro Class C or other':
            score = 0.5
        elif sub_atr == 'Euro Class B':
            score = 1
        elif sub_atr == 'Euro Class A':
            score = 1.5
        else:
            score = 2

    elif atr == 'Moisture Balancing':
        if sub_atr == 'paint MVTR':
            if data < float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range1"]):
                score = 0
            elif data >=float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range1"]) and data < float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range2"]):
                score = 0.5
            elif data >= float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range2"]) and data < float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range3"]):
                score = 1
            elif data >= float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range3"]) and data < float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range4"]):
                score = 1.5
            elif data >= float(cutoffs["Moisture Balancing"]["paint MVTR"]["Range4"]):
                score = 2
            else:
                score = -1
        elif sub_atr == 'paint SD':
            if data > float(cutoffs["Moisture Balancing"]["paint SD"]["Range1"]):
                score = 0
            elif data <= float(cutoffs["Moisture Balancing"]["paint SD"]["Range1"]) and data > float(cutoffs["Moisture Balancing"]["paint SD"]["Range2"]):
                score = 1
            elif data <= float(cutoffs["Moisture Balancing"]["paint SD"]["Range2"]) and data > float(cutoffs["Moisture Balancing"]["paint SD"]["Range3"]):
                score = 1.5
            elif data <= float(cutoffs["Moisture Balancing"]["paint SD"]["Range3"]):
                score = 2
            else:
                score = -1
        elif sub_atr == 'other BMs':
            if data > float(cutoffs["Moisture Balancing"]["other BMs"]["Range1"]):
                score = 0
            elif data <= float(cutoffs["Moisture Balancing"]["other BMs"]["Range1"]) and data > float(cutoffs["Moisture Balancing"]["other BMs"]["Range2"]):
                score = 0.5
            elif data <= float(cutoffs["Moisture Balancing"]["other BMs"]["Range2"]) and data > float(cutoffs["Moisture Balancing"]["other BMs"]["Range3"]):
                score = 1
            elif data <= float(cutoffs["Moisture Balancing"]["other BMs"]["Range3"]) and data > float(cutoffs["Moisture Balancing"]["other BMs"]["Range4"]):
                score = 1.5
            elif data <= float(cutoffs["Moisture Balancing"]["other BMs"]["Range4"]):
                score = 2
            else:
                score = -1
        else:
            score = -1

    else:
        score = -1

    return score


attrs = (
    'Low embodied energy', ## Dropdown  @
    'Low embodied Carbon', ## Dropdown  @
    'Recycled content', # Direct        @
    'Durable', #? Need to explain       @
    'Moisture Balancing', #X
    'Acoustic Regulator', ## Dropdown   @
    'Thermal Barrier', ## Dropdown      @
    'Fire resistance' #Not Applicable   @
)
width = max(map(len, attrs))+1

LER_a = (
    'Overall',
    'Cladding',
    'Flooring',
    'Insulation MJ/m2',
    'Insulation MJ/m3',
    'Interior Finishes',
    'Roofing',
    'Structure'
)

LEC_a = (
    'Overall',
    'Cladding',
    'Flooring',
    'Insulation kgCO2eq/m2',
    'Insulation kgCO2eq/m3',
    'Interior Finishes',
    'Roofing',
    'Structure'
)

DURABLE_a = (
    'Overall',
    'Structure',
    'Walls',
    'Flooring finishes',
    'Paint/Plaster',
    'Insulation',
    'Boards',
    'Roofs',
    'Ceilings',
    'Window & Door'
)

THERMAL_a = (
    'Floor Finish and others',
    'insulation',
    'U value for windows'
)

ACOUSTIC_a = (
    'db Reduction wall/floor unit',
    'db Reduction insulation, Windows and doors',
    'Impact absorption',
    'Noise Reduction Coefficient'
)

FIRE_a = (
    'No Certification',
    'Euro Class C or other',
    'Euro Class B',
    'Euro Class A',
    'Higher than Euro Class A'
)

MOIST_a = (
    'paint SD',
    'paint MVTR',
    'other BMs'
)

try:
    layout = [
        [sg.Image('FirstPlanit_logo')],
        [sg.Text('Multiplier Calculator', font='Lucida', text_color='Black')],
        [sg.Combo(attrs, size=(30, 1), enable_events=True, key='-COMBO-', default_value=attrs[0])],
        [sg.Combo(LER_a, size=(30, 1), enable_events=True, key='-COMBO2-', default_value=LER_a[0])],
        [sg.Text('Data: '), sg.InputText(size=(25, 1), key='data')],
        [sg.Button("Submit")],
        [sg.Text('Score: '), sg.InputText(size=(24, 1), key='score')],
        [sg.Button("Exit")]
    ]

    window  = sg.Window(title = "Firstplanit MulCal", layout=layout, margins=(100, 50))

    while True:
        try:
            event, values = window.read()
            val_val = list(values.values())
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            elif event == "-COMBO-":
                if val_val[0] == 'Low embodied energy':
                    item = values[event]
                    window['-COMBO2-'].update(value=LER_a[0], values=LER_a)
                    window['data'].update("")
                elif val_val[0] == 'Low embodied Carbon':
                    item = values[event]
                    window['-COMBO2-'].update(value=LEC_a[0], values=LEC_a)
                    window['data'].update("")
                elif val_val[0] == 'Durable':
                    item = values[event]
                    window['-COMBO2-'].update(value=DURABLE_a[0], values=DURABLE_a)
                    window['data'].update("")
                elif val_val[0] == 'Thermal Barrier':
                    item = values[event]
                    window['-COMBO2-'].update(value=THERMAL_a[0], values=THERMAL_a)
                    window['data'].update("")
                elif val_val[0] == 'Acoustic Regulator':
                    item = values[event]
                    window['-COMBO2-'].update(value=ACOUSTIC_a[0], values=ACOUSTIC_a)
                    window['data'].update("")
                elif val_val[0] == 'Fire resistance':
                    item = values[event]
                    window['-COMBO2-'].update(value=FIRE_a[0], values=FIRE_a)
                    window['data'].update("Not Applicable")
                elif val_val[0] == 'Moisture Balancing':
                    item = values[event]
                    window['-COMBO2-'].update(value=MOIST_a[0], values=MOIST_a)
                    window['data'].update("")
                elif val_val[0] == 'Recycled content': #CHECK DROP DOWN
                    item = values[event]
                    window['-COMBO2-'].update(value="Not Applicable", values="")
                    window['data'].update("")
                else:
                    window['data'].update("")

            elif event == "Submit":
                print(event, values)
                score = score_cal(val_val[0], val_val[1], val_val[2])
                window['score'].update(score)

        except Exception as e:
            print("An exception occurred:\n", e)
            with open('logs.txt', 'a') as output:
                current_datetime = datetime.now()
                output.write(str(current_datetime) + ' :INSIDE EXCEPTION: ' + str(e) + '\n')
            window['score'].update("Error, Check Logs!")

    window.close()

except Exception as e:
    with open('logs.txt', 'a') as output:
        current_datetime = datetime.now()
        output.write(str(current_datetime) + ' ' + str(e) + '\n')
    print(e)