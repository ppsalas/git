$(document).ready(function () {
    $("#basic-form").validate({
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