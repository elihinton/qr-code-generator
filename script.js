const toggleBtn = document.getElementById("toggleAdvanced");
const advanced = document.getElementById("advancedSettings");
const generateBtn = document.getElementById("generateBtn");
const preview = document.getElementById("preview");

toggleBtn.addEventListener("click", () => {
    advanced.classList.toggle("hidden");
    toggleBtn.textContent = advanced.classList.contains("hidden")
    ? "Show Advanced Settings"
    : "Hide Advanced Settings";
});

generateBtn.addEventListener("click", () => {
    const text = document.getElementById("linkInput").value.trim();
    if (!text) return alert("Please enter a link!");

    const size = parseInt(document.getElementById("sizeInput").value) || 256;
    const margin = parseInt(document.getElementById("borderInput").value) || 4;
    const filename = document.getElementById("filenameInput").value.trim() || "qr.png";
    const colorDark = document.getElementById("colorInput").value || "#000000";
    const colorLight = document.getElementById("bgInput").value || "#ffffff";

    QRCode.toCanvas(text, {
    width: size,
    margin: margin,
    color: {
        dark: colorDark,
        light: colorLight
    }
    }, (err, canvas) => {
    if (err) return console.error(err);

    preview.innerHTML = "";
    preview.appendChild(canvas);

    const link = document.createElement("a");
    link.download = filename.endsWith(".png") ? filename : filename + ".png";
    link.href = canvas.toDataURL("image/png");
    link.click();
    });
});