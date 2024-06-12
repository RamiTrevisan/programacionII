class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.puntos = 0

    def mostrar_habilidades(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def incrementar_puntos(self, puntos_ganados):
        self.puntos += puntos_ganados

class Bardo(Personaje):
    def __init__(self, nombre, nivel, poder_lamento, astucia):
        super().__init__(nombre, nivel)
        self.poder_lamento = poder_lamento
        self.astucia = astucia

    def mostrar_habilidades(self):
        return f"Lamento: {self.poder_lamento}, Astucia: {self.astucia}"

class Cazador(Personaje):
    def __init__(self, nombre, nivel, flecha_divina, arco_reforzado):
        super().__init__(nombre, nivel)
        self.flecha_divina = flecha_divina
        self.arco_reforzado = arco_reforzado

    def mostrar_habilidades(self):
        return f"Flecha Divina: {self.flecha_divina}, Arco Reforzado: {self.arco_reforzado}"

class Clerigo(Personaje):
    def __init__(self, nombre, nivel, curar_criticas, poder_divino):
        super().__init__(nombre, nivel)
        self.curar_criticas = curar_criticas
        self.poder_divino = poder_divino

    def mostrar_habilidades(self):
        return f"Curar Críticas: {self.curar_criticas}, Poder Divino: {self.poder_divino}"

class Guerrero(Personaje):
    def __init__(self, nombre, nivel, golpe_furtivo, poder_igneo):
        super().__init__(nombre, nivel)
        self.golpe_furtivo = golpe_furtivo
        self.poder_igneo = poder_igneo

    def mostrar_habilidades(self):
        return f"Golpe Furtivo: {self.golpe_furtivo}, Poder Ígneo: {self.poder_igneo}"

class Mago(Personaje):
    def __init__(self, nombre, nivel, juicio_final, apocalipsis):
        super().__init__(nombre, nivel)
        self.juicio_final = juicio_final
        self.apocalipsis = apocalipsis

    def mostrar_habilidades(self):
        return f"Juicio Final: {self.juicio_final}, Apocalipsis: {self.apocalipsis}"

class Paladin(Personaje):
    def __init__(self, nombre, nivel, castigo_divino, honor):
        super().__init__(nombre, nivel)
        self.castigo_divino = castigo_divino
        self.honor = honor

    def mostrar_habilidades(self):
        return f"Castigo Divino: {self.castigo_divino}, Honor: {self.honor}"
