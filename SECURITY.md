# Security Policy

Do not publish secrets in this repository.

Keep these values private:

- `BOT_TOKEN`
- `STRING_SESSION`
- `MONGO_DB_URI`
- `API_HASH`
- `COOKIE_URL` and raw cookie contents
- API keys for external providers

If a secret is leaked, rotate it immediately from the original provider and update the Railway environment variables.

Report security issues through the repository issues page:

https://github.com/shnwazdeveloper/saya-music/issues
