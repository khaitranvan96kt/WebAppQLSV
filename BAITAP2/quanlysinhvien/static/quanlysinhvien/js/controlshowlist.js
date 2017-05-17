$(document).ready(() => {
    function testfn() {
        alert('Khai dep trai')
    }

    function deletefn(event) {
        id = event.target.dataset.id
        console.log(id)
        $.ajax({
            type: "POST",
            url: 'showlist/',
            data: {
                masv: event.target.dataset.id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                //alert("A user with this username already exists.");
                message = response
                console.log(message)
                if (message == 'thanhcong') {
                    $('.' + id).remove();
                }
                //location.reload();
            }
        }).fail((err) => {
            console.log(err)
        })
    }
    $('body').on('click', '.delete', deletefn);

});