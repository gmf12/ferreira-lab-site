// Contador de acessos do jogo, por IP único.
// GET  -> { unicos, total }
// POST -> registra a visita (IP guardado só como hash SHA-256 com sal) e devolve os números.
import { getStore } from "@netlify/blobs";
import { createHash } from "node:crypto";

const json = (obj) =>
  new Response(JSON.stringify(obj), {
    headers: { "content-type": "application/json", "cache-control": "no-store" },
  });

export default async (req, context) => {
  const store = getStore("jogo-acessos");
  let c = (await store.get("contador", { type: "json" })) || { unicos: 0, total: 0 };

  if (req.method === "POST") {
    const ip = context.ip || req.headers.get("x-nf-client-connection-ip") || "desconhecido";
    const salt = Netlify.env.get("CONTADOR_SALT") || "libnm-jogo";
    const key = "ip-" + createHash("sha256").update(salt + ip).digest("hex");
    c.total += 1;
    if (!(await store.get(key))) {
      await store.set(key, "1");
      c.unicos += 1;
    }
    await store.setJSON("contador", c);
  }
  return json(c);
};

export const config = { path: "/api/jogo-contador" };
