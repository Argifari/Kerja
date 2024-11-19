const route = [
    {
        method:'*',
        path : '/',
        handler: (request,h) => {
            return `Halaman tidak dapat diakses dengan method tersebut`;
        },
    },
    {
        method: 'GET',
        path : '/',
        handler:(request, h) =>{
            return 'Homepage';
        },
    },
    {
        method: 'GET',
        path: '/about/{name?}',
        handler: (request, h) => {
            const { name = 'stranger'} = request.params;
            const { lang } = request.query;
            if (lang === 'id') {
                return `ini tentang ${name} yang paling asli`;
            }
            return `ini tentang ${name}`;
        },
    },
    {
        method: '*',
        path: '/about',
        handler: (request,h) => {
            return `Halaman tidak dapat diakses dengan method tersebut`;
        },

    }
    

];

module.exports = route;