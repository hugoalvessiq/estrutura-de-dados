// --- 1. UTILITY FUNCTIONS ---

// Label Wrapping Logic (Mandatory for > 16 chars)
function wrapLabel(label) {
    if (label.length <= 16) return label;
    const words = label.split(" ");
    const lines = [];
    let currentLine = words[0];

    for (let i = 1; i < words.length; i++) {
        if ((currentLine + " " + words[i]).length <= 16) {
            currentLine += " " + words[i];
        } else {
            lines.push(currentLine);
            currentLine = words[i];
        }
    }
    lines.push(currentLine);
    return lines;
}

// Common Tooltip Config (Mandatory)
const commonTooltipConfig = {
    callbacks: {
        title: function (tooltipItems) {
            const item = tooltipItems[0];
            let label = item.chart.data.labels[item.dataIndex];
            if (Array.isArray(label)) {
                return label.join(" ");
            } else {
                return label;
            }
        },
    },
};

// --- 2. CHART.JS VISUALIZATIONS ---

// Chart 1: Big-O Complexity (Line Chart)
const ctxBigO = document.getElementById("bigOChart").getContext("2d");
const xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

new Chart(ctxBigO, {
    type: "line",
    data: {
        labels: xValues,
        datasets: [
            {
                label: "O(1) - Excelente",
                data: xValues.map(() => 1),
                borderColor: "#22c55e", // Green
                borderWidth: 3,
                pointRadius: 0,
                tension: 0.1,
            },
            {
                label: "O(log n) - Bom",
                data: xValues.map((x) => Math.log2(x)),
                borderColor: "#06b6d4", // Cyan
                borderWidth: 3,
                pointRadius: 0,
                tension: 0.1,
            },
            {
                label: "O(n) - Justo",
                data: xValues.map((x) => x),
                borderColor: "#facc15", // Yellow
                borderWidth: 3,
                pointRadius: 0,
                tension: 0.1,
            },
            {
                label: "O(n^2) - Ruim",
                data: xValues.map((x) => Math.pow(x, 1.8)), // Scaled down slightly for visuals
                borderColor: "#f43f5e", // Pink/Red
                borderWidth: 3,
                pointRadius: 0,
                tension: 0.1,
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                display: false,
                title: { display: true, text: "Tempo" },
            },
            x: {
                display: false,
                title: { display: true, text: "Dados (N)" },
            },
        },
        plugins: {
            tooltip: commonTooltipConfig,
            legend: { position: "bottom" },
        },
    },
});

// Chart 2: Linear Structures Comparison (Grouped Bar)
const ctxLinear = document.getElementById("linearChart").getContext("2d");
const rawLabelsLinear = [
    "Acesso (Leitura)",
    "Inserção (Início)",
    "Inserção (Fim)",
    "Busca",
];
const wrappedLabelsLinear = rawLabelsLinear.map(wrapLabel);

new Chart(ctxLinear, {
    type: "bar",
    data: {
        labels: wrappedLabelsLinear,
        datasets: [
            {
                label: "Array (Lista Python)",
                data: [1, 4, 1, 3], // 1=Fast, 4=Very Slow
                backgroundColor: "#1e3a8a", // Deep Blue
                borderRadius: 4,
            },
            {
                label: "Lista Ligada",
                data: [3, 1, 1, 3], // 1=Fast, 3=Slow
                backgroundColor: "#06b6d4", // Cyan
                borderRadius: 4,
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                max: 5,
                ticks: {
                    callback: function (val) {
                        if (val === 1) return "Rápido O(1)";
                        if (val === 3) return "Lento O(n)";
                        if (val === 4) return "Muito Lento";
                        return "";
                    },
                },
            },
        },
        plugins: {
            tooltip: commonTooltipConfig,
            legend: { position: "bottom" },
        },
    },
});

// Chart 3: Graph Network (Scatter Chart)
const ctxGraph = document.getElementById("graphChart").getContext("2d");
const nodes = [
    { x: 2, y: 5, label: "Você" },
    { x: 4, y: 8, label: "Alice" },
    { x: 4, y: 2, label: "Bob" },
    { x: 7, y: 6, label: "Charlie" },
    { x: 6, y: 3, label: "Dani" },
];

new Chart(ctxGraph, {
    type: "scatter",
    data: {
        datasets: [
            {
                label: "Nós (Vértices)",
                data: nodes,
                backgroundColor: "#f97316", // Orange
                pointRadius: 10,
                pointHoverRadius: 12,
            },
            // Simulating Edges
            {
                type: "line",
                label: "Conexão",
                data: [
                    { x: 2, y: 5 },
                    { x: 4, y: 8 },
                ], // You -> Alice
                borderColor: "#cbd5e1",
                borderWidth: 2,
                showLine: true,
                pointRadius: 0,
            },
            {
                type: "line",
                label: "Conexão",
                data: [
                    { x: 2, y: 5 },
                    { x: 4, y: 2 },
                ], // You -> Bob
                borderColor: "#cbd5e1",
                borderWidth: 2,
                showLine: true,
                pointRadius: 0,
            },
            {
                type: "line",
                label: "Conexão",
                data: [
                    { x: 4, y: 8 },
                    { x: 7, y: 6 },
                ], // Alice -> Charlie
                borderColor: "#cbd5e1",
                borderWidth: 2,
                showLine: true,
                pointRadius: 0,
            },
            {
                type: "line",
                label: "Conexão",
                data: [
                    { x: 4, y: 2 },
                    { x: 6, y: 3 },
                ], // Bob -> Dani
                borderColor: "#cbd5e1",
                borderWidth: 2,
                showLine: true,
                pointRadius: 0,
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: { display: false, min: 0, max: 10 },
            y: { display: false, min: 0, max: 10 },
        },
        plugins: {
            legend: { display: false },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        if (context.dataset.type === "scatter") {
                            return context.raw.label;
                        }
                        return "";
                    },
                },
            },
        },
    },
});

// --- 3. PLOTLY.JS VISUALIZATIONS ---

// Tree Balance Chart (Bar)
// Comparison of height of Balanced vs Unbalanced Tree for N=15
const trace1 = {
    x: ["Árvore Balanceada", "Árvore Desbalanceada (Lista)"],
    y: [4, 15], // Log2(15) approx 4, Linear is 15
    type: "bar",
    marker: {
        color: ["#22c55e", "#ef4444"],
    },
};

const layoutPlotly = {
    title: {
        text: "Altura da Árvore (Passos de Busca)",
        font: { size: 14 },
    },
    font: { family: "Poppins" },
    autosize: true,
    margin: { t: 40, b: 30, l: 30, r: 20 },
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    yaxis: { title: "Passos Necessários" },
};

const configPlotly = { responsive: true, displayModeBar: false };

Plotly.newPlot("treePlotlyChart", [trace1], layoutPlotly, configPlotly);
