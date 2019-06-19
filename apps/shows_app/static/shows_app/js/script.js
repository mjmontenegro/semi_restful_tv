$(document).ready(function(){
    var original_title = $('#title').val();
    $('#title').keyup(function() {
        var data = $('form').serialize()
        $.ajax({
            method: 'POST',
            url: '/validate_name',
            data: data,
        })
        .done( function(res) {
            if (original_title == $('#title').val()) {
                res = ""
            }
            $('#title_res').html(res)
        })
    })
    $('#network').keyup(function() {
        if ($('#network').val().length < 3) {
            $('#network_res').html("Network name must be at least 3 characters long");
        }
        else {
            $('#network_res').html("");
        }
    })
    $('#description').keyup(function() {
        if ($('#description').val().length > 0 && $('#description').val().length < 10) {
            $('#description_res').html("Description is optional but must be at least 10 characters if included");
        }
        else {
            $('#description_res').html("");
        }
    })
    $('#release_date').on("change", function() {
        r_date = new Date(($(this).val()));
        if (r_date > Date.now()) {
            $('#release_date_res').html("Release date must be in the past")
        }
    })



})