function toggleform(checkboxnumber) {
    var form1 = document.getElementById("form1");
    var form2 = document.getElementById("form2");
    var checkbox1 = document.getElementById("checkbox1");
    var checkbox2 = document.getElementById("checkbox2");

    if(!checkbox1.checked && !checkbox2.checked) {
        form1.style.display = "none";
        form2.style.display = "none";
    }
    else if(checkboxnumber === 1) {
        form1.style.display = checkbox1.checked ? "block" : "none";
        checkbox2.checked = false;
        form2.style.display = "none";
    }
    else if(checkboxnumber === 2) {
        form2.style.display = checkbox2.checked ? "block" : "none";
        checkbox1.checked = false;
        form1.style.display = "none";
    }
}