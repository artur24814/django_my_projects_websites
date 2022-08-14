
$(document).ready(function () {

    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    $("#pl-en").click(function (){
        const text = $("#text").val();
        $.ajax({
            url: '',
            type: 'get',
            data: {
                word: text
            },
            success: function (response) {
                $(".btn")
                $('#translated').append('<div class="card mb-1"><button type="button" class="btn-close" aria-label="Close"></button><div class="card-body">' + response.word + "---" + response.translated + '</div></div>')
                $('.btn-close').on('click', function(event) {
                    $(this).parent().remove();
                })
            }
        })
    })

    $('#translated').on('click', '.card-body', function () {
        $.ajax({
            url: '',
            type: 'post',
            data: {
                text: $(this).text(),
                csrfmiddlewaretoken: csrf
            },
            dataType: 'json',
            success: function (response) {

                alert(response.data)
                $(this).parent().css('background-color', 'green');
            }
        })

    })
})