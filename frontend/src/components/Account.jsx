import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { useState, useEffect } from 'react'
import { createContext, useContext } from 'react'

const LOGIN_API = "http://localhost:5000/dang-nhap";

function Account() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loginMessage, setLoginMessage] = useState('');
    const handleSubmit = async (event) => {
        event.preventDefault();
        const requestBody = {
            email: email,
            password: password
        };
        const request = new Request(
            LOGIN_API,
            {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestBody)
            }
        );
        try {
            const response = await fetch(request);
            console.log("Response status", response.status);
            if (response.ok) {
                const data = await response.json();
                console.log("response data", console.data);
                if (data.success) {
                    setLoginMessage("Login successful! Welcome, " + data.user.email);
                    console.log("User Information:", data.user);
                } else {
                    setLoginMessage("Login failed" + data.message);
                }
            } else {
                const errorData = await response.json();
                setLoginMessage("Server error: " + errorData.message);
                console.error("Server responded with an error status:", response.status);
                console.error("Error details:", errorData.message);
            }
        } catch (error) {
            setLoginMessage("Network error: " + error.message);
            console.error("Error during fetch:", error);
        }
    }
    return (
        <>
            <form onSubmit={handleSubmit}>
                <div className="row mb-3">
                    <label htmlFor="emailInput" className="col-sm-2 col-form-label">Email</label>
                    <div class="col-sm-10">
                        <input
                            type="email"
                            className="form-control"
                            id="emailInput"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)} // Update email state on change
                            required // Make field required
                        ></input>
                    </div>
                </div>
                <div className="row mb-3">
                    <label className="col-sm-2 col-form-label">Password</label>
                    <div className="col-sm-10">
                        <input
                            type="password"
                            className="form-control"
                            id="passwordInput"
                            value={password}
                            onChange={(e) => setPassword(e.target.value) //update password constantly
                            }
                        ></input>
                    </div>
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
            {loginMessage && <div className="mt-3 alert alert-info">{loginMessage}</div>} {/* Display login messages */}
        </>
    )
}

export default Account;