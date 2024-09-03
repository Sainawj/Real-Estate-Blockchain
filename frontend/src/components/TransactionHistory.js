import React from 'react';

const TransactionHistory = ({ transactions }) => {
    return (
        <div className="transaction-history">
            <h2>Transaction History</h2>
            <table>
                <thead>
                    <tr>
                        <th>Tran Date</th>
                        <th>Due Date</th>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Check No</th>
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
                            <td>{transaction.tranDate}</td>
                            <td>{transaction.dueDate}</td>
                            <td>{transaction.amount}</td>
                            <td>{transaction.description}</td>
                            <td>{transaction.checkNo}</td>
                            <td>{transaction.balance}</td>
                            <td>{transaction.receipt}</td>
                            <td>{transaction.balancePaid}</td>
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