def salario (horas, salarioBase):
    if horas <= 40:
        print(f"O seu salario foi somente o salario base de {salarioBase}")
    else:
        horasExtras = horas - 40
        valorPorHoraBase = salarioBase / 40 
        valorPorHoraExtra = valorPorHoraBase + (valorPorHoraBase * 0.5) 
        salarioAdicional = valorPorHoraExtra * horasExtras
        salarioTotal = salarioBase + salarioAdicional
        print(f"O seu salario foi de {salarioTotal}, sendo que voce trabalho {horasExtras} horas extras, recebendo um adicional de {salarioAdicional}")

salario(50, 1000)