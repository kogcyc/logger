export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).send("Method Not Allowed");
  }

  const { url, timestamp } = req.body;
  const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;

  const logEntry = {
    url,
    timestamp,
    ip,
    userAgent: req.headers["user-agent"]
  };

  console.log("Log entry:", logEntry);

  // Persisting logs:
  // 👉 Option A: Use Vercel's built-in logging (console only)
  // 👉 Option B: Forward to a real database (e.g. PlanetScale, Supabase, Tinybird)
  // 👉 Option C: Write to a third-party logging service (like Logtail, Loggly)

  res.status(204).end(); // Success, no content
}
