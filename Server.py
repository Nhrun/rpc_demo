from xmlrpc.server import SimpleXMLRPCServer

def fun_add(a, b):
    total = a + b
    print("[INFO] Being Called")
    return total

if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 9090))
    server.register_function(fun_add)
    print("RPC Server in online ...")
    server.serve_forever()

