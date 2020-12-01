window.onload = function(){


  var items = document.getElementsByClassName('item')
  for (var i = 0; i < items.length; i++) {
    var name = items[i].getAttribute('name');
    var code = items[i].getAttribute('code');
    items[i].innerHTML = `<td>${name}</td><td>${code}</td><td><div id="${name}::${code}" class="qr"></div></td>`;

    //document.getElementById(`${name}::${code}`)
    var qrcode = new QRCode(`${name}::${code}`, {
      text: `${name}::${code}`,
      width: 64,
      height: 64,
      colorDark : "#000000",
      colorLight : "#ffffff",
      correctLevel : QRCode.CorrectLevel.H
  });

  }

}
