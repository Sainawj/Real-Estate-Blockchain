import React from 'react';

const Sidebar = () => {
    return (
        <div className="sidebar">
            <a href="/">About us</a>
            <a href="/profile">My Profile</a>
            <a href="/listings">Property Listings</a>
            <a href="/share-property">Share/List Property</a>
            <a href="/logout">Log out</a>
        </div>
    );
};

export default Sidebar;