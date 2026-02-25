document.addEventListener('DOMContentLoaded', () => {

    document.querySelector("#form").onsubmit = () => {

        // initialize a new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').value;
        request.open('POST', '/convert');

        // callback function for when request completes
        request.onload = () => {
            // extract json data from request
            const data = JSON.parse(request.responseText);

            //update the result div
            if (data.success) {
                const content = `1 USD is equal to ${data.rate} ${currency}`;
                document.querySelector("#result").innerHTML = content;
            } else {
                document.querySelector("#result").innerHTML = "There was no error.";
            }
        }

        const data = new FormData();
        data.append('currency', currency);

        request.send(data);
        return false;

    }
})