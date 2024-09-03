const IPFS = require('ipfs-http-client');

// Connect to the IPFS daemon running locally or on a remote server
const ipfs = IPFS({ host: 'localhost', port: '5001', protocol: 'http' });

module.exports = ipfs;