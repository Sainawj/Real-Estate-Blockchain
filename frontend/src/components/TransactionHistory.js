import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TransactionHistory = ({ userId }) => {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                const response = await axios.get(`/api/transactions/${userId}`);
                setTransactions(response.data);
            } catch (error) {
                console.error('Error fetching transactions:', error);
            }
        };

        fetchTransactions();
    }, [userId]);

    return (
        <div>
            <h2>Transaction History</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Check</th>
                        <th>Who</th>
                        <th>Balance</th>
                        <th>Receipt</th>
                        <th>Balance Paid</th>
                        <th>Interest</th>
                        <th>Fees</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map((transaction, index) => (
                        <tr key={index}>
                            <td>{transaction.date}</td>
                            <td>{transaction.amount}</td>
                            <td>{transaction.description}</td>
                            <td>{transaction.check}</td>
                            <td>{transaction.who}</td>
                            <td>{transaction.balance}</td>
                            <td>{transaction.receipt}</td>
                            <td>{transaction.balance_paid}</td>
                            <td>{transaction.interest}</td>
                            <td>{transaction.fees}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default TransactionHistory;