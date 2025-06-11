// static/script.js

// Crosshair plugin for Chart.js
const crosshairPlugin = {
  id: 'crosshairPlugin',
  afterDraw(chart) {
    if (chart.tooltip._active && chart.tooltip._active.length) {
      const ctx = chart.ctx;
      const x = chart.tooltip._active[0].element.x;
      const y = chart.tooltip._active[0].element.y;
      const topY = chart.scales.y.top;
      const bottomY = chart.scales.y.bottom;
      const leftX = chart.scales.x.left;
      const rightX = chart.scales.x.right;

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(x, topY);
      ctx.lineTo(x, bottomY);
      ctx.moveTo(leftX, y);
      ctx.lineTo(rightX, y);
      ctx.lineWidth = 1;
      ctx.strokeStyle = '#888';
      ctx.setLineDash([5, 5]);
      ctx.stroke();
      ctx.restore();
    }
  }
};

Chart.register(crosshairPlugin);

async function fetchStock() {
  const symbol = document.getElementById("symbol").value;
  const range = document.getElementById("range").value;

  try {
    const response = await fetch(`/api/stock?symbol=${symbol}&range=${range}`);
    const data = await response.json();

    if (data.error) {
      alert(data.error);
      return;
    }

    document.getElementById("live-price").innerText = `Latest Price: $${data.latest_price}`;

    const ctx = document.getElementById("chart").getContext("2d");

    if (window.myChart) {
      window.myChart.destroy();
    }

    window.myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: data.dates,
        datasets: [{
          label: `${data.symbol} Price`,
          data: data.prices,
          borderColor: "#764ba2",
          backgroundColor: "rgba(118, 75, 162, 0.1)",
          tension: 0.3,
          pointRadius: 3,
          pointHoverRadius: 6,
          fill: true,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        interaction: {
          mode: 'nearest',
          axis: 'x',
          intersect: false
        },
        plugins: {
          legend: {
            labels: {
              font: {
                size: 14,
                weight: "bold"
              },
              color: "#333"
            }
          },
          tooltip: {
            backgroundColor: "#333",
            titleColor: "#fff",
            bodyColor: "#fff"
          },
          zoom: {
            pan: {
              enabled: true,
              mode: 'x',
              modifierKey: 'ctrl'
            },
            zoom: {
              wheel: {
                enabled: true
              },
              pinch: {
                enabled: true
              },
              mode: 'x'
            }
          }
        },
        scales: {
          x: {
            ticks: {
              color: "#555",
              font: {
                size: 12,
                weight: "600"
              },
              maxRotation: 35,
              minRotation: 20,
              autoSkip: true,
              padding: 10
            },
            grid: {
              display: false
            }
          },
          y: {
            ticks: {
              color: "#555",
              font: {
                size: 12,
                weight: "600"
              },
              padding: 8
            },
            grid: {
              color: "#ececec"
            }
          }
        }
      }
    });

  } catch (error) {
    console.error("Error fetching data:", error);
    alert("Failed to fetch data.");
  }
}

function resetZoom() {
  if (window.myChart) {
    window.myChart.resetZoom();
  }
}
