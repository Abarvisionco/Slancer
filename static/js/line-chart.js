var ctx = document.getElementById("line-chart");
(Chart.defaults.global.defaultFontFamily = "iransans"), (Chart.defaults.global.defaultFontSize = 14), (Chart.defaults.global.defaultFontStyle = "500"), (Chart.defaults.global.defaultFontColor = "#233d63");
var chart = new Chart(ctx, {
    type: "line",
    data: {
        labels: ["جمعه", "پنجشنبه", "چهارشنبه", "سه شنبه", "دوشنبه", "یکشنبه", "شنبه"],
        datasets: [
            { label: "بازدید", data: [20, 40, 38, 55, 30, 40, 60], backgroundColor: "rgba(56, 127, 12, 0.05)", borderColor: "#38BB0C", pointBorderColor: "#ffffff", pointBackgroundColor: "#38BB0C", pointBorderWidth: 2, pointRadius: 4 },
        ],
    },
    options: {
        tooltips: { xPadding: 12, yPadding: 12, backgroundColor: "#232c3b",rtl:true },
        legend: { display: !1, tooltips: { displayColors: !1 } },
        scales: { xAxes: [{ display: !0, gridLines: { color: "#eee" } }], yAxes: [{ display: !0, gridLines: { color: "#eee" }, ticks: { fontSize: 14 } }] },
    },
});
