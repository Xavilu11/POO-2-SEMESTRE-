# Temperaturas 1
# Programación tradicional  
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 17}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp":26}
        ]
    ]
]
ciudades = ["Quito","Guayaquil"]
# Calculamos el promedio de temperaturas para cada ciudad
for i, ciudad in enumerate(ciudades):
    print(f"Promedios de temperatura para {ciudad}:")
    for semana in range(4):
        total_temperatura = 0
        for dia in range(7):
            total_temperatura += temperaturas[i][semana][dia]["temp"]
        promedio = total_temperatura / 7
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
