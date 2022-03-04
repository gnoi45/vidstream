from vidstream import StreamingServer
import threading

host = StreamingServer('192.168.43.94',8080)

th = threading.Thread(target=host.start_server)
th.start()


while input ("") !="stop":
    continue

host.stop_server()




