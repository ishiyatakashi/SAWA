$(document).ready(function () {
    $('#select-category').submit(function () {
        let list = [];
        $('input:checked').each(function () {
            list.push($(this).val());
        });
        $.ajax({
            'async': false,
            'url': $('form#select-category').attr('action'),
            'type': 'POST',
            'datatype': 'json',
            'data': {
                'image': $('#image').val(),
                'select-category': list
            }
        }).done(function () {

        }).fail(function () {

        });
    })


});