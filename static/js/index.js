let sub_btn = document.getElementById('submit_btn');

sub_btn.addEventListener("click", function (e) {
    e.preventDefault()
    var formData = new FormData();
    formData.append('file', $('#code_form')[0]);
    console.log(formData.get("file"));
    
    $.ajax({
           url : 'http://localhost:8000/code_review/validate/',
           type : 'POST',
           data : formData,
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType
           success : function(data) {
               console.log(data);
               alert(data);
           }
    });
});
