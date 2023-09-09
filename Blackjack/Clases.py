
class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False


class Baraja:
    def __init__(self):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass

    def repartir_cartas(self, tapada: bool) -> Carta:
        pass

    def pedir_carta(self) -> Carta:
        pass


class Mano:
    def __init__(self, cartas: tuple[Carta, Carta]):
        self.cartas: list[Carta] = []

    def es_blackjack(self) -> bool:
        pass


    def repartir_carta(self, carta: Carta):
        pass


class Casa:
    def __init__(self):
        self.mano: Mano = None

    def inicializar_mano(self, cartas: tuple[Carta, Carta]):
        pass

    def destapar_carta(self) -> bool:
        pass

    def plantarse_casa(self):
        pass

    def jugada_casa(self)-> Mano:
        pass


class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas
        self.mano: Mano = None

    def plantarse_jugador(self):
        pass

class Blackjack:
    def __init__(self):
        self.jugador: Jugador = None
        self.cupier: Casa = None
        self.baraja: Baraja = None

    def registrar_jugador(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass

    def seleccionar_jugada(self):
        pass

    def comaparar_manos(self, mano_jugador: Mano, mano_casas: Mano):
        pass

    def seguir_jugando(self, fichas: int):
        pass

    def finalizar_partida(self,fichas: int):
        pass
