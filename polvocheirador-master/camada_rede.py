import struct
import socket

#Classe que representa a camada de rede
class IP:

	dns_name_list = [] #Relembra os nomes DNS para evitar o timeout da função socket.gethostbyaddr()

	#Recupera o nome DNS já pesquisados ou pergunta para o SO
	def reverse_lookup(addr):
		if addr in dict(IP.dns_name_list).keys():
			return dict(IP.dns_name_list)[addr]
		else:
			try:
				dns_name = socket.gethostbyaddr(addr)[0]
				IP.dns_name_list.append((addr, dns_name))
				return dns_name
			except:
				return 'Nome DNS não encontrado'

	class Datagrama:

		TCP = 6
		UDP = 17

		def __init__(self, bytes_brutos):
			self.versao = bytes_brutos[0] >> 4
			self.tam_cabecalho = (bytes_brutos[0] & 15) * 4
			self.ttl, self.protocolo, self.orig_bruto, self.dest_bruto = struct.unpack('! 8x B B 2x 4s 4s', bytes_brutos[:20])
			self.orig = self.stringfy_endr(self.orig_bruto)
			self.dest = self.stringfy_endr(self.dest_bruto)
			self.dados = bytes_brutos[self.tam_cabecalho:]

		def stringfy_endr(self, endr):
			return '.'.join(map(str, endr))