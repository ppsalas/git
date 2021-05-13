$(document).ready(function () {
    $("#registrarsee").validate({
        rules: {
            name: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 4
            },
            email: {
                required: true,
                email: true
            },
        }
    });
});


$(document).ready(function () {
    $("#iniciarsesion").validate({
        rules: {
            name: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 4
            },
            email: {
                required: true,
                email: true
            },
        }
    });
});


$(document).ready(function() {
    $("#subirobraa").validate({
      rules: {
        name : {
          required: true,
          minlength: 3
        },
        precio: {
          required: true,
          number: true,
          min: 1
        },
        email: {
          required: true,
          email: true
        },
      }
    });
  });

