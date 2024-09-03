import React from 'react';

const PropertyWatchList = ({ properties }) => {
    return (
        <div className="property-watchlist">
            <h2>Properties on my Watch List</h2>
            <div className="property-list">
                {properties.map((property, index) => (
                    <img key={index} src={property.image} alt="Property" />
                ))}
            </div>
        </div>
    );
};

export default PropertyWatchList;