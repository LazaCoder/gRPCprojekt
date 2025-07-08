import grpc, threading, queue, time, datetime
from concurrent import futures

import chat_pb2, chat_pb2_grpc

# Globalna lista za sve klijentske queueove
klijenti = []

class ChatServicer(chat_pb2_grpc.ChatServiceServicer):
    def ChatStream(self, request_iterator, context):
        # Svakom klijentu dodijeljujemo svoj queue
        q = queue.Queue()
        klijenti.append(q)
        
        # Funkcija koja čita poruke od klijenta
        def citaj_poruke():
            try:
                for poruka in request_iterator:
                    trenutak = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"[{trenutak}] Primljena poruka od {poruka.username}: {poruka.message}")
                    # Pošalji poruku svim ostalim klijentima
                    for k in klijenti:
                        if k != q:
                            k.put(poruka)
            except Exception as e:
                print("Greška pri čitanju poruka:", e)
        
        # Pokreni čitanje poruka u zasebnoj niti
        threading.Thread(target=citaj_poruke, daemon=True).start()
        
        try:
            while True:
                msg = q.get()
                yield msg
        except Exception as e:
            print("Greška pri slanju poruka:", e)
        finally:
            # Ukloni queue kad klijent prekine vezu
            klijenti.remove(q)

def pokreni_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server pokrenut na portu 50051")
    try:
        while True:
            time.sleep(86400)  # Da se server vrti jedan dan
    except KeyboardInterrupt:
        print("Zaustavljam server...")
        server.stop(0)

if __name__=="__main__":
    pokreni_server()
