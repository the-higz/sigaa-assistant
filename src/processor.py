from datetime import datetime

def processar_atividades(atividades):

    agora = datetime.now()

    for atividade in atividades:

        data_convertida = datetime.strptime(
            atividade["data"],
            "%d/%m/%Y %H:%M"
        )

        situacao = data_convertida > agora

        atividade["ativa"] = situacao

    return atividades

def filtrar_ativas(atividades):

    atividades_filtradas = []

    for atividade in atividades:

        if atividade["ativa"]:
            atividades_filtradas.append(atividade)

    return atividades_filtradas