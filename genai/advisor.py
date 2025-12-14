from model import predictor


def genai_advisor(input_data):
    delay = predictor.predict_delay(input_data)

    fatores = []

    if input_data["chuva"]:
        fatores.append("chuva")
    if input_data["feriado"]:
        fatores.append("feriado")
    if input_data["dia_jogo"]:
        fatores.append("dia de jogo")
    if input_data["transito_nivel"] >= 4:
        fatores.append("trânsito intenso")
    if input_data["volume_pedidos"] > 200:
        fatores.append("alto volume de pedidos")

    fatores_str = ", ".join(fatores) if fatores else "condições normais"

    explicacao = f"""
A previsão indica um atraso médio de aproximadamente {delay} minutos.

Os principais fatores que impactam esse cenário são: {fatores_str}.

Recomendações operacionais:
- Reforçar a quantidade de entregadores neste período.
- Antecipar o preparo dos pedidos em horários críticos.
- Ajustar o raio de entrega temporariamente.
- Priorizar pedidos com maior SLA.

Essa análise permite decisões proativas para reduzir atrasos e melhorar a experiência do cliente.
"""

    return delay, explicacao
