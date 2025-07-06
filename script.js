document.getElementById("feedback-form").addEventListener("submit", async function (e) {
  e.preventDefault();
  
  const payload = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value
  };

  try {
    const res = await fetch("https://your-api-id.execute-api.us-east-1.amazonaws.com/prod", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      alert("Feedback submitted!");
    } else {
      alert("Error submitting feedback.");
    }
  } catch (err) {
    alert("Network error.");
  }
});