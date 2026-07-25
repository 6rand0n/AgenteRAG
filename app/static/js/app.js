const pregunta = document.getElementById("pregunta");
const boton = document.getElementById("consultar");
const loading = document.getElementById("loading");
const resultado = document.getElementById("resultado");
const respuesta = document.getElementById("respuesta");
const fuentes = document.getElementById("fuentes");

async function consultar(){
    if(!pregunta.value.trim()) return;

    resultado.style.display="none";
    loading.style.display="block";

    boton.disabled=true;
    boton.innerText="Consultando...";

    const r = await fetch("/preguntar",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            pregunta:pregunta.value
        })
    });

    const data = await r.json();
    respuesta.textContent=data.respuesta;
    fuentes.innerHTML="";

    data.fuentes.forEach(p=>{
        const badge=document.createElement("div");
        badge.className="badge";
        badge.innerText="Página "+p;
        fuentes.appendChild(badge);
    });

    loading.style.display="none";
    resultado.style.display="block";

    boton.disabled=false;
    boton.innerText="Consultar";
}

boton.addEventListener("click",consultar);

pregunta.addEventListener("keydown",e=>{
    if(e.key==="Enter" && !e.shiftKey){
        e.preventDefault();
        consultar();
    }
});