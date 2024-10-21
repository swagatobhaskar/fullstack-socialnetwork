'use client'

import Link from "next/link";
import { useState } from "react";

export default function SignUp() {

    const [formData, setFormData] = useState({email:'', password:'', confirmPassword:''});
    const [error, setError] = useState();
    const [loading, setLoading] = useState();
    // const [confirmPassword, setConfirmPassword] = useState();

    const handleSignup = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const signupRoute = 'http://127.0.0.1:5000/user/signup'; // use env variable
        
        try {
            const response = await fetch(signupRoute, {
                method: 'POST',
                body: JSON.stringify(formData),
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const result = await response.json();
            // do something with the result
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }

    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    return (
        <div>
            <form onSubmit={handleSignup} className="">
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
                <div>
                    <label htmlFor="Confirm-password">Confirm Password: </label>
                    <input
                        type="password"
                        name="confirm-password"
                        id="confirm-password"
                        required
                        value={formData.confirmPassword}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Sign Up</button>
            </form>
            <span>Have an account?<Link href="/login">Log in</Link> </span>
        </div>
    )
}