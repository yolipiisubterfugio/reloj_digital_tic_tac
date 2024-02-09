class RelojDigital:
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        self.horas = horas % 24
        self.minutos = minutos
        self.segundos = segundos
        
    def info(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}" #:02d es para poner el numerode ceros que queremos de formato delante del dato
    
    def avanzar_tiempo(self):
        self.segundos += 1

        if self.segundos >= 60:
            self.minutos += 1
            self.segundos %= 60

        if self.minutos >= 60:
            self.horas += 1
            self.minutos %= 60

        self.horas %= 24

    def tic(self):
        self.segundos += 1

        # Ajustar los minutos y los segundos si exceden 60
        if self.segundos >= 60:
            self.minutos += 1
            self.segundos = 0

        if self.minutos >= 60:
            self.horas += 1
            self.minutos = 0