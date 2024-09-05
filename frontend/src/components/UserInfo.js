import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserInfo = ({ userId }) => {
    const [userInfo, setUserInfo] = useState({});

    useEffect(() => {
        const fetchUserInfo = async () => {
            try {
                const response = await axios.get(`/api/user/${userId}`);
                setUserInfo(response.data);
            } catch (error) {
                console.error('Error fetching user info:', error);
            }
        };

        fetchUserInfo();
    }, [userId]);

    return (
        <div>
            <h2>User Information</h2>
            <p>Full Names: {userInfo.full_name}</p>
            <p>Location: {userInfo.location}</p>
            <p>Email Address: {userInfo.email}</p>
            <p>Phone: {userInfo.phone}</p>
            <p>Properties Owned: {userInfo.properties_owned}</p>
            <p>Properties Leased: {userInfo.properties_leased}</p>
        </div>
    );
};

export default UserInfo;