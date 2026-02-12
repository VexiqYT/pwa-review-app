// -----------------------------
// PWA CACHE VERSIONING
// -----------------------------
const CACHE_VERSION = "v3";  
const CACHE_NAME = `reviewcentral-${CACHE_VERSION}`;

const FILES_TO_CACHE = [
    "/",
    "/static/css/style.css",
    "/static/js/script.js",
    "/static/js/service_worker.js",
    "/manifest.json",
    "/offline.html"
];

// -----------------------------
// INSTALL — Cache Files
// -----------------------------
self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(FILES_TO_CACHE);
        })
    );
    self.skipWaiting(); // Activate immediately
});

// -----------------------------
// ACTIVATE — Delete Old Caches
// -----------------------------
self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys
                    .filter((key) => key !== CACHE_NAME)
                    .map((key) => caches.delete(key))
            );
        })
    );
    self.clients.claim(); // Take control immediately
});

// -----------------------------
// FETCH — Network First, Cache Fallback
// -----------------------------
self.addEventListener("fetch", (event) => {
    event.respondWith(
        fetch(event.request)
            .then((response) => {
                // Save fresh version to cache
                const clone = response.clone();
                caches.open(CACHE_NAME).then((cache) => {
                    cache.put(event.request, clone);
                });
                return response;
            })
            .catch(() => {
                // Offline fallback
                return caches.match(event.request).then((cached) => {
                    return cached || caches.match("/offline.html");
                });
            })
    );
});
