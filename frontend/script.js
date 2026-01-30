const API_URL = "http://127.0.0.1:5000/api/incidents";

async function loadIncidents() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        const container = document.getElementById("incidents");

        if (data.length === 0) {
            container.innerHTML = "<p>No incidents detected yet.</p>";
            return;
        }

        container.innerHTML = "";

        data.forEach((incident, index) => {
            const div = document.createElement("div");
            div.className = "incident-item";
            div.textContent = `#${index + 1} — ${incident}`;
            container.appendChild(div);
        });

    } catch (error) {
        console.error("Error fetching incidents:", error);
    }
}

// auto refresh every 3 seconds
setInterval(loadIncidents, 3000);

// first load
loadIncidents();
