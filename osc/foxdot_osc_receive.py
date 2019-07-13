from pythonosc import dispatcher
from pythonosc import osc_server

def processing(unused_addr, command):
    exec(command)

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/command", processing)

server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 8000), dispatcher)
server.serve_forever()