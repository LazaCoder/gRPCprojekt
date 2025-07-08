import threading, queue, tkinter as tk, datetime, grpc
from tkinter import scrolledtext, font

import chat_pb2, chat_pb2_grpc

SERVER = 'localhost:50051'  # Server adresa

class ChatKlijent:
 def __init__(self, ime):
  self.ime = ime
  self.out_msg = queue.Queue()
  self.in_msg = queue.Queue()
  self.channel = grpc.insecure_channel(SERVER)
  self.stub = chat_pb2_grpc.ChatServiceStub(self.channel)
  threading.Thread(target=self.chat_stream, daemon=True).start()  # pokreni stream u pozadini
  
  # UI postavke
  self.root = tk.Tk()
  self.root.title("gRPC Chat - " + self.ime)
  self.root.configure(bg="#2C3E50")
  
  # fontovi
  self.font_chat = font.Font(family="Helvetica", size=12)
  self.font_entry = font.Font(family="Helvetica", size=12)
  
  # okvir za sve
  okvir = tk.Frame(self.root, bg="#2C3E50")
  okvir.pack(padx=10, pady=10)
  
  # polje za chat
  self.chat_okvir = scrolledtext.ScrolledText(okvir, state='disabled', width=60, height=20, 
                                               bg="#ECF0F1", fg="#2C3E50", font=self.font_chat, 
                                               wrap=tk.WORD, borderwidth=2, relief="groove")
  self.chat_okvir.pack(pady=(0,10))
  
  # unos poruke
  self.unos = tk.Entry(okvir, width=55, font=self.font_entry, bg="#FFFFFF", fg="#2C3E50", 
                       borderwidth=2, relief="groove")
  self.unos.pack(side=tk.LEFT, padx=(0,5))
  self.unos.bind("<Return>", self.posalji)
  
  # gumb za slanje
  self.gumb = tk.Button(okvir, text="Pošalji", command=lambda: self.posalji(None),
                         font=self.font_entry, bg="#3498DB", fg="#FFFFFF", activebackground="#2980B9",
                         relief="raised")
  self.gumb.pack(side=tk.LEFT)
  
  self.root.after(100, self.polleraj)
  
 # Generator poruka za stream
 def poruka_generator(self):
  while True:
   txt = self.out_msg.get()
   yield chat_pb2.ChatMessage(username=self.ime, message=txt)
   
 # Funkcija za chat stream
 def chat_stream(self):
  try:
   responses = self.stub.ChatStream(self.poruka_generator())
   for resp in responses:
    self.in_msg.put(f"{resp.username}: {resp.message}")
  except Exception as e:
   print("Greška u chat streamu:", e)
   
 # Funkcija za slanje poruka
 def posalji(self, event):
  txt = self.unos.get().strip()
  if txt:
   self.out_msg.put(txt)
   self.prikazi_poruku("Ti: " + txt)
   self.unos.delete(0, tk.END)
   
 # Provjera ulaznih poruka
 def polleraj(self):
  while not self.in_msg.empty():
   p = self.in_msg.get()
   self.prikazi_poruku(p)
  self.root.after(100, self.polleraj)
  
 # Prikaz poruka u chatu
 def prikazi_poruku(self, p):
  trenutak = datetime.datetime.now().strftime("%H:%M:%S")
  poruka = f"[{trenutak}] {p}"
  self.chat_okvir.configure(state='normal')
  self.chat_okvir.insert(tk.END, poruka + "\n")
  self.chat_okvir.configure(state='disabled')
  self.chat_okvir.see(tk.END)
  
 def pokreni(self):
  self.root.mainloop()

if __name__=="__main__":
 ime = input("Upiši svoje ime: ").strip() or "Anonimac"
 klijent = ChatKlijent(ime)
 klijent.pokreni()
