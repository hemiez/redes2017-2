import socket 
import binascii

def createPacket(instruction,id_param,ip_source,ip_destin,ttl,flags):

	version = '0010'
	IHL = '0000'
	type_service = '00000000'
	total_len = '0000000000000000'
	identif = id_param.zfill(16)
	flag_p = flags
	frag_off = '0000000000000'
	protoc = '00000000'
	header_check = '0000000000000000'
	source = ip_source.zfill(32)
	destin = ip_destin.zfill(32)

	if(not(flag == '000'):
		ttl = format((int(ttl,2)-1), '08b')
	

	if(instruction[1] == 'ps'):
		protoc = '00000001'
	elif(instruction[1] == 'df'):
		protoc = '00000010'
	elif(instruction[1] == 'finger'):
		protoc = '00000011'
	elif(instruction[1] == 'uptime'):
		protoc = '00000100'

	IHL = bin(len(version+IHL+type_service+total_len+identif+flag_p+frag_off+ttl+protoc+header_check+source+destin+option+padding))
	
	filler = bin(0).lstrip('-0b')
	
	if(len(options)%32 == 0):
		padding == ''
	else:
		padding = filler.zfill(32-len(options)%32)

	total_len = bin(len(version+IHL+type_service+total_len+identif+flag_p+frag_off+ttl+protoc+header_check+source+destin+option+padding))

	pack = version+IHL+type_service+total_len+identif+flag_p+frag_off+ttl+protoc+header_check+source+destin+option+padding

	header_check = checksum(pack)

	return pack

def checksum(pack):
	checksum = 0
	
	for i in range(0, len(pack), 16):
		checksum += int(pack[i:i+16],2)
		checksum = (checksum >> 16) + checksum (checksum & 0xFFFF)
	return format(~checksum & 0xFFFF, '016b')

def decodePack(pack):
	version = pack[0:4]
	IHL = int(pack[4:8],2)
	type_service = pack[8:16]
	total_len = int(pack[16:32],2)
	identif = pack[32:48]
	flag_p = pack[48:51]
	frag_off = pack[51:64]
	ttl = pack[64:72]
	protoc = pack[72:80]
	header_check = pack[80:96]
	ip_source = pack[96:128]
	ip_destin = pack[128:160]
	options = pack[160:160+32*(IHL-5)]
	data = pack[160+32*(IHL-5):total_len]

	if(protoc == 1):
		comando = 'ps'
	elif(protoc == 2):
		comando = 'df'
	elif(protoc == 3):
		comando = 'finger'
	elif(protoc == 4):
		comando = 'uptime'

	
