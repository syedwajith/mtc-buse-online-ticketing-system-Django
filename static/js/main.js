function toggleform(checkboxnumber) {
    const form1 = document.getElementById("form1");
    const form2 = document.getElementById("form2");
    const checkbox1 = document.getElementById("checkbox1");
    const checkbox2 = document.getElementById("checkbox2");

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

function payment_checkbox(checkboxnumber) {
    const checkbox1 = document.getElementById("checkbox1");
    const checkbox2 = document.getElementById("checkbox2");
    const checkbox3 = document.getElementById("checkbox3");

    if(checkboxnumber === 1) {
        checkbox1.checked = true;
        checkbox2.checked = false;
        checkbox3.checked = false;
    }
    else if(checkboxnumber === 2) {
        checkbox1.checked = false;
        checkbox2.checked = true;
        checkbox3.checked = false;
    }
    else if(checkboxnumber === 3) {
        checkbox1.checked = false;
        checkbox2.checked = false;
        checkbox3.checked = true;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const no_ticket_input = document.getElementById('no_ticket');
    no_ticket_input.addEventListener('input', calculateTotalamt);

    function calculateTotalamt() {
        const ticket_amt = parseFloat(document.getElementById('ticket_amt').value);
        const no_ticket = parseInt(document.getElementById('no_ticket').value);
        const tot_amt = ticket_amt * no_ticket;
    
        document.getElementById('tot_amt').value = tot_amt.toFixed(2);
    }
});

function submitform(event) {
    event.preventDefault();

    const checkbox1 = document.querySelector('input[name="checkbox1"]');
    const checkbox2 = document.querySelector('input[name="checkbox2"]');
    const checkbox3 = document.querySelector('input[name="checkbox3"]');

    if(checkbox1.checked || checkbox2.checked || checkbox3.checked) {
        document.getElementById("myform").submit();
    }
    else {
        alert("Please select the payment method");
    }
}