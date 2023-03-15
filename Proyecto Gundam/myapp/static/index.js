
const logo = document.getElementById('logo');

const mostrarTexto = () => {
    const x = document.getElementById("textoPrincipal");
    if (x.style.visibility === "hidden") {
        x.style.visibility= "visible"
    } else {
      x.style.visibility = "hidden";
    }
  }


  logo.addEventListener('click', async (event) => {
    event.preventDefault(); 
    try {
      await new Promise((resolve) => setTimeout(resolve, 2500)); 
      window.location.assign('index.html'); 
    } catch (error) {
      console.error(error);
      alert('No se ha podido cargar la pagina'); 
    }
  });

  function reproducirMusica() {
    setTimeout(function(){
      document.getElementById("miAudio").play();
    }, 4000);
  }