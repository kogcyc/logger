export default async function handler(req, res) {
  // CORS headers
  res.setHeader("Access-Control-Allow-Origin", "*"); // You can restrict this to your domain
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  // Preflight request support
  if (req.method === "OPTIONS") {
    return res.status(200).end();
  }

  // Allow only POST
  if (req.method !== "POST") {
    res.setHeader("Allow", ["POST"]);
    return res.status(405).send("Method Not Allowed");
  }

  try {
    const { url, timestamp } = req.body;
    const ip = req.headers["x-forwarded-for"] || req.socket?.remoteAddress;
    const userAgent = req.headers["user-agent"];

    const logEntry = {
      url,
      timestamp,
      ip,https://logger-235mcgydq-kogswell-cycles-projects.vercel.app/
      userAgent,
    };

    // Log to Vercel dashboard
    console.log("Log entry:", logEntry);

    res.status(204).end(); // No content on success
  } catch (error) {
    console.error("Error handling log request:", error);
    res.status(500).send("Server error");
  }
}
