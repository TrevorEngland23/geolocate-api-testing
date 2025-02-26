require('dotenv').config();
const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());

app.use(express.static('public')); 

app.get('/get-ip-info', async (req, res) => {
    const apiKey = process.env.IP_API_KEY;
    const ip = req.query.ip;

    if (!ip) return res.status(400).json({ error: "IP address is required" });

    try {
        const response = await axios.get(`https://ipgeolocation.abstractapi.com/v1/?api_key=${apiKey}&ip_address=${ip}`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Failed to fetch data" });
    }
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
