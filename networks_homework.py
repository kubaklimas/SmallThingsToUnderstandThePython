import requests, socket
#156.17.88.0
#156.17.91.0
# Nie potrafiłem wydobyć informacji o e-mailach. Dlatego ich nie ma
# Źródła : Stackoverflow, oraz dokumentacja requests socket

for i in range(1, 254):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.settimeout(0.1)
   a = '156.17.88.'+str(i)
   result = sock.connect_ex(('156.17.88.'+str(i), 80))

   try:
      if result == 0:
         r = requests.head('http://' + a + ':' + str(80))
         typ = r.headers['Server']
         print(a)
         sn = socket.getfqdn(a)
         print(i, "Port is open", ' Hostname:', sn,';', typ)

      else:
         pass
   except:
      pass
   sock.close()
print('Dla drugiego ip')
for i in range(1, 254):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.settimeout(0.1)
   a = '156.17.91.'+str(i)
   result = sock.connect_ex(('156.17.91.'+str(i), 80))

   try:
      if result == 0:
         r = requests.head('http://' + a + ':' + str(80))
         typ = r.headers['Server']
         print(a)
         sn = socket.getfqdn(a)
         print(i, "Port is open", ' Hostname:', sn,';', typ)

      else:
         pass
   except:
      pass
   sock.close()