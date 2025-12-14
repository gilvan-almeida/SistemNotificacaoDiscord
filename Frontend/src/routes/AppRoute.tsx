import { Route, Routes } from "react-router-dom";

import LoginPage from "../pages/LoginPage"
import HomePage from "../pages/Home";

function AppRoutes(){
    return(
        <Routes>
            <Route path="/" element={<LoginPage/>}/>
            <Route path="/home" element={<HomePage/>}/>
        </Routes>
    )
}

export default AppRoutes;