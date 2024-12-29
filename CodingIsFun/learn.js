// const Hapi = require('@hapi/hapi');
// const route = require('./dot'); 

// const init = async () => {
//     const server = Hapi.server({
//         port : 5000,
//         host : 'localhost',
//     });
//     server.route(route);
//     await server.start();
//     console.log(`server ini berjalan di ${server.info.uri}`);
// };

// init();

const fs = require('fs');
// fs.writeFileSync('./CodingIsFun/text.txt','ini adalah baru');
// const answer= fs.readFile('./CodingIsFun/text.txt', 'utf-8',(err,data) => {
//     if (err) throw err;
//     console.log(data);
// });

// console.log(answer)


const readline = require('readline');

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
});

rl.question('masukkan nama anda : ', (nama) => {
    rl.question('masukkan judul anda : ', (noHP) => {
        const person = {nama, noHP};
        const fileBuffer = fs.readFileSync('./CodingIsFun/contacs.json','utf-8');
        const contacs = JSON.parse(fileBuffer);
        contacs.push(person);
        fs.writeFileSync('./CodingIsFun/contacs.json',JSON.stringify(contacs));
        rl.close(); 
    });
});
