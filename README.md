
# Requisitos Funcionales

## R1 - Registrar jugador

- **Resumen:** El sistema debe permitir registrar un jugador para poder iniciar un juego.

- **Entradas:** 
  - Nombre del jugador

- **Resultado:**
  1. El sistema muestra un mensaje dando la bienvenida al jugador.
  2. El sistema carga 100 fichas al jugador.
  3. El sistema le muestra el menú con la opción para iniciar un nuevo juego.

- **Pasos:**

  | Paso              | Método                   | Responsable |
  |-------------------|--------------------------|-------------|
  | Registrar jugador | registrar_jugador(nombre) | Blackjack   |
  | Crear jugador     | __init__(nombre, fichas) | Jugador     |

## R2 – Iniciar juego

- **Resumen:** El sistema permite iniciar un juego, repartiendo las cartas al jugador y la casa.

- **Entradas:**
  - Apuesta (cantidad de fichas)

- **Resultado:**
  1. El sistema recibe la apuesta del jugador.
  2. Revolver las cartas.
  3. El sistema reparte dos cartas destapadas al jugador.
  4. El sistema reparte dos cartas a la casa, una destapada y la otra tapada.
  5. El sistema verifica si la mano del jugador es blackjack.
     - 5.1 Si tiene blackjack, se ejecuta el requisito R5 Finalizar juego.
     - 5.2 Si no tiene blackjack, se ejecuta el requisito R3 Hacer jugada jugador.

- **Pasos:**

  | Paso             | Método                 | Responsable |
  |------------------|------------------------|-------------|
  | Iniciar juego    | Iniciar_juego(apuesta) | Blackjack   |
  | Revolver las cartas | revolver()            | Baraja      |
  | Repartir carta   | repartir_carta(tapada: bool) -> Carta | Baraja |
  | Iniciar la mano  | inicializar_mano(cartas) | Casa, Jugador |
  | Crear mano       | __init__(carta)        | Mano        |
  | Verificar si la mano es blackjack | es_blackjack() -> bool | Mano |

- **Controlador Blackjack:** Recibe información de la otra capa (interfaz con el usuario).

## R3 – Hacer jugada del jugador

- **Resumen:** El sistema debe permitir que el jugador realice una jugada durante su turno.

- **Entradas:**
  - Tipo de jugada (pedir carta o plantarse)

- **Resultado:**
  1. El sistema solicita al jugador que seleccione una jugada.
  2. Si el jugador pide una carta:
     - 2.1 El sistema le reparte una carta a la mano del jugador.
     - 2.2 Si el valor de la mano del jugador es mayor a 21, se ejecuta el requisito R5 finalizar juego.
     - 2.3 Si el valor de la mano no supera 21, se vuelve a ejecutar el requisito R3.
  3. Si el jugador se planta:
     - 3.1 Se calcula el valor de la mano, se muestra y se guarda.
     - 3.2 Se ejecuta el requisito R4 hacer jugada de la casa.

- **Pasos:**

  | Paso               | Método                | Responsable |
  |--------------------|-----------------------|-------------|
  | Solicitar jugada   | Seleccionar_jugada()  | Blackjack   |
  | Pedir carta (jugador) | pedir_carta() -> Carta | Baraja   |
  | El jugador se planta | plantarse_jugador() | Jugador     |

## R4 – Hacer jugada de la casa

- **Resumen:** El sistema debe permitir que la casa realice una jugada durante su turno.

- **Entradas:** Ninguna

- **Resultado:**
  1. Destapar la carta oculta de la casa.
  2. Si la mano de la casa es blackjack:
     - 2.1 Se ejecuta el requisito R5 finalizar juego (la casa gana).
  3. Si la mano de la casa no es blackjack:
     - 3.1 Si la mano de la casa es menor o igual que 16 y menor que la mano del jugador:
       - 3.1.1 Se reparte una carta a la mano de la casa.
       - 3.1.2 Se calcula el valor de la mano y se vuelve a evaluar (punto 3.1).
     - 3.2 Si la mano de la casa es mayor a 16 y menor o igual a 21:
       - 3.2.1 Se ejecuta el requisito R5 Finalizar juego.
     - 3.3 Si la mano de la casa se pasó de 21:
       - 3.3.1 Se ejecuta el requisito R5 Finalizar juego.

- **Pasos:**

  | Paso               | Método                 | Responsable |
  |--------------------|------------------------|-------------|
  | Destapar carta      | destapar_carta(self) -> bool | Casa    |
  | Verificar jugada   | es_blackjack() -> bool | Mano        |
  | Jugada de la casa  | Jugada_casa(self) -> Mano | Casa      |

## R5 – Finalizar juego

- **Resumen:** El sistema debe permitir que se finalice la partida y se determine el ganador.

- **Entradas:** Ninguna

- **Resultado:**
  1. El sistema compara las manos del jugador y de la casa.
  2. Si el jugador tiene blackjack, su mano es mayor que la mano de la casa o la mano de la casa superó 21:
     - 2.1 El sistema anuncia al jugador como ganador.
     - 2.2 Se doblan las fichas de la apuesta realizada.
  3. Si la casa tiene blackjack, su mano es mayor que la mano del jugador o la mano del jugador superó 21:
     - 3.1 El sistema anuncia que el jugador perdió.
     - 3.2 Se restan las fichas de la apuesta de las fichas del jugador.
  4. Si la mano del jugador y la mano de la casa tienen el mismo valor:
     - 4.1 El sistema anuncia empate.
     - 4.2 Se devuelven las fichas apostadas al jugador.
  5. Si el usuario tiene fichas disponibles:
     - 5.1 Se presenta un menú con las opciones para iniciar un nuevo juego (R2) o salir de la aplicación.
  6. Si el usuario no tiene fichas disponibles:
     - 6.1 Se termina la aplicación.

  | Paso                     | Método                        | Responsable |
  |--------------------------|-------------------------------|-------------|
  | Compara las manos de la casa y jugador | comparar_manos(self, mano_jugador: Mano, mano_casas: Mano) | Blackjack |
  | Seguir jugando           | seguir_jugando(self, fichas: int) | Blackjack   |
  | Finalizar partida        | finalizar_partida(self, fichas: int) | Blackjack |

# Modelo del mundo

- Blackjack
- Jugador
  - Fichas
  - Nombre
- Carta
  - Pinta
  - Valor
- Casa
- Mano
- Baraja
![Modelo del mundo](requirements/UML.01.png)