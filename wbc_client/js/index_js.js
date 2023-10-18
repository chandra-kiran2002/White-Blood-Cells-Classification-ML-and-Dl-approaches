function get_data(){
  document.getElementById("spinner").style.display = 'inline-block'
    var formdata = new FormData();
    console.log(document.getElementById("formFileLg").files[0])
formdata.append("file1",document.getElementById("formFileLg").files[0]);

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("https://wbc-back.onrender.com/upload", requestOptions)
  .then(response => response.json())
  .then(result => {console.log(result.result[1])
    document.getElementById("crop_img").src = "data:image/png;base64," + result.result[1];
    document.getElementById("img").src = "data:image/png;base64," + result.result[0];
    document.getElementById("class").innerHTML=result.class
    document.getElementById("eos1").innerHTML=result.prob0+"%"
    document.getElementById("lym1").innerHTML=result.prob1+"%"
    document.getElementById("mon1").innerHTML=result.prob2+"%"
    document.getElementById("neu1").innerHTML=result.prob3+"%"

    document.getElementById("eos").style.width=result.prob0+'px'
    document.getElementById("lym").style.width=result.prob1+'px'
    document.getElementById("mon").style.width=result.prob2+'px'
    document.getElementById("neu").style.width=result.prob3+'px'

    document.getElementById("spinner").style.display = 'none'

    })
  .catch(error => console.log('error', error));
}



