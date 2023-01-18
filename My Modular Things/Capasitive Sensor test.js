var pin = [];
pin.length = 6;

function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}

loop (async() => {
  for (let i = 0; i < 6; i++){
    pin[i] = await MyCap.readPad(i);
    console.log("pin" + i);
    console.log(pin[i]);
    if (pin[i] > 0.5)
      pin[i] = 1;
    else 
      pin[i] = 0;
  }
  
  await MyCap.setRGB(pin[0], pin[1], pin[2]);
  await sleep(50);
  
},  0)