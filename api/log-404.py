"""
Serverless function that logs 404 requests on Vercel.

Any request that does not map to a static asset is routed here via `vercel.json`.
The function prints a structured JSON log entry, which appears in the Vercel logs,
and returns a simple 404 response body.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler


def _log_404(handler: BaseHTTPRequestHandler) -> None:
    """Emit a structured JSON line that Vercel will capture in the deployment logs."""
    log_entry = {
        "level": "warn",
        "event": "http.404",
        "method": handler.command,
        "path": handler.path,
        "remote_addr": handler.client_address[0] if handler.client_address else None,
        "user_agent": handler.headers.get("user-agent"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    print(json.dumps(log_entry))


class handler(BaseHTTPRequestHandler):
    """Respond with 404 for any HTTP method and log the attempt."""

    def _send_response(self) -> None:
        _log_404(self)
        body = json.dumps(
            {
                "error": "Not Found",
                "detail": f"No route matches {self.command} {self.path}",
            }
        ).encode("utf-8")

        self.send_response(404)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # Delegate every HTTP verb Vercel might send to `_send_response`.
    def do_GET(self) -> None:  # noqa: N802 (Vercel uses BaseHTTPRequestHandler API)
        self._send_response()

    def do_POST(self) -> None:  # noqa: N802
        self._send_response()

    def do_PUT(self) -> None:  # noqa: N802
        self._send_response()

    def do_PATCH(self) -> None:  # noqa: N802
        self._send_response()

    def do_DELETE(self) -> None:  # noqa: N802
        self._send_response()

    def do_HEAD(self) -> None:  # noqa: N802
        _log_404(self)
        self.send_response(404)
        self.end_headers()


