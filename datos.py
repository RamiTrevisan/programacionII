from personajes import Bardo, Cazador, Clerigo, Guerrero, Mago, Paladin

def obtener_personajes():
    bardo = Bardo("Bardo", 5, 80, 90)
    cazador = Cazador("Cazador", 6, 75, 85)
    clerigo = Clerigo("Clerigo", 7, 90, 95)
    guerrero = Guerrero("Guerrero", 8, 85, 90)
    mago = Mago("Mago", 9, 95, 100)
    paladin = Paladin("Paladin", 10, 85, 95)
    
    return [bardo, cazador, clerigo, guerrero, mago, paladin]
