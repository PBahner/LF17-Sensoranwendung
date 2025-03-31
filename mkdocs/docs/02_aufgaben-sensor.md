## Aufbau der Anwendung

Die Anwendung ist nach dem **MVC** (Model-View-Controller) Muster entwickelt.

Im Folgenden ist noch einmal das MVC-Muster dargestellt:

![MVC.drawio.svg](images%2FMVC.drawio.svg)

Das folgende Diagramm zeigt eine Übersicht zu allen Klassen der Sensor-Anwendung:

![class_overview.svg](images%2Fclass_overview.svg)

## Dateiarbeit in Python
In Python gibt es verschiedene Möglichkeiten, mit Dateien zu arbeiten. Zum Schreiben von Daten in eine Datei verwendet man die Funktion open(), die die Datei öffnet, und den Modus w (write) oder a (append). Wenn man den Modus w verwendet, wird die Datei überschrieben, während bei a neue Daten am Ende der Datei angehängt werden. Zum Schreiben von Daten wird die Methode write() verwendet.

Beispiel:

```python
# Öffnet die Datei "beispiel.txt" im Schreibmodus ('w')
with open("beispiel.txt", "w") as file:
    file.write("Hallo, Welt!")
```

In diesem Beispiel:

Die with open()-Anweisung öffnet die Datei und sorgt dafür, dass sie nach dem Schreiben korrekt geschlossen wird.
Die file.write()-Methode schreibt den Text "Hallo, Welt!" in die Datei.

## Aufgabe

**Erstelle eine neue Implementierung des `DataStorageInterface`.**

Du benötigst folgende Datei: `python-app/src/lf17_sensor/data_storage.py`

Die `DataStoragePrinter` Klasse gibt die Sensor-Werte der Anwendung aktuell nur auf der Konsole aus. Die neue Klasse soll die Sensor-Werte in eine Datei schreiben.
Implementiere die Klasse `DataStorageFileWriter`, welche anstelle der `DataStoragePrinter` Klasse verwendet werden soll.


## Zusatzaufgabe
**Erstelle eine neue Implementierung des `DataGetter`.**

Nutze folgende API, um anstelle zufälliger Werte echte Wetterdaten zu erhalten: [Open-Meteo API](https://open-meteo.com/en/docs)

Du benötigst folgende Datei: `python-app/src/lf17_sensor/data_getter.py`
