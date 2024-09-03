const { addFile } = require('./ipfs_utils');

const filename = process.argv[2];
const fileContent = process.argv[3];

addFile({ path: filename, content: fileContent })
    .then(result => {
        console.log(JSON.stringify(result));
    })
    .catch(error => {
        console.error('Error:', error);
    });