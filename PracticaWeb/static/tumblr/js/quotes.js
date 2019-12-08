function addQuotationMarks(e) {
    let write = e.target.value;
    write = `"${write}"`
    var x = document.getElementById("quote");

    x.innerHtml(write);

    //let z = x.value.toString().includes('"');
    //if (!z){x.value = '"' + x.value + '"';}

}

function addSource() {
    var x = document.getElementById("source");
    let z = x.value.toString().includes('— ');
    if (!z){x.value = '—  ' + x.value;}
}