# homepage

Beispiel-Konfiguration für [gethomepage.dev](https://gethomepage.dev) — ein selbst gehostetes Start-Dashboard.

**Läuft sofort:** Dateien in den Homepage-Config-Ordner legen, Container starten — du siehst direkt
ein sauberes Dashboard (Begrüßung, Uhrzeit, Ressourcen, Suche, Lesezeichen und öffentliche Links).

**Eigene Dienste mit Live-Widgets** (Home Assistant, Proxmox, AdGuard …) liegen in `services.yaml`
als auskommentierte Beispiele bereit. Einkommentieren, Adresse anpassen, Geheimnisse über
`{{HOMEPAGE_VAR_…}}` aus einer privaten `.env` einbinden (Vorlage: `.env.example`).

> Keine echten Daten: alle Hosts sind Beispiele (`*.local`), alle Geheimnisse sind Platzhalter.

## Dateien

| Datei | Zweck |
|-------|-------|
| `settings.yaml` | Titel, Layout, Suche |
| `widgets.yaml` | Kopf-Widgets (Begrüßung, Uhrzeit, Ressourcen, Suche) |
| `bookmarks.yaml` | Lesezeichen (öffentliche Links) |
| `services.yaml` | Schnellzugriff (läuft sofort) + optionale Widget-Dienste |
| `custom.css` | Services horizontal anordnen |
| `.env.example` | Vorlage für Geheimnisse (nur für optionale Widgets) |
