import React from 'react';
import './App.css';
import React, { useEffect, useState } from 'react';
import Sidebar from './components/Sidebar';
import UserInfo from './components/UserInfo';
import TransactionHistory from './components/TransactionHistory';
import PropertyWatchList from './components/PropertyWatchList';
import axios from 'axios';
import Web3 from 'web3';
import PropertyContract from './contracts/PropertyContract.json';

function App() {
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState('');
    const [contract, setContract] = useState(null);
    const [properties, setProperties] = useState([]);

    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                setWeb3(web3);

                const accounts = await web3.eth.getAccounts();
                setAccount(accounts[0]);

                const networkId = await web3.eth.net.getId();
                const deployedNetwork = PropertyContract.networks[networkId];
                const contract = new web3.eth.Contract(
                    PropertyContract.abi,
                    deployedNetwork && deployedNetwork.address
                );
                setContract(contract);
            } else {
                console.error("Ethereum browser extension not detected.");
            }
        };

        initWeb3();
    }, []);

    const listProperty = async (title, description, price) => {
        const priceInWei = web3.utils.toWei(price, 'ether');
        await contract.methods.listProperty(title, description, priceInWei)
            .send({ from: account });
    };

    const buyProperty = async (propertyId) => {
        const priceInWei = web3.utils.toWei(properties[propertyId].price, 'ether');
        await contract.methods.buyProperty(propertyId)
            .send({ from: account, value: priceInWei });
    };

    return (
        <div className="App">
            {/* Your components and UI logic */}
            {properties.map(property => (
                <div key={property.id}>
                    <h3>{property.title}</h3>
                    <p>{property.description}</p>
                    <p>Price: {property.price}</p>
                </div>
            ))}
        </div>
    );
}

export default App;