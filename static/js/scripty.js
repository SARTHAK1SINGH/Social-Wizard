
$(document).ready(function(){
    console.log("loaded");

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log("form-submitted");
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();

        var form = $('#login-form').serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "error"){
                    alert("could not log in..");
                }
                else{
                    console.log("logged in as: ", res);
                    window.location.href = "/";
                }
            }
        });
    });

    $(document).on('click', '#logout-link', function(e){
        e.preventDefault();

        $.ajax({
            url : '/logout',
            type: 'GET',
            success: function(res){
                if(res == 'success'){
                    window.location.href = '/login';
                }
                else
                {
                    alert("something went wrong");
                }
            }
        });

    });


    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault();

        var form = $('#post-activity').serialize();

        $.ajax({
            url : '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                console.log(res);
                window.location.href = window.location.href;
                }
        });

     });


     $(document).on("submit", "#update-form", function(e){
        e.preventDefault();

        var form = $('#update-form').serialize();

        $.ajax({
            url : '/update-settings',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "success")
                {
                    window.location.href = window.location.href;
                }else
                {
                    alert(res);
                }
                }


        });

     });

     $(document).on("submit", "#comment-form", function(e){
        e.preventDefault();

        var form = $('#comment-form').serialize();

        $.ajax({
            url : '/submit-comment',
            type: 'POST',
            data: form,
            dataType: "json",
            success: function(res){
                console.log(res);
                }
        });

     });

});
