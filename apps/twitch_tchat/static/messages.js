$(document).ready(function(){
    var interval;

    getMessages = function() {
        $.ajax({
            url: '/msg/'+$('#messages').data('username')
        }).done(function (result) {
            if(result.status) {
                 $('#messages').append(result.content);
                 $("html, body").animate(
                     { scrollTop: $(document).height() }
                 , "slow");
            } else {
                $('#messages').html('<div class="error">Not Found</div>')
                clearInterval(interval)
            }
        })
    }

    interval = setInterval(function(){
        getMessages()
    }, 500)
})
