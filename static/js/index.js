// Add an event listener to handle form submission
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("cropForm");

  form.addEventListener("submit", async (event) => {
      event.preventDefault(); // Prevent default form submission

      // Collect input values
      const nitrogen = document.getElementById("nitrogen").value;
      const phosphorous = document.getElementById("phosphorous").value;
      const potassium = document.getElementById("potassium").value;
      const temperature = document.getElementById("temperature").value;
      const humidity = document.getElementById("humidity").value;
      const ph = document.getElementById("ph").value;
      const rainfall = document.getElementById("rainfall").value;

      // Prepare the data to send
      const requestData = {
          nitrogen: parseFloat(nitrogen),
          phosphorous: parseFloat(phosphorous),
          potassium: parseFloat(potassium),
          temperature: parseFloat(temperature),
          humidity: parseFloat(humidity),
          ph: parseFloat(ph),
          rainfall: parseFloat(rainfall),
      };

      try {
          // Send the data to the Flask backend
          const response = await fetch("/predict", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify(requestData),
          });

          // Handle the response
          const result = await response.json();

          if (response.ok) {
              // Display the recommended crop
              document.getElementById("result").textContent = `Recommended Crop: ${result.crop}`;
          } else {
              // Display an error message
              document.getElementById("result").textContent = `Error: ${result.error}`;
          }
      } catch (error) {
          // Handle network or unexpected errors
          document.getElementById("result").textContent = `Error: ${error.message}`;
      }
  });
});
