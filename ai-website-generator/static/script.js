function sendPrompt() {
    var prompt = document.getElementById("prompt").value;
    var chat = document.getElementById("chat");

    chat.textContent = "Generating website...";

    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(res => res.json())
    .then(data => {
        loadGeneratedPage(data.html);
    })
    .catch(err => {
        chat.textContent = "Error: " + err;
    });
}

function loadGeneratedPage(html) {
    var wrappedHTML = `
<!DOCTYPE html>
<html>
<head>
<title>Generated Website</title>
</head>
<body>

<div style="background:#0b1220;color:white;padding:10px;">
    <button onclick="goBack()">⬅ Back to Generator</button>
    <button onclick="saveHTML()">💾 Save HTML</button>
</div>

${html}

<script>
function goBack() {
    location.reload();
}

function saveHTML() {
    var blob = new Blob([\`${html.replace(/`/g, "\\`")}\`], { type: "text/html" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "generated-site.html";
    a.click();
}
<\/script>

</body>
</html>
`;

    document.open();
    document.write(wrappedHTML);
    document.close();
}
