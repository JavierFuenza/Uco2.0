document.addEventListener("DOMContentLoaded", function () {

    function calcularEdad(fecha) {
        var hoy = new Date();
        var cumpleanos = new Date(fecha);
        var edad = hoy.getFullYear() - cumpleanos.getFullYear();
        var m = hoy.getMonth() - cumpleanos.getMonth();

        if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
            edad--;
        }

        return edad;
    }

    document.getElementById("formulario").addEventListener('submit', function (event) {

        event.preventDefault();

        var nombre = document.getElementById('nombreUsuario').value;
        if (nombre.length < 3 || nombre.length > 20) {
            alert('Nombre no Valido');
            return;
        }
        var apellido = document.getElementById('apellidoUsuario').value;
        if (apellido.length < 3 || apellido.length > 20) {
            alert('Apellido no Valido');
            return;
        }
        var edad = calcularEdad(document.getElementById('fecnacUsuario').value);
        if (edad < 18) {
            alert('Solo pueden tener cuenta personas mayores de edad');
            return;
        }
        this.submit();

        $(document).ready(function () {
            $.ajax({
                url: "https://apis.digital.gob.cl/dpa/regiones",
                type: "GET",
                crossDomain: true,
                dataType: "jsonp",
                success: function (data) {
                    $.each(data, function (i, item) {
                        $("#cboRegiones").append(
                            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
                        );
                    });
                },
                error: function (xhr, status, error) {
                    console.log("Error al obtener las regiones: " + error);
                },
            });


            //Accionador de evento de tipo Change indicando que cada vez que se cambie el item de region se realizara lo siguiente

            $("#cboRegiones").change(function () {
                //Tomamos el valor del item seleccionado en el select de region
                var idRegion = $("#cboRegiones").val();
                //QUitamos el atributo de deshabilitado del select de provincias
                $("#cboProvincias").attr("disabled", false);
                //Vaciamos las opciones de provincias(Para evitar una sobrecarga de los mismos campos)
                $("#cboProvincias").empty();
                //Al quedar vacio quedaria en blanco ,m para evitar esto insertamos un registro base de tipo disable hidden que diga seleccione una opcion
                $("#cboProvincias").append("<option hidden disable>Seleccione una opcion</option>");
                //Mismo proceso para comunas y asi evitar la sobrecarga de campos y el correcto funcionamiento de los campos
                $("#cboComunas").empty();
                $("#cboComunas").append("<option hidden disable>Seleccione una opcion</option>");
                //Mismo proceso que con las regiones solo que en este caso insertaremos el ID obtenido de regiones en el URL de la api de regiones
                //URL Original: https://apis.digital.gob.cl/dpa/regiones/{codigo}/provincias
                $.ajax({
                    url: "https://apis.digital.gob.cl/dpa/regiones/" + idRegion + "/provincias",
                    type: "GET",
                    crossDomain: true,
                    dataType: "jsonp",
                    success: function (data) {
                        $.each(data, function (i, item) {
                            $("#cboProvincias").append(
                                "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
                            );
                        });
                    },
                    error: function (xhr, status, error) {
                        console.log("Error al obtener las regiones: " + error);
                    },
                });
            });

            //Replicamos el mismo proceso de la funcion anterior pero con el select de provincias
            $("#cboProvincias").change(function () {
                var idRegion = $("#cboRegiones").val();
                var idProvincia = $("#cboProvincias").val();
                $("#cboComunas").attr("disabled", false);
                $("#cboComunas").empty();
                $("#cboComunas").append("<option hidden disable>Seleccione una opcion</option>");
                //URL original https://apis.digital.gob.cl/dpa/regiones/{codigo}/provincias/{codigo}/comunas
                $.ajax({
                    url: "https://apis.digital.gob.cl/dpa/regiones/" + idRegion + "/provincias/" + idProvincia + "/comunas",
                    type: "GET",
                    crossDomain: true,
                    dataType: "jsonp",
                    success: function (data) {
                        $.each(data, function (i, item) {
                            $("#cboComunas").append(
                                "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
                            );
                        });
                    },
                    error: function (xhr, status, error) {
                        console.log("Error al obtener las regiones: " + error);
                    },
                });
            });
        });
    });
});