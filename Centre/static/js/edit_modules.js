$(document).ready(function () {
    let updateModules = function (courseId) {
        let url = "/get-modules/" + courseId + "/";
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
    };

    // Actualiza los módulos cuando se carga la página
    updateModules($('#id_courses').val());

    // Actualiza los módulos cuando se cambia el curso
    $('#id_courses').change(function () {
        updateModules($(this).val());
    });
});