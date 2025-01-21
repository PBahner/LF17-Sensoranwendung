# Übungsaufgaben

[Zurück zur Info-Seite](./klassenbeziehungen.md)

Nachfolgend finden Sie verschiedene Übungsaufgaben, die sich auf die Themen **Assoziation**, **Aggregation**, 
**Komposition** und **Vererbung** (inklusive der Verwendung von `super()`) beziehen.

---

## 1. Assoziation

**Aufgabe:**  
Erstellen Sie zwei Klassen, die über eine Assoziation miteinander verknüpft sind. Achten Sie darauf, dass die eine Klasse
keinen Besitzanspruch an die andere Klasse hat, sondern lediglich eine (optionale) Referenz darauf hält.

1. Definieren Sie beispielsweise die Klassen `Order` und `Customer`.  
2. Sorgen Sie dafür, dass `Order` optional auf einen `Customer` verweisen kann (z. B. `set_customer` / `get_customer`).
3. Implementieren Sie eine Methode, die prüft, ob ein `Order`-Objekt einen gültigen `Customer` hat, und geben Sie das
   Ergebnis als Text (z. B. `"Hat Kunden"` / `"Hat keinen Kunden"`) aus.
4. Testen Sie Ihr Programm, indem Sie sowohl einen `Order` ohne Kunden als auch einen `Order` mit Kunde erstellen.

**Erweiterung:**  
- Fügen Sie eine zweite Klasse hinzu, zum Beispiel `ShippingAddress`, die von `Order` referenziert wird, und verdeutlichen
  Sie damit, dass mehrere Assoziationen gleichzeitig existieren können.

---

## 2. Aggregation

**Aufgabe:**  
Erstellen Sie eine Aggregation, bei der eine Klasse eine Liste von Objekten einer anderen Klasse verwaltet. Ein
mögliches Szenario wäre zum Beispiel eine `Garage`, in der sich mehrere `Car`-Objekte befinden.

1. Legen Sie die Klassen `Garage` und `Car` an.  
2. Implementieren Sie in der Klasse `Garage` Methoden, um `Car`-Objekte zur Liste hinzuzufügen und zu entfernen.  
3. Schreiben Sie eine Methode, die alle vorhandenen `Car`-Objekte (z. B. über `__str__` in Python) ausgibt.  
4. Testen Sie das Programm, indem Sie mehrere `Car`-Objekte erstellen, sie in die `Garage` legen und die Ausgabe
   kontrollieren.

**Erweiterung:**  
- Fügen Sie eine zusätzliche Klasse `Bike` hinzu, die ebenfalls in dieselbe `Garage` aufgenommen werden kann.  
- Prüfen Sie, wie Sie die Verwaltung der Objekte am besten organisieren: z. B. eine Liste für alle Fahrzeuge, oder
  getrennte Listen für verschiedene Typen von Fahrzeugen?

---

## 3. Komposition

**Aufgabe:**  
Erstellen Sie eine Komposition, bei der das enthaltene Objekt nur in Zusammenhang mit dem übergeordneten Objekt 
existieren kann. Ein mögliches Szenario könnte z. B. ein `House` sein, das immer genau ein `Door`-Objekt besitzt. 
Sobald das `House` zerstört wird, existiert auch die `Door` nicht mehr.

1. Definieren Sie die Klasse `House`, die im Konstruktor ein `Door`-Objekt anlegt.  
2. Definieren Sie die Klasse `Door`, die über eine einfache Eigenschaft (z. B. Farbe oder Material) verfügt.  
3. Implementieren Sie in der Klasse `House` Methoden, um auf die Eigenschaften des `Door`-Objekts zuzugreifen (z. B.
   `open_door`, `close_door` oder einfach `get_door_color`).  
4. Testen Sie das Programm, indem Sie ein `House`-Objekt erstellen und die Eigenschaften oder Methoden des
   `Door`-Objekts aufrufen.

**Erweiterung:**  
- Fügen Sie weitere Kompositionen in der Klasse `House` hinzu, z. B. ein `Roof`, das ebenfalls nur in Verbindung mit
  dem `House` existiert.
- Stellen Sie sich vor, das `House` kann optional mehr als eine `Door` haben (z. B. Haustür, Hintertür). Diskutieren Sie:
  Handelt es sich dann noch um Komposition oder eher um Aggregation?

---

## 4. Vererbung

