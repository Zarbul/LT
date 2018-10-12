$("#submit").click(function () {
    var filial = $("#filial").val();
    var locomotive = $('#locomotive').val();
    var period = $('#period').val();
//  отправляем ajax запрос на сервер
    $.ajax({
        type: "GET",
        url: '/index/',
        data: {
            'filial': filial,
            'locomotive': locomotive,
            'period': period
        },
        dataType: "json",
        success: function (data) {
            console.log(data);
            render(data);
        }
    });
    return false;
});

function render(obj) {
    var value = [];
    var year = [];
    for (var key in obj) {
        year.push(key);
        value.push(obj[key]);
    }
    var barChartData = {
        labels: year,
        datasets: [
            {
                fillColor: "rgba(220,220,220,0.5)",
                strokeColor: "rgba(220,220,220,0.8)",
                highlightFill: "rgba(220,220,220,0.75)",
                highlightStroke: "rgba(220,220,220,1)",
                data: value
            }
        ]
    };
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myBar = new Chart(ctx).Bar(barChartData, {
        responsive: true
    });
}


// удаление дубликатов select
$('select option').each(function () {
    $(this).prevAll('option[value="' + this.value + '"]').remove();
});


