// Run function calls on page load
window.onload = function() {
    updateDailyFirstPoints();
    updateTotalFirstPoints();
    updateSevenDayAvgPoints();
    updateDailySecondPoints();
    updateTotalSecondPoints();
    updateDailyThirdPoints();
    updateTotalThirdPoints();
};

function fetchUpdates() {
    updateDailyFirstPoints();
    updateTotalFirstPoints();
    updateDailySecondPoints();
    updateTotalSecondPoints();
    updateDailyThirdPoints();
    updateTotalThirdPoints();
}

// Poll every x seconds; refresh values displayed
setInterval(fetchUpdates, 15000);

// first points
document.getElementById('first-button').addEventListener('click', function() {
    fetch('first-point', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        updateDailyFirstPoints();
        updateTotalFirstPoints();
    })
    .catch(error => console.error('Error:', error));
});

function updateDailyFirstPoints() {
    fetch('daily-first-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('daily-first-points').textContent = data.daily_first_points || 0;
    })
    .catch(error => {
        document.getElementById('daily-first-points').textContent = 'Error retrieving daily points';
        console.error('Error:', error);
    });
}

function updateTotalFirstPoints() {
    fetch('total-first-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('total-first-points').textContent = data.max_id || 'No data yet';
    })
    .catch(error => {
        document.getElementById('total-first-points').textContent = 'Error retrieving total points';
        console.error('Error:', error);
    });
}

function updateSevenDayAvgPoints() {
    fetch('seven-day-avg-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('seven-day-avg-points').textContent = data.seven_day_avg_points || '0';
    })
    .catch(error => {
        document.getElementById('seven-day-avg-points').textContent = 'Error retrieving seven-day-avg';
        console.error('Error:', error);
    });
}

// second point
document.getElementById('second-button').addEventListener('click', function() {
    fetch('second-point', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        updateDailySecondPoints();
        updateTotalSecondPoints();
    })
    .catch(error => console.error('Error:', error));
});

function updateDailySecondPoints() {
    fetch('daily-second-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('daily-second-points').textContent = data.daily_second_points || 0;
    })
    .catch(error => {
        document.getElementById('daily-second-points').textContent = 'Error retrieving daily points';
        console.error('Error:', error);
    });
}

function updateTotalSecondPoints() {
    fetch('total-second-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('total-second-points').textContent = data.total_second_points || 'No data yet';
    })
    .catch(error => {
        document.getElementById('total-second-points').textContent = 'Error retrieving total points';
        console.error('Error:', error);
    });
}

// third points
document.getElementById('third-button').addEventListener('click', function() {
    fetch('third-point', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        updateDailyThirdPoints();
        updateTotalThirdPoints();
    })
    .catch(error => console.error('Error:', error));
});

function updateDailyThirdPoints() {
    fetch('daily-third-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('daily-third-points').textContent = data.daily_third_points || 0;
    })
    .catch(error => {
        document.getElementById('daily-third-points').textContent = 'Error retrieving daily points';
        console.error('Error:', error);
    });
}

function updateTotalThirdPoints() {
    fetch('total-third-points')
    .then(response => response.json())
    .then(data => {
        document.getElementById('total-third-points').textContent = data.total_third_points || 'No data yet';
    })
    .catch(error => {
        document.getElementById('total-third-points').textContent = 'Error retrieving total points';
        console.error('Error:', error);
    });
}


