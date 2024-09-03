import React, { useState } from 'react';

const PropertyUpload = () => {
    const [file, setFile] = useState(null);
    const [propertyDetails, setPropertyDetails] = useState({
        title: '',
        description: '',
        price: ''
    });

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleInputChange = (e) => {
        setPropertyDetails({ ...propertyDetails, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const fileContent = await file.text();
        const response = await fetch('/add_property', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ...propertyDetails,
                file_content: fileContent,
                filename: file.name
            })
        });
        const result = await response.json();
        console.log('Property added with ID:', result.property_id);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="title" placeholder="Title" onChange={handleInputChange} />
            <input type="text" name="description" placeholder="Description" onChange={handleInputChange} />
            <input type="number" name="price" placeholder="Price" onChange={handleInputChange} />
            <input type="file" onChange={handleFileChange} />
            <button type="submit">Upload Property</button>
        </form>
    );
};

export default PropertyUpload;