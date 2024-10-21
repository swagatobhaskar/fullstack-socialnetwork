'use client'

export default function UserProfile() {

    const fetchProfile = async() => {
        try{
            const profileURL = `http://127.0.0.1:5000/user/profile`
            const profile_response = await fetch(profileURL, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            })
        const profile_data = await profile_response.json();
        console.log(profile_data);
        
        } catch(error) {
            console.error(error);
        }
        
    }
}