import React, { useEffect, useState } from 'react';
import propertyService from '../../services/propertyService';

const PropertyList = () => {
    const [properties, setProperties] = useState([]);

    useEffect(() => {
        const fetchProperties = async () => {
            const data = await propertyService.getProperties();
            setProperties(data);
        };
        fetchProperties();
    }, []);

    return (
        <div>
            <h2>Property Listings</h2>
            <ul>
                {properties.map((property) => (
                    <li key={property.id}>{property.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default PropertyList;