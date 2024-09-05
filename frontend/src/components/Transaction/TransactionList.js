import React, { useEffect, useState } from 'react';
import contractService from '../../services/contractService';

const TransactionList = () => {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        const fetchTransactions = async () => {
            const data = await contractService.getTransactions();
            setTransactions(data);
        };
        fetchTransactions();
    }, []);

    return (
        <div>
            <h2>Transaction History</h2>
            <ul>
                {transactions.map((transaction) => (
                    <li key={transaction.id}>{transaction.details}</li>
                ))}
            </ul>
        </div>
    );
};

export default TransactionList;