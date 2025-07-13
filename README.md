# gRPC chat aplikacija
Ovaj projekt je napravljen u sklopu kolegija _Uvod u distribuirane informacijske sustave_ na Fakultetu elektrotehnike, strojarstva i brodogradnje (FESB), Sveučilišta u Splitu.

## Svrha i ciljevi
Svrha ove aplikacije je demonstracija implementacije gRPC streaminga u Pythonu, s jednostavnim GUI sučeljem.
Ciljevi projekta su:
- Demonstrirati osnovni princip rada gRPC-a
- Omogućiti višekorisničku komunikaciju u stvarnom vremenu putem gRPC-a.
- Demonstrirati kako se koristi threading i queue za obradu poruka u pozadini.

## Funkcionalnosti
- Real-time chat između više klijenata
- Svaki klijent vidi poruke svih drugih korisnika
- Timestamp svakog slanja poruke
- GUI sučelje u tkinteru s prikazom povijesti poruka

## Pokretanje servisa (Windows)
Za pokretanje servisa potrebno je imati instaliran [Python](https://www.python.org/downloads/) i [Git](https://git-scm.com/downloads) na vašem računalu. Nakon instalacije potrebno je klonirati ovaj repozitorij i postaviti se u mapu u kojoj se nalaze python skripte ovog projekta, te pokrenuti server i klijent na način da se u naredbeni redak Windowsa upišu sljedeće naredbe:
Naredba za kloniranje projekta:
```cmd 
git clone https://github.com/LazaCoder/gRPCprojekt 
```
Naredba za pozicioniranje u mapu (stavite vaš path):
```cmd 
cd put/do/vaseg/direktorija
```
Naredba za pokretanje servera:
```cmd 
python chat_server.py
```
Te za pokretanje klijenta:
```cmd
python chat_client.py
```
> [!NOTE]
> Server i klijent potrebno je pokrenuti u različitim prozorima naredbenog retka. Također, potrebno je pokrenuti klijenta dva puta (svaki u svom prozoru) ako želimo simulirati dva korisnika.

## Moguća proširenja
- Privatne poruke
- Pohrana poruka (npr. PostgreSQL)
- Web sučelje (Flask / React frontend)
- Autentifikacija korisnika
- Enkripcija poruka

