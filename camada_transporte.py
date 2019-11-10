import struct
import socket

#Ver também página 141 do Kurose
#https://docs.python.org/3/library/stdtypes.html
#

class Transporte:

	#Pega o nome do serviço que geralmente usa a porta https://pt.wikipedia.org/wiki/Lista_de_portas_dos_protocolos_TCP_e_UDP
	def apelido_porta(porta, proto='udp'):
		try:
			return socket.getservbyport(porta, proto)
		except:
			return ''

	#Conforme página 148 do Kurose
	class SegmentoUDP:
		def __init__(self, bytes_brutos):
			self.orig_porta, self.dest_porta, self.comprimento, self.soma_verificacao = struct.unpack('! H H H H', bytes_brutos[:8])
			self.dados = bytes_brutos[8:]

	#Conforme página 172 do Kurose
	class SegmentoTCP:
		def __init__(self, bytes_brutos):
			self.orig_porta, self.dest_porta, self.sequencia, self.reconhecimento, comprimento_cabecalho_bruto, flags_brutos, self.janela_recepcao, self.soma_verificacao, self.ponteiro_urgencia = struct.unpack('! H H L L B B H H H', bytes_brutos[:20])
			self.comprimento_cabecalho = comprimento_cabecalho_bruto >> 4
			flags_byte = (flags_brutos << 2) >> 2
			self.flags = (int(bool(flags_byte & 32)),int(bool(flags_byte & 16)),int(bool(flags_byte & 8)),int(bool(flags_byte & 4)),int(bool(flags_byte & 2)),int(bool(flags_byte & 1)))
			self.opcoes = bytes_brutos[20:int(self.comprimento_cabecalho * 4)]
			self.dados = bytes_brutos[int(self.comprimento_cabecalho * 4):]


