$(document).ready(function(){
    getMessages = function() {
        $.ajax({
            url: '/msg/'+$('#messages').data('username')
        }).done(function (messages) {
            messages.forEach(function(message) {
                var p = document.createElement('p');
                $(p).css('color', message.color).text(message.username + '> ');

                var div = document.createElement('div');
                $(div).addClass('message').text(message.text);
                $(div).prepend(p)
                $('#messages').append(div)
            })

            $("html, body").animate({ scrollTop:
                    $(document).height() }, "slow");
        })
    }

    setInterval(function(){
        getMessages()
    }, 500)
})
