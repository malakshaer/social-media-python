import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./register.css";
import request from "../../config";

const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    const data = {
      firstName,
      lastName,
      email,
      password,
      confirmPassword,
    };
    request({
      method: "post",
      url: "/register",
      data,
    })
      .then((response) => {
        console.log(response);
        localStorage.setItem("token", response.token);
        localStorage.setItem("user", response.name);
        navigate("/home");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="form">
      <div className="form-body">
        <h3 className="header">Register</h3>
        <div className="input">
          <input
            className="form__input"
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            id="firstName"
            placeholder="First Name"
          />
        </div>
        <div className="input">
          <input
            className="form__input"
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            id="lastName"
            placeholder="Last Name"
          />
        </div>
        <div className="input">
          <input
            type="email"
            id="email"
            className="form__input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
          />
        </div>
        <div className="input">
          <input
            className="form__input"
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </div>
        <div className="input">
          <input
            className="form__input"
            type="password"
            id="confirmPassword"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirm Password"
          />
        </div>
      </div>
      <div className="footer">
        <button onClick={() => handleSubmit()} type="submit">
          Register
        </button>
        <div>
          <p>
            Already have an account <a href="/login">Login</a>{" "}
          </p>
        </div>
      </div>
    </div>
  );
};

export default Register;
