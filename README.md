# alexandru.miclea
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