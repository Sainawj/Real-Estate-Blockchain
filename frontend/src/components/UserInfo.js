import React from 'react';

const UserInfo = ({ user }) => {
    return (
        <div className="user-info">
            <h2>User Information</h2>
            <p>Full Names: {user.fullName}</p>
            <p>Location: {user.location}</p>
            <p>Email Address: {user.email}</p>
            <p>Phone No: {user.phone}</p>
            <p>Properties Owned: {user.propertiesOwned}</p>
            <p>Properties Leased: {user.propertiesLeased}</p>
        </div>
    );
};

export default UserInfo;