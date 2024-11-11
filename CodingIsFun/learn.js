const fs = require('fs');

const writeMyStream = fs.createWriteStream('./CodingIsFun/Untitled-1.txt');

writeMyStream.write('Ini merupakan baris pertama\n');
writeMyStream.end('inilah akhirnya\n');

const readAble = fs.createReadStream('./CodingIsFun/Untitled-1.txt' , {
    highWaterMark : 10
});

readAble.on('readable', () => {
    try {
        process.stdout.write(`[${readAble.read()}]`);
    }
    catch(error){

    }
});

readAble.on('end', () => {
    console.log('done');
});

