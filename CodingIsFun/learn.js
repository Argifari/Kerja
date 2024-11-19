const Hapi = require('@hapi/hapi');
const route = require('./dot'); 

const init = async () => {
    const server = Hapi.server({
        port : 5000,
        host : 'localhost',
    });
    server.route(route);
    await server.start();
    console.log(`server ini berjalan di ${server.info.uri}`);
};

init();