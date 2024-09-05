import React from 'react';
import UserInfo from './UserInfo';
import TransactionHistory from './TransactionHistory';
import WatchList from './WatchList';

const Dashboard = ({ userId }) => {
    return (
        <div className="dashboard-container">
            <div className="sidebar">
                <a href="#about">About us</a>
                <a href="#profile">My Profile</a>
                <a href="#listings">Property Listings</a>
                <a href="#share-list">Share/List Property</a>
                <a href="#logout">Log out</a>
            </div>
            <div className="main-content">
                <div className="user-info">
                    <UserInfo userId={userId} />
                </div>
                <div className="analytics">
                    {/* Insert your chart components here */}
                </div>
                <div className="transaction-history">
                    <TransactionHistory userId={userId} />
                </div>
                <div className="watch-list">
                    <WatchList userId={userId} />
                </div>
            </div>
        </div>
    );
};

export default Dashboard;