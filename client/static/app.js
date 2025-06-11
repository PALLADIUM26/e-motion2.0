console.log("JavaScript file loaded successfully!");
async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const resultDisplay = document.getElementById('fileNameDisplay');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);

    try{
        console.log('lol');
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData,
        });
        console.log(response);
        if(response == '') {
            // throw new Error('Empty response');
            console.log('Empty response');
        }
        if (!response.ok) {
            console.log('Network response was not ok');
            // throw new Error('Network response was not ok');
        }
        // console.log("lol2");
        const result = await response.text();
        console.log(result);
        // prompt(result);
        resultDisplay.textContent = `Backend response: ${result}`;

        // const data = await response.json();
        // console.log('Prediction:', data.prediction);
        // const resultDiv = document.getElementById('result');
        // resultDiv.textContent = `Result: ${data.prediction}`;
        // document.getElementById('result').value = data.prediction;
        // .then(response => {
        //     console.log("Response received:", response); // Log the response
        //     return response.json(); // Parse the response as JSON
        // })
        // .then(data => {
        //     // alert('File uploaded and processed: ' + data.message);
        //     console.log("Parsed data:", data); // Log the parsed data
        //     const resultDiv = document.getElementById('result');
        //     resultDiv.textContent = `Result: ${data.prediction}`;
        // })
        // .catch(error => {
        //     console.error('Error:', error);
        // });
    }  catch (error) {
        console.error('Error:', error);
        resultDisplay.textContent = `Error: ${error.message}`;
    }
}
