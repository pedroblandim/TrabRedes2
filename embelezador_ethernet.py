from camada_enlace import Ethernet
from camada_rede import IP
from camada_transporte import Transporte
#Classe que representa a transformação dos dados em linhas legíveis no teminal
class Filtro:

	def __init__(self, quadro_ethernet):
		self.quadro = quadro_ethernet
		self.datagrama_IP = IP.Datagrama(bytes_brutos=self.quadro.data)

	def pormenorizar(self, numero):
		if self.quadro.type == Ethernet.Quadro.IPv4_TYPE:
			self.printar("Quadro Ethernet {}".format(numero), recuo=0)
			self.printar("MAC Origem:\t\t\t{}".format(self.quadro.dest, numero), recuo=1)
			self.printar("MAC Destino:\t\t\t{}".format(self.quadro.orig, numero), recuo=1)
			self.mostrar_IP()
		#else:
		#	self.printar("Quadro Ethernet {} tipo {} (não IPv4)".format(numero, self.quadro.type))

	def mostrar_IP(self):
		self.printar("Datagrama IPv{}".format(str(self.datagrama_IP.versao)), recuo=2)
		self.printar(("Tempo de vida (TTL):\t\t" + str(self.datagrama_IP.ttl)), recuo=3)
		self.printar("Protocolo superior:\t\t{}".format('TCP' if self.datagrama_IP.protocolo == IP.Datagrama.TCP else 'UDP' if self.datagrama_IP.protocolo == IP.Datagrama.UDP else str(self.datagrama_IP.protocolo)), recuo=3)
		self.printar("Endereço de Origem:\t\t{} ({})".format(self.datagrama_IP.orig, IP.reverse_lookup(addr=self.datagrama_IP.orig)), recuo=3)
		self.printar("Endereço de Destino:\t\t{} ({})".format(self.datagrama_IP.dest, IP.reverse_lookup(addr=self.datagrama_IP.dest)), recuo=3)
		self.printar("Tamanho dos dados:\t\t{} bytes".format(str(len(self.datagrama_IP.dados))), recuo=3)

		if self.datagrama_IP.protocolo == IP.Datagrama.TCP:
			self.mostrar_TCP()
		elif self.datagrama_IP.protocolo == IP.Datagrama.UDP:
			self.mostrar_UDP()

	def mostrar_TCP(self):
		pacote_TCP = Transporte.SegmentoTCP(bytes_brutos=self.datagrama_IP.dados)
		self.printar("Segmento TCP", recuo=4)
		self.printar("Porta de origem:\t\t{} {}".format(pacote_TCP.orig_porta,Transporte.apelido_porta(pacote_TCP.orig_porta, 'tcp')), recuo=5)
		self.printar("Porta de destino:\t\t{} {}".format(pacote_TCP.dest_porta,Transporte.apelido_porta(pacote_TCP.dest_porta, 'tcp')), recuo=5)
		self.printar("Número de sequência:\t{}".format(pacote_TCP.sequencia), recuo=5)
		self.printar("Número de reconhecimento:\t{}".format(pacote_TCP.reconhecimento), recuo=5)
		self.printar("Comprimento do cabecalho:\t{} palavras de 32 bits ({} bytes)".format(pacote_TCP.comprimento_cabecalho, pacote_TCP.comprimento_cabecalho * 4), recuo=5)
		self.printar("Janela de recepção:\t{}".format(pacote_TCP.janela_recepcao), recuo=5)
		self.printar("Soma de verificação:\t{}".format(pacote_TCP.soma_verificacao), recuo=5)
		self.printar("Ponteiro de urgência:\t{} ".format(pacote_TCP.ponteiro_urgencia), recuo=5)
		self.printar("Comprimento de opções:\t{} bytes".format(len(pacote_TCP.opcoes)), recuo=5)
		self.printar("Comprimento dos dados:\t{} bytes".format(len(pacote_TCP.dados)), recuo=5)
		self.printar("URG:{} ACK:{} PSH:{} RST:{} SYN:{} FIN:{} ".format(*pacote_TCP.flags), recuo=5)

	def mostrar_UDP(self):
		pacote_UDP = Transporte.SegmentoUDP(bytes_brutos=self.datagrama_IP.dados)
		self.printar("Segmento UDP", recuo=4)
		self.printar("Porta de origem:\t\t{} {}".format(pacote_UDP.orig_porta, Transporte.apelido_porta(pacote_UDP.orig_porta)), recuo=5)
		self.printar("Porta de destino:\t\t{} {}".format(pacote_UDP.dest_porta,Transporte.apelido_porta(pacote_UDP.dest_porta)), recuo=5)
		self.printar("Comprimento do segmento:\t{} bytes".format(pacote_UDP.comprimento), recuo=5)
		self.printar("Soma de verificação:\t{}".format(pacote_UDP.soma_verificacao), recuo=5)
		self.printar("Comprimento dados:\t\t{} bytes".format(len(pacote_UDP.dados)), recuo=5)

	def printar(self, txt, recuo=0):
		str_recuo = ' ' * recuo
		print(str_recuo + txt)