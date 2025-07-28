import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { useState, useEffect } from 'react'
import { createContext, useContext } from 'react'

const LOGIN_API = "http://localhost:5000/dang-nhap";
const request = new Request(LOGIN_API, {
    method: "POST",
    headers: {
        'Content-Type': 'application/json' // This is crucial
    },
    body: JSON.stringify(
        {
            email: "phuong.nguyen@gmail.com",
            password: "123456"
        }
    )
});
try {
    const response = await fetch(request);
    console.log("Response Status:", response.status);

    // Check if the response is OK (status 200-299)
    if (response.ok) {
        const data = await response.json(); // This is where you get your JSON data
        console.log("Parsed Data:", data);

        if (data.success) {
            console.log("Login successful!");
            console.log("User Information:", data.user); // Here's your user data!
            // You can now use data.user to update your UI or state
        } else {
            console.log("Login failed:", data.message);
        }
    } else {
        console.error("Server responded with an error status:", response.status);
        // If the server sends an error message in JSON, you can still try to parse it
        const errorData = await response.json();
        console.error("Error details:", errorData.message);
    }
} catch (error) {
    console.error("Error during fetch:", error);
}

function Account() {
    return (
        <>
            
        </>
    )
}

export default Account;