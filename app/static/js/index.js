fetch("http://localhost:8000/code_review/validate/")
  .then(response => response.json())
  .then(function(data) {
      console.log(data)
      let json_obj = JSON.parse(data)
      let prob_info = document.getElementById('prob_info')
      prob_info.innerHTML += json_obj["20"]["p1"]["desc"] + "<br>"
      lang_keys = Object.keys(json_obj["20"]["p1"]["languages"])
      for(let i = 0; i < lang_keys.length; i++) {
          let lang_obj = json_obj["20"]["p1"]["languages"][lang_keys[i]]
          prob_info.innerHTML += "<br>Score : " + lang_obj["score"] + "<br>Allowed libraries: <ul>"
          for(let j = 0; j < + lang_obj["libs"].length; j++) {
            prob_info.innerHTML +=  "<li>" + lang_obj["libs"][j].replace(/</g,'&lt;').replace(/>/g,'&gt;') + "</li>"
          } 
          prob_info.innerHTML += "</ul>"
      }

  });


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
                if(result.startsWith("Invalid")) {
                    $('#response').css("color", "red")
                    $('#response').html(result)
                }
                else {
                    $('#response').css("color", "green")
                    $('#response').html(result)
                }
            }
        } );
        e.preventDefault();
    } 
);
