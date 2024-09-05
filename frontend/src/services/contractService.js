import Web3 from 'web3';
import RealEstate from './RealEstate.json'; // Import the compiled contract ABI

const web3 = new Web3(Web3.givenProvider || 'http://localhost:7545');

const contractAddress = '0x...'; // Replace with the deployed contract address
const realEstate = new web3.eth.Contract(RealEstate.abi, contractAddress);

const listProperty = async (name, location, price) => {
    const accounts = await web3.eth.getAccounts();
    return await realEstate.methods.listProperty(name, location, price).send({ from: accounts[0] });
};

const purchaseProperty = async (id, price) => {
    const accounts = await web3.eth.getAccounts();
    return await realEstate.methods.purchaseProperty(id).send({ from: accounts[0], value: price });
};

const getProperties = async () => {
    const properties = [];
    const propertyCount = await realEstate.methods.propertyCount().call();

    for (let i = 1; i <= propertyCount; i++) {
        const property = await realEstate.methods.getProperty(i).call();
        properties.push(property);
    }
    return properties;
};

export default {
    listProperty,
    purchaseProperty,
    getProperties,
};

