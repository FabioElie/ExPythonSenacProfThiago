# Crie uma função que receba como argumento a potência 
# elétrica de determinado aparelho e o tempo ligado e retorne o 
# consumo em KWh em seguida chame outra função para calcular a 
# conta de energia, levando em consideração o  consumo e o valor 
# do KWh como argumentos. Em seguida, chame uma outra função 
# para calcular o valor da conta de acordo com o consumo 
# calculado

def calcular_consumo(potencia_watts, tempo_horas):
    potencia_kw = potencia_watts / 1000
    consumo = potencia_kw * tempo_horas
    return consumo


def calcular_valor_energia(consumo_kwh, valor_kwh):
    valor = consumo_kwh * valor_kwh
    return valor


def calcular_conta(potencia_watts, tempo_horas, valor_kwh):
    consumo = calcular_consumo(potencia_watts, tempo_horas)
    valor_final = calcular_valor_energia(consumo, valor_kwh)
    
    print(f"Consumo Total: {consumo:.2f} kWh")
    print(f"Valor a pagar de energia: R${valor_final:.2f}")
    
    return valor_final


calcular_conta(1500, 5, 800)