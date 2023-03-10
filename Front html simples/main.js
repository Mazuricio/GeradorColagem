window.URL = window.URL || window.webkitURL
function Get_status(){
    var code_status
    let url = "http://127.0.0.1:8000/status"
    fetch(url)
        .then(response => {
            code_status = response.status
            return response.json()})
        .then(data => {
            let status = document.getElementById("status")
            let html =  "Status:" +  data.status + "<br> Code Status: " + code_status + "<br> Versão:" + data.version +"<br> Imagens Geradas: " + String(data.generatedImages) +"<br> " + "Imagens em cache: " + String(data.img_cache)
            status.innerHTML = html
        })
        .catch(err =>{
            let html = "Status: Erro> " + err
            let status = document.getElementById("status")
            status.innerHTML = html
        })
}

var formulario = document.querySelector("form")
formulario.addEventListener('submit', function(e){
    e.preventDefault()
    var tipo = document.querySelector('input[name="tipo"]:checked').value // pega o tipo marcado
    let texto = document.getElementById("texto")
    //url da pesquisa 
    let urlForm = "http://127.0.0.1:8000/colagem?texto=" + texto.value + '&tipo=' + tipo
    // corrige caso tenha alguma letra maiscula
    urlForm = urlForm.toLocaleLowerCase()
    // Resposta HTML
    fetch(urlForm)
        .then(resposta => resposta.blob()) //.json())
        .then(blob=>{
            //log.innerText = "Retorno: " + data
            var img = document.getElementById("img") //.setAttribute('src', img)
            img.src = window.URL.createObjectURL(blob)
            Get_status()
    })
    .catch(err =>{
        console.log(err)
        if (err == "TypeError: NetworkError when attempting to fetch resource.") {
            let mensagem = "A API está offline :("
            log.innerText = mensagem
        }
    })
    
})

Get_status()