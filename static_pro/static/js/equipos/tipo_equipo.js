$(function () {
  $('#tipo-equipo-table tbody').animateCss('lightSpeedIn');
  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-tipo-equipo .modal-content").html("");
        $("#modal-tipo-equipo").modal("show");
      },
      success: function (data) {
        $("#modal-tipo-equipo .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {

          $("#tipo-equipo-table tbody").html(data.html_tipo_equipo_list);
          $('#tipo-equipo-table tbody').animateCss('lightSpeedIn');
          $("#modal-tipo-equipo").modal("hide");
          $.notify("Guardado con exito!", {
              placement: {
                  from: 'bottom',
                  align: 'center'
              },
              icon:'far fa-paw',
              type:'success',
              animate: {
                  enter: 'animated bounceIn',
                  exit: 'animated bounceOut'
              },
              delay:100
          });
        }
        else {
          $("#modal-tipo-equipo .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create equipo
  $(".js-create-tipo-equipo").click(loadForm);
  $("#modal-tipo-equipo").on("submit", ".js-tipo-equipo-create-form", saveForm);

  // Update equipo
  $("#tipo-equipo-table").on("click", ".js-update-tipo-equipo", loadForm);
  $("#modal-tipo-equipo").on("submit", ".js-tipo-equipo-update-form", saveForm);

  // Delete equipo
  $("#tipo-equipo-table").on("click", ".js-delete-tipo-equipo", loadForm);
  $("#modal-tipo-equipo").on("submit", ".js-tipo-equipo-delete-form", saveForm);






});
