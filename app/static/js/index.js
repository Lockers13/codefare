$('#code_form' ).submit(
    function(e) {
        $.ajax( {
            url: 'http://localhost:8000/code_review/validate/',
            type: 'POST',
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function(result){
                console.log(result);
                }
        } );
        e.preventDefault();
    } 
);
