 // Function to display user location details
        function showUserLocation(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            // Create a map
            const map = L.map('map').setView([latitude, longitude], 13);

            // Add a tile layer (e.g., OpenStreetMap)
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            // Add a marker at the user's location
            const marker = L.marker([latitude, longitude]).addTo(map);

            // Call Nominatim reverse geocoding API to get location details.
            fetch(`https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`)
                .then((response) => response.json())
                .then((data) => {
                    const address = data.address;
                    const city = address.city || address.town || address.village;
                    const placeName = address.suburb || address.locality || address.neighbourhood;
                    const pincode = address.postcode;

                    // Update HTML elements with location details.
                    document.getElementById("city").textContent = city;
                    document.getElementById("placeName").textContent = placeName;
                    document.getElementById("pincode").textContent = pincode;

                    // Pre-fill the automatic location input field
                    document.getElementById("automaticLocation").value = `${city}, ${placeName}, ${pincode}`;

                })
                .catch((error) => {
                    console.error("Error fetching location:", error);
                });
        }

        // Function to handle geolocation errors
        function showError(error) {
            console.log("Error fetching location:", error.message);
        }

        // Function to request and display user location
        function getUserLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(showUserLocation, showError);
            } else {
                console.log("Geolocation is not supported by your browser.");
            }
        }

        // Call getUserLocation when the page loads
        window.addEventListener("load", getUserLocation);