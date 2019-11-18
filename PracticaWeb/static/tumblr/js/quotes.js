function addQuotationMarks() {
    var x = document.getElementById("quote");

    let z = x.value.toString().includes('"');
    if (!z){x.value = '"' + x.value + '"';}

}

function addSource() {
    var x = document.getElementById("source");
    let z = x.value.toString().includes('— ');
    if (!z){x.value = '—  ' + x.value;}
}