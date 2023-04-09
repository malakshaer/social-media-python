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
  const [errors, setErrors] = useState({});

  const navigate = useNavigate();

  const validateFields = () => {
    let validationErrors = {};
    let valid = true;

    // Validate first name
    if (!firstName.trim()) {
      validationErrors.firstName = "First name is required";
      valid = false;
    }

    // Validate last name
    if (!lastName.trim()) {
      validationErrors.lastName = "Last name is required";
      valid = false;
    }

    // Validate email
    const emailRegex = /\S+@\S+\.\S+/;
    if (!email.trim()) {
      validationErrors.email = "Email is required";
      valid = false;
    } else if (!emailRegex.test(email)) {
      validationErrors.email = "Invalid email";
      valid = false;
    }

    // Validate password
    if (!password) {
      validationErrors.password = "Password is required";
      valid = false;
    } else if (password.length < 6) {
      validationErrors.password = "Password must be at least 6 characters long";
      valid = false;
    }

    // Validate confirm password
    if (password !== confirmPassword) {
      validationErrors.confirmPassword = "Passwords do not match";
      valid = false;
    }

    setErrors(validationErrors);
    return valid;
  };

  const handleSubmit = async () => {
    const data = {
      firstName,
      lastName,
      email,
      password,
      confirmPassword,
    };
    if (validateFields()) {
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
    }
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
          {errors.firstName && <p className="error">{errors.firstName}</p>}
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
          {errors.lastName && <p className="error">{errors.lastName}</p>}
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
          {errors.email && <p className="error">{errors.email}</p>}
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
          {errors.password && <p className="error">{errors.password}</p>}
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
