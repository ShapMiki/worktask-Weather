document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("weather-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // отменяем перезагрузку страницы
        getWeather();
    });
});

function getWeather() {
    const city = document.querySelector("#city-input").value;
    console.log("Запрашиваем погоду для:", city);
    const endpoint = "/api/weather/current/" + encodeURIComponent(city);

    fetch(endpoint)
        .then(async response => {
            if (!response.ok) {
                  const errorData = await response.json();
                  document.querySelector(".weather-result").innerHTML = "";
                  alert("Error: " + (errorData.detail || response.statusText || response.status));
                  throw new Error("Ошибка сети: " + (errorData.detail || response.statusText || response.status));
            }
            return response.json();
        })
        .then(data => {
            const weatherDiv = document.querySelector(".weather-result");
            weatherDiv.innerHTML = "";

            if (data.error) {
                alert(data.error);
                weatherDiv.textContent = "";
            } else {
                const container = document.createElement("div");
                container.classList.add("weather-block");

                const cityP = document.createElement("p");
                cityP.textContent = `Weather in ${city}`;
                cityP.classList.add("weather-city");

                const conditionP = document.createElement("p");
                conditionP.textContent = `Condition: ${data.condition}, temperature: ${data.temp}°C`;
                conditionP.classList.add("weather-condition");

                const windP = document.createElement("p");
                windP.textContent = `Wind: ${data.wind_speed} m/s, feels like: ${data.feels_like}°C`;
                windP.classList.add("weather-wind");

                container.appendChild(cityP);
                container.appendChild(conditionP);
                container.appendChild(windP);

                weatherDiv.appendChild(container);
            }
        })
        .catch(error => {
            document.querySelector(".weather-result").innerHTML = "";
            console.error("Ошибка при получении погоды:", error);
        });
}

document.querySelector('.cleaner-button').addEventListener('click', async () => {
  try {
    const response = await fetch('/api/user/', {
      method: 'DELETE',
      credentials: 'same-origin'
    });
    if (response.ok) {
      window.location.reload();
    } else {
      alert('Ошибка при очистке истории');
    }
  } catch (error) {
    alert('Ошибка сети');
    console.error(error);
  }
});
