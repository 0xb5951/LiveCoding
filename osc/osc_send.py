import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)
    while True:
        client.send_message("/command", input())
