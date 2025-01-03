# WebKess: Bedienungsanleitung

## Einführung
**WebKess** ist ein lokales Python-Programm, das Rohdaten von [Aktion Saubere Hände](https://www.aktion-sauberehaende.de/ueber-uns-ash) in ein Excel-freundliches Format umwandelt.

---

## Systemanforderungen
- **Windows 11**
- **Windows 10**, mit einer Betriebssystem-Buildnummer > `16299`  
  _Hinweis: Die Buildnummer kann unter `Einstellungen > System > Info` bei den `Windows-Spezifikationen` überprüft werden._

---

## Installation
### mit Downloadscript (Einfach)
**Funktioniert nur auf Windows**
1. Die Release-Website öffnen: https://github.com/LunaDEV-net/WebKess/releases
2. Die Datei `download.bat` herunterladen. <br> <img src="imgs/2025-01-03_WebKess_Manual-Download-bat.jpg">
3. Die heruntergeladene Datei in den Überordner kopieren, wo das Programm hingeladen werden soll: <br> Z.B. Wenn die `download.bat` im Pfad `D:\Programme\download.bat` liegt, dann wird das Programm nach `D:\Programme\WebKess` installiert
4. Sobald die `download.bat` an der gewünschten Stelle liegt, diese im File-Explorer mit einem Doppelklick öffnen.
5. 
### erweitert
1. **Benötigte Software installieren**
   - **Python 3.13.0** (oder höher)
   - **Git** (optional, zum Herunterladen des Projekts)
   - **PowerShell** (Windows) oder eine vergleichbare Shell

2. **Projekt herunterladen**
   - Mit Git:  
     ```bash
     git clone https://github.com/LunaDEV-net/WebKess.git
     cd WebKess
     ```
   - Alternativ über [GitHub Releases](https://github.com/LunaDEV-net/WebKess/releases) (Anleitung in Arbeit).

3. **Virtuelle Umgebung erstellen**
   - Führen Sie in Ihrem Projektverzeichnis folgenden Befehl aus:  
     ```shell
     python -m venv .venv
     ```
   - Verwenden Sie den Standardpfad `.venv`. Bei Änderungen muss das Startskript angepasst werden.

4. **Programm ausführen**
   - Windows:  
     ```shell
     .\.venv\Scripts\Activate.ps1
     python src\main.py {arguments}
     ```
     Alternativ:  
     ```shell
     run.bat
     ```
   - Linux:  
     ```bash
     .venv/bin/python src/main.py {arguments}
     ```

---

## Nutzung
Führen Sie das Programm über die Kommandozeile aus:
```shell
usage: main.py [-h] [--version] path_in path_out
```

| Argument    | Typ         | Beschreibung                                                            | Beispielwert       |
|-------------|-------------|-------------------------------------------------------------------------|--------------------|
| `path_in`   | `.csv Datei`| Pfad zur Eingabedatei                                                   | `data/input.csv`   |
| `path_out`  | `.csv Datei`| Pfad zur Ausgabedatei. **Achtung: Überschreibt bestehende Dateien!**   | `data/output.csv`  |
| `--version` |             | Gibt die aktuelle Version des Programms aus                            |                    |

---

## Support
- Kontaktieren Sie mich persönlich oder erstellen Sie ein [GitHub Issue](https://github.com/LunaDEV-net/WebKess/issues).

---