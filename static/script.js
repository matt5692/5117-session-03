function addEntry(){
    const name = document.getElementById('name').value;
    const entryList = document.getElementById('entries');
    const entry = document.createElement("li");

    if(name){
        console.log(name);
        entry.innerText = name;
        entryList.appendChild(entry);
    }
}