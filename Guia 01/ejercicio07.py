"""Ejercicio 7:
Crear un programa que calcule el sueldo bruto de una persona que trabaja de lunes a viernes 8 hs y su pago por hora es de 400 pesos. Devolver el sueldo por pantalla."""

valor_hora = 400
horas_por_dia = 8
cantidad_dias = 5

sueldo_bruto_semana = valor_hora * horas_por_dia * cantidad_dias

sueldo_bruto_mes = sueldo_bruto_semana * 4

print(sueldo_bruto_mes)
