# 05 – Automatisierung

Übersicht. Jede Automatik hat eine eigene
Anleitung unten. Alle Schritte gehen am Handy.

| Nr. | Was | Wo | Kosten |
|---|---|---|---|
| 1 | PDFs automatisch bauen | GitHub Action | 0 € |
| 2 | Wochen-Check jeden Montag | GitHub Action | 0 € |
| 3 | Einnahmen/Ausgaben-Liste | CSV im Repo | 0 € |
| 4 | Verkäufe → Tabelle | Make.com | 0 € (Free) |
| 5 | Pinterest-Pins planen | Pinterest-App | 0 € |

---

## 1 – PDFs automatisch bauen

**Was passiert:** Sobald sich eine Datei in
`04-content/produkte/` ändert, baut GitHub das
PDF und legt es in `04-content/pdf/` ab.

**Einrichtung (einmalig, ca. 3 Min.):**
1. GitHub-App → Repo öffnen → Tab **Actions**.
   Falls gefragt: Actions aktivieren.
2. Falls die Action beim Speichern scheitert:
   Im Handy-Browser github.com → Repo →
   **Settings → Actions → General →
   Workflow permissions → Read and write**
   → Save. (Desktop-Ansicht im Browser
   aktivieren, falls das Menü fehlt.)

**PDF holen:** GitHub-App → `04-content/pdf/`
→ Datei antippen → Teilen/Öffnen → in Dateien
speichern.

**Manuell starten:** Actions → „PDFs bauen“
→ „Run workflow“ (ggf. im Browser).

---

## 2 – Wochen-Check

**Was passiert:** Jeden Montag früh legt GitHub
ein Issue mit Checkliste an. Du bekommst eine
Push-Nachricht in der GitHub-App.

**Einrichtung:** GitHub-App → Profil →
Einstellungen → Benachrichtigungen → Push für
„Issues“ aktivieren. Sonst nichts zu tun.

Hinweis: Zeitpläne laufen nur auf dem
**Standard-Branch** des Repos. Das klappt erst,
wenn die Dateien dort liegen (nach dem Merge).

---

## 3 – Einnahmen/Ausgaben (Buchhaltung light)

Dateien: `buchhaltung/einnahmen.csv` und
`buchhaltung/ausgaben.csv`.

- Einmal pro Woche (Wochen-Check) eintragen.
- Belege als Foto in einem Cloud-Ordner
  „Belege“ ablegen (z. B. Google Drive).
- Am Jahresende baue ich daraus die Zahlen
  für die EÜR (Steuererklärung – PRÜFEN,
  ggf. Steuerberater).

Am Handy bearbeiten: GitHub-App → Datei →
Stift-Symbol → neue Zeile anhängen.

Ab ca. 10 Verkäufen/Monat lohnt sich Nr. 4.

---

## 4 – Verkäufe automatisch in Tabelle (Make.com)

**Was passiert:** Jeder Etsy-Verkauf landet
automatisch als Zeile in einem Google Sheet.

**Einrichtung (ca. 20 Min., Handy-Browser):**
1. Google-Sheets-App: neue Tabelle „Verkäufe“,
   Spalten wie in `einnahmen.csv`.
2. make.com im Browser → kostenloses Konto.
3. „Create scenario“ → Modul **Etsy →
   Watch Receipts** (oder ähnlich benannt –
   PRÜFEN, ob das Etsy-Modul verfügbar ist)
   → mit Etsy-Konto verbinden.
4. Zweites Modul: **Google Sheets → Add a row**
   → Tabelle „Verkäufe“ wählen → Felder
   zuordnen (Datum, Bestellnummer, Produkt,
   Betrag).
5. Zeitplan: alle 24 Stunden (spart Free-
   Kontingent). Scenario **ON** schalten.

⚠️ Make im Handy-Browser ist fummelig, geht
aber. Falls das Etsy-Modul fehlt: bei Nr. 3
bleiben (manuell, 5 Min./Woche).

---

## 5 – Pinterest-Pins planen (ab Woche 7)

**Was passiert:** Pins zu deinen Produkten
gehen über Wochen verteilt online.

1. Pinterest-App → „+“ → Pin erstellen.
2. Bild: Hochformat 1000 × 1500 px aus Canva.
3. Link: deine Etsy-Listing-URL.
4. Titel/Beschreibung: schreibe ich dir je
   Produkt in `04-content/listings/`.
5. **Veröffentlichen später** wählen → Datum.
   (Planung im Voraus begrenzt – PRÜFEN, wie
   weit aktuell möglich.)

Ziel: 1 Sitzung pro Woche, 5–10 Pins planen.
