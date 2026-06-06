document.addEventListener('DOMContentLoaded', function() {
    initSidebar();
    initTableSearch();
    initPasswordToggle();
    initCharts();
    initTooltips();
    initAutoCloseAlerts();
});

/* Sidebar Toggle */
function initSidebar() {
    const toggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');

    if (toggle && sidebar) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            if (window.innerWidth < 992) {
                sidebar.classList.toggle('show');
            } else {
                sidebar.classList.toggle('collapsed');
                mainContent.classList.toggle('expanded');
            }
        });
    }
}

/* Table Search */
function initTableSearch() {
    document.querySelectorAll('.table-search').forEach(function(input) {
        input.addEventListener('keyup', function() {
            var filter = this.value.toLowerCase();
            var table = this.closest('.card').querySelector('table');
            if (!table) return;
            var rows = table.querySelectorAll('tbody tr');
            rows.forEach(function(row) {
                var text = row.textContent.toLowerCase();
                row.style.display = text.includes(filter) ? '' : 'none';
            });
        });
    });
}

/* Password Toggle */
function initPasswordToggle() {
    document.querySelectorAll('.password-toggle').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var input = this.closest('.input-group').querySelector('input');
            var icon = this.querySelector('i');
            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.replace('bi-eye', 'bi-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.replace('bi-eye-slash', 'bi-eye');
            }
        });
    });
}

/* Charts */
function initCharts() {
    initOcupacaoChart();
    initEspecialidadeChart();
    initReceitaChart();
    initConsumoChart();
}

function initOcupacaoChart() {
    var el = document.getElementById('ocupacaoChart');
    if (!el) return;
    var ctx = el.getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Sala 01', 'Sala 02', 'Sala 03', 'Sala 04', 'Sala 05', 'Sala 06', 'Sala 07', 'Sala 08', 'Sala 09', 'Sala 10', 'Sala 11', 'Sala 12'],
            datasets: [{
                label: 'Horas Utilizadas',
                data: [6, 8, 4, 7, 5, 3, 6, 2, 5, 4, 7, 1],
                backgroundColor: ['rgba(58,80,107,0.7)', 'rgba(91,192,190,0.7)'],
                borderColor: ['#3A506B', '#5BC0BE'],
                borderWidth: 1,
                borderRadius: 4,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' } },
                x: { grid: { display: false } }
            }
        }
    });
}

function initEspecialidadeChart() {
    var el = document.getElementById('especialidadeChart');
    if (!el) return;
    new Chart(el.getContext('2d'), {
        type: 'pie',
        data: {
            labels: ['Geral', 'Cardíaca', 'Ortopédica', 'Neurológica', 'Pediátrica', 'Outras'],
            datasets: [{
                data: [35, 15, 20, 10, 12, 8],
                backgroundColor: ['#3A506B', '#5BC0BE', '#4A90D9', '#F4A261', '#E76F51', '#D9E2EC'],
                borderWidth: 2,
                borderColor: '#fff',
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { position: 'bottom', labels: { padding: 12, usePointStyle: true } } }
        }
    });
}

function initReceitaChart() {
    var el = document.getElementById('receitaChart');
    if (!el) return;
    var meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
    new Chart(el.getContext('2d'), {
        type: 'line',
        data: {
            labels: meses,
            datasets: [{
                label: 'Receita 2026',
                data: [180000, 210000, 195000, 230000, 245000, 220000, 260000, 240000, 275000, 290000, 310000, 335000],
                borderColor: '#5BC0BE',
                backgroundColor: 'rgba(91,192,190,0.1)',
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#5BC0BE',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 4,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { callback: function(v) { return 'R$ ' + (v/1000).toFixed(0) + 'k'; } },
                    grid: { color: 'rgba(0,0,0,0.05)' }
                },
                x: { grid: { display: false } }
            }
        }
    });
}

function initConsumoChart() {
    var el = document.getElementById('consumoChart');
    if (!el) return;
    new Chart(el.getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Fios Cirúrgicos', 'Lâminas', 'Sondas', 'Luvas', 'Compressas', 'Medicamentos'],
            datasets: [{
                data: [25, 15, 20, 18, 12, 10],
                backgroundColor: ['#3A506B', '#5BC0BE', '#4A90D9', '#F4A261', '#E76F51', '#6C5CE7'],
                borderWidth: 2,
                borderColor: '#fff',
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '60%',
            plugins: { legend: { position: 'bottom', labels: { padding: 10, usePointStyle: true, font: { size: 11 } } } }
        }
    });
}

/* Tooltips */
function initTooltips() {
    var tooltips = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltips.map(function(el) { return new bootstrap.Tooltip(el); });
}

/* Auto close alerts */
function initAutoCloseAlerts() {
    document.querySelectorAll('.alert-dismissible').forEach(function(alert) {
        setTimeout(function() {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

/* Open info modal */
function openInfoModal(title, body) {
    document.getElementById('infoModalTitle').textContent = title;
    document.getElementById('infoModalBody').innerHTML = body;
    var modal = new bootstrap.Modal(document.getElementById('infoModal'));
    modal.show();
}

/* Print table */
function printTable(tableId) {
    var printContents = document.getElementById(tableId).outerHTML;
    var win = window.open('', '_blank');
    win.document.write('<html><head><title>Impressão</title>');
    win.document.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">');
    win.document.write('</head><body>' + printContents + '</body></html>');
    win.document.close();
    win.print();
}

/* Format currency */
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value);
}

/* Format date */
function formatDate(dateStr) {
    var d = new Date(dateStr);
    return d.toLocaleDateString('pt-BR');
}
