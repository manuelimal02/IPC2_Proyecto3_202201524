$(document).ready(function() {
    $("#cargar_archivo_mensaje").click(function(e) {
        e.preventDefault();
        var form = new FormData();
        form.append('data', $("#inputData").val());
        form.append('file', $("#file-input-mensaje")[0].files[0]);
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        form.append('csrfmiddlewaretoken', csrfToken);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/grabarMensajes",
            data: form,
            processData: false,
            contentType: false,
            success: function(response) {
                alert(response.message);
                
            },
            error: function(xhr, status, error) {
                alert(error);
            }
        });
    });

    $("#consultar_hashtag").click(function() {
        $.get("/MyApp/consultaHashtag", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });    

    $("#consultar_menciones").click(function() {
        $.get("/MyApp/consultaMenciones", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#consultar_sentimiento").click(function() {
        $.get("/MyApp/consultaSentimiento", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#grafica_hashtag").click(function() {
        $.get("/MyApp/graficaHashtag", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });    

    $("#grafica_menciones").click(function() {
        $.get("/MyApp/graficaMenciones", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#grafica_sentimiento").click(function() {
        $.get("/MyApp/graficaSentimiento", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#resumen_mensajes").click(function() {
        $.get("/MyApp/resumenMensajes", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#resumen_configuraciones").click(function() {
        $.get("/MyApp/resumenConfiguraciones", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#informacion_estudiante").click(function() {
        $.get("/MyApp/informacionEstudiante", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

    $("#resetear_datos").click(function() {
        $.get("/MyApp/resetarDatos", function(response) {
            $("#mensajeTexto").val(response.message);
        });
    });

});

$(document).ready(function() {
    $("#cargar_archivo_config").click(function(e) {
        e.preventDefault();
        var form = new FormData();
        form.append('data', $("#inputData").val());
        form.append('file', $("#file-input-config")[0].files[0]);
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        form.append('csrfmiddlewaretoken', csrfToken);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/grabarConfiguracion",
            data: form,
            processData: false,
            contentType: false,
            success: function(response) {
                alert(response.message);
                
            },
            error: function(xhr, status, error) {
                alert(error);
            }
        });
    });
});