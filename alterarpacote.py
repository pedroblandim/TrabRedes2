from camada_enlace import SocketBaixoNivel, Ethernet
from camada_rede import IP
from embelezador_ethernet import Filtro

socket = SocketBaixoNivel()
ethernet = Ethernet(bytes_socket=socket)

try:

    quadro = ethernet.pegar_quadro()
    Filtro(quadro_ethernet=quadro).pormenorizar(numero=ethernet.contador_quadros)

    quadro.change_orig('127.0.0.1')
    Filtro(quadro_ethernet=quadro).pormenorizar(numero=ethernet.contador_quadros)

except KeyboardInterrupt:

	socket.fechar()

	print("\nSniffador fechou o socket! Programa finalizado")
