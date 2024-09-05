import React, { useEffect, useState } from 'react';
import contractService from '../../services/contractService';
import axios from 'axios';

const PropertyList = () => {
    const [properties, setProperties] = useState([]);

    useEffect(() => {
        const fetchProperties = async () => {
            const data = await contractService.getProperties();
            setProperties(data);
        };
        fetchProperties();
    }, []);

    const purchase = async (id, price) => {
        try {
            await contractService.purchaseProperty(id, price);
            alert('Property purchased successfully');
        } catch (error) {
            alert('Purchase failed');
        }
    };

    return (
        <div>
            <h2>Property Listings</h2>
            <ul>
                {properties.map((property) => (
                    <li key={property.id}>
                        {property.name} - {property.location} - {property.price} ETH
                        <button onClick={() => purchase(property.id, property.price)}>Buy</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

const propertyService = {
    getPropertiesByUserId: async (userId) => {
        try {
            const response = await axios.get(`/api/properties/${userId}`);
            return response.data;
        } catch (error) {
            console.error('Error fetching properties:', error);
            return [];
        }
    },

    createProperty: async (propertyData) => {
        try {
            const response = await axios.post('/api/properties', propertyData);
            return response.data;
        } catch (error) {
            console.error('Error creating property:', error);
            return null;
        }
    }
};

export default PropertyList;