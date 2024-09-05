// Wallet Expenditure Chart (Last 6 Months)
const walletCtx = document.getElementById('walletChart').getContext('2d');
const walletChart = new Chart(walletCtx, {
    type: 'bar',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [{
            label: 'Ksh Spent',
            data: [25000, 20000, 18000, 30000, 15000, 21000],
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Pie Chart for Expenditure vs Income
const expenditureIncomeCtx = document.getElementById('expenditureIncomeChart').getContext('2d');
const expenditureIncomeChart = new Chart(expenditureIncomeCtx, {
    type: 'pie',
    data: {
        labels: ['Expenditure', 'Income'],
        datasets: [{
            label: 'Expenditure vs Income',
            data: [400000, 600000], // Adjust the values for income and expenditure
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',  // Expenditure (red)
                'rgba(75, 192, 192, 0.6)'   // Income (green)
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true
    }
});