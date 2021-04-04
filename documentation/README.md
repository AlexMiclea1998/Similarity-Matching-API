How to:
Install Python3.9.1 : https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe
Beim installieren auf "add to PATH" klicken.
Python Packages Installieren:
In einen Command Prompt : pip install -r requirements.txt
(requirements.txt mit Pfad wenn notig).
Server:
In einen neuen Command Prompt mit : "python server.py" (mit Pfad wenn notig ) den Flask Server starten.
Client:
In den client.py muss mann den Pfad zu die BPMN Dateien enpassen.
Von prozess1 = r"C:\Users\alexm\TestFlask\P1 (en).bpmn" zu z.B. prozess1 = r"D:\Dokuments\P1 (en).bpmn", dass selbe muss man auch beim "prozess2" machen.
Danach parallel in einen anderen Command Promp der Client mit: "python client.py" starten.
In die Console von der Server muss normaler Weise ein Eintrag reinkommen und in die Console der Clients sollte die Similaritat dargestellt werden.



Algorithm:
Die Levenshtein-Distanz

Die Levenshtein-Distanz ist eine Metrik, die misst, wie weit zwei Wortfolgen voneinander entfernt sind. Mit anderen Worten, sie misst die minimale Anzahl von Bearbeitungen, die Sie vornehmen müssen, um eine Wortfolge in die andere zu ändern. Diese Bearbeitungen können Einfügungen, Löschungen oder Ersetzungen sein. Diese Metrik wurde nach Vladimir Levenshtein benannt, der sie ursprünglich 1965 in Betracht zog.

z.B. Lev Distanz zwischen eggs und egg ist 1.
                 zwischen egg und egg ist 0.
                 zwischen egg und bacon ist 5.

                 Da im Beispiel 1 nur eine Buschstabe anders ist, Lev-Distanz "0" bedeutet die Worter sind gleich.
                 Beispiel 3:
                 1.egg->bgg
                 2.bgg->bag
                 3.bag->bac
                 4.bac->baco
                 5.baco->bacon deswegen ist die Lev-Dist. 5 mann braucht 5 Bearbeitungen.

FuzzyWuzzy hat, genau wie das Levenshtein-Paket, eine Verhältnisfunktion, die das Standard-Levenshtein-Distanzähnlichkeitsverhältnis zwischen zwei Sequenzen berechnet. FuzzyWuzzy im Vergleich zu Levenshtein Distanz ist nicht case-sensitve also Distanz zwischen "Apfel" und "apfel" ist 0. Weiterhin FuzzyWuzzy macht substring pre processing also im Falle von "Apfel kaufen" und "kaufen apfel" die Levenshtein Distantz ware 7. Mit FuzzyWuzzy mit substring prozessign sieht es als 100% einstimmend da die reihenfolge der Worter nicht wichtig ist.

_**Funktionen der Algorithmus**_:

**fuzz.ratio**
 Ruft einfach difflib.ratio für die beiden Eingangsstrings auf.

**Token_Set_Ratio**
 Versucht, Unterschiede in den Zeichenketten auszuschließen. Ruft ratio auf drei bestimmten Teilzeichensätzen auf und gibt die max:

    #intersection-only und die Schnittmenge mit dem Rest von Zeichenkette eins
    #nur Schnittmenge und die Schnittmenge mit dem Rest der Zeichenkette zwei
    #Schnittmenge mit Rest von eins und Schnittmenge mit Rest von zwei 


**Token_Sort_Ratio**
 Versucht, ähnliche Zeichenketten in der falschen Reihenfolge zu berücksichtigen. Ruft Ratio für beide Zeichenfolgen auf, nachdem die Token in   jeder Zeichenfolge sortiert wurden. 


**Partielles_Token_Sort_Ratio**
 Gleicher Algorithmus wie in token_sort_ratio, aber anstatt das Verhältnis nach dem Sortieren der Token anzuwenden, wird partial_ratio verwendet 

**WRatio**
- 1. Nehmen Sie das Verhältnis der beiden verarbeiteten Strings (fuzz.ratio)
  
- 2. Führen Sie Prüfungen aus, um die Länge der Zeichenketten zu vergleichen
    * Wenn eine der Zeichenketten mehr als 1,5 mal so lang ist wie die andere
      verwenden Sie partial_ratio-Vergleiche - skalieren Sie Teilergebnisse um 0,9
      (dies stellt sicher, dass nur vollständige Ergebnisse 100 zurückgeben können)
    * Wenn eine der Zeichenketten mehr als 8-mal so lang ist wie die andere
      stattdessen um 0,6 skalieren
  
- 3. Führen Sie die anderen Verhältnisfunktionen aus
    * Wenn Sie partielle Verhältnisfunktionen verwenden, rufen Sie partial_ratio,
      partial_token_sort_ratio und partial_token_set_ratio
      skalieren Sie alle mit dem auf der Länge basierenden Verhältnis
    * sonst Aufruf von token_sort_ratio und token_set_ratio
    * alle tokenbasierten Vergleiche werden mit 0,95 skaliert
      (zusätzlich zu allen Teilskalaren)
  
- 4. Nehmen Sie den höchsten Wert aus diesen Ergebnissen
   runden Sie ihn und geben Sie ihn als Ganzzahl zurück.

Das Similaritat Wert ist die mittelnote der Output der oben genannten Methoden.

References:
https://www.datacamp.com/community/tutorials/fuzzy-string-python
https://flask-restful.readthedocs.io/en/latest/
https://stackoverflow.com/questions/31806695/when-to-use-which-fuzz-function-to-compare-2-strings