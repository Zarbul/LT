$("#submit").click(function () {
//  отправляем ajax запрос на сервер
  $.ajax({
      type: "GET",
      url: "/",
      data: {
          'filial': $("#filial").val(),
          'locomotive': $('#locomotive').val(),
          'period': $('#period').val(),
      },
      dataType: "text",
      cache: false,
      success: function (data) {
          if (data == 'ok'){

          }
          else if (data == 'no') {

          }
      }
  })
  })

// var totalCost = 0;
// var cost = (+{{ i.rate }} * +{{ j.run }});
// totalCost += cost;


// удаление дубликатов select
$('select option').each(function() {
  $(this).prevAll('option[value="' + this.value + '"]').remove();
});


