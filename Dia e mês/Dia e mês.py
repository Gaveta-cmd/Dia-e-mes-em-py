dia_niver = int(input("Qual dia vc nasceu:"))
mes_niver = int(input("Qual o mes: "))
dia_hj = int(input("Que dia é hj: "))
mes_hj = int(input("Que mes é hj: "))
calculo1 = dia_hj + mes_hj * 30
calculo2 = dia_niver + mes_niver * 30
calculo3 = calculo1 - calculo2
calculo4 = calculo2 - calculo1
if calculo1 == calculo2:
    print("Parabéns hj é seu aniversário!")
elif calculo1 > calculo2:
    print(f"Se passou {calculo3} dias para o seu aniversário!")
elif calculo2 > calculo1:
    print(f"Faltam {calculo4} dias do seu aniversário!")