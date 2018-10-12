$("#submit").click(function () {
//  отправляем ajax запрос на сервер
  $.ajax({
      type: "GET",
      url: this,
      data: {
          'filial': $("#filial").val(),
          'locomotive': $('#locomotive').val(),
          'period': $('#period').val(),
      },
      dataType: "text",
      cache: false,
      success: function (data) {
          if (data == 'ok'){
              console.log('OK')
          }
          else if (data == 'no') {
            console.log('NO')
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


