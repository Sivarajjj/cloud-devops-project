
async function loadApplicationStatus() {
    const statusElement = document.getElementById("app-status");

    try {
        const response = await fetch("/api/status");

        if (!response.ok) {
            throw new Error("Application status request failed");
        }

        const data = await response.json();

        statusElement.textContent = data.status;
        statusElement.style.color = "#34d399";

        document.getElementById("server").textContent = data.server;
        document.getElementById("os").textContent = data.operating_system;

        document.getElementById("timestamp").textContent =
            new Date(data.timestamp).toLocaleString();

    } catch (error) {
        statusElement.textContent = "Unavailable";
        statusElement.style.color = "#f87171";
    }
}

async function checkHealth() {
    const healthElement = document.getElementById("health-status");

    healthElement.textContent = "Checking...";

    try {
        const response = await fetch("/health");

        if (!response.ok) {
            throw new Error("Health check failed");
        }

        const data = await response.json();

        healthElement.textContent = "Application is " + data.status;
        healthElement.style.color = "#34d399";

    } catch (error) {
        healthElement.textContent = "Application is unavailable";
        healthElement.style.color = "#f87171";
    }
}

loadApplicationStatus();
checkHealth();
