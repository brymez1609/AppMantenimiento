$(function () {

  /* Functions */
  $('#equipo-table tbody').animateCss('lightSpeedIn');
  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-equipo .modal-content").html("");
        $("#modal-equipo").modal("show");
      },
      success: function (data) {
        $("#modal-equipo .modal-content").html(data.html_form);
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
          $("#equipo-table tbody").html(data.html_equipo_list);
          $('#equipo-table tbody').animateCss('lightSpeedIn');
          $("#modal-equipo").modal("hide");
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
          $("#modal-equipo .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create equipo
  $(".js-create-equipo").click(loadForm);
  $("#modal-equipo").on("submit", ".js-equipo-create-form", saveForm);

  // Update equipo
  $("#equipo-table").on("click", ".js-update-equipo", loadForm);
  $("#modal-equipo").on("submit", ".js-equipo-update-form", saveForm);

  // Delete equipo
  $("#equipo-table").on("click", ".js-delete-equipo", loadForm);
  $("#modal-equipo").on("submit", ".js-equipo-delete-form", saveForm);

});
