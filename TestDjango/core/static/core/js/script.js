
$(document).ready(function() {
    $.getJSON('127.0.0.1:8000/api/lista_productos', function(data) {
        console.log(data)
        var productos = data;        
        $('#cod_producto').html(productos.cod_producto);
        $('#nombre').html(productos.nombre);
        $('#precio').html(productos.precio);
        $('#stock').html(productos.stock);
        $('#descripcion').html(productos.descripcion);
        $('#foto').attr("src", productos.foto);
    }).fail(function() {
        console.log('Error al consumir la API!');
    });

});


