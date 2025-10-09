
# TML Lantern Auditor Node (Public)

Public verification service for **Ternary Moral Logic (TML)**.
Verifies SHA-256 formats and serves governance status placeholders.
No private data, no PII, proofs only.

## Run locally
```bash
pip install -r requirements.txt
uvicorn tml_audit_project.main:app --reload
# visit http://127.0.0.1:8000/docs
```

## Deploy to Render
1. Push this folder to your GitHub repo.
2. Create a new **Web Service** on [Render.com], connect the repo.
3. Build command: *(leave blank)*
4. Start command:
   ```
   uvicorn tml_audit_project.main:app --host 0.0.0.0 --port 8000
   ```
5. After deploy, open `/docs` for the OpenAPI UI.

## Endpoints
- `GET /health`
- `GET /lantern`
- `GET /auditor/verify/sha256/{digest}`
- `POST /auditor/submit`
- `GET /regulator/governance/status`
- `POST /redress/report`

## Notes
- Wire real OpenTimestamps/EVM verifiers later.
- Keep this node public: it serves proofs, not personal data.
