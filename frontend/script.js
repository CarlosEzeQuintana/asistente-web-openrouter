document.getElementById("send").addEventListener("click", async () => {
  const mensaje = document.getElementById("input").value;
  const responseBox = document.getElementById("response");

  if (!mensaje.trim()) {
    responseBox.textContent = "⚠️ Escribí algo antes de enviar.";
    return;
  }

  responseBox.textContent = "⏳ Pensando...";

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ mensaje })
    });

    const data = await response.json();

    if (data.respuesta) {
      responseBox.textContent = data.respuesta;
    } else {
      responseBox.textContent = "❌ Error: " + (data.error || "Respuesta no válida.");
    }
  } catch (error) {
    responseBox.textContent = "❌ Error al conectar con el servidor.";
    console.error(error);
  }
});
