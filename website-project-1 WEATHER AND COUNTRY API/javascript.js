const $ = function (selector) { return document.querySelector(selector); };



// fetch country names and its up here to make sure it loads first
fetch('https://restcountries.com/v3.1/all')
.then(response => response.json()) 
.then(json => {
    countriesData = json;  
    buildPage2(countriesData);   
}) 
.catch(error => console.log(error));

// function to display country data 
const buildPage2 = function (data2) {
    console.log(data2);
}
    





let countriesData = [];
const result = [];






// reset button function
const reset = function () {

	$("#search").value = " ";
	
	const countryDataDiv = $("#countryData");
    countryDataDiv.innerHTML = "";
	
	const weatherDataDiv = $("#weatherData");
    weatherDataDiv.innerHTML = "";

	const chartCanvas = document.getElementById('weatherChart')
    if (Chart.getChart(chartCanvas)) { 
    
        // destroys chart if there is a chart
        Chart.getChart(chartCanvas).destroy();
	}

	result.length = 0; // Reset the result array

    $("#searchButton").disabled = false;
    
    

}





//COUNTRY SECTION

// Function to search for a country
// toLowerCase() converts the string to lowercase and includes(searchQuery) checks if its in  the search bar

function searchCountry() {
    const searchQuery = $("#search").value.trim().toLowerCase();

    const countryDataDiv = $("#countryData");
    countryDataDiv.innerHTML = ''; 

	
    // search query is the search box
    if (searchQuery) {

        result.length = 0;
        $("#searchButton").disabled = true;

        // for Loop through each country in the countriesData
        for (let i = 0; i < countriesData.length; i++) {
            const country = countriesData[i];

            //  if the country's name is in the search bar
            if (country.name.common.toLowerCase().includes(searchQuery)) {
                result.push(country);  // If the name matches, add the country to the result array
            }

            // if the country has capitals, check each capital
            if (country.capital) {
                for (let j = 0; j < country.capital.length; j++) {
                    if (country.capital[j].toLowerCase().includes(searchQuery)) {
                        result.push(country);  // If a capital matches, add the country to the result array
                    }
				}
			}
		}
	}





	// if something is in result array , display result (capital , region, subregion and population)
	if (result.length > 0) {
		result.forEach(country => {

            const latlng = country.latlng; // get the latitude and longitude from searched country

			const countryInfo = document.createElement("div");
                                                           
                                                            // used object.values because the data i wanted was in a array
			countryInfo.innerHTML = `
				<div class="w3-container w3-blue">
					<h2>${country.name.common}</h2>
				</div>
				
				<div class="w3-container">                  
					<p><strong>Capital:</strong>            ${country.capital}</p>
                    <p><strong>Currency:</strong>           ${Object.values(country.currencies)[0].symbol}</p>
					<p><strong>Region:</strong>             ${country.region}</p>
					<p><strong>Language:</strong>           ${Object.values(country.languages)}</p></p>
					<p><strong>Population:</strong>         ${country.population.toLocaleString()}</p>
                    <p><strong>Latitude and Longitude:</strong> ${country.latlng.join(', ')}</p>
                    <p><img src="${country.flags.svg}" class="w3-image" style="width: 50%;"></p>
				</div>
					`;



        // fetch the weather data for the selected country
        const weatherAPI = `https://api.open-meteo.com/v1/forecast?latitude=${latlng[0]}&longitude=${latlng[1]}&hourly=&daily=temperature_2m_max&timezone=GMT`;

        fetch(weatherAPI)
            .then(response => response.json())
            .then(json => buildPage(json)) 
            .catch(error => console.log(error));

        // append the country info to the page
        countryDataDiv.appendChild(countryInfo);
    });
} else {
    // If no countries matched, display a message
    countryDataDiv.innerHTML = '<p>No countries found matching that name or capital.</p>';
}



// function to display weather data 
const buildPage = function (data) {
    

	const tempMax = data.daily.temperature_2m_max; // max temperature data
    console.log(tempMax);
    
	
	showWeatherChart(tempMax.slice(0, 7)); // pass  7 days of temperature data
}



//WEATHER SECTION

function showWeatherChart(weatherdata) {
    const ctx = document.getElementById('weatherChart')

	const labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];


    // chart code from "https://www.chartjs.org/docs/latest/getting-started/"
	new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels, // x-axis labels
            datasets: [{
                label: 'Daily Max Temperature (°C)',
                data: weatherdata, // tempe data for each day
                backgroundColor: 'rgba(255, 99, 132, 0.5)', 
                borderColor: 'rgba(255, 99, 132, 1)', 
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Days of the Week',
                        font: { size: 14 },
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature (°C)',
                        font: { size: 14 },
                    },
                    beginAtZero: true,
                    min: -50,
                    max: 50, // maximum temperature
                    ticks: {
                        stepSize: 5 // Y goes up in 5
                    }
                }
            }
        }
    });
}
}
