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
        .then(response => {
            if (!response.ok) {
                throw new Error("Ошибка сети: " + response.statusText);
                alert(response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const weatherDiv = document.querySelector(".weather-result");
            weatherDiv.innerHTML = "";

            if (data.error) {
                weatherDiv.textContent = data.error;
            } else {
                const p = document.createElement("p");
                p.textContent = `Weather in ${city} </br> Condition: ${data.condition}, temperature: ${data.temp}°C </br> Wind: ${data.wind_speed} m/s, feels_like: ${data.feels_like}°C`;
                weatherDiv.appendChild(p);
            }
        })
        .catch(error => {
            console.error("Ошибка при получении погоды:", error);
        });
}


document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".choese-history-button");
    const historyList = document.querySelector(".history-ul");

    button.addEventListener("click", async function () {
        const isSelf = button.textContent === "Check self history";
        const endpoint = isSelf
            ? "/api/weather/get_self_history"
            : "/api/weather/get_all_history";

        // Меняем текст кнопки
        button.textContent = isSelf ? "Check all history" : "Check self history";

        try {
            const response = await fetch(endpoint);
            const data = await response.json(); // Ожидаем массив строк

            // Очищаем текущие элементы списка
            historyList.innerHTML = "";

            // Добавляем новые
            data.forEach(entry => {
                const li = document.createElement("li");
                li.classList.add("weather-data-li");
                li.textContent = entry;
                historyList.appendChild(li);
            });
        } catch (error) {
            console.error("Ошибка при загрузке истории:", error);
        }
    });
});