$(function(){
  $("#btnGroupDrop1").click(function(e) {
       CargarMovimientos(e);
  });

    var saveForm = function (e,valor,id_dropdown) {
        var csrftoken = getCookie('csrftoken');
        var form = $(this);
        $.ajax({
          url: 'mantenimientos/',
          data: {
              csrfmiddlewaretoken : csrftoken,
              id: valor
          },
          type: 'POST',
          dataType: 'json',
          success: function (data) {
              console.log(data);
              CargarMovimientos(e);
            //var objeto = document.getElementById(id_dropdown);
            //objeto.remove();
          },
          error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
          }
        });
        return false;
    };

        function getCookie(name) {
           var cookieValue = null;
           if (document.cookie && document.cookie != '') {
             var cookies = document.cookie.split(';');
             for (var i = 0; i < cookies.length; i++) {
             var cookie = jQuery.trim(cookies[i]);
             // Does this cookie string begin with the name we want?
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                 break;
              }
         }
     }
     return cookieValue;
    }



    function CargarMovimientos(e) {
        e.preventDefault();
        $.ajax({
             url : 'mantenimientos/', // the endpoint,commonly same url
             type : "GET", // http method
            // handle a successful response
            success : function(json) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message

                if (json.length > 0){
                    //console.log(json);
                    document.getElementById('dropdown-notifications').innerHTML = "";
                    for (x in json){
                        var id_dropdown_item = json[x]['id_equipos_id'] + json[x]['id_mantenimiento'];
                        document.getElementById('dropdown-notifications').innerHTML +="" +
                            "<div class='dropdown-item' id='"+id_dropdown_item+"'>"+
                                "<p class=''>El equipo <strong>"+json[x]['id_equipos_id']+"</strong> requiere mantenimiento !</p>"+
                                "<p class=''>Fecha de mantenimiento <strong>"+json[x]['fecha']+"</strong></p>"+
                                "<label class=\"form-check-label\">" +
                            "Mantenimiento realizado ? &nbsp;&nbsp; " +
                            "          <input id='"+json[x]['id_mantenimiento']+"' class='' value=\"\"  type=\"checkbox\">" +
                            "        </label>"+
                            "</div>"+
                            "<div class=\"dropdown-divider\"></div>";

                        $( "input" ).change(function() {
                            var text = this.id;
                            saveForm(e,text,id_dropdown_item);
                        });
                    }
                } else {
                    document.getElementById('dropdown-notifications').innerHTML ="<h6 class=\"text-center animated bounceIn\">No hay notifiaciones</h6>";
                }
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                document.getElementById('dropdown-notifications').innerHTML ="<h6 class=\"text-center animated bounceIn\">Error al cargar Movimientos</h6>";
            },
            always:function () {
               // document.getElementById("barra_progreso").removeChild();
            }
        }).done(function () {


        });
    }

});

