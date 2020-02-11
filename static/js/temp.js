if(document.readyState=='loading'){
    document.addEventListener('DOMContentLoaded', ready)
}
   else{
    ready()

}

function addUp(){
    
}

$("#ol").append("<h1>Appended item</h1>");

$(document).ready(function(){
$("#btn2").click(function(){
$("ol").append("<li>Appended item</li>");
});
});