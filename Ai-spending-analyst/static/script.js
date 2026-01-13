// Reference to the AI response box
const aiBox = document.getElementById("ai-response");

// Handles CSV upload and initial analysis
async function upload() {
  const file = document.getElementById("csv").files[0];

  // Do nothing if no file is selected
  if (!file) return;

  // Let the user know the AI is working
  aiBox.innerText = "Analyzing your spending patterns...";

  // Prepare file for backend
  const formData = new FormData();
  formData.append("file", file);

  // Send CSV to Flask backend
  const res = await fetch("/upload", {
    method: "POST",
    body: formData
  });

  // Read AI response
  const data = await res.json();

  // Display AI insight
  aiBox.innerText = data.insights;
}

// Handles chat-style follow-up questions
async function ask() {
  const message = document.getElementById("message").value;

  // Ignore empty messages
  if (!message.trim()) return;

  // Show thinking indicator
  aiBox.innerText = "Thinking...";

  // Send user question to backend
  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  // Read AI reply
  const data = await res.json();

  // Show AI reply
  aiBox.innerText = data.response;
}
