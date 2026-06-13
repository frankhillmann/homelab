# homelab

Docker-Compose-Dateien aus meinem Self-Hosted-Setup — zum Nachbauen und als Referenz.

> **Hinweis:** Alle Geheimnisse (Tokens, Passwörter) sind durch Platzhalter ersetzt.
> Echte Werte kommen in eine lokale `.env` (siehe jeweilige `.env.example`) und werden nie veröffentlicht.

## Dienste

| Dienst | Zweck |
|--------|-------|
| `glance` | Start-Dashboard |
| `paperless-ai` | KI-Tagging für Paperless-ngx (Ollama) |
| `rss-proxy` | Kleiner Flask-Proxy für RSS-Feeds |

## Nutzung

```bash
cd <dienst>
cp .env.example .env   # falls vorhanden: echte Werte eintragen
docker compose up -d
```
