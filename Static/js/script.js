document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("sidebar-overlay");
    const toggleBtn = document.getElementById("sidebar-toggle");
    const closeBtn = document.getElementById("sidebar-close");

    function openSidebar() {
        sidebar.classList.add("open");
        overlay.classList.add("visible");
    }

    function closeSidebar() {
        sidebar.classList.remove("open");
        overlay.classList.remove("visible");
    }

    if (toggleBtn) toggleBtn.addEventListener("click", openSidebar);
    if (closeBtn) closeBtn.addEventListener("click", closeSidebar);
    if (overlay) overlay.addEventListener("click", closeSidebar);
});

// -----------------------------
// Offline Detection
// -----------------------------

function updateOfflineUI() {
    const offlineBanner = document.getElementById("offline-banner");
    const isOffline = !navigator.onLine;

    // Show/hide banner
    offlineBanner.style.display = isOffline ? "block" : "none";

    // Disable Add/Edit/Delete buttons
    document.querySelectorAll(".btn, button").forEach(btn => {
        if (btn.dataset.protected === "true") {
            if (isOffline) {
                btn.classList.add("disabled");
            } else {
                btn.classList.remove("disabled");
            }
        }
    });
}

// Block form submission offline
document.addEventListener("submit", (e) => {
    if (!navigator.onLine) {
        e.preventDefault();
        alert("You are offline. This action requires an internet connection.");
    }
});

// Listen for online/offline events
window.addEventListener("online", updateOfflineUI);
window.addEventListener("offline", updateOfflineUI);

// Run on load
updateOfflineUI();
