#  Copyright (c) 2024 by https://github.com/LunaDEV-net.
#  all rights reserved

from configuration import Default, configuration as config
import runtime_tests

def setup_data(data_dict: dict, beobachtungs_id, stationsname, beobachtet_von, beobachtet_bis) -> dict:
    # setup
    if data_dict.get(beobachtungs_id) != None:
        return data_dict

    # Wenn es noch kein Eintrag für die BeobachtungsID gibt
    data_dict[beobachtungs_id] = [[], [], [], []]  # erstelle die zeilen gesamt, ärzte, pflege, andere
    for i in range(67):
        data_dict[beobachtungs_id][0].append(None)  # fülle die zeilen
        data_dict[beobachtungs_id][1].append(None)  # fülle die zeilen
        data_dict[beobachtungs_id][2].append(None)  # fülle die zeilen
        data_dict[beobachtungs_id][3].append(None)  # fülle die zeilen
    # gebe erste daten ein
    for i in range(4):
        data_dict[beobachtungs_id][i][config.POS_STATIONSNAME] = stationsname
        # data_dict[beobachtungs_id][i][config.POS_OFFIZIELLE_ART] = "Offizielle Art"
        # data_dict[beobachtungs_id][i][config.POS_TYP] = "TYP"
        # data_dict[beobachtungs_id][i][config.POS_AUTOMATISCHE_BEZEICHNUNG] = "Automat. Bezeichnung"
        # data_dict[beobachtungs_id][i][config.POS_BEOBACHTET_BIS_AUTO] = "Beob. bis (MM-JJJJ)"
        # data_dict[beobachtungs_id][i][config.POS_BERUFSGRUPPE] = "Berufsgruppe (soll nachher überschrieben werden)"
        # data_dict[beobachtungs_id][i][config.POS_HANDSCHUHE_ERHOBEN] = "Handschuhe erhoben?"
        data_dict[beobachtungs_id][i][config.POS_BEOBACHTET_VON] = beobachtet_von
        data_dict[beobachtungs_id][i][config.POS_BEOBACHTET_BIS] = beobachtet_bis

        data_dict[beobachtungs_id][i][config.POS_BEOBACHTUNGEN_GESAMT] = 0
        data_dict[beobachtungs_id][i][config.POS_HDS_GESAMT] = 0

        for key in config.indexe_indikatoren:
            data_dict[beobachtungs_id][i][config.indexe_indikatoren[key]] = 0  # Gesamt
            data_dict[beobachtungs_id][i][config.indexe_indikatoren[key] + 1] = 0  # HDs
            data_dict[beobachtungs_id][i][config.indexe_indikatoren[key] + 2] = 0  # Compliance
            data_dict[beobachtungs_id][i][config.indexe_indikatoren[key] + 3] = 0  # HS
    data_dict[beobachtungs_id][0][config.POS_BERUFSGRUPPE] = "Gesamt"
    data_dict[beobachtungs_id][1][config.POS_BERUFSGRUPPE] = "Ärzte"
    data_dict[beobachtungs_id][2][config.POS_BERUFSGRUPPE] = "Pflegepersonal"
    data_dict[beobachtungs_id][3][config.POS_BERUFSGRUPPE] = "Andere"

    return data_dict

def count_data(data_dict: dict, beobachtungs_id, berufindex, indikatorindex, hd, handschuhe) -> dict:
    # fein
    data_dict[beobachtungs_id][0][indikatorindex] += 1  # Gesamt Job egal
    data_dict[beobachtungs_id][berufindex][indikatorindex] += 1  # Gesamt Job spez
    if hd == "Ja":
        data_dict[beobachtungs_id][0][indikatorindex + 1] += 1  # HDs Job egal
        data_dict[beobachtungs_id][berufindex][indikatorindex + 1] += 1  # HDs. Job spez
    if handschuhe == "Ja":
        data_dict[beobachtungs_id][0][indikatorindex + 3] += 1  # HDs Job egal
        data_dict[beobachtungs_id][berufindex][indikatorindex + 3] += 1  # HDs. Job spez



def update_data_dict(data_dict: dict, beobachtungs_id, berufsgruppe, indikator, hd, handschuhe) -> dict:
    berufindex = config.indexe_berufsgruppen[berufsgruppe]
    indikatorindex = ""
    if not indikator.startswith("vor asept. Tätigkeit: "):
        indikatorindex = config.indexe_indikatoren[indikator]
    elif indikator.startswith("vor asept. Tätigkeit: "):
        indikatorindex = config.indexe_indikatoren["vor asept. Tätigkeit: *"]

    # gesamt vorne
    data_dict[beobachtungs_id][0][config.POS_BEOBACHTUNGEN_GESAMT] += 1
    data_dict[beobachtungs_id][berufindex][config.POS_BEOBACHTUNGEN_GESAMT] += 1
    if hd == "Ja":
        data_dict[beobachtungs_id][0][config.POS_HDS_GESAMT] += 1
        data_dict[beobachtungs_id][berufindex][config.POS_HDS_GESAMT] += 1
    # GIbt kein Feld für Handschuhe vorne

    count_data(data_dict, beobachtungs_id, berufindex, indikatorindex, hd, handschuhe)
    if not indikator.startswith("vor asept. Tätigkeit: "):
        return data_dict
    # elif indikator.startswith("vor asept. Tätigkeit: "):
    ganzfein_indikatorindex = config.indexe_indikatoren[indikator]
    count_data(data_dict, beobachtungs_id, berufindex, ganzfein_indikatorindex, hd, handschuhe)

    return data_dict


def calculate_compliance(data_dict: dict) -> dict:
    for beob_id in data_dict.keys():
        for i in range(len(data_dict[beob_id])):  # len(beob_id) = 4
            for comp_index in config.compliance:
                beob = data_dict[beob_id][i][comp_index - 2]
                hds = data_dict[beob_id][i][comp_index - 1]
                data_dict[beob_id][i][comp_index] = int(round(hds / beob * 100, 0)) if beob != 0 else ""
    return data_dict

def process_data(data_in: list) -> dict:
    data_dict: dict = {}
    runtime_tests.check_data(data_in)
    for line in data_in:
        beobachtungs_id = line[config.beobachtungs_id]
        stationsname = line[config.stationsname]
        beobachtet_von = line[config.beobachtet_von]
        beobachtet_bis = line[config.beobachtet_bis]
        berufsgruppe = line[config.berufsgruppe]
        indikator = line[config.indikator]
        hd = line[config.hd]
        handschuhe = line[config.handschuhe]

        data_dict = setup_data(data_dict, beobachtungs_id, stationsname, beobachtet_von, beobachtet_bis)
        data_dict = update_data_dict(data_dict, beobachtungs_id, berufsgruppe, indikator, hd, handschuhe)
    data_dict = calculate_compliance(data_dict)


    return data_dict