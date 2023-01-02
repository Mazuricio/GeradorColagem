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
    var gr = document.getElementsByClassName('imagem')
    let texto = document.getElementById("texto")
    // gr.innerHTML = `<img src="${img_frente}"><img src="${img_costas}">`
    //url da pesquisa 
    let urlForm = "http://127.0.0.1:8000/colagem?texto=" + texto.value
    //log.innerText = urlForm
    //let hello = "http://127.0.0.1:8000"
    // corrige caso tenha alguma letra maiscula
    urlForm = urlForm.toLocaleLowerCase()
    // Resposta HTML
    //let html = ''
    fetch(urlForm)
        .then(resposta => resposta.blob()) //.json())
        .then(blob=>{
            //log.innerText = "Retorno: " + data
            var img = document.getElementById("img") //.setAttribute('src', img)
            img.src = window.URL.createObjectURL(blob)
            //log.innerText += "\n " + 
            console.log("foi")
            //console.log(data)
            Get_status()
    })
    .catch(err =>{
        console.log(err)
        if (err == "TypeError: NetworkError when attempting to fetch resource.") {
            let mensagem = "A API está offline :("
            log.innerText = mensagem
        }
        
        //log.innerText += "\n " + hello
    })
    
})

Get_status()