**Aufgabe:**  
Demonstrieren Sie Vererbung, indem Sie eine Basisklasse und mindestens eine abgeleitete Klasse erstellen. Als Beispiel 
kann eine Basisklasse `Animal` dienen, von der Klassen wie `Dog` und `Cat` erben. 

1. Erstellen Sie eine Basisklasse `Animal` mit Methoden wie `make_sound()` und einer Eigenschaft `name`.  
2. Erstellen Sie eine abgeleitete Klasse `Dog`, die die Methoden und Eigenschaften von `Animal` erbt.  
3. Überschreiben Sie `make_sound()` in `Dog` mit einer spezifischen Ausgabe (z. B. `"Wuff"`).  
4. Instanziieren Sie Objekte von beiden Klassen und rufen Sie die jeweilige `make_sound()`-Methode auf.

**Erweiterung:**  
- Erstellen Sie eine weitere abgeleitete Klasse `Cat` und überschreiben Sie `make_sound()` ebenfalls.  
- Experimentieren Sie mit Mehrfachvererbung (falls Ihre Programmiersprache dies erlaubt) und beobachten Sie, wie 
  die *Method Resolution Order (MRO)* in Python wirkt.

---

## 5. Verwendung von `super()`

**Aufgabe:**  
Vertiefen Sie den Einsatz von `super()`, indem Sie den Konstruktor der Basisklasse explizit aus einer 
abgeleiteten Klasse aufrufen und dort zusätzliche Initialisierungen vornehmen.

1. Erstellen Sie eine Basisklasse `Book` mit Eigenschaften wie `title` und `author`.  
2. Definieren Sie eine abgeleitete Klasse `EBook`, die zusätzlich eine Eigenschaft wie `file_size` besitzt.  
3. Rufen Sie im Konstruktor von `EBook` den Basisklassen-Konstruktor mit `super().__init__(title, author)` auf, 
   bevor Sie `file_size` setzen.  
4. Legen Sie in einer Testmethode ein Objekt `EBook` an, geben Sie alle Eigenschaften aus und überprüfen Sie, 
   ob diese korrekt gesetzt wurden.

**Erweiterung:**  
- Fügen Sie eine Methode in der Basisklasse hinzu (z. B. `read()`), die in der abgeleiteten Klasse `EBook` 
  überschrieben wird. Rufen Sie innerhalb der neuen Methode in `EBook` wieder die originale Methode mit 
  `super().read()` auf, um sicherzustellen, dass der Basisklassen-Code ebenfalls ausgeführt wird.

---

## 6. Zusammenführung aller Konzepte

**Aufgabe (Projektaufgabe):**  
Entwerfen Sie ein kleines System, das **Assoziation**, **Aggregation**, **Komposition** und **Vererbung** miteinander vereint. 
Ein mögliches Szenario:

- Erstellen Sie eine Basisklasse `Sensor` und eine davon abgeleitete Klasse `TemperatureSensor`.  
- Eine Klasse `SensorManager` aggregiert mehrere `Sensor`-Objekte (Liste).  
- Eine Klasse `Device` besitzt über Komposition genau einen `SensorManager`.  
- Eine Klasse `User` ist lediglich assoziiert mit dem `Device`, da der Benutzer über ein Interface auf das `Device` zugreift 
  (z. B. `User.set_device(device)` und `User.configure_device()`).

Ziel ist es, anhand dieses Szenarios die verschiedenen Beziehungen und die Vererbung in einer Anwendung zu demonstrieren.

**Hinweise für die Umsetzung:**
1. Skizzieren Sie zunächst ein Klassendiagramm, um die Beziehungen zu verdeutlichen.  
2. Implementieren Sie die Klassen Schritt für Schritt und testen Sie die Methoden.  
3. Diskutieren Sie in kleinen Kommentaren im Code, warum es sich bei den Beziehungen um Assoziation, Aggregation oder 
   Komposition handelt und an welcher Stelle Vererbung zum Einsatz kommt.  

---

**Viel Erfolg bei der Bearbeitung der Übungsaufgaben!**  
Nutzen Sie die Beispiele aus dem Hauptdokument zur Orientierung und versuchen Sie, die Konzepte auf eigene 
Anwendungsfälle zu übertragen. Dadurch gewinnen Sie praktische Erfahrung in der Anwendung von Assoziation, Aggregation, 
Komposition und Vererbung, einschließlich der sicheren Verwendung von `super()`.
 

[Zurück zur Info-Seite](./klassenbeziehungen.md)