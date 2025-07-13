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
Za pokretanje servisa potrebno je postaviti se u mapu u kojoj se nalaze python skripte ovog projekta, a nakon toga potrebno je pokrenuti server i klijent na način da se u naredbeni redak Windowsa upišu sljedeće naredbe:
```cmd # Pokreni server python chat_server.py # Pokreni klijenta dva puta python chat_client.py ``` 
