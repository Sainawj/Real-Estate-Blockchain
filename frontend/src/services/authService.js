import axios from 'axios';

const API_URL = 'http://localhost:5000/api/auth';

const login = async (credentials) => {
    const response = await axios.post(`${API_URL}/login`, credentials);
    return response.data;
};

const register = async (userInfo) => {
    const response = await axios.post(`${API_URL}/register`, userInfo);
    return response.data;
};

export default {
    login,
    register,
};