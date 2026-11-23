# 05 – Automatisierung

Alle Schritte gehen am Handy.

| Nr. | Was | Wo | Kosten |
|---|---|---|---|
| 1 | Skript-Übersicht mit Dauer-Check | GitHub Action | 0 € |
| 2 | Wochen-Check jeden Montag | GitHub Action | 0 € |
| 3 | Videos vorausplanen | TikTok/YouTube-App | 0 € |
| 4 | Einnahmen/Ausgaben-Liste | CSV im Repo | 0 € |
| – | PDFs bauen (Etsy, pausiert) | GitHub Action | 0 € |

---

## 1 – Skript-Übersicht

**Was passiert:** Sobald sich ein Skript in
`04-content/kanal/skripte/` ändert, erneuert
GitHub die Datei `04-content/kanal/INDEX.md`:
Titel, Status, Wortzahl, geschätzte Dauer.
Warnt, wenn ein Video unter 1 Min. bliebe
(dann zahlt TikTok nicht).

**Einrichtung:** nichts. Läuft automatisch.
Falls die Action nicht speichern darf: im
Handy-Browser github.com → Repo → **Settings →
Actions → General → Workflow permissions →
Read and write** (Desktop-Ansicht aktivieren).
Die PDF-Action hat schon erfolgreich
gespeichert, also passt das vermutlich.

**Status ändern am Handy:** GitHub-App →
Skript → Stift-Symbol → `status: entwurf` zu
`status: freigegeben` ändern → Commit.

---

## 2 – Wochen-Check

Jeden Montag früh legt GitHub ein Issue mit
Checkliste an (Videos, Zahlen, Freigaben).
Push-Nachricht über die GitHub-App.

**Einrichtung:** GitHub-App → Profil →
Einstellungen → Benachrichtigungen → Push für
Issues an.

⚠️ Zeitpläne laufen nur auf dem **Standard-
Branch**. Startet also erst nach dem Merge
in den Haupt-Branch.

---

## 3 – Videos vorausplanen (Batch)

Ziel ab Woche 8: an einem Tag 4 Videos bauen,
dann über die Woche verteilt automatisch
veröffentlichen.

- **YouTube-App:** Short hochladen →
  Sichtbarkeit → **Planen** → Datum/Uhrzeit
- **TikTok-App:** Beim Posten
  „Mehr Optionen“ → **Planen** (Funktion je
  nach Konto/Region – PRÜFEN). Falls nicht
  verfügbar: TikTok Studio im Handy-Browser.

Gute Zeiten zum Testen: 18–21 Uhr. Nach
4 Wochen schaue ich mit dir in die Statistik.

---

## 4 – Einnahmen/Ausgaben

`buchhaltung/einnahmen.csv` und
`buchhaltung/ausgaben.csv`. Einmal pro Monat
eintragen (z. B. KI-Stimme-Abo, Auszahlungen).
Belege als Foto in einen Cloud-Ordner.

---

## Später (wenn Geld fließt)

- Make.com: Auszahlungs-Mails automatisch in
  Tabelle (lohnt erst ab regelmäßigen
  Einnahmen)
- Automatisches Cross-Posting TikTok → YouTube
  über Dritt-Tools: bewusst **nicht**. Kostet
  Geld und lädt oft Videos mit Wasserzeichen
  hoch, was die Reichweite drückt.
