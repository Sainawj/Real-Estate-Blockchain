const { addFile } = require('./ipfs_utils');
const fs = require('fs');

const filePath = 'path/to/your/file.ext';

(async () => {
    const content = fs.readFileSync(filePath);
    const result = await addFile({ path: filePath, content });
    console.log('File added to IPFS:', result.path);
})();