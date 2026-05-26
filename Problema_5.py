def calcular_resumen_jornada(recurso, umbral=40):
	nombre = recurso[0]
	horas_semanales = recurso[1:]
	total_horas = sum(horas_semanales)
	clasificacion = "Sobretiempo" if total_horas > umbral else "Horario Estándar o inferior"
	return nombre, total_horas, clasificacion


matriz_horas = [
	["Ana", 8, 8, 9, 8, 8],
	["Luis", 7, 8, 8, 7, 8],
	["Marta", 9, 9, 8, 9, 8],
	["Carlos", 8, 8, 8, 8, 10],
]


for recurso in matriz_horas:
	nombre, total_horas, clasificacion = calcular_resumen_jornada(recurso)
	print(f"Recurso: {nombre}")
	print(f"Total de horas semanales: {total_horas}")
	print(f"Clasificación de jornada: {clasificacion}")
	print("-" * 40)
