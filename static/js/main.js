document.addEventListener('DOMContentLoaded', function() {
    initCharts();
});

function initCharts() {
    var ocupacaoEl = document.getElementById('ocupacaoChart');
    if (ocupacaoEl) {
        new Chart(ocupacaoEl, {
            type: 'bar',
            data: {
                labels: ['Sala 1', 'Sala 2', 'Sala 3', 'Sala 4', 'Sala 5', 'Sala 6'],
                datasets: [{
                    label: 'Horas Utilizadas',
                    data: [6, 8, 4, 7, 5, 3],
                    backgroundColor: 'rgba(13, 110, 253, 0.7)',
                    borderColor: 'rgba(13, 110, 253, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } }
            }
        });
    }

    var distribuicaoEl = document.getElementById('distribuicaoChart');
    if (distribuicaoEl) {
        new Chart(distribuicaoEl, {
            type: 'doughnut',
            data: {
                labels: ['Disponível', 'Ocupada', 'Manutenção'],
                datasets: [{
                    data: [5, 6, 1],
                    backgroundColor: ['#198754', '#dc3545', '#ffc107']
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { position: 'bottom' } }
            }
        });
    }
}

htmx.onLoad(function(target) {
    if (target.querySelector('#resultado-ia')) {
        var result = target.querySelector('#resultado-ia');
        result.innerHTML = '<div class="alert alert-info">' + result.innerHTML + '</div>';
    }
});
