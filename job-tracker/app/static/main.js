async function searchJobs() {
    const keyword = document.getElementById("keyword").value;
    const location = document.getElementById("location").value;
    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = '<div class="loading">Searching for jobs...</div>';

    try {
        const response = await fetch(`/api/linkedin-jobs?keyword=${encodeURIComponent(keyword)}&locationId=${getLocationId(location)}`);
        const data = await response.json();

        if (response.ok) {
            if (Array.isArray(data) && data.length > 0) {
                displayJobs(data);
            } else if (data.error) {
                resultsDiv.innerHTML = `<div class="error">Error: ${data.error}</div>`;
            } else {
                resultsDiv.innerHTML = '<div class="no-results">No jobs found matching your criteria.</div>';
            }
        } else {
            resultsDiv.innerHTML = `<div class="error">API Error: ${response.status}</div>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<div class="error">Network error: ${error.message}</div>`;
    }
}

function getLocationId(locationName) {
    const locations = {
        "ireland": "104738515",
        "us": "103644278",
        "uk": "101165590",
        "germany": "101282230",
        "france": "105015875",
        "worldwide": "92000000"
    };

    return locations[locationName.toLowerCase()] || "104738515"; // Default to Ireland
}

function displayJobs(jobs) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = `
        <div class="results-header">
            <h2>${jobs.length} Jobs Found</h2>
        </div>
        <div class="job-list">
            ${jobs.map(job => `
                <div class="job-card">
                    <h3>${job.title}</h3>
                    <div class="company">${job.companyName}</div>
                    <div class="meta">
                        <span class="location">📍 ${job.location}</span>
                        <span class="date">📅 ${formatDate(job.datePosted)}</span>
                    </div>
                    <a href="${job.jobUrl}" target="_blank" class="apply-btn">View on LinkedIn</a>
                </div>
            `).join('')}
        </div>
    `;
}

function formatDate(dateString) {
    if (!dateString) return "Unknown date";
    try {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    } catch {
        return dateString; // Return raw string if date parsing fails
    }
}

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    searchJobs();
});