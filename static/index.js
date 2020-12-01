window.onload = function(){

  var qrcode = new QRCode("qr", {
    text: "sample",
    width: 128,
    height: 128,
    colorDark : "#000000",
    colorLight : "#ffffff",
    correctLevel : QRCode.CorrectLevel.H
});

  document.getElementById('create').onclick = function(){
    var name = document.getElementById('name').value;
    var code = document.getElementById('code').value;

    if(code=='' || name==''){
      alert('empty slot');
      return;
    }
    qrcode.makeCode(`${name}::${code}`);


    const data = { code: code, name:name };
// Fetch
    fetch('/inputprocess/', {
      method: 'POST', // or 'PUT'
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      if(data.message == 'Success'){
        alert('Success')
      }
      else{
        alert('server miscommunication')
      }

    })
    .catch((error) => {
      alert('Error: Check logs')
      console.error('Error:', error);
    });



  }



}
