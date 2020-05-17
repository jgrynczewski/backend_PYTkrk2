document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = () => {

        const request = new XMLHttpRequest();

        const amount = document.querySelector('#amount').value
        const base = document.querySelector('#base').value
        const currency = document.querySelector('#currency').value

        request.open('POST', '/');

        request.onload = () => {
            console.log(request.responseText);
            const data = JSON.parse(request.responseText);

            if (data.success) {
                const content = `Wypłacono ${data.result} ${data.currency}`
                document.querySelector('#result').innerHTML = content
            }
            else {
                document.querySelector('#result').innerHTML = 'Coś poszło nie tak.'
            }
        }

        const data = new FormData();
        data.append('amount', amount)
        data.append('base', base)
        data.append('currency', currency)

        request.send(data);
        return false;
    };
});