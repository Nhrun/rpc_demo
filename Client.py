from xmlrpc.client import ServerProxy

server = ServerProxy("http://localhost:9090")
print(server.fun_add(2,5))