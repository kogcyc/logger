export default async function handler(req, res) {
  // CORS headers for preflight and actual requests
  res.setHeader("Access-Control-Allow-Origin", "*"); // or specify your domain instead of "*"
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  // Handle preflight requests
  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

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

  return res.status(204).end();
}
