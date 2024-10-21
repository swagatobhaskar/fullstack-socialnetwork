'use client'

import Link from "next/link";
import { useState } from "react";

function UserLogin() {

    const [formData, setFormData] = useState({email:'', password:''});

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        
        try {
            const loginURL = `http://127.0.0.1:5000/user/login`
            const response = await fetch(loginURL, {
                method: 'POST',
                body: JSON.stringify(formData),
                headers: {
                    'Conyent-Type': 'application/json',
                }
            })

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();

        } catch (error) {
            console.error(error)
        }
    }

    return (
        <div>
            <form onSubmit={handleLogin} className="">
                <div>
                    <label htmlFor="email">Email: </label>
                    <input
                        type="email"
                        name="email"
                        id="email"
                        required
                        value={formData.email}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label htmlFor="password">Password: </label>
                    <input
                        type="password"
                        name="password"
                        id="password"
                        required
                        value={formData.password}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Log In</button>
            </form>
            <span>Don&apos;t have any account?<Link href="/">Sign Up</Link> </span>
        </div>
    )
}

export default UserLogin;