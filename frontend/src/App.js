import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import Home from "./pages/Home/Home";
import Logout from "./components/Logout/Logout";
import Profile from "./pages/Profile/Profile";
import EditAccount from "./components/EditAccount/EditAccount";
import PrivateRoute from "./contexts/PrivateRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route exact path="/" element={<PrivateRoute />}>
          <Route path="/home" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/edit-account" element={<EditAccount />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
