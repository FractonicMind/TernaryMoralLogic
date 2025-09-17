/**
 * Webhook stub for forwarding SPRL logs to an external governance mirror.
 * Replace with your real transport; examples use fetch() and retry.
 */

async function forwardLog(logPayload, mirrorUrl, maxRetries = 3) {
  let attempt = 0;
  while (attempt < maxRetries) {
    attempt += 1;
    try {
      const res = await fetch(mirrorUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(logPayload),
        keepalive: true
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return true;
    } catch (err) {
      if (attempt >= maxRetries) throw err;
      await new Promise(r => setTimeout(r, 250 * attempt));
    }
  }
}

module.exports = { forwardLog };
