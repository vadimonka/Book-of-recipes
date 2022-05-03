window.list_ingred = [];

function Show(ingred) {
    ingred.classList.toggle("ingred_down");
    if (ingred.classList.contains('ingred_down')){
        ingred = ingred.id
        list_ingred.push(ingred);
        document.getElementById("hidden_query").value = list_ingred;
    } else {
        index = list_ingred.indexOf(ingred)
        list_ingred.splice(index, 1);
        document.getElementById("hidden_query").value = list_ingred;
    }
}
