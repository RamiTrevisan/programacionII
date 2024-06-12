import random
from personajes import Bardo, Cazador, Clerigo, Guerrero, Mago, Paladin
from datos import obtener_personajes

def crear_personaje():
    print("Crear nuevo personaje:")
    nombre = input("Nombre: ")
    nivel = int(input("Nivel: "))
    clase = input("Clase (Bardo, Cazador, Clerigo, Guerrero, Mago, Paladin): ").lower()
    
    if clase == "bardo":
        poder_lamento = int(input("Poder de Lamento: "))
        astucia = int(input("Astucia: "))
        return Bardo(nombre, nivel, poder_lamento, astucia)
    elif clase == "cazador":
        flecha_divina = int(input("Flecha Divina: "))
        arco_reforzado = int(input("Arco Reforzado: "))
        return Cazador(nombre, nivel, flecha_divina, arco_reforzado)
    elif clase == "clerigo":
        curar_criticas = int(input("Curar Críticas: "))
        poder_divino = int(input("Poder Divino: "))
        return Clerigo(nombre, nivel, curar_criticas, poder_divino)
    elif clase == "guerrero":
        golpe_furtivo = int(input("Golpe Furtivo: "))
        poder_igneo = int(input("Poder Ígneo: "))
        return Guerrero(nombre, nivel, golpe_furtivo, poder_igneo)
    elif clase == "mago":
        juicio_final = int(input("Juicio Final: "))
        apocalipsis = int(input("Apocalipsis: "))
        return Mago(nombre, nivel, juicio_final, apocalipsis)
    elif clase == "paladin":
        castigo_divino = int(input("Castigo Divino: "))
        honor = int(input("Honor: "))
        return Paladin(nombre, nivel, castigo_divino, honor)
    else:
        print("Clase no válida.")
        return None

def mostrar_personajes(personajes):
    print("Lista de personajes:")
    for i, personaje in enumerate(personajes):
        print(f"{i+1}. {personaje.nombre} (Nivel {personaje.nivel}) - Habilidades: {personaje.mostrar_habilidades()}")

def simular_combate(personajes):
    print("Simulación de combate:")
    mostrar_personajes(personajes)
    indice1 = int(input("Seleccione el primer personaje (1-6): ")) - 1
    indice2 = int(input("Seleccione el segundo personaje (1-6): ")) - 1

    if 0 <= indice1 < len(personajes) and 0 <= indice2 < len(personajes):
        print("¡Combate!")
        print(f"{personajes[indice1].nombre} VS {personajes[indice2].nombre}")
        
        ganador = random.choice([personajes[indice1], personajes[indice2]])
        print(f"El ganador es {ganador.nombre}!")
    else:
        print("Índices de personajes no válidos.")

def menu():
    print("---- Menú ----")
    print("1. Crear Personaje")
    print("2. Mostrar Personajes")
    print("3. Simular Combate")
    print("4. Salir")

def main():
    personajes = obtener_personajes()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_personaje = crear_personaje()
            if nuevo_personaje:
                personajes.append(nuevo_personaje)
        elif opcion == "2":
            mostrar_personajes(personajes)
        elif opcion == "3":
            simular_combate(personajes)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
