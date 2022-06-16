console.log('Hello')
console.log('dff')

$(document).ready(function () {

    const csrf = $("input[name=csrfmiddlewaretoken]").val();

    $("#add-new-card").click(function () {
        $.ajax({
            url: '',
            type: 'get',
            success: function (response) {
                $('.glass').append(`<div class="frasses">
               <form method="post" > 
                   <h1>${response.word}</h1>
                   <p>write text with this word</p>
                   <textarea placeholder="write text" class="form-control" cols="1500" rows="3" >

                   </textarea>
                    </br>
                      <button type="submit" class="btn btn-primary">Save to your collection</button>
               </form>
           </div>`)
            }

        })
    })
    $('.add-to-db').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '',
            type: 'post',
            data: {
                word: $(this).parent().find('h1').text(),
                text: $(this).parent().find('.form-control').val(),
                csrfmiddlewaretoken: csrf
            },
            dataType: 'json',
            success(response){
                alert(response.data)
            }
        })
    })

})