$(document).ready(function () {
    $('#id_courses').change(function () {
        let url = "/get-modules/" + $(this).val() + "/";
        $.ajax({
            url: url,
            success: function (data) {
                let select = $('#id_modules');
                select.empty();
                $.each(data, function (index, module) {
                    select.append('<option value="' + module.id + '">' + module.description + '</option>');
                });
            }
        });
    });
});