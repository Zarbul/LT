// $.ajax({
//     type: "GET",
//     url: this,
//     data: {
//         'filial': $("#filial").val()
//     },
//     dataType: "text",
//     cache: false,
//     success: function (data) {
//         if (data == 'ok'){
//
//         }
//         else if (data == 'no') {
//
//         }
//     }
// })
// var totalCost = 0;
// var cost = (+{{ i.rate }} * +{{ j.run }});
// totalCost += cost;


//удаление дубликатов select
var found = [];
$("select option").each(function() {
  if($.inArray(this.value, found) != -1) $(this).remove();
  found.push(this.value);
});

//
// var barChartData = {
//     labels : [{{ periods.year }}],
//     datasets : [
//         {
//             fillColor : "rgba(220,220,220,0.5)",
//             strokeColor : "rgba(220,220,220,0.8)",
//             highlightFill: "rgba(220,220,220,0.75)",
//             highlightStroke: "rgba(220,220,220,1)",
//             data : [totalCost]
//         },
//         // {#{#}
//         // {#	fillColor : "rgba(151,187,205,0.5)",#}
//         // {#	strokeColor : "rgba(151,187,205,0.8)",#}
//         // {#	highlightFill : "rgba(151,187,205,0.75)",#}
//         // {#	highlightStroke : "rgba(151,187,205,1)",#}
//         // {#	data : [randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]#}
//         // {# } #}
//     ]
//
// }
// window.onload = function(){
//     var ctx = document.getElementById("canvas").getContext("2d");
//     window.myBar = new Chart(ctx).Bar(barChartData, {
//         responsive : true
//     });
// }
