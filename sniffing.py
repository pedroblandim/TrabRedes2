from camada_enlace import SocketBaixoNivel, Ethernet
from camada_rede import IP
from embelezador_ethernet import Filtro

socket = SocketBaixoNivel()
ethernet = Ethernet(bytes_socket=socket)

try:

	for quadro in ethernet.quadros():

		Filtro(quadro_ethernet=quadro).pormenorizar(numero=ethernet.contador_quadros)

except KeyboardInterrupt:

	socket.fechar()

	print("\nSniffador fechou o socket! Programa finalizado")
