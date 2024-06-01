import React from "react";
import {useAuth} from "../contexts/Contexts";
import EditJobseeker from "./EditJobseeker";
import EditCompany from "./EditCompany";

export default function EditProfile() {
    const {user} = useAuth();

    if (!user) {
        return <div>Loading...</div>;
    }
    console.log(user.user_type);
    return <div>{user.user_type === "company" ? <EditCompany /> : <EditJobseeker />}</div>;
}
