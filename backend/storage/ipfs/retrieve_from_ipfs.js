const { getFile } = require('./ipfs_utils');

const fileHash = 'Qm...';  // Replace with the actual IPFS hash

(async () => {
    const file = await getFile(fileHash);
    console.log('File retrieved from IPFS:', file.toString());
})();