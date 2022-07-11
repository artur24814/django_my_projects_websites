console.log('Hello')
console.log('dff')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    $("#add-new-card").click(function () {
        $.ajax({
            url: '',
            type: 'get',
            success: function (response) {
                $('.glass').append(`<div class="frasses">
               <form method="post" > 
                   <input type="hidden" name="csrfmiddlewaretoken" value='${csrf}' />
                   <h1>${response.word}</h1>
                   <p>write text with this word</p>
                   <textarea placeholder="write text" class="form-control" cols="1500" rows="3" ></textarea>
                    </br>
                      <button type="submit" class="btn btn-primary add-to-db">Share your thought to another users</button>
               </form>
           </div>`)
                $('.add-to-db').on('click', function (e) {
                    e.preventDefault()
                    $.ajax({
                        url: '',
                        type: 'post',
                        headers: {
                            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                        },
                        data: {
                            word: $(this).parent().find('h1').text(),
                            text: $(this).parent().find('.form-control').val(),
                        },
                        dataType: 'json',
                        success(response) {
                            alert(response.data)
                        }
                    })
                })
            }


        })
    })
    $('.add-to-db').on('click', function (e) {
        e.preventDefault()
        $.ajax({
            url: '',
            type: 'post',
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            },
            data: {
                word: $(this).parent().find('h1').text(),
                text: $(this).parent().find('.form-control').val(),
            },
            dataType: 'json',
            success(response) {
                alert(response.data)
                // if (response.data === "You save this text") {
                //     $(this).remove()
                // }
            }
        })
    })

})