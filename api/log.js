export default async function handler(req, res) {
  if (req.method !== "POST") {
    // Tell the client what methods are allowed
    res.setHeader("Allow", ["POST"]);
    return res.status(405).send("Method Not Allowed");
  }

  const { url, timestamp } = req.body;
  const ip = req.headers["x-forwarded-for"] || req.socket?.remoteAddress;

  const logEntry = {
    url,
    timestamp,
    ip,
    userAgent: req.headers["user-agent"]
  };

  console.log("Log entry:", logEntry);

  // Return a 204 (success, no content)
  res.status(204).end();
}
