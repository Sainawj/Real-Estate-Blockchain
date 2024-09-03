const ipfs = require('./ipfs_config');

// Function to add a file to IPFS
const addFile = async (file) => {
    const { path, content } = file;
    const result = await ipfs.add({ path, content });
    return result;
};

// Function to retrieve a file from IPFS
const getFile = async (hash) => {
    const file = await ipfs.cat(hash);
    return file;
};

module.exports = { addFile, getFile };