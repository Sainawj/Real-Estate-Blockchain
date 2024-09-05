import React, { useState, useEffect } from 'react';
import axios from 'axios';

const WatchList = ({ userId }) => {
    const [watchList, setWatchList] = useState([]);

    useEffect(() => {
        const fetchWatchList = async () => {
            try {
                const response = await axios.get(`/api/watchlist/${userId}`);
                setWatchList(response.data);
            } catch (error) {
                console.error('Error fetching watchlist:', error);
            }
        };

        fetchWatchList();
    }, [userId]);

    return (
        <div>
            <h2>Properties on my Watch List</h2>
            <div className="watch-list-images">
                {watchList.map((property, index) => (
                    <img
                        key={index}
                        src={property.image}
                        alt={`Property ${index + 1}`}
                        width="150"
                        height="100"
                    />
                ))}
            </div>
        </div>
    );
};

export default WatchList;