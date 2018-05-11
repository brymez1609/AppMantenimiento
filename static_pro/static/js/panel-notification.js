$(function(){
      $("#btnGroupDrop1").click(function(e) {
        e.preventDefault();
        $.ajax({
             url : 'mantenimientos/', // the endpoint,commonly same url
             type : "GET", // http method
            // handle a successful response
            success : function(json) {
                //console.log(json); // another sanity check
                //On success show the data posted to server as a message
               console.log(json);
                if (json[0].length > 0){
                    $('#dropdown-notifications').innerHTML+="<a class='dropdown-item' href='#'>"+"epaa"+"</a>";
                } else {
                    $('#dropdown-notifications').html="<h6 class=\"text-center animated bounceIn\">No hay notifiaciones</h6>";
                }
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            },
            always:function () {
               // document.getElementById("barra_progreso").removeChild();
            }
        }).done(function () {


        });
    });
});

